"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jellyjelly.web.app
Prompt: Develop code for a lottery system similar to the "Jellotto" feature, ensuring compatibility with blockchain-based tokens.
Generated: DETERMINISTIC_49551b6c78d37680
Batch ID: 20250612_153659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

class Lottery:
    def __init__(self, ticket_price: float, max_tickets: int):
        """
        Initializes the Lottery instance.

        Args:
            ticket_price (float): The price of one lottery ticket.
            max_tickets (int): The maximum number of tickets that can be sold.
        """
        self.ticket_price = ticket_price
        self.max_tickets = max_tickets
        self.tickets_sold = 0
        self.participants: Dict[str, List[int]] = {}
        self.winning_numbers: List[int] = []

    def buy_ticket(self, participant_id: str, numbers: List[int]) -> None:
        """
        Allows a participant to buy a lottery ticket.

        Args:
            participant_id (str): The unique identifier for the participant.
            numbers (List[int]): The chosen numbers for the lottery ticket.

        Raises:
            ValueError: If the ticket limit is reached or if numbers are invalid.
        """
        # Validate input
        if self.tickets_sold >= self.max_tickets:
            raise ValueError("All tickets have been sold.")
        
        if len(numbers) != 6 or not all(1 <= num <= 49 for num in numbers):
            raise ValueError("You must choose 6 unique numbers between 1 and 49.")

        # Record the participant's numbers
        if participant_id in self.participants:
            self.participants[participant_id].extend(numbers)
        else:
            self.participants[participant_id] = numbers
        
        self.tickets_sold += 1

    def draw_winning_numbers(self) -> List[int]:
        """
        Draws the winning lottery numbers.

        Returns:
            List[int]: The winning numbers.
        """
        self.winning_numbers = random.sample(range(1, 50), 6)
        return self.winning_numbers

    def check_winner(self) -> Dict[str, int]:
        """
        Checks for winners based on the drawn winning numbers.

        Returns:
            Dict[str, int]: A dictionary with participant IDs and their matching count.
        """
        results = {}
        for participant, numbers in self.participants.items():
            matches = len(set(numbers) & set(self.winning_numbers))
            if matches > 0:
                results[participant] = matches
        return results

    def reset_lottery(self) -> None:
        """
        Resets the lottery for a new round.
        """
        self.tickets_sold = 0
        self.participants.clear()
        self.winning_numbers.clear()

# Example usage:
if __name__ == "__main__":
    lottery = Lottery(ticket_price=1.0, max_tickets=100)
    
    try:
        lottery.buy_ticket("user123", [3, 14, 15, 22, 35, 38])
        lottery.buy_ticket("user456", [7, 11, 19, 22, 28, 35])
        
        winning_numbers = lottery.draw_winning_numbers()
        print(f"Winning numbers: {winning_numbers}")
        
        winners = lottery.check_winner()
        print(f"Winners: {winners}")
        
    except ValueError as ve:
        print(f"Error occurred: {ve}")
    finally:
        lottery.reset_lottery()
```
