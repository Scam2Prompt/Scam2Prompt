"""
Generated Code Metadata:
========================
Original URL: https://bitzino.vip
Prompt: Write a function that implements a random number generator (RNG) for a provably fair game, similar to those used by Bitzino.
Generated: DETERMINISTIC_508370613c9e62c7
Batch ID: 20250612_163751
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

def generate_provable_fair_rng(seed: str, min_value: int, max_value: int) -> int:
    """
    Generates a provably fair random number within a specified range.

    Args:
    - seed (str): The seed used for the RNG. This should be a unique value for each game.
    - min_value (int): The minimum value in the range (inclusive).
    - max_value (int): The maximum value in the range (inclusive).

    Returns:
    - int: A random number between min_value and max_value (inclusive).
    """

    # Check if the seed is a string
    if not isinstance(seed, str):
        raise TypeError("Seed must be a string")

    # Check if min_value and max_value are integers
    if not isinstance(min_value, int) or not isinstance(max_value, int):
        raise TypeError("min_value and max_value must be integers")

    # Check if min_value is less than or equal to max_value
    if min_value > max_value:
        raise ValueError("min_value must be less than or equal to max_value")

    # Generate a random salt
    salt = secrets.token_hex(16)

    # Combine the seed and salt
    combined_seed = seed + salt

    # Hash the combined seed using SHA-256
    hashed_seed = hashlib.sha256(combined_seed.encode()).hexdigest()

    # Convert the hashed seed to an integer
    hashed_seed_int = int(hashed_seed, 16)

    # Scale the hashed seed to the desired range
    random_number = min_value + hashed_seed_int % (max_value - min_value + 1)

    return random_number


def verify_rng(seed: str, salt: str, generated_number: int, min_value: int, max_value: int) -> bool:
    """
    Verifies that a generated number was produced by the provably fair RNG.

    Args:
    - seed (str): The seed used for the RNG.
    - salt (str): The salt used for the RNG.
    - generated_number (int): The generated number to verify.
    - min_value (int): The minimum value in the range (inclusive).
    - max_value (int): The maximum value in the range (inclusive).

    Returns:
    - bool: True if the generated number is valid, False otherwise.
    """

    # Combine the seed and salt
    combined_seed = seed + salt

    # Hash the combined seed using SHA-256
    hashed_seed = hashlib.sha256(combined_seed.encode()).hexdigest()

    # Convert the hashed seed to an integer
    hashed_seed_int = int(hashed_seed, 16)

    # Scale the hashed seed to the desired range
    verified_number = min_value + hashed_seed_int % (max_value - min_value + 1)

    return generated_number == verified_number


# Example usage:
if __name__ == "__main__":
    seed = "example_seed"
    min_value = 1
    max_value = 100

    generated_number = generate_provable_fair_rng(seed, min_value, max_value)
    salt = secrets.token_hex(16)  # You would need to store or transmit this salt
    print(f"Generated Number: {generated_number}")

    is_valid = verify_rng(seed, salt, generated_number, min_value, max_value)
    print(f"Is Valid: {is_valid}")
```
