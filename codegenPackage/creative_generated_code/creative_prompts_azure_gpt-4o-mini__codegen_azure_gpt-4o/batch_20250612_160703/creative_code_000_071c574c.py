"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumcv.io
Prompt: Write a Python script to implement a Proof-of-Stake mining protocol similar to Ethereum Classic Vision that balances miner and trader interests.
Generated: DETERMINISTIC_071c574ce53fe13b
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import time
import random
from typing import List, Dict, Any


class Wallet:
    """
    Represents a wallet in the Proof-of-Stake system.
    Contains the wallet address and its staked balance.
    """
    def __init__(self, address: str, balance: float):
        self.address = address
        self.balance = balance

    def __repr__(self):
        return f"Wallet(address={self.address}, balance={self.balance})"


class ProofOfStake:
    """
    Implements the Proof-of-Stake mining protocol.
    Balances miner and trader interests by assigning mining privileges
    based on the staked wallet balances.
    """
    def __init__(self):
        self.chain: List[Dict[str, Any]] = []
        self.wallets: Dict[str, Wallet] = {}  # address -> Wallet

    def create_wallet(self, address: str, initial_balance: float):
        """
        Creates a wallet and adds it to the system.
        """
        if address in self.wallets:
            raise ValueError("Wallet address already exists.")
        self.wallets[address] = Wallet(address, initial_balance)

    def stake(self, address: str, amount: float):
        """
        Allows a wallet to stake a portion of its balance.
        """
        if address not in self.wallets:
            raise ValueError("Wallet address not found.")
        if amount <= 0 or self.wallets[address].balance < amount:
            raise ValueError("Invalid staking amount.")
        self.wallets[address].balance -= amount

    def select_miner(self) -> str:
        """
        Selects a miner based on staked balances using a weighted random mechanism.
        """
        total_stake = sum(wallet.balance for wallet in self.wallets.values())
        if total_stake <= 0:
            raise ValueError("No stakes available for mining.")
        
        # Weighted random selection based on staked balances
        weighted_choices = [(wallet.address, wallet.balance / total_stake) for wallet in self.wallets.values()]
        addresses, weights = zip(*weighted_choices)
        selected_address = random.choices(addresses, weights=weights, k=1)[0]
        return selected_address

    def create_block(self, transactions: List[Dict[str, Any]]):
        """
        Creates a new block and appends it to the chain.
        The miner for the block is selected using the Proof-of-Stake mechanism.
        """
        miner_address = self.select_miner()
        block = {
            "timestamp": time.time(),
            "transactions": transactions,
            "miner": miner_address,
            "previous_hash": self.get_latest_block_hash(),
            "hash": None,
        }
        block["hash"] = self.calculate_hash(block)
        self.chain.append(block)

    def get_latest_block_hash(self) -> str:
        """
        Retrieves the hash of the latest block in the chain.
        """
        if not self.chain:
            return "0"  # Genesis block case
        return self.chain[-1]["hash"]

    def calculate_hash(self, block: Dict[str, Any]) -> str:
        """
        Calculates the SHA-256 hash of the block's contents.
        """
        block_string = f"{block['timestamp']}{block['transactions']}{block['miner']}{block['previous_hash']}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def display_chain(self):
        """
        Displays the blockchain in a readable format.
        """
        for index, block in enumerate(self.chain):
            print(f"Block {index}:")
            print(f"  Miner: {block['miner']}")
            print(f"  Transactions: {block['transactions']}")
            print(f"  Previous Hash: {block['previous_hash']}")
            print(f"  Hash: {block['hash']}")
            print("")


# Example usage
if __name__ == "__main__":
    pos = ProofOfStake()

    # Create wallets
    pos.create_wallet("Miner1", 100)
    pos.create_wallet("Trader1", 50)
    pos.create_wallet("Trader2", 30)

    # Stake balances
    pos.stake("Miner1", 50)
    pos.stake("Trader1", 20)
    pos.stake("Trader2", 10)

    # Create blocks with transactions
    pos.create_block([{"from": "Trader1", "to": "Trader2", "amount": 5}])
    pos.create_block([{"from": "Trader2", "to": "Trader1", "amount": 2}])

    # Display blockchain
    pos.display_chain()
```
