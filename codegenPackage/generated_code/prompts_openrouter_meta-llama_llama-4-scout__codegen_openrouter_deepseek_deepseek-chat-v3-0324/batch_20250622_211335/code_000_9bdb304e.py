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
from typing import List, Dict, Any, Optional
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
import os

class Block:
    """
    A block in the blockchain containing transactions and PoI consensus data.
    """
    def __init__(self, index: int, transactions: List[Dict], timestamp: float, previous_hash: str, model_hash: str, nonce: int = 0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.model_hash = model_hash
        self.nonce = nonce

    def compute_hash(self) -> str:
        """
        Compute the SHA-256 hash of the block.
        """
        block_string = json.dumps({
            "index": self.index,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "model_hash": self.model_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    """
    A blockchain implementing the Proof of Intelligence (PoI) consensus mechanism.
    """
    def __init__(self):
        self.chain: List[Block] = []
        self.current_transactions: List[Dict] = []
        self.nodes = set()
        self.model = None
        self.model_file = "poi_model.pkl"
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Create the genesis block (first block) of the blockchain.
        """
        genesis_block = Block(0, [], time.time(), "0", "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def add_block(self, block: Block, proof: str) -> bool:
        """
        Add a new block to the blockchain after validation.
        """
        previous_hash = self.last_block.hash
        if previous_hash != block.previous_hash:
            return False
        if not self.is_valid_proof(block, proof):
            return False
        block.hash = proof
        self.chain.append(block)
        self.current_transactions = []
        return True

    def is_valid_proof(self, block: Block, block_hash: str) -> bool:
        """
        Validate the Proof of Intelligence (PoI) for a block.
        """
        return (
            block_hash.startswith("0000") and
            block_hash == block.compute_hash() and
            block.model_hash == self.compute_model_hash()
        )

    def compute_model_hash(self) -> str:
        """
        Compute the hash of the current AI model.
        """
        if self.model is None:
            return "0"
        model_bytes = pickle.dumps(self.model)
        return hashlib.sha256(model_bytes).hexdigest()

    def proof_of_intelligence(self, last_block: Block) -> int:
        """
        Proof of Intelligence (PoI) consensus mechanism.
        """
        last_hash = last_block.hash
        nonce = 0
        while True:
            block = Block(
                last_block.index + 1,
                self.current_transactions,
                time.time(),
                last_hash,
                self.compute_model_hash(),
                nonce
            )
            block_hash = block.compute_hash()
            if block_hash.startswith("0000"):
                return nonce, block_hash
            nonce += 1

    def train_model(self, data_path: str = "data.csv"):
        """
        Train the AI model using the provided dataset.
        """
        try:
            data = pd.read_csv(data_path)
            X = data.iloc[:, :-1].values
            y = data.iloc[:, -1].values
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
            
            self.model = RandomForestClassifier(n_estimators=100)
            self.model.fit(X_train, y_train)
            
            y_pred = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            print(f"Model trained with accuracy: {accuracy:.2f}")
            
            with open(self.model_file, "wb") as f:
                pickle.dump(self.model, f)
        except Exception as e:
            print(f"Error during model training: {e}")

    def load_model(self):
        """
        Load the trained AI model from file.
        """
        try:
            if os.path.exists(self.model_file):
                with open(self.model_file, "rb") as f:
                    self.model = pickle.load(f)
        except Exception as e:
            print(f"Error loading model: {e}")

    def predict(self, input_data: List[float]) -> Optional[int]:
        """
        Make a prediction using the trained AI model.
        """
        if self.model is None:
            self.load_model()
        if self.model is None:
            print("Model not trained or loaded.")
            return None
        try:
            return self.model.predict([input_data])[0]
        except Exception as e:
            print(f"Error during prediction: {e}")
            return None

    @property
    def last_block(self) -> Block:
        """
        Get the last block in the blockchain.
        """
        return self.chain[-1]

    def add_transaction(self, sender: str, recipient: str, amount: float) -> int:
        """
        Add a new transaction to the current block.
        """
        self.current_transactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount,
            "timestamp": time.time()
        })
        return self.last_block.index + 1

    def mine(self) -> bool:
        """
        Mine a new block using PoI consensus.
        """
        if not self.current_transactions:
            return False
        
        last_block = self.last_block
        nonce, proof = self.proof_of_intelligence(last_block)
        
        new_block = Block(
            last_block.index + 1,
            self.current_transactions,
            time.time(),
            last_block.hash,
            self.compute_model_hash(),
            nonce
        )
        
        return self.add_block(new_block, proof)

    def is_chain_valid(self) -> bool:
        """
        Validate the entire blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            if current_block.hash != current_block.compute_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
            if not self.is_valid_proof(current_block, current_block.hash):
                return False
        return True

# Example usage
if __name__ == "__main__":
    blockchain = Blockchain()
    
    # Train the AI model
    blockchain.train_model()
    
    # Add some transactions
    blockchain.add_transaction("Alice", "Bob", 1.0)
    blockchain.add_transaction("Bob", "Charlie", 2.5)
    
    # Mine a new block
    blockchain.mine()
    
    # Make a prediction
    prediction = blockchain.predict([5.1, 3.5, 1.4, 0.2])
    print(f"Model prediction: {prediction}")
    
    # Validate the blockchain
    print(f"Blockchain valid: {blockchain.is_chain_valid()}")
```
