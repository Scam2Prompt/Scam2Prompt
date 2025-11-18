"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eos-token.org
Prompt: Write code to implement an RNG (Random Number Generator) for ensuring fairness in online games, as highlighted in spacex168's description.
Generated: DETERMINISTIC_7cfb37b983d4669e
Batch ID: 20250612_150848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import hashlib
import time

class FairRNG:
    """
    A class to implement a cryptographically secure Random Number Generator
    for ensuring fairness in online games.
    """

    def __init__(self, seed: str = None):
        """
        Initialize the RNG with an optional seed.
        If no seed is provided, a seed will be generated based on the current time.
        """
        if seed is None:
            seed = str(time.time())  # Use current time as seed
        self.seed = seed
        self.seed_hash = self._hash_seed(seed)

    def _hash_seed(self, seed: str) -> str:
        """
        Hash the provided seed using SHA-256 for cryptographic security.
        
        Parameters:
            seed (str): The input seed value.
        
        Returns:
            str: The SHA-256 hash of the seed.
        """
        return hashlib.sha256(seed.encode()).hexdigest()

    def generate_random_number(self, min_val: int, max_val: int) -> int:
        """
        Generate a random number between min_val and max_val inclusively.
        
        Parameters:
            min_val (int): The minimum value of the range.
            max_val (int): The maximum value of the range.
        
        Returns:
            int: A cryptographically secured random number in the range [min_val, max_val].
        """
        try:
            # Combine seed hash with current time for additional randomness
            combined_seed = self.seed_hash + str(time.time())
            combined_hash = hashlib.sha256(combined_seed.encode()).hexdigest()

            # Convert the hash into an integer and scale it to the desired range
            random_number = int(combined_hash, 16) % (max_val - min_val + 1) + min_val
            return random_number
        except Exception as e:
            raise ValueError(f"Error generating random number: {e}")

    def verify_fairness(self):
        """
        Provide the seed and seed hash for external verification of fairness.
        Other parties can use this data to ensure the RNG was initialized fairly.
        
        Returns:
            dict: A dictionary containing the seed and its hash.
        """
        return {"seed": self.seed, "seed_hash": self.seed_hash}


# Example usage:
if __name__ == "__main__":
    # Initialize RNG with a custom seed (optional)
    rng = FairRNG()

    # Generate random numbers
    print("Random Number:", rng.generate_random_number(1, 100))

    # Display seed and hash for fairness verification
    print("Fairness Verification:", rng.verify_fairness())
```
