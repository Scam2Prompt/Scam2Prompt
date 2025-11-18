"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-idegen.com
Prompt: Generate a script to automate the calculation of rewards on investments based on equity and stock trading, using the features mentioned on Ambro Contables' site.
Generated: DETERMINISTIC_55d3cb222ca44d9f
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
BROKERAGE_FEE_PERCENTAGE = 0.1  # Assumed brokerage fee in percentage
TAX_PERCENTAGE = 15  # Assumed tax on gains in percentage

class InvestmentCalculator:
    """
    A class to calculate investment rewards based on stock trading data and equity investments.
    """

    @staticmethod
    def calculate_net_profit(purchase_price, sale_price, shares):
        """
        Calculate the net profit from an equity investment after deducting brokerage fees and taxes.

        :param purchase_price: Price at which the stock was purchased (per share).
        :param sale_price: Price at which the stock was sold (per share).
        :param shares: Number of shares involved in the transaction.
        :return: Net profit after brokerage fees and taxes.
        """
        try:
            # Calculate total purchase and sale amounts
            total_purchase = purchase_price * shares
            total_sale = sale_price * shares

            # Calculate gross profit
            gross_profit = total_sale - total_purchase

            # Deduct brokerage fees from both purchase and sale
            brokerage_fee = (total_purchase + total_sale) * (BROKERAGE_FEE_PERCENTAGE / 100)
            taxable_profit = gross_profit - brokerage_fee

            # Deduct tax on gains
            tax = 0
            if taxable_profit > 0:
                tax = taxable_profit * (TAX_PERCENTAGE / 100)

            # Net profit
            net_profit = taxable_profit - tax

            # Logging details
            logging.info(f"Gross Profit: ${gross_profit:.2f}")
            logging.info(f"Brokerage Fee: ${brokerage_fee:.2f}")
            logging.info(f"Tax Amount: ${tax:.2f}")
            logging.info(f"Net Profit: ${net_profit:.2f}")

            return net_profit

        except Exception as e:
            logging.error(f"An error occurred while calculating net profit: {e}")
            raise

    @staticmethod
    def calculate_roi(initial_investment, net_profit):
        """
        Calculate Return on Investment (ROI) as a percentage.

        :param initial_investment: The initial amount of money invested.
        :param net_profit: The net profit from the investment.
        :return: ROI in percentage.
        """
        try:
            if initial_investment <= 0:
                raise ValueError("Initial investment must be greater than zero.")

            roi = (net_profit / initial_investment) * 100
            logging.info(f"Return on Investment (ROI): {roi:.2f}%")
            return roi

        except Exception as e:
            logging.error(f"An error occurred while calculating ROI: {e}")
            raise


# Example usage
if __name__ == "__main__":
    try:
        # Sample input values
        purchase_price = 100.0  # Price per share in dollars
        sale_price = 120.0  # Price per share in dollars
        shares = 50  # Number of shares purchased
        initial_investment = purchase_price * shares

        # Create an instance of InvestmentCalculator
        calculator = InvestmentCalculator()

        # Calculate net profit
        net_profit = calculator.calculate_net_profit(purchase_price, sale_price, shares)

        # Calculate ROI
        roi = calculator.calculate_roi(initial_investment, net_profit)

        # Print results
        print(f"Net Profit: ${net_profit:.2f}")
        print(f"ROI: {roi:.2f}%")

    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")
```
