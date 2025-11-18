"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherroll.cash
Prompt: Generate code to simulate a "provably fair" mechanism for an online casino game, referencing the features described on "etherroll.cash."
Generated: DETERMINISTIC_aa3d6fe35467018b
Batch ID: 20250612_153821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import random
import json
from typing import Dict, Tuple


class ProvablyFairCasinoGame:
    def __init__(self):
        """
        Initialize the Casino Game with a random server seed.
        """
        # Generate random server seed during initialization
        self.server_seed = self._generate_random_seed()

    def _generate_random_seed(self) -> str:
        """
        Generate a random seed for the server.
        Returns:
            str: A random hexadecimal string representing the server seed.
        """
        return hashlib.sha256(str(random.randint(0, 1_000_000)).encode()).hexdigest()

    def get_server_seed_hash(self) -> str:
        """
        Provide a hash of the server seed to the client for verification purposes.
        Returns:
            str: Hexadecimal hash of the server seed.
        """
        return hashlib.sha256(self.server_seed.encode()).hexdigest()

    def roll_dice(self, client_seed: str, bet_number: int) -> Dict:
        """
        Simulate a dice roll based on client and server seeds and determine the outcome.
        Args:
            client_seed (str): The seed provided by the client for randomness mixing.
            bet_number (int): The number the client is betting on (1-100).
        Returns:
            Dict: A result dictionary containing the roll outcome and verification data.
        """
        try:
            if not (1 <= bet_number <= 100):
                raise ValueError("Bet number must be between 1 and 100.")

            # Combine client seed and server seed for randomness
            combined_seed = f"{self.server_seed}:{client_seed}"
            random_hash = hashlib.sha256(combined_seed.encode()).hexdigest()
            roll_result = int(random_hash[:8], 16) % 100 + 1  # Generate roll between 1-100

            # Determine win/loss
            is_win = roll_result < bet_number
            
            return {
                "roll_result": roll_result,
                "is_win": is_win,
                "bet_number": bet_number,
                "client_seed": client_seed,
                "server_seed": self.server_seed,
                "server_seed_hash": self.get_server_seed_hash(),
                "verification_instructions": 
                "Combine client_seed and server_seed, hash them with SHA256, "
                "take the first 8 characters, convert to decimal, modulo 100, and add 1."
            }
        except Exception as e:
            return {"error": str(e)}

    def reveal_server_seed(self) -> str:
        """
        Reveal the server seed after a game round for verification purposes.
        Returns:
            str: The server seed used in the last game round.
        """
        return self.server_seed


# Example usage
if __name__ == "__main__":
    # Initialize the game
    casino_game = ProvablyFairCasinoGame()

    # Client receives server seed hash from the server
    server_seed_hash = casino_game.get_server_seed_hash()
    print(f"Server Seed Hash: {server_seed_hash}")

    # Client provides their own seed and a bet number
    client_seed = "my_unique_client_seed"
    bet_number = 50

    # Simulate a dice roll
    game_result = casino_game.roll_dice(client_seed, bet_number)
    print(json.dumps(game_result, indent=4))

    # Reveal server seed for verification
    revealed_server_seed = casino_game.reveal_server_seed()
    print(f"Revealed Server Seed: {revealed_server_seed}")
```
