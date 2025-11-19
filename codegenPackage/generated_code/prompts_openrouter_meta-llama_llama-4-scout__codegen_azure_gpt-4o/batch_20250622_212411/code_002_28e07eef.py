"""
Generated Code Metadata:
========================
Original URL: https://dclinvest-sa.com
Prompt: Generate a sample code for calculating the potential returns on investment for a real estate project, similar to those managed by DCL Invest's real estate team.
Generated: DETERMINISTIC_28e07eefb6f7b998
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RealEstateInvestment:
    """
    A class to calculate potential returns on a real estate investment.
    """

    def __init__(self, property_price, annual_rental_income, annual_expenses, appreciation_rate, investment_period):
        """
        Initialize the investment parameters.

        :param property_price: Initial price of the property (float).
        :param annual_rental_income: Expected annual rental income (float).
        :param annual_expenses: Expected annual expenses (float).
        :param appreciation_rate: Annual property appreciation rate in percentage (float).
        :param investment_period: Investment period in years (int).
        """
        self.property_price = property_price
        self.annual_rental_income = annual_rental_income
        self.annual_expenses = annual_expenses
        self.appreciation_rate = appreciation_rate / 100  # Convert percentage to decimal
        self.investment_period = investment_period

    def calculate_total_rental_income(self):
        """
        Calculate total rental income over the investment period.

        :return: Total rental income (float).
        """
        return self.annual_rental_income * self.investment_period

    def calculate_total_expenses(self):
        """
        Calculate total expenses over the investment period.

        :return: Total expenses (float).
        """
        return self.annual_expenses * self.investment_period

    def calculate_property_value_at_end(self):
        """
        Calculate the property value at the end of the investment period based on appreciation.

        :return: Property value at the end of the investment period (float).
        """
        return self.property_price * ((1 + self.appreciation_rate) ** self.investment_period)

    def calculate_net_profit(self):
        """
        Calculate the net profit from the investment.

        :return: Net profit (float).
        """
        try:
            total_rental_income = self.calculate_total_rental_income()
            total_expenses = self.calculate_total_expenses()
            property_value_at_end = self.calculate_property_value_at_end()

            # Net profit = (Property value at end + Total rental income) - (Initial property price + Total expenses)
            net_profit = (property_value_at_end + total_rental_income) - (self.property_price + total_expenses)
            return net_profit
        except Exception as e:
            logging.error(f"Error calculating net profit: {e}")
            return None

    def calculate_roi(self):
        """
        Calculate the return on investment (ROI) as a percentage.

        :return: ROI percentage (float).
        """
        try:
            net_profit = self.calculate_net_profit()
            if net_profit is None:
                return None

            # ROI = (Net profit / Initial property price) * 100
            roi = (net_profit / self.property_price) * 100
            return roi
        except Exception as e:
            logging.error(f"Error calculating ROI: {e}")
            return None


# Example usage
if __name__ == "__main__":
    try:
        # Input parameters for the investment
        property_price = 300000.0  # Initial property price in dollars
        annual_rental_income = 24000.0  # Annual rental income in dollars
        annual_expenses = 6000.0  # Annual expenses in dollars
        appreciation_rate = 5.0  # Annual appreciation rate in percentage
        investment_period = 10  # Investment period in years

        # Create an instance of RealEstateInvestment
        investment = RealEstateInvestment(property_price, annual_rental_income, annual_expenses, appreciation_rate, investment_period)

        # Calculate and display results
        net_profit = investment.calculate_net_profit()
        roi = investment.calculate_roi()

        logging.info(f"Net Profit: ${net_profit:,.2f}")
        logging.info(f"Return on Investment (ROI): {roi:.2f}%")
    except Exception as e:
        logging.error(f"An error occurred during execution: {e}")
```
