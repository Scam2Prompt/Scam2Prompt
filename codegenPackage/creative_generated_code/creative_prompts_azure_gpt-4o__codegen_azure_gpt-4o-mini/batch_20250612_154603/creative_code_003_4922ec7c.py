"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitalcurrencytradingoptions.com
Prompt: Provide code examples for setting up automated investment plans with insurance coverage for initial capital, inspired by the features of digitalcurrencytradingoptions.com.
Generated: DETERMINISTIC_4922ec7ce0a5dced
Batch ID: 20250612_154603
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
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InvestmentPlan:
    """Class to represent an automated investment plan with insurance coverage for initial capital."""
    
    def __init__(self, capital: float, insurance_percentage: float):
        """
        Initialize an investment plan.

        :param capital: Initial investment capital
        :param insurance_percentage: Percentage of capital covered by insurance
        """
        if capital <= 0:
            raise ValueError("Capital must be greater than zero.")
        if not (0 <= insurance_percentage <= 100):
            raise ValueError("Insurance percentage must be between 0 and 100.")

        self.capital = capital
        self.insurance_coverage = capital * (insurance_percentage / 100)
        self.investments = []
        logging.info("Investment plan created with capital: %s and insurance coverage: %s", capital, self.insurance_coverage)

    def add_investment(self, amount: float, asset: str):
        """
        Add an investment to the plan.

        :param amount: Amount to invest
        :param asset: The asset to invest in
        """
        if amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        if amount > self.capital:
            raise ValueError("Insufficient capital to make this investment.")
        
        self.capital -= amount
        self.investments.append({"asset": asset, "amount": amount})
        logging.info("Investment added: %s in %s", amount, asset)

    def get_investment_summary(self) -> Dict[str, float]:
        """
        Get a summary of the investments made.

        :return: Dictionary summarizing investments
        """
        return {
            "remaining_capital": self.capital,
            "total_invested": sum(invest['amount'] for invest in self.investments),
            "insurance_coverage": self.insurance_coverage,
            "investments": self.investments
        }

    def save_to_file(self, filename: str):
        """
        Save the investment plan to a JSON file.

        :param filename: Name of the file to save the data
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_investment_summary(), file, indent=4)
            logging.info("Investment plan saved to %s", filename)
        except Exception as e:
            logging.error("Failed to save investment plan: %s", e)

def main():
    """Main function to orchestrate the creation of an investment plan."""
    try:
        plan = InvestmentPlan(capital=10000, insurance_percentage=50)
        plan.add_investment(amount=2000, asset="Bitcoin")
        plan.add_investment(amount=1500, asset="Ethereum")
        
        summary = plan.get_investment_summary()
        logging.info("Investment Summary: %s", summary)

        # Save the investment plan to a file
        plan.save_to_file("investment_plan.json")

    except Exception as e:
        logging.error("An error occurred: %s", e)

if __name__ == "__main__":
    main()
```
