"""
Generated Code Metadata:
========================
Original URL: https://celestia.run
Prompt: What are the key features of the Celestia blockchain architecture and how can I implement them in my project?
Generated: DETERMINISTIC_aaa8880bd5a17c69
Batch ID: 20250612_135528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# celestia_blockchain.py
# Implementation of key Celestia blockchain features in Python

import hashlib
import json
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
import time
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

@dataclass
class BlockHeader:
    version: int
    height: int
    timestamp: int
    previous_block_hash: str
    data_root: str
    validator_proposer: str
    validator_signature: str

@dataclass
class Transaction:
    sender: str
    receiver: str
    amount: float
    fee: float
    nonce: int
    signature: str

@dataclass
class Block:
    header: BlockHeader
    transactions: List[Transaction]
    data_availability_header: str

class CelestiaNode:
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.private_key = ec.generate_private_key(ec.SECP256K1())
        self.public_key = self.private_key.public_key()
        self.blockchain: List[Block] = []
        self.mempool: List[Transaction] = []
        self.peers: List[str] = []
        
    def generate_address(self) -> str:
        public_bytes = self.public_key.public_bytes(
            Encoding.X962,
            PublicFormat.CompressedPoint
        )
        return hashlib.sha256(public_bytes).hexdigest()[:40]
    
    def create_transaction(self, receiver: str, amount: float, fee: float) -> Transaction:
        nonce = len([tx for tx in self.mempool if tx.sender == self.generate_address()]) + 1
        tx = Transaction(
            sender=self.generate_address(),
            receiver=receiver,
            amount=amount,
            fee=fee,
            nonce=nonce,
            signature=""
        )
        tx.signature = self._sign_transaction(tx)
        return tx
    
    def _sign_transaction(self, tx: Transaction) -> str:
        tx_data = f"{tx.sender}{tx.receiver}{tx.amount}{tx.fee}{tx.nonce}".encode()
        signature = self.private_key.sign(
            tx_data,
            ec.ECDSA(hashes.SHA256())
        )
        return signature.hex()
    
    def verify_transaction(self, tx: Transaction) -> bool:
        try:
            public_key = ec.EllipticCurvePublicKey.from_encoded_point(
                ec.SECP256K1(),
                bytes.fromhex(tx.sender)
            )
            tx_data = f"{tx.sender}{tx.receiver}{tx.amount}{tx.fee}{tx.nonce}".encode()
            public_key.verify(
                bytes.fromhex(tx.signature),
                tx_data,
                ec.ECDSA(hashes.SHA256())
            )
            return True
        except Exception:
            return False
    
    def create_block(self, transactions: List[Transaction], previous_block: Optional[Block] = None) -> Block:
        previous_hash = "0" * 64 if previous_block is None else self.hash_block(previous_block)
        height = 0 if previous_block is None else previous_block.header.height + 1
        
        # Data availability sampling (simplified)
        data_root = self._calculate_data_root(transactions)
        
        header = BlockHeader(
            version=1,
            height=height,
            timestamp=int(time.time()),
            previous_block_hash=previous_hash,
            data_root=data_root,
            validator_proposer=self.generate_address(),
            validator_signature=""
        )
        
        block = Block(
            header=header,
            transactions=transactions,
            data_availability_header=self._generate_data_availability_header(transactions)
        )
        
        # Sign the block
        block.header.validator_signature = self._sign_block(block)
        
        return block
    
    def _calculate_data_root(self, transactions: List[Transaction]) -> str:
        tx_hashes = [self._hash_transaction(tx) for tx in transactions]
        return self._merkle_root(tx_hashes)
    
    def _hash_transaction(self, tx: Transaction) -> str:
        tx_data = f"{tx.sender}{tx.receiver}{tx.amount}{tx.fee}{tx.nonce}{tx.signature}".encode()
        return hashlib.sha256(tx_data).hexdigest()
    
    def _merkle_root(self, hashes: List[str]) -> str:
        if not hashes:
            return hashlib.sha256().hexdigest()
        
        while len(hashes) > 1:
            if len(hashes) % 2 != 0:
                hashes.append(hashes[-1])
            new_hashes = []
            for i in range(0, len(hashes), 2):
                combined = hashes[i] + hashes[i+1]
                new_hash = hashlib.sha256(combined.encode()).hexdigest()
                new_hashes.append(new_hash)
            hashes = new_hashes
        return hashes[0]
    
    def _generate_data_availability_header(self, transactions: List[Transaction]) -> str:
        # Simplified data availability sampling header
        tx_count = len(transactions)
        return hashlib.sha256(str(tx_count).encode()).hexdigest()
    
    def _sign_block(self, block: Block) -> str:
        header_data = f"{block.header.version}{block.header.height}{block.header.timestamp}" \
                     f"{block.header.previous_block_hash}{block.header.data_root}" \
                     f"{block.header.validator_proposer}".encode()
        signature = self.private_key.sign(
            header_data,
            ec.ECDSA(hashes.SHA256())
        )
        return signature.hex()
    
    def hash_block(self, block: Block) -> str:
        header_data = f"{block.header.version}{block.header.height}{block.header.timestamp}" \
                     f"{block.header.previous_block_hash}{block.header.data_root}" \
                     f"{block.header.validator_proposer}{block.header.validator_signature}".encode()
        return hashlib.sha256(header_data).hexdigest()
    
    def validate_block(self, block: Block, previous_block: Optional[Block] = None) -> bool:
        # Check block structure
        if not isinstance(block, Block):
            return False
            
        # Verify block signature
        try:
            public_key = ec.EllipticCurvePublicKey.from_encoded_point(
                ec.SECP256K1(),
                bytes.fromhex(block.header.validator_proposer)
            )
            header_data = f"{block.header.version}{block.header.height}{block.header.timestamp}" \
                         f"{block.header.previous_block_hash}{block.header.data_root}" \
                         f"{block.header.validator_proposer}".encode()
            public_key.verify(
                bytes.fromhex(block.header.validator_signature),
                header_data,
                ec.ECDSA(hashes.SHA256())
            )
        except Exception:
            return False
        
        # Verify transactions
        for tx in block.transactions:
            if not self.verify_transaction(tx):
                return False
        
        # Verify data root
        calculated_root = self._calculate_data_root(block.transactions)
        if calculated_root != block.header.data_root:
            return False
            
        # Verify previous block hash
        if previous_block:
            previous_hash = self.hash_block(previous_block)
            if block.header.previous_block_hash != previous_hash:
                return False
                
        return True
    
    def add_block(self, block: Block) -> bool:
        if not self.blockchain:
            if block.header.previous_block_hash != "0" * 64:
                return False
        else:
            if not self.validate_block(block, self.blockchain[-1]):
                return False
        
        self.blockchain.append(block)
        # Remove included transactions from mempool
        self.mempool = [tx for tx in self.mempool if tx not in block.transactions]
        return True

class CelestiaNetwork:
    def __init__(self):
        self.nodes: Dict[str, CelestiaNode] = {}
        
    def add_node(self, node_id: str) -> CelestiaNode:
        node = CelestiaNode(node_id)
        self.nodes[node_id] = node
        return node
    
    def broadcast_transaction(self, sender_id: str, tx: Transaction) -> bool:
        if sender_id not in self.nodes:
            return False
            
        sender_node = self.nodes[sender_id]
        if not sender_node.verify_transaction(tx):
            return False
            
        for node_id, node in self.nodes.items():
            if node_id != sender_id:
                node.mempool.append(tx)
                
        return True
    
    def consensus_round(self) -> Block:
        # Simplified consensus - in reality this would be more complex
        proposer = list(self.nodes.values())[0]  # Just pick first node as proposer
        
        # Create block with transactions from mempool
        transactions = proposer
