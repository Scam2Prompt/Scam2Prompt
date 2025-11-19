"""
Generated Code Metadata:
========================
Original URL: https://sheesh.vc
Prompt: What are some best practices for venture capital firms like Sheesh Venture Club in managing their investment portfolios?
Generated: DETERMINISTIC_e47d1394f45f59b6
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Portfolio Management System for Venture Capital Firms

This script provides a basic implementation of best practices for managing investment portfolios.
It includes functionality for tracking investments, calculating portfolio performance, and generating reports.

Language: Python
"""

import datetime
import logging

# Configure logging for error handling and debugging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("portfolio_management.log"), logging.StreamHandler()],
)

class Investment:
    """
    Represents an individual investment in the portfolio.
    Attributes:
        company_name (str): Name of the company invested in.
        amount_invested (float): Amount of money invested.
        date_of_investment (datetime.date): Date of the investment.
        equity_percentage (float): Percentage of equity acquired in the company.
    """
    def __init__(self, company_name, amount_invested, date_of_investment, equity_percentage):
        self.company_name = company_name
        self.amount_invested = amount_invested
        self.date_of_investment = date_of_investment
        self.equity_percentage = equity_percentage

    def __str__(self):
        return f"{self.company_name}: ${self.amount_invested} invested on {self.date_of_investment}, {self.equity_percentage}% equity."


class Portfolio:
    """
    Represents the investment portfolio of a venture capital firm.
    Attributes:
        investments (list): List of Investment objects.
    """
    def __init__(self):
        self.investments = []

    def add_investment(self, investment):
        """
        Adds a new investment to the portfolio.
        Args:
            investment (Investment): The investment to add.
        """
        if not isinstance(investment, Investment):
            logging.error("Invalid investment object.")
            raise ValueError("investment must be an instance of Investment class.")
        self.investments.append(investment)
        logging.info(f"Added investment: {investment}")

    def calculate_total_invested(self):
        """
        Calculates the total amount of money invested in the portfolio.
        Returns:
            float: Total amount invested.
        """
        return sum(investment.amount_invested for investment in self.investments)

    def generate_report(self):
        """
        Generates a report of all investments in the portfolio.
        Returns:
            str: Formatted report of investments.
        """
        report = "Portfolio Report\n"
        report += "=" * 20 + "\n"
        for investment in self.investments:
            report += str(investment) + "\n"
        report += "=" * 20 + "\n"
        report += f"Total Invested: ${self.calculate_total_invested():,.2f}\n"
        return report


# Example usage
if __name__ == "__main__":
    try:
        # Create a portfolio
        portfolio = Portfolio()

        # Add investments
        portfolio.add_investment(Investment("TechCorp", 500000, datetime.date(2022, 5, 1), 10))
        portfolio.add_investment(Investment("HealthInc", 300000, datetime.date(2023, 1, 15), 15))
        portfolio.add_investment(Investment("EduStart", 200000, datetime.date(2023, 3, 10), 20))

        # Generate and print portfolio report
        print(portfolio.generate_report())

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
