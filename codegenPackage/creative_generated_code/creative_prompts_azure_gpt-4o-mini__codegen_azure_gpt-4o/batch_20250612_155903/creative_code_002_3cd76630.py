"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daily-giveaway.info
Prompt: How can I create a library for managing daily giveaways in Python?
Generated: DETERMINISTIC_3cd76630667dee4c
Batch ID: 20250612_155903
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# daily_giveaway.py

import random
import datetime

class DailyGiveawayManager:
    """
    A library for managing daily giveaways.
    """

    def __init__(self, prizes, participants):
        """
        Initialize the giveaway manager.

        :param prizes: List of prizes available for the giveaway.
        :param participants: List of participants eligible for the giveaway.
        """
        if not isinstance(prizes, list) or not isinstance(participants, list):
            raise ValueError("Both prizes and participants should be provided as lists.")

        self.prizes = prizes
        self.participants = participants
        self.giveaway_history = {}  # {date: {winner: prize}}

    def run_daily_giveaway(self):
        """
        Run the daily giveaway, randomly selecting a winner and assigning a prize.

        :return: A dictionary with the winner and prize details.
        """
        if not self.prizes:
            raise ValueError("No prizes available for the giveaway.")
        if not self.participants:
            raise ValueError("No participants available for the giveaway.")
        
        # Determine today's date
        today = datetime.date.today()

        # Check if a giveaway has already been run for today
        if today in self.giveaway_history:
            raise ValueError("Giveaway for today has already been run.")

        # Randomly select a winner and a prize
        winner = random.choice(self.participants)
        prize = random.choice(self.prizes)

        # Record the giveaway result
        self.giveaway_history[today] = {"winner": winner, "prize": prize}

        return {"date": today, "winner": winner, "prize": prize}

    def get_giveaway_history(self):
        """
        Get the history of all giveaways.

        :return: Dictionary containing past giveaway details.
        """
        return self.giveaway_history

    def add_participant(self, participant):
        """
        Add a new participant to the list.

        :param participant: Name of the participant to add.
        """
        if participant in self.participants:
            raise ValueError(f"Participant '{participant}' is already in the list.")
        self.participants.append(participant)

    def remove_participant(self, participant):
        """
        Remove a participant from the list.

        :param participant: Name of the participant to remove.
        """
        if participant not in self.participants:
            raise ValueError(f"Participant '{participant}' does not exist in the list.")
        self.participants.remove(participant)

    def add_prize(self, prize):
        """
        Add a new prize to the list.

        :param prize: Name of the prize to add.
        """
        if prize in self.prizes:
            raise ValueError(f"Prize '{prize}' is already in the list.")
        self.prizes.append(prize)

    def remove_prize(self, prize):
        """
        Remove a prize from the list.

        :param prize: Name of the prize to remove.
        """
        if prize not in self.prizes:
            raise ValueError(f"Prize '{prize}' does not exist in the list.")
        self.prizes.remove(prize)

# Example usage
if __name__ == '__main__':
    # Initialize manager with sample data
    prizes = ["Gift Card", "Headphones", "Smartwatch", "Laptop"]
    participants = ["Alice", "Bob", "Charlie", "Diana"]

    manager = DailyGiveawayManager(prizes, participants)

    try:
        # Run a giveaway
        result = manager.run_daily_giveaway()
        print(f"Today's Giveaway: {result}")

        # Add a new participant
        manager.add_participant("Eve")

        # Remove a prize
        manager.remove_prize("Gift Card")

        # View past giveaways
        history = manager.get_giveaway_history()
        print("Giveaway History:", history)
    except ValueError as e:
        print(f"Error: {e}")
```
