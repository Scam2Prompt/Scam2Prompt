"""
Generated Code Metadata:
========================
Original URL: https://njax.pages.dev
Prompt: Design a decentralized protocol for staking issues, including claim airdrop and NFT minting/transfer related issues, on a secure server.
Generated: DETERMINISTIC_cca0cdb1bbe552a9
Batch ID: 20250622_211458
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
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import secrets
import requests
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest, Forbidden, NotFound

# Constants
BLOCK_TIME = 15  # seconds
STAKE_REWARD_RATE = 0.05  # 5%
AIRDROP_AMOUNT = 100  # tokens
NFT_MINT_COST = 10  # tokens

class TransactionType(Enum):
    STAKE = "STAKE"
    UNSTAKE = "UNSTAKE"
    CLAIM_AIRDROP = "CLAIM_AIRDROP"
    MINT_NFT = "MINT_NFT"
    TRANSFER_NFT = "TRANSFER_NFT"

@dataclass
class Transaction:
    tx_type: TransactionType
    sender: str
    receiver: Optional[str] = None
    amount: Optional[float] = None
    nft_id: Optional[str] = None
    timestamp: float = time.time()
    signature: Optional[str] = None

@dataclass
class Block:
    index: int
    timestamp: float
    transactions: List[Transaction]
    previous_hash: str
    nonce: int = 0
    hash: Optional[str] = None

@dataclass
class NFT:
    id: str
    owner: str
    metadata: Dict

class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.pending_transactions: List[Transaction] = []
        self.stakes: Dict[str, float] = {}  # address -> staked amount
        self.balances: Dict[str, float] = {}  # address -> balance
        self.nfts: Dict[str, NFT] = {}  # nft_id -> NFT
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(
            index=0,
            timestamp=time.time(),
            transactions=[],
            previous_hash="0"
        )
        genesis_block.hash = self.calculate_block_hash(genesis_block)
        self.chain.append(genesis_block)

    def calculate_block_hash(self, block: Block) -> str:
        block_data = {
            "index": block.index,
            "timestamp": block.timestamp,
            "transactions": [tx.__dict__ for tx in block.transactions],
            "previous_hash": block.previous_hash,
            "nonce": block.nonce
        }
        return hashlib.sha256(json.dumps(block_data, sort_keys=True).encode()).hexdigest()

    def mine_block(self) -> Block:
        last_block = self.chain[-1]
        new_block = Block(
            index=last_block.index + 1,
            timestamp=time.time(),
            transactions=self.pending_transactions,
            previous_hash=last_block.hash,
            nonce=0
        )

        # Proof of Work
        while True:
            new_block.hash = self.calculate_block_hash(new_block)
            if new_block.hash.startswith("0000"):
                break
            new_block.nonce += 1

        # Process transactions
        for tx in new_block.transactions:
            self.process_transaction(tx)

        self.chain.append(new_block)
        self.pending_transactions = []
        return new_block

    def process_transaction(self, tx: Transaction):
        if tx.tx_type == TransactionType.STAKE:
            self.stakes[tx.sender] = self.stakes.get(tx.sender, 0) + tx.amount
            self.balances[tx.sender] = self.balances.get(tx.sender, 0) - tx.amount
        elif tx.tx_type == TransactionType.UNSTAKE:
            self.stakes[tx.sender] = max(0, self.stakes.get(tx.sender, 0) - tx.amount)
            self.balances[tx.sender] = self.balances.get(tx.sender, 0) + tx.amount
        elif tx.tx_type == TransactionType.CLAIM_AIRDROP:
            self.balances[tx.sender] = self.balances.get(tx.sender, 0) + AIRDROP_AMOUNT
        elif tx.tx_type == TransactionType.MINT_NFT:
            if tx.amount < NFT_MINT_COST:
                raise ValueError("Insufficient funds for NFT minting")
            self.balances[tx.sender] = self.balances.get(tx.sender, 0) - NFT_MINT_COST
            self.nfts[tx.nft_id] = NFT(id=tx.nft_id, owner=tx.sender, metadata={})
        elif tx.tx_type == TransactionType.TRANSFER_NFT:
            if tx.nft_id not in self.nfts:
                raise ValueError("NFT does not exist")
            if self.nfts[tx.nft_id].owner != tx.sender:
                raise ValueError("Not the owner of the NFT")
            self.nfts[tx.nft_id].owner = tx.receiver

    def validate_transaction(self, tx: Transaction) -> bool:
        # Check signature if applicable
        if tx.signature and not self.verify_signature(tx.sender, tx.signature, tx.__dict__):
            return False

        if tx.tx_type == TransactionType.STAKE:
            return self.balances.get(tx.sender, 0) >= tx.amount
        elif tx.tx_type == TransactionType.UNSTAKE:
            return self.stakes.get(tx.sender, 0) >= tx.amount
        elif tx.tx_type == TransactionType.MINT_NFT:
            return tx.nft_id not in self.nfts and self.balances.get(tx.sender, 0) >= NFT_MINT_COST
        elif tx.tx_type == TransactionType.TRANSFER_NFT:
            return tx.nft_id in self.nfts and self.nfts[tx.nft_id].owner == tx.sender
        return True

    def verify_signature(self, address: str, signature: str, data: Dict) -> bool:
        # In a real implementation, this would verify the cryptographic signature
        return True  # Simplified for this example

    def distribute_staking_rewards(self):
        total_staked = sum(self.stakes.values())
        if total_staked == 0:
            return

        reward_per_token = (total_staked * STAKE_REWARD_RATE) / total_staked
        for address, amount in self.stakes.items():
            self.balances[address] = self.balances.get(address, 0) + (amount * reward_per_token)

# Flask App Setup
app = Flask(__name__)
blockchain = Blockchain()

@app.route('/transaction', methods=['POST'])
def create_transaction():
    data = request.get_json()
    try:
        tx = Transaction(
            tx_type=TransactionType(data['tx_type']),
            sender=data['sender'],
            receiver=data.get('receiver'),
            amount=data.get('amount'),
            nft_id=data.get('nft_id'),
            signature=data.get('signature')
        )
    except (KeyError, ValueError) as e:
        raise BadRequest(f"Invalid transaction data: {str(e)}")

    if not blockchain.validate_transaction(tx):
        raise Forbidden("Transaction validation failed")

    blockchain.pending_transactions.append(tx)
    return jsonify({"message": "Transaction added to pending", "tx_hash": hashlib.sha256(str(tx.__dict__).encode()).hexdigest()}), 201

@app.route('/mine', methods=['POST'])
def mine():
    if not blockchain.pending_transactions:
        raise BadRequest("No transactions to mine")

    block = blockchain.mine_block()
    blockchain.distribute_staking_rewards()
    return jsonify({
        "message": "New block mined",
        "block": {
            "index": block.index,
            "hash": block.hash,
            "transactions": len(block.transactions)
        }
    }), 200

@app.route('/chain', methods=['GET'])
def get_chain():
    return jsonify({
        "chain": [{
            "index": block.index,
            "hash": block.hash,
            "previous_hash": block.previous_hash,
            "transactions": len(block.transactions)
        } for block in blockchain.chain],
        "length": len(blockchain.chain)
    }), 200

@app.route('/balance/<address>', methods=['GET'])
def get_balance(address: str):
    return jsonify({
        "address": address,
        "balance": blockchain.balances.get(address, 0),
        "staked": blockchain.stakes.get(address, 0)
    }), 200

@app.route('/nft/<nft_id>', methods=['GET'])
def get_nft(nft_id: str):
    if nft_id not in blockchain.nfts:
        raise NotFound("NFT not found")
