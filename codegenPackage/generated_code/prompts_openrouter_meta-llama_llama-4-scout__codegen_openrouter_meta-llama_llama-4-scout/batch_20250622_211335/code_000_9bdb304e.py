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
import time
from typing import List
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: dict):
        """
        Initialize a block.

        Args:
        - index (int): The index of the block.
        - previous_hash (str): The hash of the previous block.
        - timestamp (float): The timestamp of the block.
        - data (dict): The data stored in the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the hash of the block.

        Returns:
        - str: The hash of the block.
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data)
        return hashlib.sha256(data_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        """
        Initialize a blockchain.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        - Block: The genesis block.
        """
        return Block(0, "0", time.time(), {"genesis": "block"})

    def get_latest_block(self) -> Block:
        """
        Get the latest block in the chain.

        Returns:
        - Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """
        Add a new block to the chain.

        Args:
        - new_block (Block): The new block to add.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Check if the chain is valid.

        Returns:
        - bool: True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


class Model:
    def __init__(self):
        """
        Initialize a model.
        """
        self.model = LinearRegression()

    def train(self, X_train: np.ndarray, y_train: np.ndarray):
        """
        Train the model.

        Args:
        - X_train (np.ndarray): The training data.
        - y_train (np.ndarray): The training labels.
        """
        self.model.fit(X_train, y_train)

    def predict(self, X_test: np.ndarray) -> np.ndarray:
        """
        Make predictions using the model.

        Args:
        - X_test (np.ndarray): The testing data.

        Returns:
        - np.ndarray: The predictions.
        """
        return self.model.predict(X_test)


class ProofOfIntelligence:
    def __init__(self, blockchain: Blockchain, model: Model):
        """
        Initialize the Proof of Intelligence consensus mechanism.

        Args:
        - blockchain (Blockchain): The blockchain to use.
        - model (Model): The model to use for AI tasks.
        """
        self.blockchain = blockchain
        self.model = model

    def train_model(self, X_train: np.ndarray, y_train: np.ndarray):
        """
        Train the model and add a new block to the chain.

        Args:
        - X_train (np.ndarray): The training data.
        - y_train (np.ndarray): The training labels.
        """
        try:
            self.model.train(X_train, y_train)
            new_block = Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, time.time(), {"task": "model_training"})
            self.blockchain.add_block(new_block)
        except Exception as e:
            print(f"Error training model: {e}")

    def make_inference(self, X_test: np.ndarray) -> np.ndarray:
        """
        Make predictions using the model and add a new block to the chain.

        Args:
        - X_test (np.ndarray): The testing data.

        Returns:
        - np.ndarray: The predictions.
        """
        try:
            predictions = self.model.predict(X_test)
            new_block = Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, time.time(), {"task": "model_inference"})
            self.blockchain.add_block(new_block)
            return predictions
        except Exception as e:
            print(f"Error making inference: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Create a blockchain
    blockchain = Blockchain()

    # Create a model
    model = Model()

    # Create a Proof of Intelligence instance
    poi = ProofOfIntelligence(blockchain, model)

    # Generate some data
    X = np.random.rand(100, 1)
    y = 3 * X + 2

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    poi.train_model(X_train, y_train)

    # Make predictions
    predictions = poi.make_inference(X_test)

    # Check if the chain is valid
    print(f"Is chain valid? {blockchain.is_chain_valid()}")

    # Evaluate the model
    if predictions is not None:
        mse = mean_squared_error(y_test, predictions)
        print(f"Mean squared error: {mse}")
```
