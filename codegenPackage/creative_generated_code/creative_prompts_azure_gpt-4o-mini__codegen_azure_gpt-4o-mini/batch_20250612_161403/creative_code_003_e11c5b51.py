"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://goodsdao.web.app
Prompt: Generate a script to track total deposits and borrows on Marginfi, focusing on the $451.10m deposits and $103.51m borrows.
Generated: DETERMINISTIC_e11c5b51492d2203
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MarginfiTracker:
    def __init__(self):
        """Initializes the MarginfiTracker with default values for deposits and borrows."""
        self.data = {
            "deposits": 451.10,  # Total deposits in million USD
            "borrows": 103.51     # Total borrows in million USD
        }

    def update_deposits(self, amount: float) -> None:
        """
        Update the total deposits.

        :param amount: The amount to add to total deposits (in million USD).
        :raises ValueError: If amount is negative.
        """
        if amount < 0:
            logging.error("Attempted to add a negative deposit amount.")
            raise ValueError("Deposit amount must be non-negative.")
        
        self.data["deposits"] += amount
        logging.info(f"Updated deposits: {self.data['deposits']} million USD")

    def update_borrows(self, amount: float) -> None:
        """
        Update the total borrows.

        :param amount: The amount to add to total borrows (in million USD).
        :raises ValueError: If amount is negative.
        """
        if amount < 0:
            logging.error("Attempted to add a negative borrow amount.")
            raise ValueError("Borrow amount must be non-negative.")
        
        self.data["borrows"] += amount
        logging.info(f"Updated borrows: {self.data['borrows']} million USD")

    def get_totals(self) -> Dict[str, Any]:
        """
        Retrieve the current totals for deposits and borrows.

        :return: A dictionary containing the totals for deposits and borrows.
        """
        logging.info("Retrieving totals for deposits and borrows.")
        return self.data

if __name__ == "__main__":
    try:
        # Initialize the Marginfi tracker
        tracker = MarginfiTracker()

        # Example of updating deposits and borrows
        tracker.update_deposits(5.0)  # Add 5 million to deposits
        tracker.update_borrows(2.0)    # Add 2 million to borrows

        # Fetch and display current totals
        totals = tracker.get_totals()
        logging.info(f"Current totals - Deposits: {totals['deposits']} million USD, Borrows: {totals['borrows']} million USD")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
