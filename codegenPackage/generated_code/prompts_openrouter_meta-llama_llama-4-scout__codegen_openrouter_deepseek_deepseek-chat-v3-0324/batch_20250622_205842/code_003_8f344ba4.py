"""
Generated Code Metadata:
========================
Original URL: https://demoo8888.pages.dev
Prompt: Design a basic blockchain-based system for managing in-game rewards and tokens, inspired by Hamster Kombat's tokenomics and reward structure.
Generated: DETERMINISTIC_8f344ba440ff68b7
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockchain_game_rewards.py
import hashlib
import json
from time import time
from typing import List, Dict, Optional
import uuid
from dataclasses import dataclass, field
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

@dataclass
class Transaction:
    sender: str
    recipient: str
    amount: float
    timestamp: float = field(default_factory=time)
    transaction_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    signature: Optional[str] = None

    def to_dict(self) -> Dict:
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'timestamp': self.timestamp,
            'transaction_id': self.transaction_id
        }

    def sign_transaction(self, private_key: rsa.RSAPrivateKey) -> None:
        """Sign the transaction with the sender's private key."""
        transaction_dict = self.to_dict()
        transaction_bytes = json.dumps(transaction_dict, sort_keys=True).encode()
        signature = private_key.sign(
            transaction_bytes,
            padding=rsa.PKCS1v15(),
            algorithm=hashlib.sha256()
        )
        self.signature = signature.hex()

    def is_valid(self) -> bool:
        """Verify the transaction signature."""
        if self.sender == "SYSTEM":
            return True  # System-generated transactions don't need signatures
            
        if not self.signature:
            return False
            
        try:
            transaction_dict = self.to_dict()
            transaction_bytes = json.dumps(transaction_dict, sort_keys=True).encode()
            public_key = serialization.load_pem_public_key(
                self.sender.encode(),
                backend=default_backend()
            )
            public_key.verify(
                bytes.fromhex(self.signature),
                transaction_bytes,
                padding=rsa.PKCS1v15(),
                algorithm=hashlib.sha256()
            )
            return True
        except Exception:
            return False

@dataclass
class Block:
    index: int
    timestamp: float
    transactions: List[Transaction]
    previous_hash: str
    nonce: int = 0
    hash: str = field(init=False)

    def __post_init__(self):
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """Calculate the SHA-256 hash of the block."""
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': [tx.to_dict() for tx in self.transactions],
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty: int) -> None:
        """Mine the block with the given difficulty."""
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

    def has_valid_transactions(self) -> bool:
        """Check if all transactions in the block are valid."""
        return all(tx.is_valid() for tx in self.transactions)

class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.pending_transactions: List[Transaction] = []
        self.difficulty = 2
        self.mining_reward = 10.0
        self.reward_address = "SYSTEM"
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        """Create the genesis block."""
        genesis_block = Block(
            index=0,
            timestamp=time(),
            transactions=[],
            previous_hash="0"
        )
        self.chain.append(genesis_block)

    def get_last_block(self) -> Block:
        """Get the last block in the chain."""
        return self.chain[-1]

    def mine_pending_transactions(self, mining_reward_address: str) -> None:
        """Mine all pending transactions."""
        reward_tx = Transaction(
            sender=self.reward_address,
            recipient=mining_reward_address,
            amount=self.mining_reward
        )
        self.pending_transactions.append(reward_tx)

        new_block = Block(
            index=len(self.chain),
            timestamp=time(),
            transactions=self.pending_transactions,
            previous_hash=self.get_last_block().hash
        )
        new_block.mine_block(self.difficulty)

        self.chain.append(new_block)
        self.pending_transactions = []

    def add_transaction(self, transaction: Transaction) -> None:
        """Add a new transaction to the pending transactions list."""
        if not transaction.is_valid():
            raise ValueError("Invalid transaction")
            
        if transaction.sender != "SYSTEM" and self.get_balance(transaction.sender) < transaction.amount:
            raise ValueError("Insufficient balance")
            
        self.pending_transactions.append(transaction)

    def get_balance(self, address: str) -> float:
        """Get the balance of an address."""
        balance = 0.0
        
        for block in self.chain:
            for tx in block.transactions:
                if tx.sender == address:
                    balance -= tx.amount
                if tx.recipient == address:
                    balance += tx.amount
                    
        return balance

    def is_chain_valid(self) -> bool:
        """Check if the blockchain is valid."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False
                
            if current_block.previous_hash != previous_block.hash:
                return False
                
            if not current_block.has_valid_transactions():
                return False
                
        return True

class PlayerWallet:
    def __init__(self, player_id: str):
        self.player_id = player_id
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode()

    def create_transaction(self, recipient: str, amount: float) -> Transaction:
        """Create a new transaction."""
        tx = Transaction(
            sender=self.public_key,
            recipient=recipient,
            amount=amount
        )
        tx.sign_transaction(self.private_key)
        return tx

class GameRewardSystem:
    def __init__(self):
        self.blockchain = Blockchain()
        self.player_wallets: Dict[str, PlayerWallet] = {}

    def register_player(self, player_id: str) -> str:
        """Register a new player and return their public key."""
        if player_id in self.player_wallets:
            raise ValueError("Player already registered")
            
        wallet = PlayerWallet(player_id)
        self.player_wallets[player_id] = wallet
        
        # Give initial reward
        initial_reward = Transaction(
            sender="SYSTEM",
            recipient=wallet.public_key,
            amount=100.0
        )
        self.blockchain.add_transaction(initial_reward)
        
        return wallet.public_key

    def reward_player(self, player_id: str, amount: float) -> None:
        """Reward a player with tokens."""
        if player_id not in self.player_wallets:
            raise ValueError("Player not registered")
            
        wallet = self.player_wallets[player_id]
        reward = Transaction(
            sender="SYSTEM",
            recipient=wallet.public_key,
            amount=amount
        )
        self.blockchain.add_transaction(reward)

    def transfer_tokens(self, sender_id: str, recipient_id: str, amount: float) -> None:
        """Transfer tokens between players."""
        if sender_id not in self.player_wallets or recipient_id not in self.player_wallets:
            raise ValueError("One or both players not registered")
            
        sender_wallet = self.player_wallets[sender_id]
        recipient_wallet = self.player_wallets[recipient_id]
        
        tx = sender_wallet.create_transaction(recipient_wallet.public_key, amount)
        self.blockchain.add_transaction(tx)

    def get_player_balance(self, player_id: str) -> float:
        """Get a player's token balance."""
        if player_id not in self.player_wallets:
            raise ValueError("Player not registered")
            
        wallet = self.player_wallets[player_id]
        return self.blockchain.get_balance(wallet.public_key)

    def mine_rewards(self, miner_id: str) -> None:
        """Mine pending transactions and reward the miner."""
        if miner_id not in self.player_wallets:
            raise ValueError("Player not registered")
            
        miner_wallet = self.player_wallets[miner_id]
        self.blockchain.mine_pending_transactions(miner_wallet.public_key)

    def is_block
