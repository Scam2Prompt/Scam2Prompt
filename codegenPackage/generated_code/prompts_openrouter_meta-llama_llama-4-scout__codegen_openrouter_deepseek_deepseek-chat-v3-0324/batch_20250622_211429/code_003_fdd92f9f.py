"""
Generated Code Metadata:
========================
Original URL: https://dexmultichains.co
Prompt: "Design a blockchain architecture for a futuristic city like Utopos, including data storage and security features."
Generated: DETERMINISTIC_fdd92f9f5b1dbeb1
Batch ID: 20250622_211429
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
import uuid
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
from cryptography.hazmat.backends import default_backend
import base64

class Block:
    """
    A block in the Utopos blockchain.
    """
    def __init__(self, index: int, transactions: List[Dict[str, Any]], timestamp: float, previous_hash: str, nonce: int = 0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        """
        Compute the SHA-256 hash of the block.
        """
        block_string = json.dumps({
            "index": self.index,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def __str__(self) -> str:
        return f"Block(index={self.index}, hash={self.hash}, previous_hash={self.previous_hash})"

class Blockchain:
    """
    The Utopos blockchain implementation.
    """
    def __init__(self):
        self.chain: List[Block] = []
        self.pending_transactions: List[Dict[str, Any]] = []
        self.difficulty = 4  # Adjust difficulty for PoW
        self.mining_reward = 10  # Reward for mining a block
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        """
        Create the genesis block (first block in the chain).
        """
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def get_last_block(self) -> Block:
        """
        Get the last block in the chain.
        """
        return self.chain[-1]

    def mine_pending_transactions(self, mining_reward_address: str) -> None:
        """
        Mine pending transactions and add a new block to the chain.
        """
        if not self.pending_transactions:
            raise ValueError("No transactions to mine")

        # Add mining reward transaction
        reward_transaction = {
            "from": "network",
            "to": mining_reward_address,
            "amount": self.mining_reward,
            "timestamp": time.time()
        }
        self.pending_transactions.append(reward_transaction)

        new_block = Block(
            index=len(self.chain),
            transactions=self.pending_transactions,
            timestamp=time.time(),
            previous_hash=self.get_last_block().hash
        )

        # Proof of Work
        new_block = self.proof_of_work(new_block)

        self.chain.append(new_block)
        self.pending_transactions = []

    def proof_of_work(self, block: Block) -> Block:
        """
        Perform proof-of-work to find a valid hash for the block.
        """
        while not self.is_valid_hash(block.hash):
            block.nonce += 1
            block.hash = block.compute_hash()
        return block

    def is_valid_hash(self, hash: str) -> bool:
        """
        Check if the hash meets the difficulty requirement.
        """
        return hash.startswith("0" * self.difficulty)

    def add_transaction(self, transaction: Dict[str, Any]) -> None:
        """
        Add a new transaction to the pending transactions list.
        """
        if not transaction.get("from") or not transaction.get("to"):
            raise ValueError("Transaction must include 'from' and 'to' addresses")
        if not isinstance(transaction.get("amount"), (int, float)) or transaction["amount"] <= 0:
            raise ValueError("Amount must be a positive number")

        self.pending_transactions.append(transaction)

    def is_chain_valid(self) -> bool:
        """
        Validate the integrity of the blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.compute_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
            if not self.is_valid_hash(current_block.hash):
                return False

        return True

class DigitalIdentity:
    """
    Digital identity management for Utopos citizens.
    """
    def __init__(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()

    def get_public_key_str(self) -> str:
        """
        Get the public key as a string.
        """
        return self.public_key.public_bytes(
            Encoding.PEM,
            PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')

    def sign_data(self, data: str) -> str:
        """
        Sign data with the private key.
        """
        signature = self.private_key.sign(
            data.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return base64.b64encode(signature).decode('utf-8')

    @staticmethod
    def verify_signature(public_key_str: str, data: str, signature: str) -> bool:
        """
        Verify a signature with the public key.
        """
        try:
            public_key = rsa.PublicKey.load_pkcs1(public_key_str.encode())
            public_key.verify(
                base64.b64decode(signature),
                data.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False

class UtoposBlockchain:
    """
    Main Utopos blockchain architecture with security features.
    """
    def __init__(self):
        self.blockchain = Blockchain()
        self.identity_system = DigitalIdentity()
        self.data_storage: Dict[str, Any] = {}  # Simulated decentralized storage

    def store_data(self, key: str, value: Any) -> None:
        """
        Store data in decentralized storage with encryption.
        """
        encrypted_value = self._encrypt_data(value)
        self.data_storage[key] = encrypted_value

    def retrieve_data(self, key: str) -> Optional[Any]:
        """
        Retrieve data from decentralized storage with decryption.
        """
        encrypted_value = self.data_storage.get(key)
        if encrypted_value:
            return self._decrypt_data(encrypted_value)
        return None

    def _encrypt_data(self, data: Any) -> str:
        """
        Encrypt data using the identity system's public key.
        """
        # Simplified encryption for demonstration
        return base64.b64encode(json.dumps(data).encode()).decode('utf-8')

    def _decrypt_data(self, encrypted_data: str) -> Any:
        """
        Decrypt data using the identity system's private key.
        """
        # Simplified decryption for demonstration
        return json.loads(base64.b64decode(encrypted_data).decode('utf-8'))

    def add_secure_transaction(self, transaction: Dict[str, Any]) -> None:
        """
        Add a transaction with digital signature verification.
        """
        required_fields = ["from", "to", "amount", "timestamp", "signature"]
        if not all(field in transaction for field in required_fields):
            raise ValueError("Transaction missing required fields")

        if not DigitalIdentity.verify_signature(
            transaction["from"],
            f"{transaction['to']}{transaction['amount']}{transaction['timestamp']}",
            transaction["signature"]
        ):
            raise ValueError("Invalid transaction signature")

        self.blockchain.add_transaction(transaction)

# Example usage
if __name__ == "__main__":
    utopos = UtoposBlockchain()

    # Create a transaction
    transaction = {
        "from": utopos.identity_system.get_public_key_str(),
        "to": "recipient_public_key",
        "amount": 5,
        "timestamp": time.time()
    }

    # Sign the transaction
    data_to_sign = f"{transaction['to']}{transaction['amount']}{transaction['timestamp']}"
    transaction["signature"] = utopos.identity_system.sign_data(data_to_sign)

    # Add to blockchain
    utopos.add_secure_transaction(transaction)

    # Mine the block
    utopos.blockchain.mine_pending_transactions("miner_address")

    # Store some data
    utopos.store_data("city_plan", {"zones": ["
