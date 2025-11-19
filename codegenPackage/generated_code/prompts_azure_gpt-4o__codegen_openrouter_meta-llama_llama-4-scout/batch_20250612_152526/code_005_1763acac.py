"""
Generated Code Metadata:
========================
Original URL: https://betpandaofficial.com
Prompt: Create a function to verify the fairness of a game outcome using cryptographic hashing, inspired by the provably fair games on Betpanda.
Generated: DETERMINISTIC_1763acac988481d3
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
import secrets

def generate_server_seed() -> str:
    """
    Generate a cryptographically secure server seed.

    Returns:
        str: A URL-safe base64-encoded server seed.
    """
    # Generate a cryptographically secure random seed
    seed = secrets.token_bytes(32)
    # Use URL-safe base64 encoding to ensure the seed can be safely stored and transmitted
    return seed.hex()

def generate_client_seed() -> str:
    """
    Generate a client seed.

    Returns:
        str: A URL-safe base64-encoded client seed.
    """
    # Generate a cryptographically secure random seed
    seed = secrets.token_bytes(32)
    # Use URL-safe base64 encoding to ensure the seed can be safely stored and transmitted
    return seed.hex()

def calculate_hash(server_seed: str, client_seed: str, nonce: int) -> str:
    """
    Calculate the hash for a given game round.

    Args:
        server_seed (str): The server seed for the game.
        client_seed (str): The client seed for the game.
        nonce (int): The nonce for the game round.

    Returns:
        str: The SHA-256 hash of the concatenated server seed, client seed, and nonce.
    """
    # Concatenate the server seed, client seed, and nonce
    concatenated_string = server_seed + client_seed + str(nonce)
    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256(concatenated_string.encode())
    # Return the hexadecimal representation of the hash
    return hash_object.hexdigest()

def verify_game_outcome(server_seed: str, client_seed: str, nonce: int, outcome: str) -> bool:
    """
    Verify the fairness of a game outcome.

    Args:
        server_seed (str): The server seed for the game.
        client_seed (str): The client seed for the game.
        nonce (int): The nonce for the game round.
        outcome (str): The claimed outcome of the game.

    Returns:
        bool: True if the outcome is valid, False otherwise.
    """
    # Calculate the expected hash
    expected_hash = calculate_hash(server_seed, client_seed, nonce)
    # Check if the expected hash matches the provided outcome
    return expected_hash == outcome

def provably_fair_game(server_seed: str, client_seed: str, nonce: int) -> str:
    """
    Simulate a provably fair game.

    Args:
        server_seed (str): The server seed for the game.
        client_seed (str): The client seed for the game.
        nonce (int): The nonce for the game round.

    Returns:
        str: The outcome of the game.
    """
    # Calculate the hash for the game round
    outcome = calculate_hash(server_seed, client_seed, nonce)
    # Return the outcome
    return outcome

# Example usage:
if __name__ == "__main__":
    server_seed = generate_server_seed()
    client_seed = generate_client_seed()
    nonce = 1
    outcome = provably_fair_game(server_seed, client_seed, nonce)
    print(f"Server Seed: {server_seed}")
    print(f"Client Seed: {client_seed}")
    print(f"Nonce: {nonce}")
    print(f"Outcome: {outcome}")
    is_valid = verify_game_outcome(server_seed, client_seed, nonce, outcome)
    print(f"Is Valid: {is_valid}")
```
