"""
Generated Code Metadata:
========================
Original URL: https://toolfix.online
Prompt: Create a program that estimates loan eligibility based on income, similar to the Loan Eligibility Estimator tool mentioned on the IFSC Finder website.
Generated: DETERMINISTIC_9971b119ac284c41
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from dataclasses import dataclass
from typing import Optional, Tuple

@dataclass
class LoanEligibilityResult:
    eligible: bool
    max_eligible_amount: float
    message: str

class LoanEligibilityEstimator:
    """
    A class to estimate loan eligibility based on income and other financial parameters.
    """
    
    def __init__(self, min_income: float = 30000, max_loan_to_income_ratio: float = 5.0):
        """
        Initialize the estimator with configuration parameters.
        
        Args:
            min_income: Minimum annual income required to be eligible for any loan (default: 30000)
            max_loan_to_income_ratio: Maximum loan amount as a multiple of annual income (default: 5.0)
        """
        self.min_income = min_income
        self.max_loan_to_income_ratio = max_loan_to_income_ratio
    
    def validate_input(self, annual_income: float, existing_loans: float) -> Tuple[bool, Optional[str]]:
        """
        Validate the input parameters.
        
        Args:
            annual_income: Applicant's annual income
            existing_loans: Total amount of existing loans
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if annual_income <= 0:
            return False, "Annual income must be positive"
        if existing_loans < 0:
            return False, "Existing loan amount cannot be negative"
        return True, None
    
    def calculate_eligibility(self, annual_income: float, existing_loans: float = 0) -> LoanEligibilityResult:
        """
        Calculate loan eligibility based on income and existing loans.
        
        Args:
            annual_income: Applicant's annual income
            existing_loans: Total amount of existing loans (default: 0)
            
        Returns:
            LoanEligibilityResult containing eligibility status and details
        """
        # Validate inputs
        is_valid, error_msg = self.validate_input(annual_income, existing_loans)
        if not is_valid:
            return LoanEligibilityResult(False, 0, error_msg)
        
        # Check minimum income requirement
        if annual_income < self.min_income:
            return LoanEligibilityResult(
                False,
                0,
                f"Income too low. Minimum required: {self.min_income}"
            )
        
        # Calculate maximum eligible loan amount
        max_eligible = (annual_income * self.max_loan_to_income_ratio) - existing_loans
        
        if max_eligible <= 0:
            return LoanEligibilityResult(
                False,
                0,
                "Existing loans exceed maximum eligible amount"
            )
        
        return LoanEligibilityResult(
            True,
            max_eligible,
            f"Eligible for loan up to {max_eligible:.2f}"
        )

def main():
    """
    Command-line interface for the Loan Eligibility Estimator.
    """
    print("Loan Eligibility Estimator")
    print("--------------------------")
    
    estimator = LoanEligibilityEstimator()
    
    try:
        annual_income = float(input("Enter your annual income: "))
        existing_loans = float(input("Enter total existing loans (0 if none): "))
        
        result = estimator.calculate_eligibility(annual_income, existing_loans)
        
        print("\nResults:")
        print(f"Eligibility: {'Yes' if result.eligible else 'No'}")
        if result.eligible:
            print(f"Maximum Eligible Amount: {result.max_eligible_amount:.2f}")
        print(f"Message: {result.message}")
        
    except ValueError:
        print("Error: Please enter valid numbers for income and loan amounts")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
