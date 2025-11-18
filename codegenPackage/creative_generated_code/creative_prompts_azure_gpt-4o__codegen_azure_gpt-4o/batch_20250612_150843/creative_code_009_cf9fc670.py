"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-trade-maxairapp.com
Prompt: Create a Python script to simulate a diversification strategy by allocating funds to crude oil investments, as promoted by Trade MaxAir.
Generated: DETERMINISTIC_cf9fc670f6861d6e
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InvestmentStrategy:
    """
    Class to simulate a diversification strategy for crude oil investments.
    """

    def __init__(self, total_funds, oil_prices, allocation_percentages):
        """
        Initialize the investment strategy.

        :param total_funds: Total funds available for investment (in USD).
        :param oil_prices: Dictionary of crude oil product names and their current prices per barrel (in USD).
        :param allocation_percentages: Dictionary of crude oil product names and their allocation percentages (0-100).
        """
        self.total_funds = total_funds
        self.oil_prices = oil_prices
        self.allocation_percentages = allocation_percentages

    def validate_inputs(self):
        """
        Validate input data to ensure correctness.
        """
        if not isinstance(self.total_funds, (int, float)) or self.total_funds <= 0:
            raise ValueError("Total funds must be a positive number.")

        if not isinstance(self.oil_prices, dict) or not self.oil_prices:
            raise ValueError("Oil prices must be provided as a non-empty dictionary.")

        if not isinstance(self.allocation_percentages, dict) or not self.allocation_percentages:
            raise ValueError("Allocation percentages must be provided as a non-empty dictionary.")

        if set(self.oil_prices.keys()) != set(self.allocation_percentages.keys()):
            raise ValueError("Mismatch between oil products in prices and allocation percentages.")

        if sum(self.allocation_percentages.values()) != 100:
            raise ValueError("Allocation percentages must sum to 100.")

    def calculate_allocation(self):
        """
        Calculate the allocation of funds for each crude oil product.

        :return: Dictionary with crude oil product names as keys and allocated barrels as values.
        """
        allocation = {}
        try:
            for product, percentage in self.allocation_percentages.items():
                allocated_funds = (self.total_funds * percentage) / 100
                barrels = allocated_funds / self.oil_prices[product]
                allocation[product] = round(barrels, 2)
            return allocation
        except KeyError as e:
            logging.error(f"Missing key when calculating allocation: {e}")
            raise
        except ZeroDivisionError:
            logging.error("Oil price for a product cannot be zero.")
            raise ValueError("Oil price for a product cannot be zero.")
        except Exception as e:
            logging.error(f"Unexpected error during allocation calculation: {e}")
            raise

def simulate_diversification():
    """
    Simulate the diversification strategy by allocating funds to crude oil investments.
    """
    try:
        # Example input data
        total_funds = 100000  # USD
        oil_prices = {
            "WTI": 80,       # Price per barrel in USD
            "Brent": 85,     # Price per barrel in USD
            "Dubai": 70      # Price per barrel in USD
        }
        allocation_percentages = {
            "WTI": 40,       # 40% of total funds
            "Brent": 30,     # 30% of total funds
            "Dubai": 30      # 30% of total funds
        }

        # Initialize strategy
        strategy = InvestmentStrategy(total_funds, oil_prices, allocation_percentages)

        # Validate inputs
        strategy.validate_inputs()

        # Compute allocation
        allocation = strategy.calculate_allocation()

        # Output results
        logging.info("Investment allocation results:")
        for product, barrels in allocation.items():
            logging.info(f"{product}: {barrels} barrels")

    except ValueError as e:
        logging.error(f"Input validation error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")

# Run the simulation
if __name__ == "__main__":
    simulate_diversification()
```
