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
import hmac


def verify_game_outcome(server_seed: str, client_seed: str, nonce: int, number_of_outcomes: int) -> int:
    """
    Verifies the fairness of a game outcome using a provably fair algorithm.

    Args:
        server_seed (str): The server's secret random seed, typically generated securely.
        client_seed (str): The player's provided random seed.
        nonce (int): A unique number for the game round (incremented per game).
        number_of_outcomes (int): The total number of possible outcomes in the game.

    Returns:
        int: The index of the outcome (0-based) determined to be fair, between 0 and number_of_outcomes - 1.

    Raises:
        ValueError: If any of the inputs are invalid (e.g., number_of_outcomes <= 0).
    """

    # Input validation
    if not isinstance(server_seed, str) or not isinstance(client_seed, str):
        raise ValueError("Both server_seed and client_seed must be strings.")
    if not isinstance(nonce, int) or nonce < 0:
        raise ValueError("Nonce must be a non-negative integer.")
    if not isinstance(number_of_outcomes, int) or number_of_outcomes <= 0:
        raise ValueError("Number of outcomes must be a positive integer.")

    # Combine server seed, client seed, and nonce to create the input for the hash function
    combined_input = f"{server_seed}:{client_seed}:{nonce}"

    # Generate a HMAC-SHA256 hash using the server seed as the key
    hmac_hash = hmac.new(server_seed.encode('utf-8'), combined_input.encode('utf-8'), hashlib.sha256).hexdigest()

    # Convert the hash into a deterministic integer
    random_number = int(hmac_hash, 16)

    # Determine the outcome index using modulo operation
    outcome_index = random_number % number_of_outcomes

    return outcome_index


if __name__ == "__main__":
    # Example usage:
    try:
        server_seed = "secure_random_seed_server_12345"
        client_seed = "player_random_seed_67890"
        nonce = 1
        number_of_outcomes = 10

        fair_outcome_index = verify_game_outcome(server_seed, client_seed, nonce, number_of_outcomes)
        print(f"Fair game outcome index: {fair_outcome_index}")
    except ValueError as e:
        print(f"Error: {e}")
```
