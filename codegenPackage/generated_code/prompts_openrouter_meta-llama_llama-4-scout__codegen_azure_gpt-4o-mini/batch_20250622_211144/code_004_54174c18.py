"""
Generated Code Metadata:
========================
Original URL: https://beets-fi.com
Prompt: Write a function to calculate the costs of selling a home in Las Vegas, including commission fees and marketing expenses, based on information from AndySellsVegas.com.
Generated: DETERMINISTIC_54174c188f51a982
Batch ID: 20250622_211144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HomeSaleCalculator:
    """
    A class to calculate the costs associated with selling a home in Las Vegas.
    """

    def __init__(self, sale_price, commission_rate, marketing_expenses):
        """
        Initializes the HomeSaleCalculator with sale price, commission rate, and marketing expenses.

        :param sale_price: The selling price of the home (float).
        :param commission_rate: The commission rate as a percentage (float).
        :param marketing_expenses: The total marketing expenses (float).
        """
        self.sale_price = sale_price
        self.commission_rate = commission_rate / 100  # Convert percentage to decimal
        self.marketing_expenses = marketing_expenses

    def calculate_commission(self):
        """
        Calculates the commission based on the sale price and commission rate.

        :return: The commission amount (float).
        """
        commission = self.sale_price * self.commission_rate
        return commission

    def calculate_total_costs(self):
        """
        Calculates the total costs of selling the home, including commission and marketing expenses.

        :return: The total costs (float).
        """
        try:
            commission = self.calculate_commission()
            total_costs = commission + self.marketing_expenses
            return total_costs
        except Exception as e:
            print(f"An error occurred while calculating total costs: {e}")
            return None

    def display_costs(self):
        """
        Displays the breakdown of costs associated with selling the home.
        """
        try:
            commission = self.calculate_commission()
            total_costs = self.calculate_total_costs()

            print(f"Sale Price: ${self.sale_price:,.2f}")
            print(f"Commission Rate: {self.commission_rate * 100:.2f}%")
            print(f"Commission Amount: ${commission:,.2f}")
            print(f"Marketing Expenses: ${self.marketing_expenses:,.2f}")
            print(f"Total Costs: ${total_costs:,.2f}")
        except Exception as e:
            print(f"An error occurred while displaying costs: {e}")


# Example usage:
if __name__ == "__main__":
    # Define the sale price, commission rate, and marketing expenses
    sale_price = 500000  # Example sale price
    commission_rate = 6  # Example commission rate in percentage
    marketing_expenses = 2000  # Example marketing expenses

    # Create an instance of HomeSaleCalculator
    calculator = HomeSaleCalculator(sale_price, commission_rate, marketing_expenses)

    # Display the costs associated with selling the home
    calculator.display_costs()
```
