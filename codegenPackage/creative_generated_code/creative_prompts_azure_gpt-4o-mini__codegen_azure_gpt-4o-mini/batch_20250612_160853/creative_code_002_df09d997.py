"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeihdjl7xixuxxuxsexbtlzb37crgafyrxd5652yvkz4aokv7np4uty.ipfs.dweb.link
Prompt: Can you explain the MOR20 Platform and how it supports the fair launch of the MOR token?
Generated: DETERMINISTIC_df09d99704ef59d4
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
MOR20 Platform - Token Launch Mechanism

This script simulates the MOR20 platform which facilitates the fair launch of the MOR token.
It includes functionalities for launching the token, tracking participants, and ensuring fair distribution.
"""

import random
from datetime import datetime, timedelta

class TokenLaunchError(Exception):
    """Custom exception for token launch errors."""
    pass

class Participant:
    """Class representing a participant in the MOR token launch."""
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address
        self.tokens_received = 0

class MOR20Platform:
    """Class representing the MOR20 platform for launching the MOR token."""

    def __init__(self):
        self.participants = {}
        self.launch_time = None
        self.token_supply = 1_000_000  # Total MOR tokens available

    def set_launch_time(self, hours_ahead=1):
        """Set the launch time for the token."""
        self.launch_time = datetime.now() + timedelta(hours=hours_ahead)

    def register_participant(self, wallet_address):
        """Register a participant for the token launch."""
        if self.launch_time is None:
            raise TokenLaunchError("Launch time must be set before registration.")
        
        if wallet_address in self.participants:
            raise TokenLaunchError("Participant already registered.")

        self.participants[wallet_address] = Participant(wallet_address)

    def allocate_tokens(self):
        """Allocate tokens to registered participants after launch time."""
        if datetime.now() < self.launch_time:
            raise TokenLaunchError("Cannot allocate tokens before launch time.")

        num_participants = len(self.participants)
        if num_participants == 0:
            raise TokenLaunchError("No participants registered for token allocation.")

        # Allocate tokens fairly among participants
        tokens_per_participant = self.token_supply // num_participants
        for participant in self.participants.values():
            participant.tokens_received = tokens_per_participant

    def get_participant_info(self, wallet_address):
        """Return info about a specific participant."""
        if wallet_address not in self.participants:
            raise TokenLaunchError("Participant not found.")
        
        participant = self.participants[wallet_address]
        return {
            "wallet_address": participant.wallet_address,
            "tokens_received": participant.tokens_received,
        }

# Example usage
if __name__ == "__main__":
    try:
        mor_platform = MOR20Platform()
        mor_platform.set_launch_time(hours_ahead=1)  # Set launch time to 1 hour ahead
        mor_platform.register_participant("wallet_1")
        mor_platform.register_participant("wallet_2")
        
        # Wait until the launch time (simulate this in actual implementation)
        # For testing, we can directly call the allocation method
        mor_platform.launch_time = datetime.now()  # Forcing launch time for testing

        mor_platform.allocate_tokens()
        
        # Get participant info
        print(mor_platform.get_participant_info("wallet_1"))
        print(mor_platform.get_participant_info("wallet_2"))

    except TokenLaunchError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
