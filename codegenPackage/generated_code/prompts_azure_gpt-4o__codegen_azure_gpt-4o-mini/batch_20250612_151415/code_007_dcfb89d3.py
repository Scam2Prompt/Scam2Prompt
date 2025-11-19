"""
Generated Code Metadata:
========================
Original URL: https://toolfix.online
Prompt: Develop a tool to calculate income tax liability for FY 2024–25, using the Income Tax Calculator described on the IFSC Finder webpage.
Generated: DETERMINISTIC_dcfb89d3322a0af4
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class IncomeTaxCalculator:
    """
    A class to calculate income tax liability for the financial year 2024-25.
    """

    def __init__(self, income):
        """
        Initializes the IncomeTaxCalculator with the given income.

        :param income: Annual income of the individual
        """
        self.income = income

    def calculate_tax(self):
        """
        Calculates the income tax based on the income slabs for FY 2024-25.

        :return: The calculated income tax
        """
        try:
            if self.income < 0:
                raise ValueError("Income cannot be negative.")

            tax = 0

            # Define tax slabs and rates
            slabs = [
                (250000, 0.0),   # No tax for income up to 2.5 lakhs
                (500000, 0.05),  # 5% for income between 2.5 to 5 lakhs
                (1000000, 0.1),  # 10% for income between 5 to 10 lakhs
                (float('inf'), 0.3)  # 30% for income above 10 lakhs
            ]

            previous_limit = 0

            for limit, rate in slabs:
                if self.income > previous_limit:
                    taxable_income = min(self.income, limit) - previous_limit
                    tax += taxable_income * rate
                    previous_limit = limit
                else:
                    break

            return tax

        except Exception as e:
            print(f"Error calculating tax: {e}")
            return None

def main():
    """
    Main function to execute the income tax calculation.
    """
    try:
        # Input income from the user
        income = float(input("Enter your annual income for FY 2024-25: "))
        
        # Create an instance of IncomeTaxCalculator
        tax_calculator = IncomeTaxCalculator(income)
        
        # Calculate the tax
        tax_liability = tax_calculator.calculate_tax()
        
        if tax_liability is not None:
            print(f"Your income tax liability for FY 2024-25 is: ₹{tax_liability:.2f}")

    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
