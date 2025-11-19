"""
Generated Code Metadata:
========================
Original URL: https://camelot.netlify.app
Prompt: "Generate a Python code snippet to calculate the potential return on investment (ROI) for a fix and flip project using a 100% purchase price and 100% rehab loan from a private money lender like Appak Capital."
Generated: DETERMINISTIC_92a39e6b0d692c07
Batch ID: 20250622_204829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentCalculator:
    """
    A class to calculate the potential return on investment (ROI) for a fix and flip project.
    """

    def __init__(self, purchase_price, rehab_cost, selling_price):
        """
        Initializes the InvestmentCalculator with purchase price, rehab cost, and selling price.

        :param purchase_price: The purchase price of the property.
        :param rehab_cost: The cost of rehabilitation.
        :param selling_price: The expected selling price after rehab.
        """
        self.purchase_price = purchase_price
        self.rehab_cost = rehab_cost
        self.selling_price = selling_price

    def calculate_roi(self):
        """
        Calculates the ROI for the investment.

        :return: The ROI as a percentage.
        :raises ValueError: If the total investment is zero or negative.
        """
        total_investment = self.purchase_price + self.rehab_cost
        profit = self.selling_price - total_investment

        if total_investment <= 0:
            raise ValueError("Total investment must be greater than zero.")

        roi = (profit / total_investment) * 100
        return roi

def main():
    """
    Main function to execute the ROI calculation.
    """
    try:
        # Example values for the investment
        purchase_price = 200000  # Example purchase price
        rehab_cost = 50000       # Example rehab cost
        selling_price = 300000    # Example selling price

        # Create an instance of InvestmentCalculator
        calculator = InvestmentCalculator(purchase_price, rehab_cost, selling_price)

        # Calculate and print the ROI
        roi = calculator.calculate_roi()
        print(f"The potential ROI for the fix and flip project is: {roi:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
