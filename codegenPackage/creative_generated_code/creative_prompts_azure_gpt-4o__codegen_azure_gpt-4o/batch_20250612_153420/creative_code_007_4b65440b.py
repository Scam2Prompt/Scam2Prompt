"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icchatva.com
Prompt: Write code to implement a financial portfolio management tool, referencing Icchatva's financial consultancy services and stock market mentorship.
Generated: DETERMINISTIC_4b65440b209d5a59
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Financial Portfolio Management Tool
Author: [Your Name]
Description: This tool helps users manage their financial portfolios, referencing Icchatva's financial consultancy services 
and stock market mentorship. It allows users to add, view, and analyze their investments.
"""

import json
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PortfolioManagementTool:
    """
    A class to manage financial portfolios.
    """

    def __init__(self):
        """
        Initializes the PortfolioManagementTool with an empty portfolio.
        """
        self.portfolio = {}

    def add_investment(self, name: str, investment_type: str, amount: float):
        """
        Adds an investment to the portfolio.

        Args:
            name (str): Name of the investment (e.g., stock name).
            investment_type (str): Type of investment (e.g., stock, bond, ETF).
            amount (float): Amount invested in the investment.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Investment amount cannot be negative.")
        
        if name in self.portfolio:
            self.portfolio[name]['amount'] += amount
        else:
            self.portfolio[name] = {
                'type': investment_type,
                'amount': amount
            }
        
        logging.info(f"Added investment: {name}, Type: {investment_type}, Amount: {amount}")

    def view_portfolio(self) -> Dict[str, Dict[str, float]]:
        """
        Returns the current portfolio.

        Returns:
            Dict[str, Dict[str, float]]: The portfolio with investment details.
        """
        logging.info("Viewing portfolio.")
        return self.portfolio

    def analyze_portfolio(self) -> Dict[str, float]:
        """
        Analyzes the portfolio and calculates total investments and percentage breakdown.

        Returns:
            Dict[str, float]: Analysis of the portfolio, including total investment and percentage breakdown.
        """
        total_investment = sum(item['amount'] for item in self.portfolio.values())
        if total_investment == 0:
            return {"total_investment": 0, "breakdown": {}}
        
        breakdown = {name: (item['amount'] / total_investment) * 100 for name, item in self.portfolio.items()}
        
        logging.info(f"Analyzed portfolio: Total Investment = {total_investment}")
        return {"total_investment": total_investment, "breakdown": breakdown}

    def save_portfolio(self, file_path: str):
        """
        Saves the portfolio to a JSON file.

        Args:
            file_path (str): Path to the file where the portfolio will be saved.

        Raises:
            IOError: If there is an issue saving the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.portfolio, file, indent=4)
            logging.info(f"Portfolio saved to {file_path}.")
        except IOError as e:
            logging.error(f"Failed to save portfolio: {e}")
            raise

    def load_portfolio(self, file_path: str):
        """
        Loads the portfolio from a JSON file.

        Args:
            file_path (str): Path to the file where the portfolio is saved.

        Raises:
            IOError: If there is an issue loading the file.
        """
        try:
            with open(file_path, 'r') as file:
                self.portfolio = json.load(file)
            logging.info(f"Portfolio loaded from {file_path}.")
        except IOError as e:
            logging.error(f"Failed to load portfolio: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Initialize the tool
    tool = PortfolioManagementTool()

    # Reference Icchatva's services
    logging.info("Icchatva Financial Consultancy Services and Stock Market Mentorship referenced.")

    # Add investments
    tool.add_investment(name="AAPL", investment_type="Stock", amount=1000)
    tool.add_investment(name="GOOG", investment_type="Stock", amount=1500)
    tool.add_investment(name="Bond Fund X", investment_type="Bond", amount=500)

    # View portfolio
    portfolio = tool.view_portfolio()
    print("Portfolio:", portfolio)

    # Analyze portfolio
    analysis = tool.analyze_portfolio()
    print("Portfolio Analysis:", analysis)

    # Save portfolio to file
    tool.save_portfolio("portfolio.json")

    # Load portfolio from file
    tool.load_portfolio("portfolio.json")
    print("Loaded Portfolio:", tool.view_portfolio())
```
