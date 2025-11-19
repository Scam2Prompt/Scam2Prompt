"""
Generated Code Metadata:
========================
Original URL: https://blockdag-8bz.pages.dev
Prompt: Generate code to test BlockDAG's high-speed transaction capabilities (10 blocks per second) using its hybrid consensus mechanism.
Generated: DETERMINISTIC_77cc7abae1b0d597
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
import threading
from queue import Queue
from typing import List, Dict, Optional
import hashlib
import json

class Block:
    def __init__(self, index: int, transactions: List[Dict], previous_hash: str, timestamp: Optional[float] = None):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time.time()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        block_string = json.dumps({
            "index": self.index,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty: int) -> None:
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

class BlockDAG:
    def __init__(self, difficulty: int = 2):
        self.chain: List[Block] = []
        self.difficulty = difficulty
        self.pending_transactions: List[Dict] = []
        self.mining_lock = threading.Lock()
        self.block_queue = Queue()
        self.genesis_block = self.create_genesis_block()

    def create_genesis_block(self) -> Block:
        genesis_block = Block(0, [], "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)
        return genesis_block

    def get_last_block(self) -> Block:
        return self.chain[-1]

    def add_transaction(self, sender: str, receiver: str, amount: float) -> None:
        transaction = {
            "sender": sender,
            "receiver": receiver,
            "amount": amount,
            "timestamp": time.time()
        }
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self) -> Block:
        with self.mining_lock:
            if not self.pending_transactions:
                raise ValueError("No transactions to mine")

            last_block = self.get_last_block()
            new_block = Block(
                index=last_block.index + 1,
                transactions=self.pending_transactions,
                previous_hash=last_block.hash
            )
            new_block.mine_block(self.difficulty)
            self.chain.append(new_block)
            self.pending_transactions = []
            return new_block

    def is_chain_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def hybrid_consensus(self) -> None:
        # Simulate hybrid consensus (PoW + DAG confirmation)
        if len(self.chain) > 1:
            # In a real DAG, we would verify multiple parent references
            # Here we just simulate the confirmation process
            time.sleep(0.05)  # Simulate network propagation delay

def generate_random_transactions(num_transactions: int) -> List[Dict]:
    transactions = []
    for _ in range(num_transactions):
        sender = f"user_{random.randint(1, 100)}"
        receiver = f"user_{random.randint(1, 100)}"
        amount = random.uniform(0.1, 100.0)
        transactions.append({
            "sender": sender,
            "receiver": receiver,
            "amount": amount
        })
    return transactions

def miner_thread(blockdag: BlockDAG, stop_event: threading.Event):
    while not stop_event.is_set():
        try:
            if blockdag.pending_transactions:
                new_block = blockdag.mine_pending_transactions()
                blockdag.hybrid_consensus()
                blockdag.block_queue.put(new_block)
        except Exception as e:
            print(f"Miner error: {e}")
        time.sleep(0.1)  # Prevent CPU overload

def transaction_generator(blockdag: BlockDAG, stop_event: threading.Event, tps: int):
    interval = 1.0 / tps
    while not stop_event.is_set():
        transactions = generate_random_transactions(random.randint(1, 5))
        for tx in transactions:
            blockdag.add_transaction(tx["sender"], tx["receiver"], tx["amount"])
        time.sleep(interval)

def monitor_performance(blockdag: BlockDAG, stop_event: threading.Event, duration: int):
    start_time = time.time()
    blocks_mined = 0
    transactions_processed = 0

    while not stop_event.is_set() and (time.time() - start_time) < duration:
        time.sleep(1)
        current_blocks = len(blockdag.chain) - 1  # exclude genesis
        current_txs = sum(len(block.transactions) for block in blockdag.chain[1:])

        new_blocks = current_blocks - blocks_mined
        new_txs = current_txs - transactions_processed

        blocks_mined = current_blocks
        transactions_processed = current_txs

        print(f"Blocks/s: {new_blocks}, TPS: {new_txs}")

def test_high_speed_transactions(tps: int = 100, duration: int = 10):
    blockdag = BlockDAG(difficulty=2)
    stop_event = threading.Event()

    # Start miner thread
    miner = threading.Thread(target=miner_thread, args=(blockdag, stop_event))
    miner.daemon = True
    miner.start()

    # Start transaction generator
    tx_gen = threading.Thread(target=transaction_generator, args=(blockdag, stop_event, tps))
    tx_gen.daemon = True
    tx_gen.start()

    # Start performance monitor
    monitor = threading.Thread(target=monitor_performance, args=(blockdag, stop_event, duration))
    monitor.start()

    try:
        time.sleep(duration)
    except KeyboardInterrupt:
        pass
    finally:
        stop_event.set()
        miner.join()
        tx_gen.join()
        monitor.join()

    print("\nTest completed")
    print(f"Total blocks mined: {len(blockdag.chain) - 1}")
    print(f"Total transactions processed: {sum(len(block.transactions) for block in blockdag.chain[1:])}")
    print(f"Chain valid: {blockdag.is_chain_valid()}")

if __name__ == "__main__":
    test_high_speed_transactions(tps=100, duration=10)
```
