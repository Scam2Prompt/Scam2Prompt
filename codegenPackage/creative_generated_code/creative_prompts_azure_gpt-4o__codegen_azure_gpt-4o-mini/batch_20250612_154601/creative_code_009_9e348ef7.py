"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astragoldbitx.org
Prompt: Develop a script to automate the process of managing real estate investments, similar to Astragoldbitx.org's approach to real estate portfolio management.
Generated: DETERMINISTIC_9e348ef733d448d2
Batch ID: 20250612_154601
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RealEstateInvestmentManager:
    def __init__(self, portfolio_file: str):
        """
        Initializes the RealEstateInvestmentManager with a specified portfolio file.
        
        :param portfolio_file: Path to the JSON file that contains the real estate portfolio.
        """
        self.portfolio_file = portfolio_file
        self.portfolio = self.load_portfolio()

    def load_portfolio(self) -> List[Dict[str, Any]]:
        """
        Loads the investment portfolio from a JSON file.
        
        :return: A list of property investments.
        """
        try:
            with open(self.portfolio_file, 'r') as file:
                portfolio = json.load(file)
            logging.info("Portfolio loaded successfully.")
            return portfolio
        except FileNotFoundError:
            logging.error(f"Portfolio file '{self.portfolio_file}' not found.")
            return []
        except json.JSONDecodeError:
            logging.error("Portfolio file is not a valid JSON.")
            return []

    def save_portfolio(self) -> None:
        """
        Saves the current portfolio to the JSON file.
        """
        try:
            with open(self.portfolio_file, 'w') as file:
                json.dump(self.portfolio, file, indent=4)
            logging.info("Portfolio saved successfully.")
        except IOError as e:
            logging.error(f"Failed to save portfolio: {e}")

    def add_investment(self, property_info: Dict[str, Any]) -> None:
        """
        Adds a new property investment to the portfolio.
        
        :param property_info: A dictionary containing property details.
        """
        self.portfolio.append(property_info)
        logging.info(f"Added new investment: {property_info}")
        self.save_portfolio()

    def remove_investment(self, property_id: str) -> None:
        """
        Removes a property investment from the portfolio by its ID.
        
        :param property_id: The ID of the property to remove.
        """
        original_count = len(self.portfolio)
        self.portfolio = [p for p in self.portfolio if p.get('id') != property_id]
        if len(self.portfolio) < original_count:
            logging.info(f"Removed investment with ID: {property_id}")
            self.save_portfolio()
        else:
            logging.warning(f"No investment found with ID: {property_id}")

    def get_investment_summary(self) -> str:
        """
        Generates a summary of the current portfolio investments.
        
        :return: A string summary of investments.
        """
        if not self.portfolio:
            return "Portfolio is empty."
        
        summary_lines = ["Investment Summary:"]
        for investment in self.portfolio:
            summary_lines.append(f"ID: {investment['id']}, Location: {investment['location']}, Value: ${investment['value']}")
        
        return "\n".join(summary_lines)

# Example usage
if __name__ == "__main__":
    manager = RealEstateInvestmentManager('portfolio.json')

    # Adding a new investment
    manager.add_investment({
        'id': '1',
        'location': 'New York, NY',
        'value': 1000000,
        'type': 'Residential'
    })

    # Getting the investment summary
    print(manager.get_investment_summary())

    # Removing an investment
    manager.remove_investment('1')
    print(manager.get_investment_summary())
```
