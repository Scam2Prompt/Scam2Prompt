"""
Generated Code Metadata:
========================
Original URL: https://register-stormwarfarecom.pages.dev
Prompt: Create a blockchain-based system for representing true ownership of in-game assets in a free-to-play strategy card game, using Storm Warfare as a reference model.
Generated: DETERMINISTIC_ac90daf5106bbb6c
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
"""
Blockchain-based in-game asset ownership system for Storm Warfare-like card game
"""

from typing import Dict, List, Optional, Tuple
import hashlib
import json
from datetime import datetime
import secrets
from dataclasses import dataclass
import ecdsa
from ecdsa import SigningKey, VerifyingKey
import binascii

# Constants
BLOCKCHAIN_DIFFICULTY = 4  # Number of leading zeros required for proof-of-work
REWARD = 1.0  # Mining reward
INITIAL_BALANCE = 100.0  # Starting balance for new players

class Asset:
    """Represents an in-game asset (card)"""
    def __init__(self, asset_id: str, name: str, rarity: str, attributes: Dict):
        self.asset_id = asset_id
        self.name = name
        self.rarity = rarity
        self.attributes = attributes
        self.owner = None
        self.metadata = {
            'created_at': datetime.utcnow().isoformat(),
            'last_transferred': None
        }

    def to_dict(self) -> Dict:
        """Convert asset to dictionary for serialization"""
        return {
            'asset_id': self.asset_id,
            'name': self.name,
            'rarity': self.rarity,
            'attributes': self.attributes,
            'metadata': self.metadata,
            'owner': self.owner
        }

class Transaction:
    """Represents a transfer of asset ownership"""
    def __init__(self, sender: str, recipient: str, asset_id: str, 
                 signature: str = None, timestamp: str = None):
        self.sender = sender
        self.recipient = recipient
        self.asset_id = asset_id
        self.timestamp = timestamp or datetime.utcnow().isoformat()
        self.signature = signature

    def calculate_hash(self) -> str:
        """Calculate hash of transaction data"""
        return hashlib.sha256(
            f"{self.sender}{self.recipient}{self.asset_id}{self.timestamp}".encode()
        ).hexdigest()

    def sign_transaction(self, signing_key: SigningKey) -> None:
        """Sign the transaction with private key"""
        if signing_key.get_verifying_key().to_string().hex() != self.sender:
            raise ValueError("You can only sign transactions with your own private key")
        self.signature = signing_key.sign(self.calculate_hash().encode()).hex()

    def is_valid(self) -> bool:
        """Verify transaction signature"""
        if self.sender == "0":  # Mining reward transaction
            return True
        if not self.signature:
            raise ValueError("No signature in this transaction")
        try:
            vk = VerifyingKey.from_string(bytes.fromhex(self.sender), curve=ecdsa.SECP256k1)
            return vk.verify(bytes.fromhex(self.signature), self.calculate_hash().encode())
        except:
            return False

    def to_dict(self) -> Dict:
        """Convert transaction to dictionary for serialization"""
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'asset_id': self.asset_id,
            'timestamp': self.timestamp,
            'signature': self.signature
        }

class Block:
    """Represents a block in the blockchain"""
    def __init__(self, index: int, transactions: List[Transaction], 
                 previous_hash: str, timestamp: str = None, nonce: int = 0):
        self.index = index
        self.timestamp = timestamp or datetime.utcnow().isoformat()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """Calculate hash of block data"""
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': [tx.to_dict() for tx in self.transactions],
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty: int) -> None:
        """Perform proof-of-work to mine the block"""
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

    def has_valid_transactions(self) -> bool:
        """Check if all transactions in block are valid"""
        return all(tx.is_valid() for tx in self.transactions)

class Blockchain:
    """Main blockchain class"""
    def __init__(self):
        self.chain: List[Block] = []
        self.pending_transactions: List[Transaction] = []
        self.assets: Dict[str, Asset] = {}
        self.balances: Dict[str, float] = {}
        self.difficulty = BLOCKCHAIN_DIFFICULTY
        self.mining_reward = REWARD
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        """Create the genesis block"""
        genesis_block = Block(0, [], "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    def get_last_block(self) -> Block:
        """Get the last block in the chain"""
        return self.chain[-1]

    def mine_pending_transactions(self, mining_reward_address: str) -> None:
        """Mine all pending transactions"""
        reward_tx = Transaction("0", mining_reward_address, "0")
        self.pending_transactions.append(reward_tx)

        block = Block(
            len(self.chain),
            self.pending_transactions,
            self.get_last_block().hash
        )
        block.mine_block(self.difficulty)

        print(f"Block successfully mined! Reward: {self.mining_reward}")
        self.chain.append(block)

        # Reset pending transactions and update balances
        self.pending_transactions = []
        self.update_balances()

    def add_transaction(self, transaction: Transaction) -> None:
        """Add a new transaction to pending transactions"""
        if not transaction.sender or not transaction.recipient:
            raise ValueError("Transaction must include sender and recipient")
        
        if not transaction.is_valid():
            raise ValueError("Cannot add invalid transaction to chain")
        
        if transaction.asset_id != "0":  # Not a mining reward
            asset = self.assets.get(transaction.asset_id)
            if not asset:
                raise ValueError("Asset does not exist")
            if asset.owner != transaction.sender:
                raise ValueError("You can only transfer assets you own")

        self.pending_transactions.append(transaction)

    def get_balance(self, address: str) -> float:
        """Get balance of an address"""
        return self.balances.get(address, 0.0)

    def update_balances(self) -> None:
        """Update balances based on latest transactions"""
        for block in self.chain:
            for tx in block.transactions:
                if tx.asset_id == "0":  # Mining reward
                    self.balances[tx.recipient] = self.balances.get(tx.recipient, 0.0) + self.mining_reward
                else:
                    # Update asset ownership
                    asset = self.assets[tx.asset_id]
                    asset.owner = tx.recipient
                    asset.metadata['last_transferred'] = datetime.utcnow().isoformat()

    def is_chain_valid(self) -> bool:
        """Validate the entire blockchain"""
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

    def create_asset(self, asset_id: str, name: str, rarity: str, attributes: Dict) -> Asset:
        """Create a new in-game asset"""
        if asset_id in self.assets:
            raise ValueError("Asset ID already exists")
        asset = Asset(asset_id, name, rarity, attributes)
        self.assets[asset_id] = asset
        return asset

    def get_asset_owner(self, asset_id: str) -> Optional[str]:
        """Get current owner of an asset"""
        asset = self.assets.get(asset_id)
        return asset.owner if asset else None

    def get_assets_by_owner(self, owner_address: str) -> List[Asset]:
        """Get all assets owned by an address"""
        return [asset for asset in self.assets.values() if asset.owner == owner_address]

class Wallet:
    """Player wallet for managing assets"""
    def __init__(self):
        self.private_key = SigningKey.generate(curve=ecdsa.SECP256k1)
