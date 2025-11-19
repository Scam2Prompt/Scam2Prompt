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
import hmac
import secrets
import time

class ProvablyFairGame:
    def __init__(self, server_seed, client_seed=None):
        """
        Initialize the game with a server seed and optional client seed.

        :param server_seed: The server's secret seed.
        :param client_seed: The client's seed, defaults to a random value if not provided.
        """
        self.server_seed = server_seed
        self.client_seed = client_seed if client_seed else self.generate_client_seed()

    @staticmethod
    def generate_client_seed():
        """
        Generate a random client seed.

        :return: A random client seed.
        """
        return secrets.token_hex(16)

    def get_combined_seed(self, round_id):
        """
        Combine the server and client seeds with a round ID to create a unique seed for each round.

        :param round_id: A unique identifier for the round.
        :return: The combined seed.
        """
        return f"{self.server_seed}{self.client_seed}{round_id}"

    def generate_outcome(self, round_id, bet_amount, bet_type):
        """
        Generate a game outcome based on the combined seed.

        :param round_id: A unique identifier for the round.
        :param bet_amount: The amount bet by the client.
        :param bet_type: The type of bet (e.g., "higher" or "lower").
        :return: The game outcome (win or loss).
        """
        combined_seed = self.get_combined_seed(round_id)
        hash_object = hashlib.sha256(combined_seed.encode())
        outcome_hash = hash_object.hexdigest()
        outcome = int(outcome_hash, 16) / (2**256 - 1)

        # Simple win/loss logic for demonstration purposes
        if bet_type == "higher":
            return outcome > 0.5
        elif bet_type == "lower":
            return outcome < 0.5
        else:
            raise ValueError("Invalid bet type")

    def verify_outcome(self, round_id, bet_amount, bet_type, outcome):
        """
        Verify the game outcome by re-generating the combined seed and outcome.

        :param round_id: A unique identifier for the round.
        :param bet_amount: The amount bet by the client.
        :param bet_type: The type of bet (e.g., "higher" or "lower").
        :param outcome: The claimed game outcome (win or loss).
        :return: True if the outcome is valid, False otherwise.
        """
        generated_outcome = self.generate_outcome(round_id, bet_amount, bet_type)
        return generated_outcome == outcome

def main():
    server_seed = "my_secret_server_seed"
    client_seed = "my_client_seed"
    game = ProvablyFairGame(server_seed, client_seed)

    round_id = int(time.time() * 1000)
    bet_amount = 1.0
    bet_type = "higher"

    outcome = game.generate_outcome(round_id, bet_amount, bet_type)
    print(f"Game outcome: {'Win' if outcome else 'Loss'}")

    is_valid = game.verify_outcome(round_id, bet_amount, bet_type, outcome)
    print(f"Is outcome valid? {is_valid}")

if __name__ == "__main__":
    main()
```
