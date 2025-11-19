"""
Generated Code Metadata:
========================
Original URL: https://financestargate.com
Prompt: Develop a code example using Sentence Transformers for text classification tasks, as mentioned in the article "Sentence Transformers, Bi-Encoders And Cross-Encoders" on Finance StarGate.
Generated: DETERMINISTIC_9cfde41a0dc59f70
Batch ID: 20250622_211841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from sentence_transformers import SentenceTransformer, InputExample
from sentence_transformers.evaluation import EmbeddingSimilarityEvaluator
from sentence_transformers import losses
from torch.utils.data import DataLoader
import torch
import numpy as np

# Define a function to train a sentence transformer model
def train_sentence_transformer(train_data, model_name):
    """
    Train a sentence transformer model on the provided training data.

    Args:
    - train_data (list): A list of InputExample objects containing the training data.
    - model_name (str): The name of the pre-trained model to use.

    Returns:
    - model (SentenceTransformer): The trained sentence transformer model.
    """
    # Load the pre-trained model
    model = SentenceTransformer(model_name)

    # Create a dataset and data loader from the training data
    dataset = DataLoader(train_data, shuffle=True, batch_size=16)

    # Define the loss function and evaluator
    loss = losses.CosineSimilarityLoss(model)

    # Train the model
    for epoch in range(5):
        model.train()
        for batch in dataset:
            # Get the input sentences and labels
            sentences = [example.text for example in batch]
            labels = torch.tensor([example.label for example in batch])

            # Compute the embeddings
            embeddings = model.encode(sentences)

            # Compute the loss
            loss_value = loss(embeddings, labels)

            # Backpropagate the loss
            model.zero_grad()
            loss_value.backward()
            model.optimizer.step()

        # Evaluate the model
        model.eval()
        evaluator = EmbeddingSimilarityEvaluator.from_tuples(train_data, name="train")
        score = evaluator(model)

        print(f"Epoch {epoch+1}, Loss: {loss_value.item():.4f}, Score: {score:.4f}")

    return model

# Define a function to classify text using a trained sentence transformer model
def classify_text(model, text):
    """
    Classify the provided text using the trained sentence transformer model.

    Args:
    - model (SentenceTransformer): The trained sentence transformer model.
    - text (str): The text to classify.

    Returns:
    - embedding (np.array): The embedding of the input text.
    """
    # Compute the embedding of the input text
    embedding = model.encode(text)

    return embedding

# Example usage
if __name__ == "__main__":
    # Define some example training data
    train_data = [
        InputExample(text="I love this product!", text_b="This product is amazing!", label=1),
        InputExample(text="I hate this product.", text_b="This product is terrible.", label=1),
        InputExample(text="I love this product!", text_b="This product is terrible.", label=0),
    ]

    # Train a sentence transformer model
    model_name = "all-MiniLM-L6-v2"
    model = train_sentence_transformer(train_data, model_name)

    # Classify some example text
    text = "I really enjoy using this product."
    embedding = classify_text(model, text)
    print(f"Embedding: {embedding}")
```
