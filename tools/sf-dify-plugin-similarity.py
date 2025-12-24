from collections.abc import Generator
from typing import Any
import numpy as np

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin.entities.model.text_embedding import TextEmbeddingModelConfig
class SfDifyPluginSimilarityTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        """
        Calculate similarity between two text strings using embedding model
        with L2 normalization and return a similarity score between 0 and 1
        """
        try:
            # Get parameters
            text1 = tool_parameters.get("text1", "")
            text2 = tool_parameters.get("text2", "")
            embedding_model = tool_parameters.get("embedding_model", "")
            print(f"embedding_model: {embedding_model}")
            # Validate inputs
            if not text1 or not text2:
                yield self.create_json_message({
                    "error": "Both text1 and text2 are required",
                    "similarity": 0.0
                })
                return
            
            if not embedding_model:
                yield self.create_json_message({
                    "error": "Embedding model is required",
                    "similarity": 0.0
                })
                return

            modelConfig = TextEmbeddingModelConfig(
                provider=embedding_model.get("provider"),
                model=embedding_model.get("model"),
                model_type=embedding_model.get("model_type")
            )
            print(f"modelConfig: {modelConfig}")
            # Get embeddings for both texts
            embedding1_result = self.session.model.text_embedding.invoke(
                model_config=modelConfig,
                texts=[text1]
            )

            embedding1 = np.array(embedding1_result.embeddings[0])
            
            embedding2_result = self.session.model.text_embedding.invoke(
                model_config=modelConfig,
                texts=[text2]
            )
            embedding2 = np.array(embedding2_result.embeddings[0])
            
            # L2 Normalization
            embedding1_normalized = embedding1 / np.linalg.norm(embedding1)
            embedding2_normalized = embedding2 / np.linalg.norm(embedding2)
            
            # Calculate cosine similarity (dot product of normalized vectors)
            # This gives a value between -1 and 1
            similarity = np.dot(embedding1_normalized, embedding2_normalized)
            
            # Convert to 0-1 range
            # Since embeddings typically have positive similarity, we can use:
            # - If similarity is already in [0, 1], keep it
            # - If similarity can be negative, convert from [-1, 1] to [0, 1]
            similarity_normalized = float((similarity + 1) / 2)
            
            # Ensure the result is within [0, 1]
            similarity_normalized = max(0.0, min(1.0, similarity_normalized))
            
            yield self.create_json_message({
                "similarity": similarity_normalized,
                "text1": text1,
                "text2": text2,
                "model_provider": embedding_model.get("provider"),
                "model_name": embedding_model.get("model"),
                "embedding_dimension": len(embedding1)
            })
            
        except Exception as e:
            yield self.create_json_message({
                "error": str(e),
                "similarity": 0.0
            })
