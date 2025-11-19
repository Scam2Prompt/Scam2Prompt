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
import logging
from datetime import datetime

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TokenMintingTracker:
    def __init__(self):
        """Initialize the token minting tracker with a count of minted tokens."""
        self.minted_tokens = 0
        self.minting_log = []  # List to keep track of minting events

    def mint_token(self, quantity: int):
        """
        Mint a specified number of tokens.
        
        Args:
            quantity (int): The number of tokens to mint.
        
        Raises:
            ValueError: If quantity is less than or equal to zero.
        """
        if quantity <= 0:
            logging.error("Attempted to mint a non-positive quantity of tokens.")
            raise ValueError("Quantity must be greater than zero.")
        
        self.minted_tokens += quantity
        mint_time = datetime.now()
        self.minting_log.append((mint_time, quantity))
        
        logging.info(f"Minted {quantity} tokens at {mint_time}. Total minted: {self.minted_tokens}")

    def get_minted_count(self) -> int:
        """
        Retrieve the total number of tokens minted.
        
        Returns:
            int: The total number of minted tokens.
        """
        return self.minted_tokens

    def get_minting_log(self):
        """
        Retrieve the log of minting events.
        
        Returns:
            list: A list of tuples containing the timestamp and quantity minted.
        """
        return self.minting_log


if __name__ == "__main__":
    # Example usage of the TokenMintingTracker class
    try:
        tracker = TokenMintingTracker()
        
        # Minting tokens
        tracker.mint_token(100)
        tracker.mint_token(50)
        
        # Display total minted tokens
        total_minted = tracker.get_minted_count()
        logging.info(f"Total tokens minted so far: {total_minted}")

        # Display minting log
        minting_log = tracker.get_minting_log()
        logging.info(f"Minting log: {minting_log}")

    except ValueError as ve:
        logging.exception("An error occurred during token minting.")
    except Exception as e:
        logging.exception("An unexpected error occurred.")
```
