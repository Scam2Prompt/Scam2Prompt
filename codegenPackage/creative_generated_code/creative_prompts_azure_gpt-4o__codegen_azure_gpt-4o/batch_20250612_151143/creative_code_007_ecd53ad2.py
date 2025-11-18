"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solnarize-in.pages.dev
Prompt: Create a function to display the total $SRIZE tokens raised during the pre-sale, updating dynamically as new contributions are made.
Generated: DETERMINISTIC_ecd53ad2d2fc0d0d
Batch ID: 20250612_151143
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import threading

class TokenPresale:
    """
    Class to manage and display $SRIZE tokens raised during the presale.
    """
    def __init__(self):
        # Initialize the total tokens raised to zero
        self.total_tokens_raised = 0
        
        # Lock to ensure thread-safe updates to the token count
        self.lock = threading.Lock()

    def add_contribution(self, tokens):
        """
        Adds new contributions to the total tokens raised.

        Args:
            tokens (int): Number of $SRIZE tokens contributed in this transaction.
        """
        if tokens < 0:
            raise ValueError("Contribution amount cannot be negative.")

        with self.lock:
            # Safely update the total tokens raised
            self.total_tokens_raised += tokens

    def get_total_tokens_raised(self):
        """
        Returns the current total of $SRIZE tokens raised.

        Returns:
            int: Total tokens raised during the presale.
        """
        with self.lock:
            return self.total_tokens_raised

    def display_total_tokens_raised(self):
        """
        Displays the current total of $SRIZE tokens raised in a user-friendly format.
        """
        with self.lock:
            print(f"Total $SRIZE tokens raised: {self.total_tokens_raised:,}")

# Example usage
if __name__ == "__main__":
    # Instantiate the TokenPresale class
    presale = TokenPresale()

    try:
        # Simulate contributions
        presale.add_contribution(500)
        presale.add_contribution(1500)
        
        # Display the current total tokens raised
        presale.display_total_tokens_raised()
        
    except ValueError as e:
        print(f"Error: {e}")
```
