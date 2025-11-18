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
    A class to calculate loan eligibility for a fix-and-flip project.
    
    Attributes:
        purchase_price (float): The purchase price of the property.
        rehab_cost (float): The cost of rehabilitation for the property.
        arv (float): The After Repair Value of the property.
    """

    def __init__(self, purchase_price: float, rehab_cost: float, arv: float):
        """
        Initializes the LoanEligibilityCalculator with purchase price, rehab cost, and ARV.

        Args:
            purchase_price (float): The purchase price of the property.
            rehab_cost (float): The cost of rehabilitation for the property.
            arv (float): The After Repair Value of the property.
        """
        self.purchase_price = purchase_price
        self.rehab_cost = rehab_cost
        self.arv = arv

    def calculate_max_loan_amount(self) -> float:
        """
        Calculates the maximum loan amount based on purchase price, rehab cost, and ARV.

        Returns:
            float: The maximum loan amount eligible for application.
        """
        # Maximum loan amount based on ARV
        max_loan_based_on_arv = self.arv * 0.75
        
        # Total cost of the project
        total_project_cost = self.purchase_price + self.rehab_cost
        
        # Maximum loan amount is the lesser of the two calculations
        max_loan_amount = min(max_loan_based_on_arv, total_project_cost)
        
        return max_loan_amount

    def is_eligible(self) -> bool:
        """
        Determines if the loan eligibility criteria are met.

        Returns:
            bool: True if eligible for the loan, False otherwise.
        """
        # Check for valid inputs
        if self.purchase_price < 0 or self.rehab_cost < 0 or self.arv < 0:
            raise ValueError("Purchase price, rehab cost, and ARV must be non-negative.")
        
        # Calculate the maximum loan amount
        max_loan_amount = self.calculate_max_loan_amount()
        
        # Check eligibility criteria
        eligible = max_loan_amount >= (self.purchase_price + self.rehab_cost)
        return eligible

# Example usage
if __name__ == "__main__":
    try:
        # Example input values
        purchase_price = 200000.0  # Example purchase price
        rehab_cost = 50000.0        # Example rehab cost
        arv = 300000.0              # Example After Repair Value

        # Create a LoanEligibilityCalculator instance
        calculator = LoanEligibilityCalculator(purchase_price, rehab_cost, arv)

        # Calculate the maximum loan amount
        max_loan = calculator.calculate_max_loan_amount()
        print(f"Maximum Loan Amount: ${max_loan:.2f}")

        # Check eligibility
        eligibility = calculator.is_eligible()
        if eligibility:
            print("The project is eligible for funding.")
        else:
            print("The project is not eligible for funding.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
```
