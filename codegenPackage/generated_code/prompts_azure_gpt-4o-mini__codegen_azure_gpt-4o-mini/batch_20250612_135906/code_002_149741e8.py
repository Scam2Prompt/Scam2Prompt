"""
Generated Code Metadata:
========================
Original URL: https://bearsontheblock.com
Prompt: Can you provide code examples for tracking earnings on the rewards dashboard in Nifty Island as described on Bears On The Block?
Generated: DETERMINISTIC_149741e800f38a0f
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from datetime import datetime
from typing import List, Dict, Any

# Configure logging for tracking errors and information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EarningsTracker:
    def __init__(self):
        """Initialize the EarningsTracker with an empty earnings list."""
        self.earnings: List[Dict[str, Any]] = []

    def add_earning(self, amount: float, source: str, date: str) -> None:
        """
        Add a new earning entry to the tracker.

        :param amount: The amount earned.
        :param source: The source of the earning.
        :param date: The date of the earning in 'YYYY-MM-DD' format.
        :raises ValueError: If the amount is negative or date format is incorrect.
        """
        if amount < 0:
            logging.error("Attempted to add a negative earning amount.")
            raise ValueError("Earning amount cannot be negative.")
        
        # Validate date format
        try:
            earning_date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            logging.error("Date format is incorrect. Expected 'YYYY-MM-DD'.")
            raise ValueError("Date format must be 'YYYY-MM-DD'.")

        earning_entry = {
            'amount': amount,
            'source': source,
            'date': earning_date.strftime('%Y-%m-%d')
        }
        self.earnings.append(earning_entry)
        logging.info(f"Earning added: {earning_entry}")

    def get_total_earnings(self) -> float:
        """Calculate the total earnings from the tracked entries."""
        total = sum(entry['amount'] for entry in self.earnings)
        logging.info(f"Total earnings calculated: {total}")
        return total

    def get_earnings_summary(self) -> List[Dict[str, Any]]:
        """
        Get a summary of all earnings.

        :return: A list of earnings entries.
        """
        logging.info("Retrieving earnings summary.")
        return self.earnings

    def save_to_file(self, filename: str) -> None:
        """
        Save the earnings data to a JSON file.

        :param filename: The name of the file to save the earnings data.
        :raises IOError: If there is an error writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.earnings, file, indent=4)
            logging.info(f"Earnings data saved to {filename}.")
        except IOError as e:
            logging.error(f"Failed to write to file {filename}: {e}")
            raise IOError(f"Could not write to file {filename}.")

# Example usage
if __name__ == "__main__":
    tracker = EarningsTracker()
    try:
        tracker.add_earning(100.0, "Referral Bonus", "2023-10-01")
        tracker.add_earning(50.0, "Daily Reward", "2023-10-02")
        print(f"Total Earnings: {tracker.get_total_earnings()}")
        print("Earnings Summary:", tracker.get_earnings_summary())
        tracker.save_to_file("earnings.json")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
