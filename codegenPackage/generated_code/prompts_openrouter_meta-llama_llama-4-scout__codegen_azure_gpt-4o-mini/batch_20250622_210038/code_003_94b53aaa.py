"""
Generated Code Metadata:
========================
Original URL: https://artyfact-game-6gr.pages.dev
Prompt: "Design a system for distributing prize pools in a play-to-earn game like Artyfact, where profits from NFT sales replenish the prize pool."
Generated: DETERMINISTIC_94b53aaaf3dac028
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from decimal import Decimal, getcontext
from typing import List, Dict

# Set the precision for Decimal operations
getcontext().prec = 10

class PrizePool:
    def __init__(self):
        """Initialize the prize pool with a starting balance."""
        self.balance = Decimal('0.00')
        self.contributors = {}  # Dictionary to track contributions

    def add_funds(self, amount: Decimal) -> None:
        """Add funds to the prize pool from NFT sales.

        Args:
            amount (Decimal): The amount to add to the prize pool.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        self.balance += amount
        print(f"Added {amount} to the prize pool. New balance: {self.balance}")

    def distribute_prizes(self, winners: List[str], total_prize: Decimal) -> Dict[str, Decimal]:
        """Distribute prizes among winners.

        Args:
            winners (List[str]): List of winner identifiers.
            total_prize (Decimal): Total amount to distribute.

        Returns:
            Dict[str, Decimal]: A dictionary mapping winners to their prize amounts.
        """
        if total_prize <= 0:
            raise ValueError("Total prize must be greater than zero.")
        if total_prize > self.balance:
            raise ValueError("Insufficient funds in the prize pool.")

        # Calculate individual prize amount
        prize_per_winner = total_prize / len(winners)
        prize_distribution = {}

        for winner in winners:
            prize_distribution[winner] = prize_per_winner
            print(f"Distributed {prize_per_winner} to {winner}")

        # Deduct the total prize from the balance
        self.balance -= total_prize
        print(f"Total prize of {total_prize} distributed. New balance: {self.balance}")

        return prize_distribution

    def get_balance(self) -> Decimal:
        """Get the current balance of the prize pool.

        Returns:
            Decimal: The current balance of the prize pool.
        """
        return self.balance

    def record_contribution(self, contributor: str, amount: Decimal) -> None:
        """Record a contribution to the prize pool.

        Args:
            contributor (str): The identifier of the contributor.
            amount (Decimal): The amount contributed.

        Raises:
            ValueError: If the contribution amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Contribution amount must be greater than zero.")
        
        if contributor in self.contributors:
            self.contributors[contributor] += amount
        else:
            self.contributors[contributor] = amount
        
        self.add_funds(amount)
        print(f"Recorded contribution of {amount} from {contributor}.")

    def get_contributors(self) -> Dict[str, Decimal]:
        """Get a list of contributors and their contributions.

        Returns:
            Dict[str, Decimal]: A dictionary of contributors and their contributions.
        """
        return self.contributors

# Example usage
if __name__ == "__main__":
    prize_pool = PrizePool()
    
    # Simulate contributions from NFT sales
    try:
        prize_pool.record_contribution("User1", Decimal('100.00'))
        prize_pool.record_contribution("User2", Decimal('150.00'))
        
        # Check balance
        print(f"Current prize pool balance: {prize_pool.get_balance()}")
        
        # Distribute prizes
        winners = ["User1", "User2"]
        prize_distribution = prize_pool.distribute_prizes(winners, Decimal('200.00'))
        print(f"Prize distribution: {json.dumps(prize_distribution, indent=2)}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
