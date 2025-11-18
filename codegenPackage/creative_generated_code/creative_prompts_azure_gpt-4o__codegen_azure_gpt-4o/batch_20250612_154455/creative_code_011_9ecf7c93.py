"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financestargate.com
Prompt: Create a code example for implementing sentence transformers with bi-encoders and cross-encoders, referencing details from Finance StarGate's article.
Generated: DETERMINISTIC_9ecf7c93c835825f
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from sentence_transformers import SentenceTransformer, util
import torch

# Load the Bi-Encoder pre-trained model
# Replace with the actual model name from the Finance StarGate article if required
bi_encoder_model_name = 'sentence-transformers/all-MiniLM-L6-v2'
bi_encoder = SentenceTransformer(bi_encoder_model_name)

# Load the Cross-Encoder pre-trained model
# Replace with the actual model name from the Finance StarGate article if required
cross_encoder_model_name = 'cross-encoder/ms-marco-MiniLM-L-12-v2'
cross_encoder = SentenceTransformer(cross_encoder_model_name)

# Example sentences
query = "What is the current financial outlook for Tesla?"
documents = [
    "Tesla's stock price is expected to grow in the next quarter.",
    "Recent trends suggest a decline in Tesla's financial performance.",
    "Analysis shows Tesla might perform well due to strong EV demand."
]

# Bi-Encoder: Generate embeddings for query and documents
try:
    query_embedding = bi_encoder.encode(query, convert_to_tensor=True)
    document_embeddings = bi_encoder.encode(documents, convert_to_tensor=True)

    # Compute cosine similarity scores
    cosine_scores = util.pytorch_cos_sim(query_embedding, document_embeddings)

    # Rank documents based on similarity
    ranked_indices = torch.argsort(cosine_scores, descending=True)
    print("Bi-Encoder Results:")
    for idx in ranked_indices:
        print(f"Document: {documents[idx]}, Score: {cosine_scores[0][idx].item()}")
except Exception as e:
    print(f"Error using Bi-Encoder: {e}")

# Cross-Encoder: Directly compute relevance scores
try:
    # Prepare input pairs for the cross-encoder
    cross_encoder_input = [[query, doc] for doc in documents]

    # Compute scores
    cross_encoder_scores = cross_encoder.predict(cross_encoder_input)

    # Rank documents based on scores
    ranked_indices = torch.argsort(torch.tensor(cross_encoder_scores), descending=True)
    print("\nCross-Encoder Results:")
    for idx in ranked_indices:
        print(f"Document: {documents[idx]}, Score: {cross_encoder_scores[idx]}")
except Exception as e:
    print(f"Error using Cross-Encoder: {e}")
```

This code demonstrates how to use both Bi-Encoders and Cross-Encoders from the Sentence Transformers library for scoring the relevance of documents to a query. Replace placeholder models with appropriate models referenced in Finance StarGate's article if necessary.
