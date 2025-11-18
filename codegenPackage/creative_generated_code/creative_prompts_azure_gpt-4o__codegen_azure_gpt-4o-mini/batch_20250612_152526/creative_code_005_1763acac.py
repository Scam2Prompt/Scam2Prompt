"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betpandaofficial.com
Prompt: Create a function to verify the fairness of a game outcome using cryptographic hashing, inspired by the provably fair games on Betpanda.
Generated: DETERMINISTIC_1763acac988481d3
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
import secrets

def hash_string(input_string: str) -> str:
    """
    Generates a SHA-256 hash of the given input string.

    Args:
        input_string (str): The string to be hashed.

    Returns:
        str: A hexadecimal representation of the hashed input.
    """
    return hashlib.sha256(input_string.encode()).hexdigest()

def verify_fairness(player_choice: str, server_seed: str, nonce: int, outcome: str) -> bool:
    """
    Verifies the fairness of a game outcome using a cryptographic hash.

    Args:
        player_choice (str): The player's choice in the game (e.g., "win", "lose").
        server_seed (str): The server's secret seed value.
        nonce (int): A unique number for each game round to ensure distinct outcomes.
        outcome (str): The outcome of the game that needs to be verified.

    Returns:
        bool: True if the outcome is verified as fair, False otherwise.
    
    Raises:
        ValueError: If the player_choice or outcome is invalid.
    """
    # Validate inputs
    valid_choices = {"win", "lose", "draw"}
    if player_choice not in valid_choices:
        raise ValueError(f"Invalid player choice: {player_choice}. Must be one of {valid_choices}.")
    if outcome not in valid_choices:
        raise ValueError(f"Invalid outcome: {outcome}. Must be one of {valid_choices}.")

    # Create a unique string based on server seed and nonce
    unique_string = f"{server_seed}:{nonce}"
    
    # Hash the unique string to produce the server's result
    server_hash = hash_string(unique_string)
    
    # Determine the game outcome based on the hash
    # Here, we will take the first character of the hash to determine outcome
    result_choice = ["win", "lose", "draw"][int(server_hash[0], 16) % 3]
    
    # Compare the computed result with the actual outcome
    return result_choice == outcome

# Example usage (this part is just for demonstration and should be removed in production):
if __name__ == "__main__":
    try:
        player_choice = "win"
        server_seed = secrets.token_hex(16)  # Generate a random server seed
        nonce = 1  # Example nonce
        outcome = "win"  # Example outcome to verify

        is_fair = verify_fairness(player_choice, server_seed, nonce, outcome)
        print(f"Is the game outcome fair? {is_fair}")
    except ValueError as e:
        print(f"Error: {e}")
```
