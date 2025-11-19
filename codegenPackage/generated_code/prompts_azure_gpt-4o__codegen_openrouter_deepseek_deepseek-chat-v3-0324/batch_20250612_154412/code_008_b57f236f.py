"""
Generated Code Metadata:
========================
Original URL: https://tomatoclub.xyz
Prompt: Develop a Python script to simulate distributed ledger transactions across multiple nodes, incorporating the key ideas from the "분산원장이 뭔데?" page from https://tomatoclub.xyz.
Generated: DETERMINISTIC_b57f236f1de97bed
Batch ID: 20250612_154412
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
import threading
from uuid import uuid4
from collections import defaultdict
import socket
import pickle
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class Block:
    """
    Represents a block in the distributed ledger.
    """
    def __init__(self, index: int, transactions: List[Dict[str, Any]], timestamp: float, previous_hash: str):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0
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

    def mine_block(self, difficulty: int) -> None:
        """
        Mine the block by finding a hash that meets the difficulty criteria.
        """
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.compute_hash()
        logger.info(f"Block mined: {self.hash}")

class DistributedLedger:
    """
    Represents a distributed ledger with consensus mechanism.
    """
    def __init__(self, node_id: str, port: int, peer_ports: List[int]):
        self.node_id = node_id
        self.port = port
        self.peer_ports = peer_ports
        self.chain: List[Block] = []
        self.current_transactions: List[Dict[str, Any]] = []
        self.nodes = set()
        self.difficulty = 4  # Proof of Work difficulty
        self.create_genesis_block()
        self.lock = threading.Lock()

    def create_genesis_block(self) -> None:
        """
        Create the genesis block (first block in the chain).
        """
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    def add_transaction(self, sender: str, recipient: str, amount: float) -> int:
        """
        Add a new transaction to the current transactions list.
        Returns the index of the block that will hold this transaction.
        """
        with self.lock:
            self.current_transactions.append({
                'sender': sender,
                'recipient': recipient,
                'amount': amount,
                'timestamp': time.time(),
                'transaction_id': str(uuid4())
            })
            return self.last_block.index + 1

    def mine_new_block(self) -> Block:
        """
        Mine a new block with the current transactions.
        """
        with self.lock:
            if not self.current_transactions:
                raise ValueError("No transactions to mine")

            last_block = self.last_block
            new_block = Block(
                index=last_block.index + 1,
                transactions=self.current_transactions,
                timestamp=time.time(),
                previous_hash=last_block.hash
            )
            new_block.mine_block(self.difficulty)
            self.chain.append(new_block)
            self.current_transactions = []
            return new_block

    @property
    def last_block(self) -> Block:
        """
        Get the last block in the chain.
        """
        return self.chain[-1]

    def validate_chain(self, chain: List[Block]) -> bool:
        """
        Validate the integrity of a blockchain.
        """
        for i in range(1, len(chain)):
            current_block = chain[i]
            previous_block = chain[i-1]

            if current_block.hash != current_block.compute_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def resolve_conflicts(self) -> bool:
        """
        Consensus algorithm: resolves conflicts by replacing our chain with the longest valid one.
        Returns True if our chain was replaced, False otherwise.
        """
        longest_chain = None
        max_length = len(self.chain)

        for node_port in self.peer_ports:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(2.0)
                    s.connect(('localhost', node_port))
                    s.sendall(pickle.dumps({'type': 'get_chain'}))
                    data = s.recv(4096)
                    response = pickle.loads(data)

                    if response['type'] == 'chain_response':
                        chain = response['chain']
                        if len(chain) > max_length and self.validate_chain(chain):
                            max_length = len(chain)
                            longest_chain = chain
            except Exception as e:
                logger.warning(f"Error communicating with node {node_port}: {e}")
                continue

        if longest_chain:
            with self.lock:
                self.chain = longest_chain
                return True
        return False

    def broadcast_transaction(self, transaction: Dict[str, Any]) -> None:
        """
        Broadcast a transaction to all peer nodes.
        """
        for node_port in self.peer_ports:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(2.0)
                    s.connect(('localhost', node_port))
                    s.sendall(pickle.dumps({
                        'type': 'new_transaction',
                        'transaction': transaction
                    }))
            except Exception as e:
                logger.warning(f"Error broadcasting to node {node_port}: {e}")

    def broadcast_block(self, block: Block) -> None:
        """
        Broadcast a new block to all peer nodes.
        """
        for node_port in self.peer_ports:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(2.0)
                    s.connect(('localhost', node_port))
                    s.sendall(pickle.dumps({
                        'type': 'new_block',
                        'block': block
                    }))
            except Exception as e:
                logger.warning(f"Error broadcasting to node {node_port}: {e}")

    def handle_connection(self, conn, addr):
        """
        Handle incoming connections from other nodes.
        """
        try:
            data = conn.recv(4096)
            if not data:
                return

            message = pickle.loads(data)

            if message['type'] == 'get_chain':
                response = {
                    'type': 'chain_response',
                    'chain': self.chain
                }
                conn.sendall(pickle.dumps(response))

            elif message['type'] == 'new_transaction':
                transaction = message['transaction']
                with self.lock:
                    self.current_transactions.append(transaction)
                logger.info(f"New transaction received: {transaction['transaction_id']}")

            elif message['type'] == 'new_block':
                block = message['block']
                with self.lock:
                    if block.index > self.last_block.index:
                        if block.previous_hash == self.last_block.hash:
                            self.chain.append(block)
                            logger.info(f"New block added: {block.hash}")
                        else:
                            logger.info("Chain conflict detected, resolving...")
                            self.resolve_conflicts()
                    else:
                        logger.info("Received block is not longer than current chain")

        except Exception as e:
            logger.error(f"Error handling connection from {addr}: {e}")
        finally:
            conn.close()

    def start_server(self):
        """
        Start the node server to listen for incoming connections.
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(('localhost', self.port))
            s.listen()
            logger.info(f"Node {self.node_id} listening on port {self.port}")

            while True:
                conn, addr = s.accept()
                threading.Thread(target=self.handle_connection, args=(conn, addr)).start()

def run_node(node_id: str, port: int, peer_ports: List[int]):
    """
    Initialize and run a distributed ledger node.
    """
    ledger = DistributedLedger(node_id, port, peer_ports)
    
    # Start server in a separate thread
    server_thread = threading.Thread(target=ledger.start_server)
    server_thread.daemon = True
    server_thread.start()

    # Simulate some transactions
    try:
        while True:
            time.sleep(10)
            
            # Add some transactions
            for _ in range(3):
                tx = {
                    'sender': str(uuid4()),
                    'recipient': str(uuid4()),
