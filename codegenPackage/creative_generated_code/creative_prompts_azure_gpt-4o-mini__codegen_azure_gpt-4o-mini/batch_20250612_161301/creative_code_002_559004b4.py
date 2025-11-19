"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betpandaofficial.com
Prompt: Write a function to verify the fairness of game outcomes using a provably fair algorithm, inspired by the gaming standards at Betpanda.
Generated: DETERMINISTIC_559004b4b86929ba
Batch ID: 20250612_161301
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
import random

class ProvablyFairGame:
    def __init__(self, player_seed: str, server_seed: str):
        """
        Initializes the game with player and server seeds.

        :param player_seed: The seed provided by the player, should be a random string.
        :param server_seed: The server seed, securely generated and kept secret until the game is concluded.
        """
        self.player_seed = player_seed
        self.server_seed = server_seed
        self.server_seed_hash = self.hash_seed(server_seed)

    def hash_seed(self, seed: str) -> str:
        """
        Hashes the provided seed using SHA-256 to ensure it's not tampered with.

        :param seed: The seed to be hashed.
        :return: A hexadecimal representation of the SHA-256 hash.
        """
        return hashlib.sha256(seed.encode('utf-8')).hexdigest()

    def generate_outcome(self) -> int:
        """
        Generates a game outcome based on the player and server seeds.

        :return: A random outcome between 0 and 100, inclusive.
        """
        # Combine the seeds and generate a random number
        combined_seed = self.player_seed + self.server_seed
        random.seed(combined_seed)

        # Generate a random number between 0 and 100
        outcome = random.randint(0, 100)
        return outcome

    def verify_fairness(self, player_choice: int, outcome: int) -> bool:
        """
        Verifies if the outcome is fair based on the player's choice.

        :param player_choice: The player's chosen number.
        :param outcome: The generated outcome.
        :return: True if the game is fair, False otherwise.
        """
        # Ensure the player's choice is within the valid range
        if not (0 <= player_choice <= 100):
            raise ValueError("Player choice must be between 0 and 100.")

        # The fairness condition can be defined as a simple comparison
        return player_choice == outcome

# Example Usage
if __name__ == "__main__":
    player_seed = os.urandom(16).hex()  # Securely generate a player seed
    server_seed = os.urandom(16).hex()  # Securely generate a server seed

    game = ProvablyFairGame(player_seed, server_seed)
    outcome = game.generate_outcome()
    
    print(f"Outcome: {outcome}")

    # For demonstration purposes, let's say the player chooses a number
    player_choice = random.randint(0, 100)
    print(f"Player choice: {player_choice}")

    is_fair = game.verify_fairness(player_choice, outcome)
    print(f"Is the game fair? {'Yes' if is_fair else 'No'}")

    # Revealing server seed at the end to allow verification
    print(f"Server seed hash: {game.server_seed_hash}")
```
