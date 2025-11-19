"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rrr-9a3.pages.dev
Prompt: What are the key considerations for setting up a token generation event (TGE) for a memecoin like BorpaToken?
Generated: DETERMINISTIC_79e902ad61b6af39
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import json
from datetime import datetime
from typing import Dict, Any, List

class TokenGenerationEvent:
    """
    A class to represent a Token Generation Event (TGE) for a memecoin.
    """

    def __init__(self, token_name: str, total_supply: int, event_date: str):
        """
        Initializes the TGE with token name, total supply, and event date.
        
        :param token_name: The name of the token.
        :param total_supply: The total supply of tokens to be generated.
        :param event_date: The date of the TGE in YYYY-MM-DD format.
        """
        self.token_name = token_name
        self.total_supply = total_supply
        self.event_date = self.validate_event_date(event_date)
        self.participants = []

    @staticmethod
    def validate_event_date(event_date: str) -> str:
        """
        Validates the event date format and checks if it is in the future.

        :param event_date: The date of the TGE in YYYY-MM-DD format.
        :return: The validated event date.
        :raises ValueError: If the date format is incorrect or the date is in the past.
        """
        try:
            event_date_obj = datetime.strptime(event_date, "%Y-%m-%d")
            if event_date_obj < datetime.now():
                raise ValueError("Event date must be in the future.")
            return event_date
        except ValueError as e:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.") from e

    def add_participant(self, participant: str) -> None:
        """
        Adds a participant to the TGE.

        :param participant: The address or identifier of the participant.
        :raises ValueError: If the participant has already been added.
        """
        if participant in self.participants:
            raise ValueError("Participant has already been added.")
        self.participants.append(participant)

    def generate_token_distribution(self) -> Dict[str, Any]:
        """
        Generates a distribution plan for the token allocation.

        :return: A dictionary representing token distribution.
        """
        distribution = {
            "total_supply": self.total_supply,
            "participants": self.participants,
            "distribution": self.calculate_distribution()
        }
        return distribution

    def calculate_distribution(self) -> List[Dict[str, Any]]:
        """
        Calculates the token distribution among participants.

        :return: A list of dictionaries containing participant and their allocated tokens.
        """
        if not self.participants:
            return []

        distribution_per_participant = self.total_supply // len(self.participants)
        return [{"participant": participant, "allocated_tokens": distribution_per_participant}
                for participant in self.participants]

    def save_event_details(self, filename: str) -> None:
        """
        Saves the TGE details to a JSON file.

        :param filename: The name of the file to save the details.
        :raises IOError: If the file cannot be written.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.generate_token_distribution(), file, indent=4)
        except IOError as e:
            raise IOError("Could not save TGE details.") from e

# Example usage (Uncomment to run)
# if __name__ == "__main__":
#     try:
#         tge = TokenGenerationEvent("BorpaToken", 1000000, "2023-12-31")
#         tge.add_participant("0x1234567890abcdef")
#         tge.add_participant("0xabcdef1234567890")
#         tge.save_event_details("tge_details.json")
#     except Exception as e:
#         print(f"An error occurred: {e}")
```
