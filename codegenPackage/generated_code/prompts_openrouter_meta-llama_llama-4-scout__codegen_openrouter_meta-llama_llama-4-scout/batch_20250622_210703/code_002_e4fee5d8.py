"""
Generated Code Metadata:
========================
Original URL: https://lenderlibrary.ca
Prompt: "Write a script to calculate mortgage ratios for a property with 1 to 4 rental units using DLC's guidelines."
Generated: DETERMINISTIC_e4fee5d81d8c95c5
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Mortgage Ratios Calculator based on DLC's guidelines

class MortgageRatiosCalculator:
    def __init__(self, purchase_price, gross_rental_income, operating_expenses, 
                 mortgage_amount, interest_rate, amortization_years, property_taxes, 
                 insurance, maintenance_reserve):
        """
        Initialize the calculator with property and mortgage details.

        Args:
            purchase_price (float): The purchase price of the property.
            gross_rental_income (float): The gross rental income of the property.
            operating_expenses (float): The operating expenses of the property.
            mortgage_amount (float): The mortgage amount.
            interest_rate (float): The interest rate as a decimal.
            amortization_years (int): The amortization period in years.
            property_taxes (float): The annual property taxes.
            insurance (float): The annual insurance premium.
            maintenance_reserve (float): The annual maintenance reserve.
        """
        self.purchase_price = purchase_price
        self.gross_rental_income = gross_rental_income
        self.operating_expenses = operating_expenses
        self.mortgage_amount = mortgage_amount
        self.interest_rate = interest_rate
        self.amortization_years = amortization_years
        self.property_taxes = property_taxes
        self.insurance = insurance
        self.maintenance_reserve = maintenance_reserve

    def calculate_net_operating_income(self):
        """
        Calculate the Net Operating Income (NOI).

        Returns:
            float: The Net Operating Income.
        """
        return self.gross_rental_income - self.operating_expenses

    def calculate_mortgage_payments(self):
        """
        Calculate the monthly mortgage payments.

        Returns:
            float: The monthly mortgage payments.
        """
        monthly_interest_rate = self.interest_rate / 12
        amortization_months = self.amortization_years * 12
        mortgage_payments = (self.mortgage_amount * monthly_interest_rate * 
                             (1 + monthly_interest_rate) ** amortization_months) / (
                             (1 + monthly_interest_rate) ** amortization_months - 1)
        return mortgage_payments

    def calculate_mortgage_ratios(self):
        """
        Calculate the mortgage ratios based on DLC's guidelines.

        Returns:
            dict: A dictionary containing the mortgage ratios.
        """
        noi = self.calculate_net_operating_income()
        mortgage_payments = self.calculate_mortgage_payments()

        # Gross Income Multiplier (GIM)
        gim = self.purchase_price / self.gross_rental_income

        # Price per Unit
        if self.get_number_of_units() > 0:
            price_per_unit = self.purchase_price / self.get_number_of_units()
        else:
            price_per_unit = 0

        # Cap Rate
        cap_rate = noi / self.purchase_price

        # Debt Service Coverage Ratio (DSCR)
        dscr = noi / (mortgage_payments * 12)

        # Loan to Value (LTV) Ratio
        ltv_ratio = self.mortgage_amount / self.purchase_price

        return {
            'GIM': gim,
            'Price per Unit': price_per_unit,
            'Cap Rate': cap_rate,
            'DSCR': dscr,
            'LTV Ratio': ltv_ratio
        }

    def get_number_of_units(self):
        """
        Assume this method returns the number of units for the property.

        For this example, we assume it's based on a parameter not provided,
        in a real scenario, this would be an input.

        Returns:
            int: The number of units.
        """
        # For demonstration, assume 1 to 4 units
        return 4  # Example number of units

def main():
    try:
        calculator = MortgageRatiosCalculator(
            purchase_price=500000,
            gross_rental_income=60000,
            operating_expenses=15000,
            mortgage_amount=400000,
            interest_rate=0.05,
            amortization_years=25,
            property_taxes=5000,
            insurance=2000,
            maintenance_reserve=3000
        )

        ratios = calculator.calculate_mortgage_ratios()

        print("Mortgage Ratios:")
        for ratio, value in ratios.items():
            print(f"{ratio}: {value}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
