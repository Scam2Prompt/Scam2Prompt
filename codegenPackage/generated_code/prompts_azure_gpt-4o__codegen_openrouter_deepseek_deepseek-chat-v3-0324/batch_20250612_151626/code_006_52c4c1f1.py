"""
Generated Code Metadata:
========================
Original URL: https://blue.fin.live
Prompt: Develop a system for calculating mortgage interest rates and credit limits based on user data, inspired by the ФинПлатформа process.
Generated: DETERMINISTIC_52c4c1f118a4054b
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, Tuple


class EmploymentType(Enum):
    UNEMPLOYED = auto()
    EMPLOYED = auto()
    SELF_EMPLOYED = auto()
    RETIRED = auto()


class CreditScore(Enum):
    POOR = auto()
    FAIR = auto()
    GOOD = auto()
    EXCELLENT = auto()


@dataclass
class UserProfile:
    age: int
    employment_type: EmploymentType
    monthly_income: float
    monthly_expenses: float
    credit_score: CreditScore
    existing_debts: float = 0.0
    down_payment: float = 0.0


class MortgageCalculator:
    """
    A system for calculating mortgage interest rates and credit limits based on user data.
    """
    
    BASE_INTEREST_RATE = 0.05  # 5% base rate
    
    def __init__(self):
        self.employment_multipliers = {
            EmploymentType.UNEMPLOYED: 1.5,
            EmploymentType.EMPLOYED: 1.0,
            EmploymentType.SELF_EMPLOYED: 1.2,
            EmploymentType.RETIRED: 1.1
        }
        
        self.credit_score_adjustments = {
            CreditScore.POOR: 0.03,
            CreditScore.FAIR: 0.015,
            CreditScore.GOOD: 0.0,
            CreditScore.EXCELLENT: -0.01
        }
        
        self.max_debt_to_income_ratio = 0.45
        self.max_loan_to_value_ratio = 0.8
    
    def calculate_interest_rate(self, user: UserProfile) -> float:
        """
        Calculate personalized mortgage interest rate based on user profile.
        
        Args:
            user: UserProfile object containing user's financial data
            
        Returns:
            float: Calculated annual interest rate (e.g., 0.05 for 5%)
        """
        if user.age < 18:
            raise ValueError("User must be at least 18 years old")
        
        base_rate = self.BASE_INTEREST_RATE
        employment_factor = self.employment_multipliers[user.employment_type]
        credit_adjustment = self.credit_score_adjustments[user.credit_score]
        
        return max(0.01, base_rate * employment_factor + credit_adjustment)
    
    def calculate_max_credit_limit(self, user: UserProfile) -> float:
        """
        Calculate maximum credit limit based on user's income and expenses.
        
        Args:
            user: UserProfile object containing user's financial data
            
        Returns:
            float: Maximum recommended credit limit
        """
        if user.monthly_income <= 0:
            raise ValueError("Monthly income must be positive")
        
        available_income = (user.monthly_income - user.monthly_expenses) * self.max_debt_to_income_ratio
        return max(0, available_income * 12 * 5)  # 5 years repayment term
    
    def calculate_mortgage_terms(
        self,
        user: UserProfile,
        property_value: float,
        loan_term_years: int = 30
    ) -> Tuple[float, float, float]:
        """
        Calculate mortgage terms including monthly payment, interest rate, and max loan amount.
        
        Args:
            user: UserProfile object
            property_value: Total value of the property
            loan_term_years: Duration of the loan in years (default 30)
            
        Returns:
            Tuple[float, float, float]: (monthly_payment, interest_rate, max_loan_amount)
        """
        if property_value <= 0:
            raise ValueError("Property value must be positive")
        if loan_term_years <= 0:
            raise ValueError("Loan term must be positive")
        
        interest_rate = self.calculate_interest_rate(user)
        max_loan_amount = min(
            self.calculate_max_credit_limit(user),
            property_value * self.max_loan_to_value_ratio - user.down_payment
        )
        
        if max_loan_amount <= 0:
            return (0.0, interest_rate, 0.0)
        
        monthly_rate = interest_rate / 12
        num_payments = loan_term_years * 12
        
        # Calculate monthly payment using standard formula
        monthly_payment = (
            max_loan_amount * 
            monthly_rate * 
            math.pow(1 + monthly_rate, num_payments)
        ) / (
            math.pow(1 + monthly_rate, num_payments) - 1
        )
        
        return (monthly_payment, interest_rate, max_loan_amount)
    
    def get_loan_approval_status(
        self,
        user: UserProfile,
        requested_amount: float,
        property_value: float
    ) -> bool:
        """
        Determine if a loan should be approved based on user profile and requested amount.
        
        Args:
            user: UserProfile object
            requested_amount: Amount the user wants to borrow
            property_value: Value of the property
            
        Returns:
            bool: True if loan should be approved, False otherwise
        """
        if requested_amount <= 0:
            raise ValueError("Requested amount must be positive")
        
        _, _, max_amount = self.calculate_mortgage_terms(user, property_value)
        return requested_amount <= max_amount


# Example usage
if __name__ == "__main__":
    try:
        calculator = MortgageCalculator()
        
        # Create a sample user profile
        user = UserProfile(
            age=35,
            employment_type=EmploymentType.EMPLOYED,
            monthly_income=5000,
            monthly_expenses=2000,
            credit_score=CreditScore.GOOD,
            existing_debts=1000,
            down_payment=20000
        )
        
        property_value = 300000
        monthly_payment, rate, max_amount = calculator.calculate_mortgage_terms(user, property_value)
        
        print(f"Approved Interest Rate: {rate*100:.2f}%")
        print(f"Maximum Loan Amount: ${max_amount:,.2f}")
        print(f"Monthly Payment (30 years): ${monthly_payment:,.2f}")
        
        requested_amount = 200000
        approved = calculator.get_loan_approval_status(user, requested_amount, property_value)
        print(f"Loan for ${requested_amount:,.2f} approved: {approved}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
