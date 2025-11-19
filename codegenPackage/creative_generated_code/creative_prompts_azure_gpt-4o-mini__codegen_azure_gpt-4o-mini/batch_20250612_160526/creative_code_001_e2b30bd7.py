"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://restore-tenon.pages.dev
Prompt: Write a script that facilitates rapid liquidity transactions within a DeFi protocol, incorporating micropools and decentralized governance.
Generated: DETERMINISTIC_e2b30bd701d86bab
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from dataclasses import dataclass
from typing import List, Dict, Any, Optional

# Custom exception for transaction errors
class TransactionError(Exception):
    """Exception raised for errors in the transaction process."""
    pass

@dataclass
class LiquidityPool:
    """Data class to represent a liquidity pool."""
    id: str
    balance: float
    governance: str  # Address of the governance contract
    micropools: Dict[str, float]  # Dictionary to hold micropool id and balance

class DeFiProtocol:
    """Class representing the DeFi protocol for liquidity transactions."""
    
    def __init__(self):
        self.pools: Dict[str, LiquidityPool] = {}

    def create_pool(self, pool_id: str, governance: str) -> None:
        """Create a new liquidity pool."""
        if pool_id in self.pools:
            raise ValueError(f"Pool with id {pool_id} already exists.")
        
        pool = LiquidityPool(id=pool_id, balance=0.0, governance=governance, micropools={})
        self.pools[pool_id] = pool

    def add_liquidity(self, pool_id: str, amount: float) -> None:
        """Add liquidity to a specific pool."""
        if pool_id not in self.pools:
            raise TransactionError(f"Liquidity pool {pool_id} does not exist.")
        
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        self.pools[pool_id].balance += amount

    def create_micropool(self, pool_id: str, micropool_id: str, initial_balance: float) -> None:
        """Create a micropool within a specific liquidity pool."""
        if pool_id not in self.pools:
            raise TransactionError(f"Liquidity pool {pool_id} does not exist.")
        
        if micropool_id in self.pools[pool_id].micropools:
            raise ValueError(f"Micropool with id {micropool_id} already exists in pool {pool_id}.")

        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        
        self.pools[pool_id].micropools[micropool_id] = initial_balance

    def perform_transaction(self, pool_id: str, micropool_id: str, amount: float) -> None:
        """Facilitate a liquidity transaction in a micropool."""
        if pool_id not in self.pools:
            raise TransactionError(f"Liquidity pool {pool_id} does not exist.")
        
        if micropool_id not in self.pools[pool_id].micropools:
            raise TransactionError(f"Micropool {micropool_id} does not exist in pool {pool_id}.")
        
        micropool_balance = self.pools[pool_id].micropools[micropool_id]
        
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        
        if amount > micropool_balance:
            raise TransactionError("Insufficient balance in micropool for this transaction.")
        
        # Deduct from micropool balance
        self.pools[pool_id].micropools[micropool_id] -= amount

    def show_pools(self) -> List[Dict[str, Any]]:
        """Return a list of all pools with their details."""
        return [
            {
                "id": pool.id,
                "balance": pool.balance,
                "micropools": pool.micropools
            }
            for pool in self.pools.values()
        ]

# Example usage
if __name__ == "__main__":
    try:
        protocol = DeFiProtocol()
        protocol.create_pool('pool1', 'gov_address_1')
        protocol.add_liquidity('pool1', 100.0)
        protocol.create_micropool('pool1', 'micropool1', 50.0)
        protocol.perform_transaction('pool1', 'micropool1', 20.0)
        print(protocol.show_pools())
    except Exception as e:
        print(f"Error: {e}")
```
