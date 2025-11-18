"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jesse-9y3.pages.dev
Prompt: Create a function to track the remaining JESSE tokens available for purchase during the presale, based on the total supply and transactions processed.
Generated: DETERMINISTIC_e8c0b9706b10ceca
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: token_presale_tracker.py

class JesseTokenPresaleTracker:
    """
    A class to track the remaining JESSE tokens available for purchase during the presale.
    """

    def __init__(self, total_supply):
        """
        Initializes the tracker with the total supply.

        :param total_supply: The total supply of JESSE tokens available for presale.
        """
        if total_supply < 0:
            raise ValueError("Total supply must be greater than or equal to 0.")
        
        self.total_supply = total_supply  # Total tokens available at the start
        self.tokens_sold = 0             # Counter for tokens sold

    def process_transaction(self, tokens_purchased):
        """
        Processes a transaction and updates the number of tokens sold.

        :param tokens_purchased: The number of tokens being purchased in the transaction.
                                  Must be a non-negative integer.
        :raises ValueError: If tokens_purchased is negative or exceeds available supply.
        """
        if tokens_purchased < 0:
            raise ValueError("Tokens purchased must be a non-negative value.")
        
        if tokens_purchased > self.get_remaining_tokens():
            raise ValueError("Insufficient tokens available for this transaction.")
        
        self.tokens_sold += tokens_purchased

    def get_remaining_tokens(self):
        """
        Calculates and returns the number of remaining tokens available for purchase.

        :return: Integer representing the remaining tokens.
        """
        return self.total_supply - self.tokens_sold

    def __str__(self):
        """
        Returns a string representation of the current presale status.

        :return: A string with the total supply, tokens sold, and remaining tokens.
        """
        return (f"Total Supply: {self.total_supply}, "
                f"Tokens Sold: {self.tokens_sold}, "
                f"Remaining Tokens: {self.get_remaining_tokens()}")

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the tracker with a total supply of tokens
        tracker = JesseTokenPresaleTracker(total_supply=1000)

        # Process some transactions
        tracker.process_transaction(tokens_purchased=100)
        tracker.process_transaction(tokens_purchased=200)

        # Print the current status
        print(tracker)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
