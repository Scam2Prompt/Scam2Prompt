"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bits-check.web.app
Prompt: Write code to implement a no-loss lottery system using interest earned from BITS-tracked assets, similar to PoolTogether.
Generated: DETERMINISTIC_13c41f413b83e50d
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from decimal import Decimal, getcontext
from typing import List, Dict, Optional

# Set the precision for Decimal calculations
getcontext().prec = 28

class NoLossLottery:
    def __init__(self, interest_rate: Decimal):
        """
        Initialize the NoLossLottery with a specified interest rate.
        
        :param interest_rate: Annual interest rate as a Decimal (e.g., 0.05 for 5%)
        """
        if not (0 <= interest_rate <= 1):
            raise ValueError("Interest rate must be between 0 and 1.")
        
        self.interest_rate = interest_rate
        self.participants: Dict[str, Decimal] = {}
        self.prize_pool: Decimal = Decimal(0)

    def deposit(self, participant_id: str, amount: Decimal) -> None:
        """
        Allow a participant to deposit a specified amount into the lottery.
        
        :param participant_id: Unique identifier for the participant
        :param amount: The amount to deposit (must be positive)
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        # Update participant's balance
        if participant_id in self.participants:
            self.participants[participant_id] += amount
        else:
            self.participants[participant_id] = amount
        
        # Add to prize pool
        self.prize_pool += amount

    def draw_winner(self) -> Optional[str]:
        """
        Randomly select a winner from the participants.
        
        :return: The participant_id of the winner, or None if no participants
        """
        if not self.participants:
            return None
        
        winner = random.choice(list(self.participants.keys()))
        return winner

    def payout_winner(self, winner_id: str) -> None:
        """
        Payout the winnings to the winner and distribute the interest.
        
        :param winner_id: Unique identifier for the winner
        """
        if winner_id not in self.participants:
            raise ValueError("Winner is not a participant.")
        
        # Calculate the total interest earned
        total_interest = self.prize_pool * self.interest_rate
        
        # Reset prize pool after payout
        payout_amount = self.prize_pool + total_interest
        self.participants[winner_id] += payout_amount
        self.prize_pool = Decimal(0)

        # Log the payout
        print(f"Winner {winner_id} has been paid {payout_amount:.2f}.")

    def get_participants(self) -> List[str]:
        """
        Retrieve the list of current participants in the lottery.
        
        :return: A list of participant_ids
        """
        return list(self.participants.keys())

    def reset_lottery(self) -> None:
        """
        Reset the lottery by clearing participants and the prize pool.
        """
        self.participants.clear()
        self.prize_pool = Decimal(0)
        print("Lottery has been reset.")

# Example usage
if __name__ == "__main__":
    lottery = NoLossLottery(interest_rate=Decimal('0.05'))

    try:
        lottery.deposit("Alice", Decimal('100'))
        lottery.deposit("Bob", Decimal('150'))

        winner = lottery.draw_winner()
        if winner:
            lottery.payout_winner(winner)
        else:
            print("No participants to draw a winner.")

    except ValueError as e:
        print(f"Error: {e}")
```
