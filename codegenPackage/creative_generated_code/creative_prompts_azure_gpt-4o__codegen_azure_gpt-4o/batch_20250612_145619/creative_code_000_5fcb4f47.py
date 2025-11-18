"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://camelot.netlify.app
Prompt: Write Python code to calculate loan eligibility for a fix-and-flip project based on 100% purchase price, 100% rehab cost, and up to 75% ARV as described by Appak Capital's loan products.
Generated: DETERMINISTIC_5fcb4f47d07d0eab
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LoanEligibilityCalculator:
    """
    A class to calculate loan eligibility for a fix-and-flip project based on:
    - 100% purchase price
    - 100% rehab cost
    - Up to 75% of ARV (After Repair Value)

    The loan is constrained by these conditions:
    - Total loan amount = Purchase Price + Rehab Cost
    - Total loan amount must not exceed 75% of the ARV
    """
    
    def __init__(self, purchase_price: float, rehab_cost: float, arv: float):
        """
        Initializes the LoanEligibilityCalculator with given project details.

        :param purchase_price: Purchase price of the property
        :param rehab_cost: Estimated cost of rehabilitation
        :param arv: After Repair Value (ARV) of the property
        """
        if purchase_price <= 0 or rehab_cost <= 0 or arv <= 0:
            raise ValueError("Purchase Price, Rehab Cost, and ARV must all be positive numbers.")
        
        self.purchase_price = purchase_price
        self.rehab_cost = rehab_cost
        self.arv = arv

    def calculate_loan_eligibility(self) -> float:
        """
        Calculates the maximum eligible loan amount.

        :return: Eligible loan amount (in dollars)
        """
        # Total Loan Amount = Purchase Price + Rehab Cost
        total_loan_amount = self.purchase_price + self.rehab_cost
        
        # Maximum Loan Amount = 75% of the ARV
        max_loan_limit = 0.75 * self.arv
        
        # Eligible loan amount is the minimum of the total loan amount and the max loan limit
        eligible_loan_amount = min(total_loan_amount, max_loan_limit)
        
        return eligible_loan_amount

    def is_loan_eligible(self) -> bool:
        """
        Determines if the loan is eligible based on the constraints.

        :return: True if the loan is eligible, False otherwise
        """
        return self.calculate_loan_eligibility() > 0


# Example usage
def main():
    try:
        # Input details for the loan project
        purchase_price = float(input("Enter the purchase price of the property: "))
        rehab_cost = float(input("Enter the estimated rehab cost: "))
        arv = float(input("Enter the after repair value (ARV): "))

        # Create a LoanEligibilityCalculator object
        calculator = LoanEligibilityCalculator(purchase_price, rehab_cost, arv)

        # Calculate and display loan eligibility
        eligible_amount = calculator.calculate_loan_eligibility()

        if calculator.is_loan_eligible():
            print(f"The loan is eligible. Maximum loan amount: ${eligible_amount:,.2f}")
        else:
            print("The loan is not eligible based on the given constraints.")
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
