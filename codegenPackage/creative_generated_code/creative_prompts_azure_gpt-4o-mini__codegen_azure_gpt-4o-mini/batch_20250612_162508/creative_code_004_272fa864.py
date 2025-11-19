"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raffle-front-beige.vercel.app
Prompt: How do I implement a feature to handle different cryptocurrency options like SOL and USDC in a raffle system?
Generated: DETERMINISTIC_272fa864452b430b
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from decimal import Decimal, InvalidOperation

class RaffleEntry:
    """Class representing a single entry in the raffle."""
    
    def __init__(self, user_id, amount, currency):
        self.user_id = user_id
        self.amount = Decimal(amount)
        self.currency = currency

class Raffle:
    """Class representing the raffle system that handles multiple cryptocurrencies."""
    
    def __init__(self):
        self.entries = []
        self.total_value = Decimal('0')

    def add_entry(self, user_id, amount, currency):
        """
        Add a new entry to the raffle.
        
        Args:
            user_id: The ID of the user entering the raffle.
            amount: The amount in the specified currency.
            currency: The cryptocurrency type (e.g., 'SOL', 'USDC').
        """
        try:
            entry = RaffleEntry(user_id, amount, currency)
            self.entries.append(entry)
            self.total_value += entry.amount
            print(f"Entry added: {entry.user_id} with {entry.amount} {entry.currency}")
        except InvalidOperation as e:
            print(f"Error adding entry: {e}")

    def draw_winner(self):
        """
        Randomly select a winner from the entries.
        
        Returns:
            The user ID of the winner, or None if there are no entries.
        """
        if not self.entries:
            print("No entries in the raffle.")
            return None
        
        winner = random.choice(self.entries)
        print(f"Winner selected: {winner.user_id} with {winner.amount} {winner.currency}")
        return winner.user_id

    def display_entries(self):
        """Display all entries in the raffle."""
        if not self.entries:
            print("No entries in the raffle.")
            return
        
        print("Current Raffle Entries:")
        for entry in self.entries:
            print(f"User ID: {entry.user_id}, Amount: {entry.amount}, Currency: {entry.currency}")

# Example Usage
if __name__ == "__main__":
    raffle = Raffle()
    
    # Adding entries
    raffle.add_entry(user_id='user123', amount='1.5', currency='SOL')
    raffle.add_entry(user_id='user456', amount='100', currency='USDC')
    
    # Display current entries
    raffle.display_entries()
    
    # Draw a winner
    winner = raffle.draw_winner()
```
