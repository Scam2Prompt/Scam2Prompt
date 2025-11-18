"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hameiriz.co.il
Prompt: Provide a Python script for calculating National Insurance contributions for self-employed individuals in Israel, referencing the methods described by Zvika Hameiri's accounting firm.
Generated: DETERMINISTIC_8e878e0b520bc27f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NationalInsuranceCalculator:
    """
    A class to calculate National Insurance contributions for self-employed individuals in Israel.
    """

    def __init__(self, annual_income):
        """
        Initializes the calculator with the annual income of the self-employed individual.

        :param annual_income: float, the total annual income of the self-employed individual.
        """
        if annual_income < 0:
            raise ValueError("Annual income must be a non-negative number.")
        self.annual_income = annual_income

    def calculate_contribution(self):
        """
        Calculates the National Insurance contribution based on the annual income.

        Contribution rates are based on current regulations for self-employed individuals in Israel.
        This method applies the relevant brackets and rates to calculate the total contribution.

        :return: float, the total National Insurance contribution.
        """
        # Define the contribution brackets and rates
        brackets = [
            (0, 6430, 0.0),        # Income below the minimum threshold
            (6431, 10424, 0.1),    # 10% for income between 6431 and 10424
            (10425, 19962, 0.12),   # 12% for income between 10425 and 19962
            (19963, float('inf'), 0.14)  # 14% for income above 19963
        ]

        total_contribution = 0.0
        remaining_income = self.annual_income

        for lower_bound, upper_bound, rate in brackets:
            if remaining_income > lower_bound:
                taxable_income = min(remaining_income, upper_bound) - lower_bound
                contribution = taxable_income * rate
                total_contribution += contribution
                remaining_income -= taxable_income

                if remaining_income <= 0:
                    break

        return total_contribution

def main():
    """
    Main function to execute the National Insurance contribution calculation.
    """
    try:
        # Input: annual income from the user
        annual_income = float(input("Enter your annual income: "))
        
        # Calculate National Insurance contribution
        calculator = NationalInsuranceCalculator(annual_income)
        contribution = calculator.calculate_contribution()
        
        # Output the result
        print(f"Your National Insurance contribution is: {contribution:.2f} ILS")
    
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
