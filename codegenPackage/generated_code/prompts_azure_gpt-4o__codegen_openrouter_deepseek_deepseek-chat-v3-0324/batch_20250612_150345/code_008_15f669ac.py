"""
Generated Code Metadata:
========================
Original URL: https://eth-mix.to
Prompt: Develop a Python script that simulates the mixing process described on the Ethereum Mixer site, including breaking the link between addresses and generating a new reserve of premixed Ether.
Generated: DETERMINISTIC_15f669acf882e4fe
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import hashlib
from typing import List, Dict, Tuple
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class MixingTransaction:
    input_address: str
    output_address: str
    amount: float
    timestamp: datetime
    transaction_hash: str

class EthereumMixer:
    def __init__(self, reserve_size: int = 100):
        """
        Initialize the Ethereum Mixer with a reserve of premixed Ether.
        
        Args:
            reserve_size: Number of addresses to maintain in the reserve pool
        """
        self.reserve_size = reserve_size
        self.reserve_pool: List[str] = []
        self.transaction_history: List[MixingTransaction] = []
        self._initialize_reserve()

    def _initialize_reserve(self) -> None:
        """Generate initial reserve pool of addresses."""
        self.reserve_pool = [self._generate_random_address() for _ in range(self.reserve_size)]

    def _generate_random_address(self) -> str:
        """Generate a random Ethereum-like address."""
        return '0x' + hashlib.sha256(str(random.getrandbits(256)).encode()).hexdigest()[:40]

    def _generate_transaction_hash(self, input_addr: str, output_addr: str, amount: float) -> str:
        """Generate a unique transaction hash."""
        data = f"{input_addr}{output_addr}{amount}{datetime.now().timestamp()}"
        return '0x' + hashlib.sha256(data.encode()).hexdigest()

    def mix_ether(self, input_address: str, amount: float) -> Tuple[str, str]:
        """
        Mix Ether by breaking the link between input and output addresses.
        
        Args:
            input_address: The source address to mix from
            amount: The amount of Ether to mix
            
        Returns:
            Tuple of (output_address, transaction_hash)
            
        Raises:
            ValueError: If amount is not positive
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")

        # Select random output address from reserve
        output_address = random.choice(self.reserve_pool)
        
        # Generate transaction hash
        tx_hash = self._generate_transaction_hash(input_address, output_address, amount)
        
        # Record transaction
        transaction = MixingTransaction(
            input_address=input_address,
            output_address=output_address,
            amount=amount,
            timestamp=datetime.now(),
            transaction_hash=tx_hash
        )
        self.transaction_history.append(transaction)
        
        # Replenish reserve with new address
        self._replenish_reserve(output_address)
        
        return output_address, tx_hash

    def _replenish_reserve(self, used_address: str) -> None:
        """
        Maintain reserve pool by replacing used addresses with new ones.
        
        Args:
            used_address: The address that was just used and needs replacement
        """
        if used_address in self.reserve_pool:
            self.reserve_pool.remove(used_address)
            new_address = self._generate_random_address()
            self.reserve_pool.append(new_address)

    def get_transaction_history(self, time_window: timedelta = None) -> List[Dict]:
        """
        Get transaction history within a specified time window.
        
        Args:
            time_window: Optional timedelta to filter recent transactions
            
        Returns:
            List of transaction dictionaries
        """
        if time_window:
            cutoff = datetime.now() - time_window
            recent_txs = [tx for tx in self.transaction_history if tx.timestamp >= cutoff]
            return [self._transaction_to_dict(tx) for tx in recent_txs]
        return [self._transaction_to_dict(tx) for tx in self.transaction_history]

    def _transaction_to_dict(self, transaction: MixingTransaction) -> Dict:
        """Convert MixingTransaction to dictionary for output."""
        return {
            'input_address': transaction.input_address,
            'output_address': transaction.output_address,
            'amount': transaction.amount,
            'timestamp': transaction.timestamp.isoformat(),
            'transaction_hash': transaction.transaction_hash
        }

    def get_reserve_status(self) -> Dict:
        """Get current status of the reserve pool."""
        return {
            'reserve_size': len(self.reserve_pool),
            'total_transactions': len(self.transaction_history),
            'last_transaction': self.transaction_history[-1].timestamp.isoformat() if self.transaction_history else None
        }

# Example usage
if __name__ == "__main__":
    mixer = EthereumMixer(reserve_size=50)
    
    # Simulate mixing
    input_addr = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
    amount = 1.5
    
    try:
        output_addr, tx_hash = mixer.mix_ether(input_addr, amount)
        print(f"Mixed {amount} ETH from {input_addr} to {output_addr}")
        print(f"Transaction hash: {tx_hash}")
        
        # Get recent transactions
        print("\nRecent transactions (last 24 hours):")
        recent_txs = mixer.get_transaction_history(time_window=timedelta(hours=24))
        for tx in recent_txs:
            print(f"{tx['timestamp']}: {tx['amount']} ETH from {tx['input_address'][:8]}... to {tx['output_address'][:8]}...")
            
        # Get reserve status
        status = mixer.get_reserve_status()
        print(f"\nReserve status: {status['reserve_size']} addresses, {status['total_transactions']} total transactions")
        
    except ValueError as e:
        print(f"Error: {e}")
```
