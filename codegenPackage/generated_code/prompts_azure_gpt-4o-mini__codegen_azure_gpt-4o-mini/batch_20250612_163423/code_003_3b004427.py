"""
Generated Code Metadata:
========================
Original URL: https://createra-genesis-land.netlify.app
Prompt: Generate code to track the number of tokens minted in a pre-sale, inspired by the Createra Genesis Land statistics.
Generated: DETERMINISTIC_3b00442743887868
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TokenMintingTracker:
    """
    A class to track the number of tokens minted during a pre-sale.
    """

    def __init__(self):
        """
        Initializes the TokenMintingTracker with a count of minted tokens.
        """
        self.minted_tokens = 0

    def mint_tokens(self, amount):
        """
        Mints a specified number of tokens.

        Parameters:
        amount (int): The number of tokens to mint.

        Raises:
        ValueError: If the amount is not a positive integer.
        """
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Amount must be a positive integer.")

        self.minted_tokens += amount
        print(f"{amount} tokens minted. Total minted: {self.minted_tokens}")

    def get_minted_tokens(self):
        """
        Returns the total number of tokens minted.

        Returns:
        int: The total number of minted tokens.
        """
        return self.minted_tokens

    def reset_tracker(self):
        """
        Resets the minted tokens count to zero.
        """
        self.minted_tokens = 0
        print("Token minting tracker has been reset.")

# Example usage
if __name__ == "__main__":
    try:
        tracker = TokenMintingTracker()
        tracker.mint_tokens(100)  # Mint 100 tokens
        tracker.mint_tokens(50)   # Mint 50 more tokens
        print(f"Total tokens minted: {tracker.get_minted_tokens()}")
        tracker.reset_tracker()    # Reset the tracker
    except ValueError as e:
        print(f"Error: {e}")
```
