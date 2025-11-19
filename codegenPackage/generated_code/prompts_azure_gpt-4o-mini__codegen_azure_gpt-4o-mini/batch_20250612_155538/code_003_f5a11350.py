"""
Generated Code Metadata:
========================
Original URL: https://skillchain.io
Prompt: Explain how Skillchain can be utilized by gaming companies to certify player achievements using blockchain.
Generated: DETERMINISTIC_f5a11350836cdf35
Batch ID: 20250612_155538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import hashlib
import json
from datetime import datetime

class Skillchain:
    """
    A class to represent a Skillchain for certifying player achievements using blockchain technology.
    """

    def __init__(self):
        """
        Initializes the Skillchain with an empty list of achievements and a blockchain.
        """
        self.achievements = []
        self.blockchain = []

    def create_achievement(self, player_id, achievement_name, timestamp=None):
        """
        Creates a new achievement for a player.

        Args:
            player_id (str): The unique identifier for the player.
            achievement_name (str): The name of the achievement.
            timestamp (str): The time when the achievement was earned. Defaults to current time.

        Returns:
            dict: A dictionary representing the achievement.
        """
        if timestamp is None:
            timestamp = datetime.utcnow().isoformat()

        achievement = {
            'player_id': player_id,
            'achievement_name': achievement_name,
            'timestamp': timestamp
        }
        self.achievements.append(achievement)
        return achievement

    def hash_achievement(self, achievement):
        """
        Creates a SHA-256 hash of the achievement.

        Args:
            achievement (dict): The achievement to hash.

        Returns:
            str: The SHA-256 hash of the achievement.
        """
        achievement_string = json.dumps(achievement, sort_keys=True).encode()
        return hashlib.sha256(achievement_string).hexdigest()

    def add_to_blockchain(self, achievement):
        """
        Adds an achievement to the blockchain.

        Args:
            achievement (dict): The achievement to add to the blockchain.
        """
        achievement_hash = self.hash_achievement(achievement)
        block = {
            'index': len(self.blockchain) + 1,
            'timestamp': datetime.utcnow().isoformat(),
            'achievement': achievement,
            'hash': achievement_hash
        }
        self.blockchain.append(block)

    def certify_achievement(self, player_id, achievement_name):
        """
        Certifies an achievement for a player by adding it to the blockchain.

        Args:
            player_id (str): The unique identifier for the player.
            achievement_name (str): The name of the achievement.
        """
        try:
            achievement = self.create_achievement(player_id, achievement_name)
            self.add_to_blockchain(achievement)
            print(f"Achievement '{achievement_name}' for player '{player_id}' has been certified.")
        except Exception as e:
            print(f"Error certifying achievement: {e}")

    def get_blockchain(self):
        """
        Returns the current state of the blockchain.

        Returns:
            list: The blockchain containing all certified achievements.
        """
        return self.blockchain

# Example usage
if __name__ == "__main__":
    skillchain = Skillchain()
    skillchain.certify_achievement("player123", "First Blood")
    skillchain.certify_achievement("player456", "Level Up")
    
    # Print the blockchain to verify achievements
    print(json.dumps(skillchain.get_blockchain(), indent=4))
```
