"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redstone.cx
Prompt: Generate a code snippet to track the progress of the Initia token pre-sale and airdrop.
Generated: DETERMINISTIC_18ce4eb17b519dc9
Batch ID: 20250612_161125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import time

class TokenSaleTracker:
    """
    Class to track the progress of the Initia token pre-sale and airdrop.
    """

    def __init__(self, total_tokens_for_sale, total_airdrop_tokens):
        """
        Initialize the tracker with token sale and airdrop details.
        
        :param total_tokens_for_sale: Total number of tokens available for pre-sale.
        :param total_airdrop_tokens: Total number of tokens allocated for airdrop.
        """
        self.total_tokens_for_sale = total_tokens_for_sale
        self.tokens_sold = 0
        self.total_airdrop_tokens = total_airdrop_tokens
        self.airdrop_claimed = 0
        self.start_time = time.time()

    def sell_tokens(self, amount):
        """
        Record the sale of tokens.
        
        :param amount: Number of tokens sold.
        :raises ValueError: If the sale exceeds the available tokens for pre-sale.
        """
        if self.tokens_sold + amount > self.total_tokens_for_sale:
            raise ValueError("Insufficient tokens available for sale.")
        self.tokens_sold += amount

    def claim_airdrop(self, amount):
        """
        Record the claiming of airdrop tokens.
        
        :param amount: Number of tokens claimed via airdrop.
        :raises ValueError: If the claim exceeds the allocated airdrop tokens.
        """
        if self.airdrop_claimed + amount > self.total_airdrop_tokens:
            raise ValueError("Insufficient airdrop tokens available.")
        self.airdrop_claimed += amount

    def get_progress(self):
        """
        Get the current progress of the token pre-sale and airdrop.
        
        :return: Dictionary containing the progress details.
        """
        return {
            "tokens_sold": self.tokens_sold,
            "tokens_remaining_for_sale": self.total_tokens_for_sale - self.tokens_sold,
            "airdrop_claimed": self.airdrop_claimed,
            "airdrop_remaining": self.total_airdrop_tokens - self.airdrop_claimed,
            "elapsed_time_in_seconds": time.time() - self.start_time
        }

    def to_json(self):
        """
        Serialize the progress data to JSON format.
        
        :return: JSON string containing the progress details.
        """
        progress = self.get_progress()
        return json.dumps(progress, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize tracker with 100,000 tokens for sale and 10,000 tokens for airdrop
        tracker = TokenSaleTracker(total_tokens_for_sale=100000, total_airdrop_tokens=10000)

        # Record token sales
        tracker.sell_tokens(25000)  # Sell 25,000 tokens
        tracker.sell_tokens(5000)   # Sell another 5,000 tokens

        # Record airdrop claims
        tracker.claim_airdrop(1000)  # Claim 1,000 tokens via airdrop

        # Print progress in JSON format
        print("Current Progress:")
        print(tracker.to_json())

    except ValueError as e:
        # Handle errors appropriately
        print(f"Error: {e}")
```
