"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamsbat.com
Prompt: Write code to implement airdrop tasks for distributing special cards in May 2024, based on the Hamster Kombat roadmap.
Generated: DETERMINISTIC_444bfd2c23a7cf2e
Batch ID: 20250612_145718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import random
from typing import List, Dict

class AirdropTask:
    """
    A class to represent the airdrop task for distributing special cards.
    """

    def __init__(self, airdrop_date: datetime.date):
        """
        Initializes the AirdropTask with the specified airdrop date.

        :param airdrop_date: The date when the airdrop will take place.
        """
        self.airdrop_date = airdrop_date
        self.participants: List[str] = []  # List of participants eligible for airdrop
        self.special_cards: List[str] = []  # List of special cards to be distributed

    def add_participant(self, participant: str) -> None:
        """
        Adds a participant to the airdrop list.

        :param participant: The identifier of the participant (e.g., wallet address).
        """
        if participant not in self.participants:
            self.participants.append(participant)
        else:
            raise ValueError(f"Participant {participant} is already added.")

    def remove_participant(self, participant: str) -> None:
        """
        Removes a participant from the airdrop list.

        :param participant: The identifier of the participant (e.g., wallet address).
        """
        try:
            self.participants.remove(participant)
        except ValueError:
            raise ValueError(f"Participant {participant} not found in the list.")

    def set_special_cards(self, cards: List[str]) -> None:
        """
        Sets the special cards to be distributed.

        :param cards: A list of special card identifiers.
        """
        self.special_cards = cards

    def distribute_cards(self) -> Dict[str, str]:
        """
        Distributes special cards randomly among participants.

        :return: A dictionary mapping participants to the distributed special cards.
        """
        if not self.participants:
            raise RuntimeError("No participants to distribute cards.")
        if not self.special_cards:
            raise RuntimeError("No special cards set for distribution.")

        distribution = {}
        available_cards = self.special_cards.copy()

        for participant in self.participants:
            if available_cards:
                card = random.choice(available_cards)
                distribution[participant] = card
                available_cards.remove(card)
            else:
                distribution[participant] = None  # No more cards available

        return distribution

    def execute_airdrop(self) -> None:
        """
        Executes the airdrop if the current date matches the airdrop date.
        """
        current_date = datetime.date.today()

        if current_date == self.airdrop_date:
            try:
                distribution = self.distribute_cards()
                print("Airdrop successful! Distribution:", distribution)
            except Exception as e:
                print(f"Error during airdrop execution: {e}")
        else:
            print(f"Airdrop is scheduled for {self.airdrop_date}. Current date: {current_date}.")


# Example usage
if __name__ == "__main__":
    # Define the airdrop date
    airdrop_date = datetime.date(2024, 5, 1)
    
    # Create an instance of AirdropTask
    airdrop = AirdropTask(airdrop_date)

    # Add participants
    try:
        airdrop.add_participant("0x1234abcd")
        airdrop.add_participant("0x5678efgh")
        airdrop.add_participant("0x1234abcd")  # This will raise a ValueError
    except ValueError as ve:
        print(ve)

    # Set special cards
    airdrop.set_special_cards(["CardA", "CardB", "CardC"])

    # Execute the airdrop
    airdrop.execute_airdrop()
```
