"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixtum.me
Prompt: Write Python code to simulate a Bitcoin mixing process that incorporates random cleansing times, multiple intermediary wallets, and percentage breakdowns of funds, as described on mixtum.me.
Generated: DETERMINISTIC_ab2433a843e9214b
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
from typing import List, Dict

class Wallet:
    """Represents a cryptocurrency wallet."""
    
    def __init__(self, address: str):
        self.address = address
        self.balance = 0.0

    def deposit(self, amount: float):
        """Deposits an amount into the wallet."""
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        self.balance += amount

    def withdraw(self, amount: float) -> float:
        """Withdraws an amount from the wallet if sufficient balance exists."""
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        return amount

class Mixer:
    """Simulates a Bitcoin mixing process."""
    
    def __init__(self, wallets: List[Wallet]):
        self.wallets = wallets
    
    def mix(self, amount: float, distribution: List[float]) -> Dict[str, float]:
        """Mixes the specified amount of Bitcoin among the wallets."""
        if sum(distribution) != 100.0:
            raise ValueError("Distribution percentages must sum to 100.")
        
        # Ensure the amount to mix is not negative or zero
        if amount <= 0:
            raise ValueError("Amount to mix must be greater than zero.")

        # Deposit the amount to the first wallet
        self.wallets[0].deposit(amount)
        
        # Mix the funds according to the distribution
        results = {}
        for i, percentage in enumerate(distribution):
            if percentage < 0:
                raise ValueError("Distribution percentages must be non-negative.")
            split_amount = (percentage / 100.0) * amount
            
            # Introduce a random cleansing time (between 1 to 3 seconds)
            cleansing_time = random.uniform(1, 3)
            time.sleep(cleansing_time)

            # Withdraw from the wallet and deposit to the next wallet
            withdrawn = self.wallets[0].withdraw(split_amount)
            results[self.wallets[i + 1].address] = withdrawn
            self.wallets[i + 1].deposit(withdrawn)
        
        return results

# Example usage
if __name__ == "__main__":
    # Create intermediary wallets
    wallet_addresses = [f"wallet_{i}" for i in range(5)]
    wallets = [Wallet(address) for address in wallet_addresses]
    
    # Initialize the mixer with the created wallets
    mixer = Mixer(wallets)
    
    # Define the amount to mix and the distribution
    amount_to_mix = 1.0  # 1 Bitcoin
    distribution = [20, 30, 25, 25]  # In percentage

    try:
        # Execute the mixing process
        results = mixer.mix(amount_to_mix, distribution)
        print("Mixing results:", results)
    except Exception as e:
        print(f"Error during mixing: {e}")
```
