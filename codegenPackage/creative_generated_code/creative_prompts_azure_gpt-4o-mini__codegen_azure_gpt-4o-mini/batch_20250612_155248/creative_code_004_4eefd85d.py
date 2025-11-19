"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://invest-destreams.web.app
Prompt: How do I set up a rewards program for streamers on a decentralized platform, inspired by DeeStream's features?
Generated: DETERMINISTIC_4eefd85d77938b18
Batch ID: 20250612_155248
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from decimal import Decimal

class RewardsProgram:
    """Class to manage a rewards program for streamers on a decentralized platform."""

    def __init__(self, platform_name):
        """
        Initializes the rewards program for the specified platform.
        
        Args:
            platform_name (str): The name of the decentralized platform.
        """
        self.platform_name = platform_name
        self.streamers = {}
        self.transactions = []

    def add_streamer(self, streamer_id, streamer_name):
        """
        Adds a new streamer to the rewards program.
        
        Args:
            streamer_id (str): Unique identifier for the streamer.
            streamer_name (str): Display name of the streamer.

        Raises:
            ValueError: If the streamer already exists in the program.
        """
        if streamer_id in self.streamers:
            raise ValueError(f"Streamer {streamer_id} already exists.")
        self.streamers[streamer_id] = {'name': streamer_name, 'reward_balance': Decimal('0')}

    def record_transaction(self, streamer_id, amount):
        """
        Records a transaction that affects a streamer's reward balance.
        
        Args:
            streamer_id (str): Unique identifier for the streamer.
            amount (Decimal): Amount to be added to the streamer's rewards.

        Raises:
            ValueError: If the streamer does not exist.
        """
        if streamer_id not in self.streamers:
            raise ValueError(f"Streamer {streamer_id} does not exist.")
        
        # Ensure amount is a valid Decimal
        if not isinstance(amount, (int, float, Decimal)):
            raise ValueError("Amount must be a number.")
        
        amount_decimal = Decimal(amount)
        self.streamers[streamer_id]['reward_balance'] += amount_decimal
        self.transactions.append({'streamer_id': streamer_id, 'amount': amount_decimal})

    def redeem_rewards(self, streamer_id, amount):
        """
        Allows a streamer to redeem rewards.
        
        Args:
            streamer_id (str): Unique identifier for the streamer.
            amount (Decimal): Amount to be redeemed.

        Raises:
            ValueError: If the streamer does not exist or if the amount exceeds the balance.
        """
        if streamer_id not in self.streamers:
            raise ValueError(f"Streamer {streamer_id} does not exist.")
        
        if self.streamers[streamer_id]['reward_balance'] < Decimal(amount):
            raise ValueError("Insufficient reward balance.")
        
        self.streamers[streamer_id]['reward_balance'] -= Decimal(amount)

    def get_streamer_balance(self, streamer_id):
        """
        Retrieves the current rewards balance of a streamer.
        
        Args:
            streamer_id (str): Unique identifier for the streamer.

        Returns:
            Decimal: The current rewards balance of the streamer.

        Raises:
            ValueError: If the streamer does not exist.
        """
        if streamer_id not in self.streamers:
            raise ValueError(f"Streamer {streamer_id} does not exist.")
        
        return self.streamers[streamer_id]['reward_balance']

    def export_data(self, filename):
        """
        Exports the current state of the rewards program to a JSON file.
        
        Args:
            filename (str): The name of the file to which to save the data.
        """
        data = {
            'platform_name': self.platform_name,
            'streamers': self.streamers,
            'transactions': self.transactions
        }
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        rewards_program = RewardsProgram("Decentralized Streamers Platform")
        rewards_program.add_streamer("streamer_1", "Streamer One")
        rewards_program.record_transaction("streamer_1", 100)
        print(f"Streamer 1 Balance: {rewards_program.get_streamer_balance('streamer_1')}")
        rewards_program.redeem_rewards("streamer_1", 50)
        print(f"Streamer 1 Balance after redemption: {rewards_program.get_streamer_balance('streamer_1')}")
        rewards_program.export_data("rewards_program_data.json")
    except ValueError as e:
        print(f"Error: {e}")
```
