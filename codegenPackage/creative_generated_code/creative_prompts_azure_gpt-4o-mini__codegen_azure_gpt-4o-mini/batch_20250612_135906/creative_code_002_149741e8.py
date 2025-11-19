"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bearsontheblock.com
Prompt: Can you provide code examples for tracking earnings on the rewards dashboard in Nifty Island as described on Bears On The Block?
Generated: DETERMINISTIC_149741e800f38a0f
Batch ID: 20250612_135906
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
from typing import List, Dict, Any

# Set up logging for tracking earnings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RewardTracker:
    def __init__(self):
        """
        Initializes the RewardTracker with an empty list of earnings.
        """
        self.earnings: List[Dict[str, Any]] = []

    def add_earning(self, amount: float, description: str) -> None:
        """
        Adds an earning entry to the earnings list.

        Parameters:
        amount (float): The amount earned.
        description (str): A description of the earning.
        """
        if amount <= 0:
            logging.error("Attempted to add a non-positive earning amount: %s", amount)
            raise ValueError("Earning amount must be greater than zero.")
        
        earning_entry = {
            "amount": amount,
            "description": description,
            "timestamp": datetime.now()
        }
        self.earnings.append(earning_entry)
        logging.info("Added earning: %s", earning_entry)

    def get_total_earnings(self) -> float:
        """
        Computes the total earnings.

        Returns:
        float: The total earnings accumulated.
        """
        total = sum(entry['amount'] for entry in self.earnings)
        logging.info("Total earnings computed: %s", total)
        return total

    def list_earnings(self) -> List[Dict[str, Any]]:
        """
        Returns a list of all earnings.

        Returns:
        List[Dict[str, Any]]: A list of dictionaries containing earnings details.
        """
        logging.info("Listing all earnings.")
        return self.earnings

# Example usage:
if __name__ == "__main__":
    tracker = RewardTracker()
    
    try:
        tracker.add_earning(100.00, "Referral bonus")
        tracker.add_earning(50.00, "Staking reward")
        
        total = tracker.get_total_earnings()
        print(f"Total Earnings: ${total:.2f}")
        
        all_earnings = tracker.list_earnings()
        for earning in all_earnings:
            print(earning)
    
    except ValueError as e:
        logging.error("An error occurred: %s", e)
```
