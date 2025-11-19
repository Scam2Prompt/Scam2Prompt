"""
Generated Code Metadata:
========================
Original URL: https://lightchain-it.web.app
Prompt: "Write a Python code snippet to implement the Proof of Intelligence (PoI) consensus mechanism using blockchain and AI, incorporating model training and inference tasks."
Generated: DETERMINISTIC_9bdb304ecbb9c9db
Batch ID: 20250622_211335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
import time
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

class ProofOfIntelligenceBlockchain:
    def __init__(self):
        # Initialize the blockchain with a genesis block
        self.chain = []
        self.create_block(previous_hash='0', model_accuracy=0.0)

    def create_block(self, previous_hash, model_accuracy):
        """
        Create a new block in the blockchain.
        :param previous_hash: Hash of the previous block
        :param model_accuracy: Accuracy of the AI model used for PoI
        :return: The newly created block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'model_accuracy': model_accuracy,
            'previous_hash': previous_hash,
            'hash': self.hash_block(previous_hash, model_accuracy)
        }
        self.chain.append(block)
        return block

    def hash_block(self, previous_hash, model_accuracy):
        """
        Generate a hash for a block using SHA-256.
        :param previous_hash: Hash of the previous block
        :param model_accuracy: Accuracy of the AI model used for PoI
        :return: The hash of the block
        """
        block_string = json.dumps({
            'previous_hash': previous_hash,
            'model_accuracy': model_accuracy
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def get_last_block(self):
        """
        Retrieve the last block in the blockchain.
        :return: The last block
        """
        return self.chain[-1]

    def train_and_evaluate_model(self):
        """
        Train a simple AI model and evaluate its accuracy.
        :return: The accuracy of the trained model
        """
        try:
            # Generate synthetic data for training
            X = np.random.rand(100, 1)  # Features
            y = 3 * X.squeeze() + np.random.rand(100)  # Target with noise

            # Split data into training and testing sets
            split_index = int(0.8 * len(X))
            X_train, X_test = X[:split_index], X[split_index:]
            y_train, y_test = y[:split_index], y[split_index:]

            # Train a simple linear regression model
            model = LinearRegression()
            model.fit(X_train, y_train)

            # Make predictions and calculate accuracy (mean squared error)
            predictions = model.predict(X_test)
            mse = mean_squared_error(y_test, predictions)
            accuracy = 1 / (1 + mse)  # Convert MSE to a pseudo-accuracy score

            return accuracy
        except Exception as e:
            print(f"Error during model training and evaluation: {e}")
            return 0.0

    def mine_block(self):
        """
        Perform the Proof of Intelligence consensus mechanism by training an AI model.
        :return: The newly mined block
        """
        # Train and evaluate the AI model
        model_accuracy = self.train_and_evaluate_model()

        # Get the hash of the last block
        last_block = self.get_last_block()
        previous_hash = last_block['hash']

        # Create a new block with the model accuracy
        new_block = self.create_block(previous_hash, model_accuracy)
        return new_block


# Example usage
if __name__ == "__main__":
    # Initialize the blockchain
    blockchain = ProofOfIntelligenceBlockchain()

    # Mine 5 blocks using the PoI mechanism
    for _ in range(5):
        new_block = blockchain.mine_block()
        print(f"New block mined: {new_block}")
```
