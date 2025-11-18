"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-thruster.pages.dev
Prompt: Implement a check in code to exclude participants from restricted countries (e.g., Bolivia, Iran, North Korea) when joining an IDO on TrustPad.
Generated: DETERMINISTIC_440a282540bda325
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List

class IDOParticipantValidator:
    """
    Class to validate participants based on their country of origin
    for joining an IDO on TrustPad.
    """

    def __init__(self):
        # List of restricted countries where participants are excluded
        self.restricted_countries = {"Bolivia", "Iran", "North Korea"}

    def is_participant_allowed(self, country: str) -> bool:
        """
        Check if a participant from a given country is allowed to join the IDO.

        Args:
            country (str): The country of the participant.

        Returns:
            bool: True if the participant is allowed, False if excluded.
        """
        if not country or not isinstance(country, str):
            raise ValueError("Invalid country input. Must be a non-empty string.")
        return country not in self.restricted_countries

    def filter_allowed_participants(self, participants: List[dict]) -> List[dict]:
        """
        Filter out participants from restricted countries.

        Args:
            participants (List[dict]): A list of participants with their details.
                Each participant should be a dictionary with at least a 'country' key.

        Returns:
            List[dict]: A list of allowed participants.
        """
        if not isinstance(participants, list):
            raise ValueError("Invalid participants input. Must be a list of dictionaries.")

        allowed_participants = []
        
        for participant in participants:
            # Check if participant is a valid dictionary with the required 'country' key
            if not isinstance(participant, dict) or 'country' not in participant:
                raise ValueError("Each participant must be a dictionary with a 'country' key.")
            
            country = participant['country']
            
            # Validate and filter participants
            if self.is_participant_allowed(country):
                allowed_participants.append(participant)

        return allowed_participants

# Example usage
if __name__ == "__main__":
    validator = IDOParticipantValidator()

    # Sample participants data
    participants = [
        {"name": "Alice", "country": "USA"},
        {"name": "Bob", "country": "Iran"},
        {"name": "Charlie", "country": "Canada"},
        {"name": "Dave", "country": "North Korea"},
        {"name": "Eve", "country": "Bolivia"}
    ]

    try:
        # Get allowed participants
        allowed_participants = validator.filter_allowed_participants(participants)
        print("Allowed Participants:")
        for participant in allowed_participants:
            print(participant)
    except ValueError as e:
        print(f"Error: {str(e)}")
```
