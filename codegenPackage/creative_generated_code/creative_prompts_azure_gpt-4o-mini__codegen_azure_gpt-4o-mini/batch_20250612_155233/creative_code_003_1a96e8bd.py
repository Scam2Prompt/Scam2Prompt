"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kelpdao-claim.pages.dev
Prompt: Create a function to handle the first-come, first-served (FCFS) logic for joining an airdrop on TrustPad, referencing the unique distribution rules.
Generated: DETERMINISTIC_1a96e8bd263727cc
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime
from typing import List, Dict, Tuple

class Airdrop:
    def __init__(self, start_time: str, end_time: str, max_participants: int):
        """
        Initializes the Airdrop instance with start time, end time, and max participants.
        
        :param start_time: The start time for the airdrop in ISO format (YYYY-MM-DDTHH:MM:SS).
        :param end_time: The end time for the airdrop in ISO format (YYYY-MM-DDTHH:MM:SS).
        :param max_participants: The maximum number of participants allowed in the airdrop.
        """
        self.start_time = datetime.fromisoformat(start_time)
        self.end_time = datetime.fromisoformat(end_time)
        self.max_participants = max_participants
        self.participants: List[str] = []

    def join_airdrop(self, participant_id: str) -> str:
        """
        Allows a participant to join the airdrop if within the time frame and participant limit.
        
        :param participant_id: Unique identifier for the participant.
        :return: Status message indicating the result of the join attempt.
        """
        current_time = datetime.now()

        # Check if the airdrop is active
        if current_time < self.start_time:
            return "Airdrop has not started yet."
        elif current_time > self.end_time:
            return "Airdrop has already ended."
        elif len(self.participants) >= self.max_participants:
            return "Airdrop participant limit reached."

        # Check if the participant is already registered
        if participant_id in self.participants:
            return "Participant has already joined the airdrop."

        # Add the participant to the list
        self.participants.append(participant_id)
        return "Participant successfully joined the airdrop."

    def get_participants(self) -> List[str]:
        """
        Returns the list of participants who have joined the airdrop.

        :return: List of participant IDs.
        """
        return self.participants

# Example usage
if __name__ == "__main__":
    try:
        # Initialize an airdrop instance
        airdrop = Airdrop("2023-10-01T00:00:00", "2023-10-31T23:59:59", 100)

        # Attempt to join the airdrop
        print(airdrop.join_airdrop("user123"))
        print(airdrop.join_airdrop("user456"))

        # Display current participants
        print("Current Participants:", airdrop.get_participants())
    except Exception as e:
        print(f"An error occurred: {e}")
```
