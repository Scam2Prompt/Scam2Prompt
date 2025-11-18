"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ayeaye-pro.pages.dev
Prompt: Generate Python code for tracking the first 50,000 investors in a cryptocurrency project, as described in the Aye Aye Coin presale phase.
Generated: DETERMINISTIC_f353397f33487a1d
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import json
import logging
from typing import List, Dict

# Configure logging for debugging and tracking errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Investor:
    """Class representing an investor in the cryptocurrency project."""
    
    def __init__(self, investor_id: int, wallet_address: str, investment_amount: float):
        self.investor_id = investor_id
        self.wallet_address = wallet_address
        self.investment_amount = investment_amount

    def to_dict(self) -> Dict[str, str]:
        """Convert the investor information to a dictionary format."""
        return {
            'investor_id': self.investor_id,
            'wallet_address': self.wallet_address,
            'investment_amount': self.investment_amount
        }

class InvestorTracker:
    """Class to track investors in the cryptocurrency project."""

    def __init__(self):
        self.investors: List[Investor] = []
        self.max_investors = 50000  # Maximum number of investors to track

    def add_investor(self, wallet_address: str, investment_amount: float):
        """Add a new investor if the limit has not been reached."""
        if len(self.investors) < self.max_investors:
            investor_id = len(self.investors) + 1
            new_investor = Investor(investor_id, wallet_address, investment_amount)
            self.investors.append(new_investor)
            logging.info(f'Added investor {new_investor.to_dict()}')
        else:
            logging.warning('Maximum investor limit reached. Cannot add more investors.')

    def save_to_csv(self, filename: str):
        """Save the list of investors to a CSV file."""
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['investor_id', 'wallet_address', 'investment_amount'])
                writer.writeheader()
                for investor in self.investors:
                    writer.writerow(investor.to_dict())
            logging.info(f'Successfully saved investors to {filename}')
        except Exception as e:
            logging.error(f'Failed to save investors to CSV: {e}')

    def save_to_json(self, filename: str):
        """Save the list of investors to a JSON file."""
        try:
            with open(filename, mode='w') as file:
                json_data = [investor.to_dict() for investor in self.investors]
                json.dump(json_data, file, indent=4)
            logging.info(f'Successfully saved investors to {filename}')
        except Exception as e:
            logging.error(f'Failed to save investors to JSON: {e}')

# Example usage
if __name__ == "__main__":
    tracker = InvestorTracker()

    # Simulate adding investors (In a real application, this data would come from a database or API)
    tracker.add_investor("0x1234567890abcdef1234567890abcdef12345678", 10.0)
    tracker.add_investor("0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef", 25.0)

    # Save the investors to CSV and JSON files
    tracker.save_to_csv("investors.csv")
    tracker.save_to_json("investors.json")
```
