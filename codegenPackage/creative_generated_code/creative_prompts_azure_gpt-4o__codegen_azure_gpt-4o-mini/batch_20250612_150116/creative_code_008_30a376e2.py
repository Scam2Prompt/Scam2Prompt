"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maestrofinance.co.uk
Prompt: Write code to implement a growth guarantee scheme with flexible terms and low-interest rates, enabling businesses to expand as described on Maestro Finance.
Generated: DETERMINISTIC_30a376e2c8d6ea47
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GrowthGuaranteeScheme:
    """
    A class to implement a Growth Guarantee Scheme for businesses.
    
    Attributes:
        interest_rate (float): The interest rate for the loan.
        max_loan_amount (float): The maximum loan amount available under the scheme.
        loan_duration (int): The duration of the loan in months.
    """

    def __init__(self, interest_rate: float, max_loan_amount: float, loan_duration: int):
        """
        Initializes the Growth Guarantee Scheme with the given parameters.
        
        Args:
            interest_rate (float): The interest rate for the loan.
            max_loan_amount (float): The maximum loan amount available under the scheme.
            loan_duration (int): The duration of the loan in months.
        """
        if interest_rate < 0:
            raise ValueError("Interest rate must be non-negative.")
        if max_loan_amount <= 0:
            raise ValueError("Maximum loan amount must be positive.")
        if loan_duration <= 0:
            raise ValueError("Loan duration must be a positive integer.")
        
        self.interest_rate = interest_rate
        self.max_loan_amount = max_loan_amount
        self.loan_duration = loan_duration
    
    def calculate_monthly_payment(self, principal: float) -> float:
        """
        Calculate monthly payment for the loan using the formula for an amortizing loan.
        
        Args:
            principal (float): The principal loan amount.
        
        Returns:
            float: The monthly payment amount.
            
        Raises:
            ValueError: If principal is less than or equal to zero or exceeds max loan amount.
        """
        if principal <= 0:
            raise ValueError("Principal must be a positive amount.")
        if principal > self.max_loan_amount:
            raise ValueError(f"Principal cannot exceed the maximum loan amount of {self.max_loan_amount}.")
        
        monthly_rate = self.interest_rate / 12 / 100
        numerator = monthly_rate * (1 + monthly_rate) ** self.loan_duration
        denominator = (1 + monthly_rate) ** self.loan_duration - 1
        
        if denominator == 0:
            raise ZeroDivisionError("Denominator for loan payment calculation is zero.")
        
        monthly_payment = principal * numerator / denominator
        return monthly_payment
    
    def apply_for_loan(self, requested_amount: float):
        """
        Apply for a loan under the Growth Guarantee Scheme.
        
        Args:
            requested_amount (float): The amount requested by the business.
        
        Returns:
            dict: A dictionary containing loan details.
        
        Raises:
            ValueError: If the requested amount is invalid.
        """
        if requested_amount <= 0:
            raise ValueError("Requested amount must be positive.")
        
        if requested_amount > self.max_loan_amount:
            raise ValueError(f"Requested amount cannot exceed the maximum loan amount of {self.max_loan_amount}.")
        
        monthly_payment = self.calculate_monthly_payment(requested_amount)
        
        loan_details = {
            "loan_amount": requested_amount,
            "monthly_payment": round(monthly_payment, 2),
            "interest_rate": self.interest_rate,
            "loan_duration": self.loan_duration,
        }
        
        return loan_details


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the Growth Guarantee Scheme
        scheme = GrowthGuaranteeScheme(interest_rate=5.0, max_loan_amount=500000, loan_duration=60)
        
        # Apply for a loan
        requested_amount = 100000  # Example loan amount
        loan_details = scheme.apply_for_loan(requested_amount)
        
        # Print loan details
        print("Loan Details:")
        for key, value in loan_details.items():
            print(f"{key}: {value}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
