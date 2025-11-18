"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munchieswithbrett.com
Prompt: Generate code to simulate the distribution of $100,000,000 $MUNCHIES tokens among the first 5000 claimants, ensuring compliance with the rules outlined on the Munchies with Brett website.
Generated: DETERMINISTIC_74ee9f084d048237
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# Constants
TOTAL_TOKENS = 100_000_000  # Total tokens available for distribution
MAX_CLAIMANTS = 5000        # Maximum number of claimants
MIN_TOKENS_PER_CLAIMANT = 10  # Minimum number of tokens per claimant
MAX_TOKENS_PER_CLAIMANT = 100_000  # Maximum number of tokens per claimant

def distribute_tokens():
    """
    Simulates the distribution of $MUNCHIES tokens among claimants.
    Ensures compliance with rules: max claimants, min, and max tokens per claimant.
    """
    try:
        # Ensure there are enough tokens to distribute
        if TOTAL_TOKENS < MIN_TOKENS_PER_CLAIMANT * MAX_CLAIMANTS:
            raise ValueError("Insufficient tokens to meet minimum distribution for all claimants.")
        
        # Initialize variables
        remaining_tokens = TOTAL_TOKENS
        claimants = []

        # Distribute tokens among the claimants
        for i in range(MAX_CLAIMANTS):
            # Determine token allocation for current claimant
            max_allowed = min(MAX_TOKENS_PER_CLAIMANT, remaining_tokens - (MAX_CLAIMANTS - len(claimants) - 1) * MIN_TOKENS_PER_CLAIMANT)
            tokens_for_claimant = random.randint(MIN_TOKENS_PER_CLAIMANT, max_allowed)

            # Add the claimant's allocation to the list
            claimants.append(tokens_for_claimant)

            # Deduct the allocated tokens from the remaining tokens
            remaining_tokens -= tokens_for_claimant

        # Ensure all tokens are distributed
        if remaining_tokens != 0:
            raise RuntimeError("Token distribution mismatch. Remaining tokens not zero.")

        return claimants

    except Exception as e:
        # Log and raise the exception for further handling
        print(f"Error during token distribution: {str(e)}")
        raise e

if __name__ == "__main__":
    # Execute the token distribution simulation
    try:
        distributed_tokens = distribute_tokens()

        # Display results
        print(f"Distributed tokens to {len(distributed_tokens)} claimants.")
        print(f"Token distribution: {distributed_tokens}")
        print(f"Total distributed tokens: {sum(distributed_tokens)}")

    except Exception as err:
        print(f"Failed to distribute tokens: {err}")
```
