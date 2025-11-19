"""
Generated Code Metadata:
========================
Original URL: https://betpandaofficial.com
Prompt: Write a Python script to simulate a provably fair game mechanism similar to those described on Betpanda, ensuring outcome verification for fairness.
Generated: DETERMINISTIC_06d374d0a0e0c284
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import os
import random

class ProvablyFairGame:
    def __init__(self):
        self.server_seed = self.generate_server_seed()
        self.client_seed = None
        self.nonce = 0

    def generate_server_seed(self):
        """Generates a random server seed using os.urandom for cryptographic security."""
        return os.urandom(32).hex()

    def set_client_seed(self, client_seed):
        """Sets the client seed for the game. The client seed should be a string."""
        if not isinstance(client_seed, str):
            raise ValueError("Client seed must be a string.")
        self.client_seed = client_seed

    def roll_dice(self):
        """Simulates rolling a dice and returns the outcome based on the server and client seeds."""
        if self.client_seed is None:
            raise ValueError("Client seed must be set before rolling the dice.")

        # Combine seeds and nonce to create a unique hash
        combined_seed = f"{self.server_seed}{self.client_seed}{self.nonce}".encode()
        hash_result = hashlib.sha256(combined_seed).hexdigest()

        # Convert the hash to an integer and determine the outcome
        outcome = int(hash_result, 16) % 6 + 1  # Dice outcome between 1 and 6
        self.nonce += 1  # Increment nonce for the next roll

        return outcome

    def verify_outcome(self, outcome):
        """Verifies the outcome of the game using the server and client seeds."""
        combined_seed = f"{self.server_seed}{self.client_seed}{self.nonce - 1}".encode()
        hash_result = hashlib.sha256(combined_seed).hexdigest()
        expected_outcome = int(hash_result, 16) % 6 + 1

        return expected_outcome == outcome

def main():
    """Main function to run the provably fair game simulation."""
    game = ProvablyFairGame()

    # Set a client seed (this should be provided by the user)
    client_seed = input("Enter your client seed (string): ")
    game.set_client_seed(client_seed)

    # Roll the dice
    outcome = game.roll_dice()
    print(f"Dice rolled: {outcome}")

    # Verify the outcome
    if game.verify_outcome(outcome):
        print("Outcome verified successfully. The game is fair.")
    else:
        print("Outcome verification failed. There may be an issue with the game.")

if __name__ == "__main__":
    main()
```
