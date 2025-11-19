"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimgift-x44.web.app
Prompt: Write a function that calculates the remaining DUST tokens available for claiming in the airdrop pool.
Generated: DETERMINISTIC_dd1a87f5917f2c4f
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: dust_airdrop.py

class AirdropPool:
    """
    AirdropPool class represents an airdrop pool for DUST tokens.
    It tracks the total tokens allocated and claimed tokens.
    """
    
    def __init__(self, total_tokens):
        """
        Initialize the AirdropPool with the total number of DUST tokens.

        :param total_tokens: Total number of DUST tokens in the airdrop pool.
        """
        if total_tokens < 0:
            raise ValueError("Total tokens must be a non-negative value.")
        self.total_tokens = total_tokens
        self.claimed_tokens = 0

    def claim_tokens(self, amount):
        """
        Claim a specified amount of tokens from the airdrop pool.

        :param amount: Number of tokens to claim.
        :raises ValueError: If the amount is negative or exceeds the remaining tokens.
        """
        if amount < 0:
            raise ValueError("Claim amount must be a non-negative value.")
        if amount > self.remaining_tokens():
            raise ValueError("Insufficient tokens available for claim.")
        self.claimed_tokens += amount

    def remaining_tokens(self):
        """
        Calculate the remaining tokens available for claiming.

        :return: Number of remaining DUST tokens available for claiming.
        """
        return self.total_tokens - self.claimed_tokens


# Example Usage:
if __name__ == "__main__":
    try:
        # Initialize the pool with 1000 DUST tokens
        dust_pool = AirdropPool(total_tokens=1000)

        # Claim 300 tokens
        dust_pool.claim_tokens(amount=300)

        # Calculate remaining tokens
        remaining = dust_pool.remaining_tokens()
        print(f"Remaining DUST tokens available for claiming: {remaining}")

        # Attempting to claim more tokens than available
        dust_pool.claim_tokens(amount=800)  # This will raise a ValueError
    except ValueError as e:
        print(f"Error: {e}")
```
