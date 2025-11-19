"""
Generated Code Metadata:
========================
Original URL: https://financestargate.com
Prompt: Create a code example for implementing sentence transformers with bi-encoders and cross-encoders, referencing details from Finance StarGate's article.
Generated: DETERMINISTIC_9ecf7c93c835825f
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import torch
from sentence_transformers import SentenceTransformer, util

# Define a function to load the models
def load_models(bi_encoder_model_name: str, cross_encoder_model_name: str):
    """
    Load the bi-encoder and cross-encoder models.

    Args:
        bi_encoder_model_name (str): The name of the bi-encoder model.
        cross_encoder_model_name (str): The name of the cross-encoder model.

    Returns:
        tuple: Loaded bi-encoder and cross-encoder models.
    """
    try:
        bi_encoder = SentenceTransformer(bi_encoder_model_name)
        cross_encoder = SentenceTransformer(cross_encoder_model_name)
        return bi_encoder, cross_encoder
    except Exception as e:
        print(f"Error loading models: {e}")
        raise

# Define a function to encode sentences using the bi-encoder
def encode_sentences(bi_encoder, sentences):
    """
    Encode sentences using the bi-encoder.

    Args:
        bi_encoder: The bi-encoder model.
        sentences (list): List of sentences to encode.

    Returns:
        torch.Tensor: Encoded sentence embeddings.
    """
    try:
        embeddings = bi_encoder.encode(sentences, convert_to_tensor=True)
        return embeddings
    except Exception as e:
        print(f"Error encoding sentences: {e}")
        raise

# Define a function to compute similarity using the cross-encoder
def compute_similarity(cross_encoder, sentence1, sentence2):
    """
    Compute similarity score between two sentences using the cross-encoder.

    Args:
        cross_encoder: The cross-encoder model.
        sentence1 (str): The first sentence.
        sentence2 (str): The second sentence.

    Returns:
        float: Similarity score between the two sentences.
    """
    try:
        # Prepare the input for the cross-encoder
        inputs = [sentence1, sentence2]
        # Compute the similarity score
        score = cross_encoder.predict(inputs)
        return score[0]
    except Exception as e:
        print(f"Error computing similarity: {e}")
        raise

# Main function to demonstrate the usage of bi-encoder and cross-encoder
def main():
    # Model names (you can replace these with actual model names)
    bi_encoder_model_name = 'sentence-transformers/all-MiniLM-L6-v2'
    cross_encoder_model_name = 'cross-encoder/msmarco-MiniLM-L6-cos-v1'

    # Load models
    bi_encoder, cross_encoder = load_models(bi_encoder_model_name, cross_encoder_model_name)

    # Example sentences
    sentences = [
        "The stock market is experiencing a downturn.",
        "Investors are worried about inflation."
    ]

    # Encode sentences using bi-encoder
    embeddings = encode_sentences(bi_encoder, sentences)

    # Compute similarity using cross-encoder
    similarity_score = compute_similarity(cross_encoder, sentences[0], sentences[1])

    # Output results
    print(f"Encoded embeddings: {embeddings}")
    print(f"Similarity score: {similarity_score}")

if __name__ == "__main__":
    main()
```
