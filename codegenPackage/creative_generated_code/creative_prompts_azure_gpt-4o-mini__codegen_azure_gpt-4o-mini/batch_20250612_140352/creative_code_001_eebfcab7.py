"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v2-pancake.pages.dev
Prompt: Write a function that checks if a user's lottery ticket matches the winning numbers on PancakeSwap and calculates the prize based on the matching criteria.
Generated: DETERMINISTIC_eebfcab752dc0228
Batch ID: 20250612_140352
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Lottery:
    def __init__(self, winning_numbers, prize_structure):
        """
        Initializes the Lottery class with winning numbers and a prize structure.

        :param winning_numbers: List of integers representing winning lottery numbers.
        :param prize_structure: Dictionary where keys are the count of matching numbers
                                and values are the corresponding prizes.
        """
        self.winning_numbers = set(winning_numbers)
        self.prize_structure = prize_structure

    def check_ticket(self, user_ticket):
        """
        Checks the user's lottery ticket against the winning numbers and calculates the prize.

        :param user_ticket: List of integers representing the user's lottery ticket numbers.
        :return: Tuple containing the number of matches and the prize amount.
        """
        if not isinstance(user_ticket, list) or len(user_ticket) == 0:
            raise ValueError("User ticket must be a non-empty list of integers.")

        # Convert user ticket to a set for efficient comparison
        user_ticket_set = set(user_ticket)

        # Find matching numbers
        matches = self.winning_numbers.intersection(user_ticket_set)
        match_count = len(matches)

        # Determine prize based on the number of matches
        prize = self.prize_structure.get(match_count, 0)

        return match_count, prize


# Example usage
if __name__ == "__main__":
    # Define winning numbers and prize structure
    winning_numbers = [random.randint(1, 50) for _ in range(6)]  # Simulate winning numbers
    prize_structure = {
        0: 0,
        1: 10,
        2: 50,
        3: 100,
        4: 500,
        5: 1000,
        6: 10000
    }

    # Create a lottery instance
    lottery = Lottery(winning_numbers, prize_structure)

    # User's lottery ticket
    user_ticket = [random.randint(1, 50) for _ in range(6)]

    # Check the user's ticket
    try:
        matches, prize = lottery.check_ticket(user_ticket)
        print(f"Winning Numbers: {winning_numbers}")
        print(f"User Ticket: {user_ticket}")
        print(f"Number of Matches: {matches}, Prize: ${prize}")
    except ValueError as e:
        print(f"Error: {str(e)}")
```
