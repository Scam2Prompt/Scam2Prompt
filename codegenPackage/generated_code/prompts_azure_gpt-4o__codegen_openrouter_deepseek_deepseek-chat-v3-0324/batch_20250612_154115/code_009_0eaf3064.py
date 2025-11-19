"""
Generated Code Metadata:
========================
Original URL: https://orikod.com
Prompt: Develop a tool to simulate the performance of an NFT marketplace deployed on Arbitrum Rollup, highlighting gas fee savings and transaction speed.
Generated: DETERMINISTIC_0eaf30643cdf3439
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from typing import Dict, List, Tuple
from dataclasses import dataclass
from enum import Enum
import matplotlib.pyplot as plt
import numpy as np

class TransactionType(Enum):
    MINT = "Mint"
    LIST = "List"
    BUY = "Buy"
    TRANSFER = "Transfer"

@dataclass
class Transaction:
    tx_type: TransactionType
    gas_used: int
    timestamp: float
    success: bool = True

@dataclass
class NFT:
    token_id: int
    owner: str
    price: float = 0.0
    listed: bool = False

class NFTMarketplaceSimulator:
    """
    Simulates an NFT marketplace on Arbitrum Rollup, tracking gas fees and transaction speeds.
    """
    
    def __init__(self):
        self.nfts: Dict[int, NFT] = {}
        self.transactions: List[Transaction] = []
        self.users: List[str] = ["user1", "user2", "user3", "user4", "user5"]
        
        # Gas costs (in gwei) for different operations
        self.gas_costs = {
            TransactionType.MINT: 50000,
            TransactionType.LIST: 30000,
            TransactionType.BUY: 45000,
            TransactionType.TRANSFER: 25000
        }
        
        # Arbitrum savings factor (compared to Ethereum mainnet)
        self.arbitrum_savings = 0.1  # 90% savings
    
    def _get_random_user(self) -> str:
        return random.choice(self.users)
    
    def _get_arbitrum_gas_cost(self, tx_type: TransactionType) -> int:
        """Calculate gas cost on Arbitrum with savings applied."""
        return int(self.gas_costs[tx_type] * self.arbitrum_savings)
    
    def _simulate_delay(self, tx_type: TransactionType) -> float:
        """Simulate transaction processing delay based on type."""
        delays = {
            TransactionType.MINT: 0.5,
            TransactionType.LIST: 0.3,
            TransactionType.BUY: 0.4,
            TransactionType.TRANSFER: 0.2
        }
        return delays[tx_type] * random.uniform(0.8, 1.2)
    
    def mint_nft(self) -> Tuple[NFT, Transaction]:
        """Simulate minting a new NFT."""
        token_id = len(self.nfts) + 1
        owner = self._get_random_user()
        nft = NFT(token_id=token_id, owner=owner)
        
        gas_used = self._get_arbitrum_gas_cost(TransactionType.MINT)
        delay = self._simulate_delay(TransactionType.MINT)
        
        time.sleep(delay)
        
        tx = Transaction(
            tx_type=TransactionType.MINT,
            gas_used=gas_used,
            timestamp=time.time()
        )
        
        self.nfts[token_id] = nft
        self.transactions.append(tx)
        
        return nft, tx
    
    def list_nft(self, token_id: int, price: float) -> Tuple[NFT, Transaction]:
        """Simulate listing an NFT for sale."""
        if token_id not in self.nfts:
            raise ValueError("NFT does not exist")
        
        nft = self.nfts[token_id]
        nft.price = price
        nft.listed = True
        
        gas_used = self._get_arbitrum_gas_cost(TransactionType.LIST)
        delay = self._simulate_delay(TransactionType.LIST)
        
        time.sleep(delay)
        
        tx = Transaction(
            tx_type=TransactionType.LIST,
            gas_used=gas_used,
            timestamp=time.time()
        )
        
        self.transactions.append(tx)
        return nft, tx
    
    def buy_nft(self, token_id: int, buyer: str = None) -> Tuple[NFT, Transaction]:
        """Simulate buying an NFT."""
        if token_id not in self.nfts:
            raise ValueError("NFT does not exist")
        
        nft = self.nfts[token_id]
        if not nft.listed:
            raise ValueError("NFT is not listed for sale")
        
        buyer = buyer or self._get_random_user()
        nft.owner = buyer
        nft.listed = False
        
        gas_used = self._get_arbitrum_gas_cost(TransactionType.BUY)
        delay = self._simulate_delay(TransactionType.BUY)
        
        time.sleep(delay)
        
        tx = Transaction(
            tx_type=TransactionType.BUY,
            gas_used=gas_used,
            timestamp=time.time()
        )
        
        self.transactions.append(tx)
        return nft, tx
    
    def transfer_nft(self, token_id: int, new_owner: str) -> Tuple[NFT, Transaction]:
        """Simulate transferring an NFT."""
        if token_id not in self.nfts:
            raise ValueError("NFT does not exist")
        
        nft = self.nfts[token_id]
        nft.owner = new_owner
        
        gas_used = self._get_arbitrum_gas_cost(TransactionType.TRANSFER)
        delay = self._simulate_delay(TransactionType.TRANSFER)
        
        time.sleep(delay)
        
        tx = Transaction(
            tx_type=TransactionType.TRANSFER,
            gas_used=gas_used,
            timestamp=time.time()
        )
        
        self.transactions.append(tx)
        return nft, tx
    
    def generate_report(self) -> Dict:
        """Generate a performance report with metrics."""
        if not self.transactions:
            return {}
        
        total_gas = sum(tx.gas_used for tx in self.transactions)
        avg_gas = total_gas / len(self.transactions)
        
        timestamps = [tx.timestamp for tx in self.transactions]
        durations = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
        avg_duration = sum(durations) / len(durations) if durations else 0
        
        eth_mainnet_gas = sum(self.gas_costs[tx.tx_type] for tx in self.transactions)
        savings = eth_mainnet_gas - total_gas
        
        return {
            "total_transactions": len(self.transactions),
            "total_gas_used": total_gas,
            "average_gas_per_tx": avg_gas,
            "average_tx_duration": avg_duration,
            "gas_savings_vs_ethereum": savings,
            "savings_percentage": (savings / eth_mainnet_gas) * 100 if eth_mainnet_gas else 0
        }
    
    def visualize_performance(self):
        """Generate visualizations of gas usage and transaction speeds."""
        if not self.transactions:
            print("No transactions to visualize")
            return
        
        # Prepare data
        tx_types = [tx.tx_type.value for tx in self.transactions]
        gas_used = [tx.gas_used for tx in self.transactions]
        eth_gas = [self.gas_costs[tx.tx_type] for tx in self.transactions]
        timestamps = [tx.timestamp - self.transactions[0].timestamp for tx in self.transactions]
        
        # Gas comparison plot
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        x = np.arange(len(tx_types))
        width = 0.35
        plt.bar(x - width/2, eth_gas, width, label='Ethereum Mainnet')
        plt.bar(x + width/2, gas_used, width, label='Arbitrum')
        plt.xticks(x, tx_types, rotation=45)
        plt.ylabel('Gas Used (gwei)')
        plt.title('Gas Usage Comparison')
        plt.legend()
        
        # Transaction timeline plot
        plt.subplot(1, 2, 2)
        plt.plot(timestamps, gas_used, 'o-')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Gas Used (gwei)')
        plt.title('Transaction Timeline')
        
        plt.tight_layout()
        plt.show()

def run_simulation(num_operations: int = 20):
    """Run a complete simulation with the specified number of operations."""
    simulator = NFTMarketplaceSimulator()
    
    operations = [
        simulator.mint_nft,
        simulator.list_nft,
        simulator.buy_nft,
        simulator.transfer_nft
    ]
    
    # Create some NFTs first
    for _ in range(5):
        simulator.mint_nft()
    
    # Run random operations
    for _ in range(num_operations):
        try:
            op = random.choice(operations)
            
            if op == simulator.list_nft:
                token_id = random.choice(list(simulator.nfts.keys()))
                price = random.uniform(0.1, 10.0)
                op(token_id, price)
            elif op == simulator.buy_nft:
