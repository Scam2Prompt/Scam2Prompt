"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolinacapitalre.com
Prompt: Generate a script to calculate ROI for mid-size commercial and residential properties, incorporating the investment model strategy used by Carolina Capital.
Generated: DETERMINISTIC_47a9d2000ad22acf
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# roi_calculator.py

class Property:
    """
    Class to represent a property and calculate its Return on Investment (ROI).
    """

    def __init__(self, purchase_price, renovation_cost, rental_income, operating_expenses, holding_period):
        """
        Initializes the Property instance.

        Args:
            purchase_price (float): The purchase price of the property.
            renovation_cost (float): The cost of renovations.
            rental_income (float): The annual rental income.
            operating_expenses (float): The annual operating expenses.
            holding_period (int): The holding period in years.
        """
        self.purchase_price = purchase_price
        self.renovation_cost = renovation_cost
        self.rental_income = rental_income
        self.operating_expenses = operating_expenses
        self.holding_period = holding_period

    def total_investment(self):
        """
        Calculates the total investment in the property.

        Returns:
            float: Total investment cost.
        """
        return self.purchase_price + self.renovation_cost

    def net_income(self):
        """
        Calculates the net income from the property over the holding period.

        Returns:
            float: Total net income.
        """
        return (self.rental_income - self.operating_expenses) * self.holding_period

    def roi(self):
        """
        Calculates the Return on Investment (ROI) for the property.

        Returns:
            float: ROI as a percentage.
        """
        try:
            total_investment = self.total_investment()
            net_income = self.net_income()
            roi_value = (net_income / total_investment) * 100
            return roi_value
        except ZeroDivisionError:
            print("Error: Total investment cannot be zero.")
            return None

def main():
    """
    Main function to run the ROI calculation for a property.
    """
    try:
        # Example property details
        purchase_price = 300000  # Example purchase price in dollars
        renovation_cost = 50000   # Example renovation cost in dollars
        rental_income = 40000      # Annual rental income in dollars
        operating_expenses = 10000  # Annual operating expenses in dollars
        holding_period = 5         # Holding period in years

        # Create a Property instance
        property_instance = Property(purchase_price, renovation_cost, rental_income, operating_expenses, holding_period)

        # Calculate ROI
        roi_value = property_instance.roi()
        if roi_value is not None:
            print(f"Return on Investment (ROI): {roi_value:.2f}%")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
