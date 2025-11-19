"""
Generated Code Metadata:
========================
Original URL: https://raffle-front-beige.vercel.app
Prompt: How do I implement a feature to handle different cryptocurrency options like SOL and USDC in a raffle system?
Generated: DETERMINISTIC_272fa864452b430b
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from decimal import Decimal
from typing import List, Dict, Union

class Raffle:
    def __init__(self):
        """Initialize the Raffle with an empty list of participants and a prize pool."""
        self.participants: List[Dict[str, Union[str, Decimal]]] = []
        self.prize_pool: Decimal = Decimal('0.0')

    def add_participant(self, name: str, amount: Decimal, currency: str) -> None:
        """
        Add a participant to the raffle.

        :param name: The name of the participant.
        :param amount: The amount contributed by the participant.
        :param currency: The currency of the contribution (e.g., 'SOL', 'USDC').
        :raises ValueError: If the amount is not positive or currency is unsupported.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if currency not in ['SOL', 'USDC']:
            raise ValueError("Unsupported currency. Please use 'SOL' or 'USDC'.")

        self.participants.append({'name': name, 'amount': amount, 'currency': currency})
        self.prize_pool += amount

    def draw_winner(self) -> str:
        """
        Randomly select a winner from the participants.

        :return: The name of the winner.
        :raises ValueError: If there are no participants in the raffle.
        """
        if not self.participants:
            raise ValueError("No participants in the raffle.")

        winner = random.choice(self.participants)
        return winner['name']

    def get_prize_pool(self) -> Decimal:
        """
        Get the total prize pool of the raffle.

        :return: The total prize pool.
        """
        return self.prize_pool

    def reset_raffle(self) -> None:
        """Reset the raffle for a new round by clearing participants and prize pool."""
        self.participants.clear()
        self.prize_pool = Decimal('0.0')


# Example usage
if __name__ == "__main__":
    raffle = Raffle()

    try:
        raffle.add_participant("Alice", Decimal('10.0'), 'SOL')
        raffle.add_participant("Bob", Decimal('20.0'), 'USDC')
        raffle.add_participant("Charlie", Decimal('15.0'), 'SOL')

        print(f"Total Prize Pool: {raffle.get_prize_pool()}")

        winner = raffle.draw_winner()
        print(f"The winner is: {winner}")

    except ValueError as e:
        print(f"Error: {e}")

    # Reset the raffle for a new round
    raffle.reset_raffle()
```
