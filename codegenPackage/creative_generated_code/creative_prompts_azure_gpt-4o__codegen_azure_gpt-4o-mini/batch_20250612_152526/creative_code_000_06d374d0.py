"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betpandaofficial.com
Prompt: Write a Python script to simulate a provably fair game mechanism similar to those described on Betpanda, ensuring outcome verification for fairness.
Generated: DETERMINISTIC_06d374d0a0e0c284
Batch ID: 20250612_152526
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
    def __init__(self):
        self.server_seed = self.generate_server_seed()
        self.client_seed = None
        self.nonce = 0

    def generate_server_seed(self):
        """Generate a secure random server seed."""
        return hashlib.sha256(os.urandom(32)).hexdigest()

    def set_client_seed(self, client_seed):
        """Set a client seed for the game.
        
        Args:
            client_seed (str): A string representing the client's chosen seed.
        """
        self.client_seed = client_seed

    def generate_random_number(self):
        """Generate a random number using both server and client seeds, along with a nonce.
        
        Returns:
            int: A number between 0 and 100.
        """
        if self.client_seed is None:
            raise ValueError("Client seed must be set before generating a random number.")

        # Combine the seeds and nonce
        combined = f"{self.server_seed}{self.client_seed}{self.nonce}".encode('utf-8')
        # Create a hash of the combined string
        hash_result = hashlib.sha256(combined).hexdigest()
        # Convert the hash to an integer and scale it to range 0-100
        random_number = int(hash_result, 16) % 101
        return random_number

    def play_game(self, client_seed):
        """Play a round of the game with the provided client seed.
        
        Args:
            client_seed (str): A string representing the client's chosen seed.
        
        Returns:
            dict: A dictionary containing the server seed, client seed, nonce, and the result.
        """
        self.set_client_seed(client_seed)
        result = self.generate_random_number()
        # Increment nonce for the next round
        self.nonce += 1

        # Prepare and return the game result
        return {
            "server_seed": self.server_seed,
            "client_seed": self.client_seed,
            "nonce": self.nonce - 1,
            "result": result
        }

    def verify_outcome(self, server_seed, client_seed, nonce, result):
        """Verify the fairness of the game outcome.
        
        Args:
            server_seed (str): The server seed used in the game.
            client_seed (str): The client seed used in the game.
            nonce (int): The nonce used in the game.
            result (int): The result to verify.
        
        Returns:
            bool: True if the result is valid, False otherwise.
        """
        # Recalculate the random number with the given seeds and nonce
        combined = f"{server_seed}{client_seed}{nonce}".encode('utf-8')
        hash_result = hashlib.sha256(combined).hexdigest()
        calculated_result = int(hash_result, 16) % 101

        # Return whether the calculated result matches the provided result
        return calculated_result == result

# Example usage
if __name__ == "__main__":
    game = ProvablyFairGame()
    client_seed = "my_client_seed"
    
    # Play the game
    outcome = game.play_game(client_seed)
    print("Game Outcome:", outcome)

    # Verify the outcome
    valid = game.verify_outcome(
        server_seed=outcome["server_seed"],
        client_seed=outcome["client_seed"],
        nonce=outcome["nonce"],
        result=outcome["result"]
    )
    print("Is the outcome valid?", valid)
```
