"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inmobiliariacapri.com.co
Prompt: Generate a script to calculate rental profitability for property owners, incorporating insurance coverage as mentioned in Inmobiliaria Capri's services.
Generated: DETERMINISTIC_b6da1de172cfa33d
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class RentalProperty:
    def __init__(self, purchase_price, rental_income, expenses, insurance_rate):
        """
        Initialize the RentalProperty class.

        :param purchase_price: The initial purchase price of the property.
        :param rental_income: The annual rental income from the property.
        :param expenses: The annual expenses related to the property (excluding insurance).
        :param insurance_rate: The insurance coverage rate as a percentage of purchase price.
        """
        self.purchase_price = purchase_price
        self.rental_income = rental_income
        self.expenses = expenses
        self.insurance_rate = insurance_rate

    def calculate_insurance_cost(self):
        """
        Calculate the annual insurance cost based on the insurance rate.

        :return: Annual insurance cost.
        """
        return self.purchase_price * (self.insurance_rate / 100)

    def calculate_net_income(self):
        """
        Calculate the net income from the rental property.

        :return: Net income after expenses and insurance costs.
        """
        insurance_cost = self.calculate_insurance_cost()
        total_expenses = self.expenses + insurance_cost
        net_income = self.rental_income - total_expenses
        return net_income

    def calculate_profitability(self):
        """
        Calculate the rental profitability as a percentage.

        :return: Profitability percentage.
        """
        net_income = self.calculate_net_income()
        if self.purchase_price == 0:
            raise ValueError("Purchase price cannot be zero for profitability calculation.")
        
        profitability = (net_income / self.purchase_price) * 100
        return profitability

def main():
    """
    Main function to execute the rental profitability calculation.
    """
    try:
        # Example values; in a real application, these would be gathered from user input or a database.
        purchase_price = float(input("Enter the purchase price of the property: "))
        rental_income = float(input("Enter the annual rental income: "))
        expenses = float(input("Enter the annual expenses excluding insurance: "))
        insurance_rate = float(input("Enter the insurance coverage rate (as a percentage): "))

        # Initialize the RentalProperty object
        property = RentalProperty(purchase_price, rental_income, expenses, insurance_rate)
        
        # Calculate profitability
        profitability = property.calculate_profitability()
        
        # Output the results
        print(f"Net Income: {property.calculate_net_income():.2f}")
        print(f"Rental Profitability: {profitability:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
