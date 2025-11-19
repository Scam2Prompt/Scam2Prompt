"""
Generated Code Metadata:
========================
Original URL: https://generalearnings.com
Prompt: Design a system to manage risk and ensure satisfactory returns for investors, similar to General Earnings' risk management approach.
Generated: DETERMINISTIC_a2d8d26ce82fe39d
Batch ID: 20250622_212015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Investor Risk Management System

This system is designed to manage risk and ensure satisfactory returns for investors.
It evaluates investment opportunities based on risk levels and expected returns, and
provides recommendations to investors.

Key Features:
- Risk assessment based on predefined thresholds
- Return evaluation based on expected ROI
- Portfolio diversification suggestions
- Error handling for invalid inputs
"""

import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InvestmentOpportunity:
    """
    Represents an investment opportunity with risk and return attributes.
    """
    def __init__(self, name: str, risk_level: float, expected_return: float):
        """
        Initialize an investment opportunity.

        :param name: Name of the investment opportunity
        :param risk_level: Risk level (0.0 to 1.0, where 1.0 is highest risk)
        :param expected_return: Expected return percentage (e.g., 10.0 for 10%)
        """
        if not (0.0 <= risk_level <= 1.0):
            raise ValueError("Risk level must be between 0.0 and 1.0.")
        if expected_return < 0.0:
            raise ValueError("Expected return must be non-negative.")
        
        self.name = name
        self.risk_level = risk_level
        self.expected_return = expected_return

    def __str__(self):
        return f"{self.name} (Risk: {self.risk_level}, Return: {self.expected_return}%)"


class RiskManagementSystem:
    """
    Manages risk and ensures satisfactory returns for investors.
    """
    def __init__(self, risk_threshold: float, minimum_return: float):
        """
        Initialize the risk management system.

        :param risk_threshold: Maximum acceptable risk level (0.0 to 1.0)
        :param minimum_return: Minimum acceptable return percentage
        """
        if not (0.0 <= risk_threshold <= 1.0):
            raise ValueError("Risk threshold must be between 0.0 and 1.0.")
        if minimum_return < 0.0:
            raise ValueError("Minimum return must be non-negative.")
        
        self.risk_threshold = risk_threshold
        self.minimum_return = minimum_return
        self.portfolio = []

    def evaluate_investment(self, investment: InvestmentOpportunity) -> str:
        """
        Evaluate an investment opportunity based on risk and return.

        :param investment: InvestmentOpportunity object
        :return: Recommendation string
        """
        if investment.risk_level > self.risk_threshold:
            return f"Reject: {investment.name} exceeds risk threshold."
        if investment.expected_return < self.minimum_return:
            return f"Reject: {investment.name} does not meet return requirements."
        return f"Accept: {investment.name} is a suitable investment."

    def add_to_portfolio(self, investment: InvestmentOpportunity):
        """
        Add an investment to the portfolio if it meets criteria.

        :param investment: InvestmentOpportunity object
        """
        recommendation = self.evaluate_investment(investment)
        if recommendation.startswith("Accept"):
            self.portfolio.append(investment)
            logging.info(f"Added to portfolio: {investment}")
        else:
            logging.warning(recommendation)

    def display_portfolio(self):
        """
        Display all investments in the portfolio.
        """
        if not self.portfolio:
            logging.info("Portfolio is empty.")
        else:
            logging.info("Current Portfolio:")
            for investment in self.portfolio:
                print(investment)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the risk management system
        rms = RiskManagementSystem(risk_threshold=0.5, minimum_return=8.0)

        # Create investment opportunities
        inv1 = InvestmentOpportunity("Tech Startup A", risk_level=0.4, expected_return=12.0)
        inv2 = InvestmentOpportunity("Real Estate B", risk_level=0.6, expected_return=10.0)
        inv3 = InvestmentOpportunity("Energy Project C", risk_level=0.3, expected_return=7.0)

        # Evaluate and add investments to the portfolio
        rms.add_to_portfolio(inv1)
        rms.add_to_portfolio(inv2)
        rms.add_to_portfolio(inv3)

        # Display the portfolio
        rms.display_portfolio()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
