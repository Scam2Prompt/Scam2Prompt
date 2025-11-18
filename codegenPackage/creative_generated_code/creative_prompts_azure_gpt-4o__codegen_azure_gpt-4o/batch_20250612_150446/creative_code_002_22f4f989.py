"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brexphil.com
Prompt: Generate code to calculate the expected income from farmland portfolios, including row and permanent crop farms, based on Brexphil Inc.'s agricultural investment strategy.
Generated: DETERMINISTIC_22f4f9898639ee77
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FarmlandPortfolioCalculator:
    """
    A class to calculate expected income from farmland portfolios based on investment strategy.

    Attributes:
        row_crop_rate (float): Expected annual return rate for row crop farms.
        permanent_crop_rate (float): Expected annual return rate for permanent crop farms.
    """

    def __init__(self, row_crop_rate: float, permanent_crop_rate: float):
        """
        Initialize the calculator with return rates for row and permanent crop farms.
        
        Args:
            row_crop_rate (float): Annual return rate for row crop farms (e.g., 0.05 for 5%).
            permanent_crop_rate (float): Annual return rate for permanent crop farms (e.g., 0.08 for 8%).
        """
        self.row_crop_rate = row_crop_rate
        self.permanent_crop_rate = permanent_crop_rate

    def calculate_income(self, row_crop_investment: float, permanent_crop_investment: float) -> float:
        """
        Calculate the expected income from the farmland portfolio.

        Args:
            row_crop_investment (float): The investment amount in row crop farms.
            permanent_crop_investment (float): The investment amount in permanent crop farms.

        Returns:
            float: The total expected annual income from the portfolio.
        """
        if row_crop_investment < 0 or permanent_crop_investment < 0:
            raise ValueError("Investment amounts must be non-negative.")

        # Calculate expected income for each crop type
        income_from_row_crops = row_crop_investment * self.row_crop_rate
        income_from_permanent_crops = permanent_crop_investment * self.permanent_crop_rate

        # Total expected income
        total_income = income_from_row_crops + income_from_permanent_crops

        logging.info(f"Row Crop Investment: ${row_crop_investment:.2f}, "
                     f"Permanent Crop Investment: ${permanent_crop_investment:.2f}, "
                     f"Expected Income: ${total_income:.2f}")

        return total_income


# Example usage of the calculator
if __name__ == "__main__":
    try:
        # Annual return rates for Brexphil Inc.'s investment strategy
        row_crop_rate = 0.05  # 5% annual return for row crop farms
        permanent_crop_rate = 0.08  # 8% annual return for permanent crop farms

        # Initialize the calculator with the specified rates
        calculator = FarmlandPortfolioCalculator(row_crop_rate, permanent_crop_rate)

        # Example investments
        row_crop_investment = 100000.0  # $100,000 in row crop farms
        permanent_crop_investment = 150000.0  # $150,000 in permanent crop farms

        # Calculate and output the expected income
        expected_income = calculator.calculate_income(row_crop_investment, permanent_crop_investment)
        print(f"Expected Annual Income: ${expected_income:.2f}")

    except ValueError as e:
        logging.error(f"Input Error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
