"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornerstonetrading.biz
Prompt: Generate a code snippet for a financial platform that allows users to invest in government projects like IKN using a transparent system.
Generated: DETERMINISTIC_032e344205e8292c
Batch ID: 20250612_155859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InvestmentPlatform:
    def __init__(self):
        # Initialize an empty list to store investments
        self.investments: List[Dict[str, Any]] = []

    def add_investment(self, user_id: str, project_id: str, amount: float) -> None:
        """
        Adds an investment by a user in a specific government project.
        
        Args:
            user_id (str): The ID of the user making the investment.
            project_id (str): The ID of the government project.
            amount (float): The amount of money to invest.
        
        Raises:
            ValueError: If the investment amount is less than or equal to zero.
        """
        if amount <= 0:
            logging.error(f"Invalid investment amount: {amount}")
            raise ValueError("Investment amount must be greater than zero.")
        
        investment = {
            "user_id": user_id,
            "project_id": project_id,
            "amount": amount
        }

        self.investments.append(investment)
        logging.info(f"Investment added: {investment}")

    def get_investments(self, user_id: str) -> List[Dict[str, Any]]:
        """
        Retrieves all investments made by a specific user.
        
        Args:
            user_id (str): The ID of the user whose investments are to be retrieved.
        
        Returns:
            List[Dict[str, Any]]: A list of investments made by the user.
        """
        user_investments = [inv for inv in self.investments if inv['user_id'] == user_id]
        logging.info(f"Retrieved investments for user {user_id}: {user_investments}")
        return user_investments

    def export_investments(self, file_path: str) -> None:
        """
        Exports all investments to a JSON file for transparency.
        
        Args:
            file_path (str): The path to the file where investments will be saved.
        
        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.investments, json_file, indent=4)
            logging.info(f"Investments exported to {file_path}")
        except IOError as e:
            logging.error(f"Failed to write to file {file_path}: {e}")
            raise

# Example usage
if __name__ == "__main__":
    platform = InvestmentPlatform()
    try:
        platform.add_investment("user_123", "project_456", 1000.00)
        investments = platform.get_investments("user_123")
        platform.export_investments("investments.json")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
