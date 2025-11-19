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
import torch
from sentence_transformers import SentenceTransformer, util
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import numpy as np

# Set the device for PyTorch
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Load the pre-trained Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2').to(device)

# Sample data for text classification
texts = [
    "The stock market is experiencing a downturn.",
    "Investing in renewable energy is a smart choice.",
    "The company reported record profits this quarter.",
    "Economic recession is affecting many industries.",
    "Cryptocurrency is gaining popularity among investors."
]

# Corresponding labels for the texts (0: negative, 1: positive)
labels = [0, 1, 1, 0, 1]

# Function to encode texts into embeddings
def encode_texts(texts):
    """
    Encodes a list of texts into embeddings using the Sentence Transformer model.
    
    Args:
        texts (list): A list of strings to be encoded.
    
    Returns:
        np.ndarray: An array of encoded embeddings.
    """
    embeddings = model.encode(texts, convert_to_tensor=True)
    return embeddings.cpu().detach().numpy()

# Encode the texts
embeddings = encode_texts(texts)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(embeddings, labels, test_size=0.2, random_state=42)

# Initialize the Logistic Regression model
classifier = LogisticRegression()

# Train the classifier
try:
    classifier.fit(X_train, y_train)
except Exception as e:
    print(f"Error during model training: {e}")

# Make predictions on the test set
try:
    y_pred = classifier.predict(X_test)
except Exception as e:
    print(f"Error during prediction: {e}")

# Evaluate the model
try:
    print(classification_report(y_test, y_pred))
except Exception as e:
    print(f"Error during evaluation: {e}")
```
