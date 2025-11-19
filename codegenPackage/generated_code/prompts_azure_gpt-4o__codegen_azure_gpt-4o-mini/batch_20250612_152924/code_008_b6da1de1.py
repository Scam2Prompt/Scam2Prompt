"""
Generated Code Metadata:
========================
Original URL: https://inmobiliariacapri.com.co
Prompt: Generate a script to calculate rental profitability for property owners, incorporating insurance coverage as mentioned in Inmobiliaria Capri's services.
Generated: DETERMINISTIC_b6da1de172cfa33d
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RentalProperty:
    """
    A class to represent a rental property and calculate its profitability.
    """

    def __init__(self, purchase_price, monthly_rent, monthly_expenses, insurance_cost):
        """
        Initializes the RentalProperty instance.

        :param purchase_price: The purchase price of the property.
        :param monthly_rent: The monthly rental income.
        :param monthly_expenses: The monthly expenses associated with the property.
        :param insurance_cost: The monthly insurance cost for the property.
        """
        self.purchase_price = purchase_price
        self.monthly_rent = monthly_rent
        self.monthly_expenses = monthly_expenses
        self.insurance_cost = insurance_cost

    def calculate_annual_profit(self):
        """
        Calculates the annual profit from the rental property.

        :return: Annual profit as a float.
        """
        try:
            # Calculate total annual income
            annual_income = self.monthly_rent * 12
            
            # Calculate total annual expenses
            total_expenses = (self.monthly_expenses + self.insurance_cost) * 12
            
            # Calculate annual profit
            annual_profit = annual_income - total_expenses
            
            return annual_profit
        except Exception as e:
            print(f"Error calculating annual profit: {e}")
            return None

    def calculate_roi(self):
        """
        Calculates the Return on Investment (ROI) for the rental property.

        :return: ROI as a percentage.
        """
        try:
            annual_profit = self.calculate_annual_profit()
            if annual_profit is None or self.purchase_price <= 0:
                raise ValueError("Invalid purchase price or profit calculation.")

            # Calculate ROI
            roi = (annual_profit / self.purchase_price) * 100
            
            return roi
        except Exception as e:
            print(f"Error calculating ROI: {e}")
            return None


def main():
    """
    Main function to execute the rental profitability calculations.
    """
    # Example property details
    purchase_price = 300000  # Purchase price of the property
    monthly_rent = 2000       # Monthly rental income
    monthly_expenses = 500     # Monthly expenses (maintenance, taxes, etc.)
    insurance_cost = 100       # Monthly insurance cost

    # Create a RentalProperty instance
    property = RentalProperty(purchase_price, monthly_rent, monthly_expenses, insurance_cost)

    # Calculate and display annual profit
    annual_profit = property.calculate_annual_profit()
    if annual_profit is not None:
        print(f"Annual Profit: ${annual_profit:.2f}")

    # Calculate and display ROI
    roi = property.calculate_roi()
    if roi is not None:
        print(f"Return on Investment (ROI): {roi:.2f}%")

if __name__ == "__main__":
    main()
```
