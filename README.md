# Text Similarity Calculator - Dify Plugin

**Author:** gaooof  
**Version:** 0.0.1  
**Type:** Tool Plugin

## 📖 Description

A Dify plugin that calculates the semantic similarity between two text strings using embedding models. The plugin converts text to vectors using configurable embedding models, applies L2 normalization, and computes cosine similarity to return a normalized similarity score between 0 and 1.

## ✨ Features

- 🎯 **Semantic Similarity**: Calculate similarity based on meaning, not just exact text matching
- 🔧 **Flexible Model Support**: Use any text-embedding model available in Dify
- 📊 **L2 Normalization**: Applies L2 normalization to vectors for accurate similarity calculation
- 📈 **Normalized Output**: Returns similarity scores in a standardized 0-1 range
- 🛡️ **Error Handling**: Robust error handling with informative error messages
- 📋 **Detailed Results**: Returns similarity score along with metadata (model info, vector dimensions)

## 🚀 Installation

1. Clone or download this plugin to your Dify plugins directory
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. The plugin will be automatically loaded by Dify

## 📝 Usage

### In Dify Workflow

1. Add the "Text Similarity Calculation" tool to your workflow
2. Configure the following parameters:
   - **First Text**: The first text string to compare
   - **Second Text**: The second text string to compare
   - **Embedding Model**: Select an embedding model from available providers

### Example Use Cases

- **Content Deduplication**: Check if two articles or documents are similar
- **Semantic Search**: Find how closely a query matches a document
- **Question Matching**: Determine if two questions are asking the same thing
- **Clustering**: Group similar content together based on semantic similarity
- **Plagiarism Detection**: Compare text for similarity

## 🔧 Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `text1` | string | Yes | The first text string to compare |
| `text2` | string | Yes | The second text string to compare |
| `embedding_model` | model-selector | Yes | The embedding model to use (text-embedding type) |

### Supported Embedding Models

Any text-embedding model configured in your Dify instance, including:
- OpenAI (text-embedding-ada-002, text-embedding-3-small, text-embedding-3-large)
- Tongyi (text-embedding-v1, text-embedding-v2, text-embedding-v3)
- Other compatible embedding providers

## 📤 Output

The tool returns a JSON object with the following fields:

```json
{
  "similarity": 0.85,
  "text1": "Original first text",
  "text2": "Original second text",
  "model_provider": "openai",
  "model_name": "text-embedding-ada-002",
  "embedding_dimension": 1536
}
```

### Output Fields

- **similarity** (float): Similarity score between 0 and 1
  - `0.0`: Completely dissimilar
  - `0.5`: Moderately similar
  - `1.0`: Identical or extremely similar
- **text1** (string): Echo of the first input text
- **text2** (string): Echo of the second input text
- **model_provider** (string): The embedding model provider used
- **model_name** (string): The specific embedding model used
- **embedding_dimension** (int): The dimension of the embedding vectors

### Error Response

If an error occurs, the output will include:

```json
{
  "error": "Error message description",
  "similarity": 0.0
}
```

## 🔬 How It Works

The similarity calculation follows these steps:

1. **Text Vectorization**: Both input texts are converted to high-dimensional vectors using the selected embedding model
2. **L2 Normalization**: Each embedding vector is normalized using L2 norm:
   ```
   normalized_vector = vector / ||vector||₂
   ```
3. **Cosine Similarity**: Calculate the dot product of normalized vectors:
   ```
   similarity = normalized_vector1 · normalized_vector2
   ```
4. **Range Normalization**: Convert the similarity score from [-1, 1] to [0, 1]:
   ```
   normalized_similarity = (similarity + 1) / 2
   ```

### Why L2 Normalization?

L2 normalization ensures that:
- Vectors are scaled to unit length
- The dot product becomes equivalent to cosine similarity
- Results are comparable across different text lengths
- The similarity measure focuses on direction (semantic meaning) rather than magnitude

## 📦 Dependencies

- `dify_plugin>=0.2.0,<0.3.0`: Core Dify plugin framework
- `numpy>=1.24.0`: Numerical operations for vector calculations

## 🛠️ Technical Details

- **Language**: Python 3.12+
- **Framework**: Dify Plugin SDK
- **Vector Operations**: NumPy
- **Similarity Metric**: Cosine Similarity (via L2 normalized dot product)

## 📄 License

This plugin follows the license terms specified in your Dify installation.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 📧 Contact

**Author**: gaooof

For questions or support, please open an issue in the repository.

