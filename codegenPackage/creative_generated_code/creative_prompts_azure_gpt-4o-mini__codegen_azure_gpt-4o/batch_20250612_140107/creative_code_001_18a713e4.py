"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3exodus.click
Prompt: Write a Python script that implements investment strategies discussed in a training on AI, NFTs, and Metaverses.
Generated: DETERMINISTIC_18a713e495ab1032
Batch ID: 20250612_140107
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

# Set up logging configuration
logging.basicConfig(
    filename='investment_strategy.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class InvestmentStrategy:
    """
    A class to represent investment strategies for AI, NFTs, and Metaverses.
    """

    def __init__(self, initial_balance):
        """
        Initialize the investment strategy with an initial balance.
        Args:
            initial_balance (float): Initial investment amount.
        """
        if initial_balance <= 0:
            raise ValueError("Initial balance must be greater than zero.")
        self.balance = initial_balance
        self.portfolio = {"AI": 0.0, "NFTs": 0.0, "Metaverses": 0.0}
        logging.info("Initialized investment strategy with balance: %.2f", initial_balance)

    def allocate_funds(self, ai_percentage, nfts_percentage, metaverses_percentage):
        """
        Allocate funds based on percentages for AI, NFTs, and Metaverses.

        Args:
            ai_percentage (float): Percentage allocated to AI (0-100).
            nfts_percentage (float): Percentage allocated to NFTs (0-100).
            metaverses_percentage (float): Percentage allocated to Metaverses (0-100).

        Raises:
            ValueError: If percentages do not sum to 100 or are invalid.
        """
        if ai_percentage < 0 or nfts_percentage < 0 or metaverses_percentage < 0:
            raise ValueError("Percentages must be non-negative.")
        if ai_percentage + nfts_percentage + metaverses_percentage != 100:
            raise ValueError("Percentages must sum to 100.")

        self.portfolio["AI"] = self.balance * (ai_percentage / 100)
        self.portfolio["NFTs"] = self.balance * (nfts_percentage / 100)
        self.portfolio["Metaverses"] = self.balance * (metaverses_percentage / 100)
        logging.info(
            "Funds allocated - AI: %.2f, NFTs: %.2f, Metaverses: %.2f",
            self.portfolio["AI"], self.portfolio["NFTs"], self.portfolio["Metaverses"]
        )

    def simulate_growth(self, ai_growth, nfts_growth, metaverses_growth):
        """
        Simulate growth in investment categories.

        Args:
            ai_growth (float): Growth rate for AI investments (e.g., 0.05 for 5%).
            nfts_growth (float): Growth rate for NFTs investments (e.g., 0.10 for 10%).
            metaverses_growth (float): Growth rate for Metaverses investments (e.g., 0.07 for 7%).

        Raises:
            ValueError: If growth rates are invalid (negative values).
        """
        if ai_growth < 0 or nfts_growth < 0 or metaverses_growth < 0:
            raise ValueError("Growth rates must be non-negative.")

        self.portfolio["AI"] *= (1 + ai_growth)
        self.portfolio["NFTs"] *= (1 + nfts_growth)
        self.portfolio["Metaverses"] *= (1 + metaverses_growth)
        logging.info(
            "Simulation of growth - AI: %.2f, NFTs: %.2f, Metaverses: %.2f",
            self.portfolio["AI"], self.portfolio["NFTs"], self.portfolio["Metaverses"]
        )

    def get_portfolio_status(self):
        """
        Get the current status of the portfolio.

        Returns:
            dict: Current allocation in AI, NFTs, and Metaverses.
        """
        total_value = sum(self.portfolio.values())
        logging.info("Portfolio status - Total Value: %.2f", total_value)
        return {
            "AI": round(self.portfolio["AI"], 2),
            "NFTs": round(self.portfolio["NFTs"], 2),
            "Metaverses": round(self.portfolio["Metaverses"], 2),
            "Total": round(total_value, 2),
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize investment strategy with a starting balance
        strategy = InvestmentStrategy(initial_balance=10000)

        # Allocate funds with percentages for AI, NFTs, and Metaverses
        strategy.allocate_funds(ai_percentage=40, nfts_percentage=30, metaverses_percentage=30)

        # Simulate growth rates
        strategy.simulate_growth(ai_growth=0.05, nfts_growth=0.10, metaverses_growth=0.07)

        # Print portfolio status
        portfolio_status = strategy.get_portfolio_status()
        print("Portfolio Status:", portfolio_status)

    except ValueError as e:
        logging.error("ValueError: %s", str(e))
        print(f"Error: {e}")

    except Exception as e:
        logging.error("Unexpected error: %s", str(e))
        print(f"Unexpected error: {e}")
```
