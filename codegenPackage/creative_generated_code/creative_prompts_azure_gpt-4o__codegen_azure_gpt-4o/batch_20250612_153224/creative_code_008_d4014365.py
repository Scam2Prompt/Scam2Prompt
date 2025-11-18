"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laotaigroup.com
Prompt: Write code to simulate a trading and investment planning system for Lao Tai Trading - Investment Group, incorporating financial metrics and risk analysis.
Generated: DETERMINISTIC_d40143654fb21078
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TradingInvestmentSystem:
    """
    A trading and investment planning system for Lao Tai Trading - Investment Group.
    Includes financial metrics and risk analysis.
    """

    def __init__(self):
        """
        Initializes the system with an empty portfolio and default risk tolerance.
        """
        self.portfolio = {}  # Stores investments as {asset_name: amount invested}
        self.risk_tolerance = 0.5  # Default risk tolerance (0 to 1, where 1 is high risk)
        logging.info("Trading Investment System initialized.")

    def add_investment(self, asset_name, amount):
        """
        Adds an investment to the portfolio.

        Args:
            asset_name (str): Name of the asset.
            amount (float): Amount to invest.

        Raises:
            ValueError: If amount is less than or equal to 0.
        """
        if amount <= 0:
            raise ValueError("Investment amount must be greater than 0.")
        
        self.portfolio[asset_name] = self.portfolio.get(asset_name, 0) + amount
        logging.info(f"Added investment: {asset_name} - ${amount}")

    def remove_investment(self, asset_name, amount):
        """
        Removes an investment from the portfolio.

        Args:
            asset_name (str): Name of the asset.
            amount (float): Amount to remove.

        Raises:
            ValueError: If asset is not in portfolio or amount exceeds current investment.
        """
        if asset_name not in self.portfolio:
            raise ValueError(f"Asset '{asset_name}' not found in portfolio.")
        if amount > self.portfolio[asset_name]:
            raise ValueError(f"Cannot remove ${amount}; only ${self.portfolio[asset_name]} invested.")
        
        self.portfolio[asset_name] -= amount
        logging.info(f"Removed investment: {asset_name} - ${amount}")
        
        # Remove asset if investment drops to 0
        if self.portfolio[asset_name] == 0:
            del self.portfolio[asset_name]

    def calculate_risk(self):
        """
        Simulates a risk analysis based on portfolio assets.

        Returns:
            float: Risk score (0 to 1, where 1 is high risk).
        """
        risk = random.uniform(0, 1)  # Simulated risk based on external metrics
        logging.info(f"Calculated portfolio risk: {risk:.2f}")
        return risk

    def generate_financial_metrics(self):
        """
        Generates financial metrics based on the portfolio.

        Returns:
            dict: Metrics including total investment and asset breakdown.
        """
        total_investment = sum(self.portfolio.values())
        asset_breakdown = {asset: (amount / total_investment) * 100 for asset, amount in self.portfolio.items()}
        
        metrics = {
            "total_investment": total_investment,
            "asset_breakdown": asset_breakdown
        }
        logging.info("Generated financial metrics.")
        return metrics

    def assess_strategy(self):
        """
        Assesses the current investment strategy based on risk tolerance.

        Returns:
            str: Strategy recommendation.
        """
        current_risk = self.calculate_risk()
        if current_risk > self.risk_tolerance:
            recommendation = "Reduce high-risk investments."
        else:
            recommendation = "Strategy is within acceptable risk levels."
        
        logging.info(f"Strategy recommendation: {recommendation}")
        return recommendation


# Example usage
if __name__ == "__main__":
    # Instantiate the system
    system = TradingInvestmentSystem()

    try:
        # Add some investments
        system.add_investment("Stock-A", 5000)
        system.add_investment("Bond-B", 3000)
        system.add_investment("Crypto-C", 2000)

        # Generate metrics
        metrics = system.generate_financial_metrics()
        print("Financial Metrics:", metrics)

        # Assess strategy
        recommendation = system.assess_strategy()
        print("Strategy Recommendation:", recommendation)

        # Remove investments
        system.remove_investment("Crypto-C", 1000)
        print("Updated Portfolio:", system.portfolio)

    except ValueError as e:
        logging.error(e)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
