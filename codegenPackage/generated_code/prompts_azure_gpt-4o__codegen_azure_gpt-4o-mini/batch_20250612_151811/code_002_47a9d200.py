"""
Generated Code Metadata:
========================
Original URL: https://carolinacapitalre.com
Prompt: Generate a script to calculate ROI for mid-size commercial and residential properties, incorporating the investment model strategy used by Carolina Capital.
Generated: DETERMINISTIC_47a9d2000ad22acf
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PropertyInvestment:
    """
    A class to represent a property investment and calculate its Return on Investment (ROI).
    """

    def __init__(self, purchase_price, renovation_cost, annual_rent, operating_expenses, holding_period):
        """
        Initializes the PropertyInvestment instance.

        :param purchase_price: The initial purchase price of the property.
        :param renovation_cost: The total cost of renovations.
        :param annual_rent: The expected annual rental income.
        :param operating_expenses: The annual operating expenses.
        :param holding_period: The number of years the property is held.
        """
        self.purchase_price = purchase_price
        self.renovation_cost = renovation_cost
        self.annual_rent = annual_rent
        self.operating_expenses = operating_expenses
        self.holding_period = holding_period

    def total_investment(self):
        """
        Calculates the total investment in the property.

        :return: Total investment amount.
        """
        return self.purchase_price + self.renovation_cost

    def total_income(self):
        """
        Calculates the total income generated from the property over the holding period.

        :return: Total income from rent.
        """
        return self.annual_rent * self.holding_period

    def total_expenses(self):
        """
        Calculates the total expenses incurred over the holding period.

        :return: Total operating expenses.
        """
        return self.operating_expenses * self.holding_period

    def roi(self):
        """
        Calculates the Return on Investment (ROI).

        :return: ROI as a percentage.
        """
        try:
            investment = self.total_investment()
            income = self.total_income()
            expenses = self.total_expenses()

            # ROI formula: (Total Income - Total Expenses - Total Investment) / Total Investment * 100
            roi_value = ((income - expenses - investment) / investment) * 100
            return roi_value
        except ZeroDivisionError:
            raise ValueError("Total investment cannot be zero for ROI calculation.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating ROI: {e}")

def main():
    """
    Main function to execute the ROI calculation for a property investment.
    """
    try:
        # Example property investment details
        purchase_price = 300000  # Purchase price of the property
        renovation_cost = 50000   # Renovation costs
        annual_rent = 36000       # Expected annual rent
        operating_expenses = 12000 # Annual operating expenses
        holding_period = 5        # Holding period in years

        # Create an instance of PropertyInvestment
        investment = PropertyInvestment(purchase_price, renovation_cost, annual_rent, operating_expenses, holding_period)

        # Calculate and print the ROI
        roi_value = investment.roi()
        print(f"The ROI for the property investment is: {roi_value:.2f}%")

    except ValueError as ve:
        print(f"Value error: {ve}")
    except RuntimeError as re:
        print(f"Runtime error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
