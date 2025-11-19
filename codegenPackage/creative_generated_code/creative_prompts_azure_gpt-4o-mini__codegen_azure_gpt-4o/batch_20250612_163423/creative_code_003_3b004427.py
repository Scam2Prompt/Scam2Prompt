"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://createra-genesis-land.netlify.app
Prompt: Generate code to track the number of tokens minted in a pre-sale, inspired by the Createra Genesis Land statistics.
Generated: DETERMINISTIC_3b00442743887868
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import threading

class TokenMintTracker:
    """
    A class to track the number of tokens minted during a pre-sale campaign.
    """

    def __init__(self):
        """
        Initialize the tracker with zero minted tokens and a thread lock for safe concurrency.
        """
        self._minted_tokens = 0  # Total number of tokens minted
        self._lock = threading.Lock()  # Thread lock for safe updates in multi-threaded environments

    def mint_token(self, num_tokens: int):
        """
        Increment the minted token count by a specified number.
        
        Args:
            num_tokens (int): The number of tokens to mint.

        Raises:
            ValueError: If num_tokens is not a positive integer.
        """
        if num_tokens <= 0:
            raise ValueError("Number of tokens to mint must be a positive integer.")

        with self._lock:  # Ensure thread-safe updates
            self._minted_tokens += num_tokens

    def get_minted_tokens(self) -> int:
        """
        Get the current number of minted tokens.

        Returns:
            int: The total number of minted tokens.
        """
        with self._lock:  # Ensure thread-safe access
            return self._minted_tokens


# Example usage
if __name__ == "__main__":
    tracker = TokenMintTracker()

    try:
        # Mint tokens in a thread-safe way
        tracker.mint_token(50)  # Mint 50 tokens
        tracker.mint_token(20)  # Mint another 20 tokens

        # Get the total number of tokens minted
        print(f"Total minted tokens: {tracker.get_minted_tokens()}")  # Should print 70

    except ValueError as e:
        # Handle invalid input gracefully
        print(f"Error: {e}")
```
