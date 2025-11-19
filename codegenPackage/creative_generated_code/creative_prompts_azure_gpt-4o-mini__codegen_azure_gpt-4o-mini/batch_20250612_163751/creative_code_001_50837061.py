"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitzino.vip
Prompt: Write a function that implements a random number generator (RNG) for a provably fair game, similar to those used by Bitzino.
Generated: DETERMINISTIC_508370613c9e62c7
Batch ID: 20250612_163751
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

class ProvablyFairRNG:
    def __init__(self, secret: str):
        """
        Initializes the ProvablyFairRNG with a secret key.

        :param secret: A unique secret string that is known only to the server.
        """
        self.secret = secret.encode('utf-8')

    def generate_hash(self, client_seed: str, server_seed: str, nonce: int) -> str:
        """
        Generates a SHA-256 hash based on the client seed, server seed, and nonce.

        :param client_seed: A seed provided by the client.
        :param server_seed: The server's secret seed.
        :param nonce: A counter that is incremented with each call.
        :return: A hexadecimal SHA-256 hash.
        """
        # Combine seeds and nonce into a single string
        input_string = f"{client_seed}:{server_seed}:{nonce}".encode('utf-8')
        # Return the SHA-256 hash in hexadecimal format
        return hashlib.sha256(input_string).hexdigest()

    def random_number(self, client_seed: str, nonce: int) -> int:
        """
        Generates a random number between 0 and 100 based on the provided seeds.

        :param client_seed: A seed provided by the client.
        :param nonce: A counter that is incremented with each call.
        :return: A random integer between 0 and 100.
        """
        try:
            # Generate a unique server seed for each game
            server_seed = os.urandom(32)  # Secure random server seed
            # Generate the hash using the client seed, server seed, and nonce
            hash_result = self.generate_hash(client_seed, server_seed.hex(), nonce)
            # Convert the first 8 characters of the hash to an integer
            random_num = int(hash_result[:8], 16)
            # Map the random number to a range of 0 to 100
            return random_num % 101  # Adjusting to fit in the range [0, 100]
        except Exception as e:
            # Handle any unexpected errors and log them
            print(f"Error generating random number: {e}")
            return None  # Return None in case of an error

# Example usage:
if __name__ == "__main__":
    rng = ProvablyFairRNG(secret="a_unique_secret_key")
    client_seed = "user_generated_client_seed"  # This should be provided by the client
    nonce = 0  # Start with an initial nonce value

    # Generate a random number
    random_number = rng.random_number(client_seed, nonce)
    if random_number is not None:
        print(f"Generated random number: {random_number}")
```
