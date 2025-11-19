"""
Generated Code Metadata:
========================
Original URL: https://agdbank.com.br
Prompt: Create a script to calculate the cost of agricultural financing for producers, incorporating AGDbank's focus on advantageous and accessible conditions.
Generated: DETERMINISTIC_4ddb799467808c09
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Agricultural Financing Calculator for AGDbank

This script calculates the financing cost for agricultural producers based on loan amount,
interest rate, loan term, and any applicable subsidies or discounts. The calculator is
designed to provide advantageous and accessible financing conditions as per AGDbank's focus.
"""

import math
from typing import Union, Optional

class AgriculturalFinancingCalculator:
    """
    A calculator to determine agricultural financing costs with AGDbank's advantageous conditions.
    
    Attributes:
        base_interest_rate (float): The base annual interest rate (as a decimal).
        subsidy_rate (Optional[float]): Subsidy rate applied to interest (as a decimal).
        max_loan_term (int): Maximum loan term in years.
        min_loan_amount (float): Minimum loan amount in local currency.
        max_loan_amount (float): Maximum loan amount in local currency.
    """
    
    def __init__(
        self,
        base_interest_rate: float = 0.08,
        subsidy_rate: Optional[float] = 0.02,
        max_loan_term: int = 10,
        min_loan_amount: float = 5000.0,
        max_loan_amount: float = 1000000.0
    ):
        """
        Initialize the calculator with default or custom parameters.
        
        Args:
            base_interest_rate: Base annual interest rate (default 8%).
            subsidy_rate: Subsidy rate applied to interest (default 2%, can be None).
            max_loan_term: Maximum loan term in years (default 10).
            min_loan_amount: Minimum loan amount (default 5000).
            max_loan_amount: Maximum loan amount (default 1000000).
        """
        self.base_interest_rate = base_interest_rate
        self.subsidy_rate = subsidy_rate
        self.max_loan_term = max_loan_term
        self.min_loan_amount = min_loan_amount
        self.max_loan_amount = max_loan_amount
    
    def validate_inputs(
        self,
        loan_amount: float,
        loan_term: int,
        additional_discount: Optional[float] = None
    ) -> None:
        """
        Validate loan parameters against calculator constraints.
        
        Args:
            loan_amount: Requested loan amount.
            loan_term: Loan term in years.
            additional_discount: Any additional discount (as decimal).
            
        Raises:
            ValueError: If any parameter is invalid.
        """
        if not (self.min_loan_amount <= loan_amount <= self.max_loan_amount):
            raise ValueError(
                f"Loan amount must be between {self.min_loan_amount} and {self.max_loan_amount}"
            )
        
        if not (1 <= loan_term <= self.max_loan_term):
            raise ValueError(
                f"Loan term must be between 1 and {self.max_loan_term} years"
            )
        
        if additional_discount is not None and not (0 <= additional_discount <= 0.1):
            raise ValueError("Additional discount must be between 0% and 10%")
    
    def calculate_effective_interest_rate(
        self,
        additional_discount: Optional[float] = None
    ) -> float:
        """
        Calculate the effective interest rate after subsidies and discounts.
        
        Args:
            additional_discount: Optional additional discount (as decimal).
            
        Returns:
            The effective annual interest rate.
        """
        effective_rate = self.base_interest_rate
        
        # Apply subsidy if available
        if self.subsidy_rate is not None:
            effective_rate -= self.subsidy_rate
        
        # Apply additional discount if provided
        if additional_discount is not None:
            effective_rate -= additional_discount
        
        # Ensure rate doesn't go below 1%
        return max(effective_rate, 0.01)
    
    def calculate_monthly_payment(
        self,
        loan_amount: float,
        loan_term: int,
        additional_discount: Optional[float] = None
    ) -> float:
        """
        Calculate the monthly payment using the effective interest rate.
        
        Args:
            loan_amount: Principal loan amount.
            loan_term: Loan term in years.
            additional_discount: Optional additional discount (as decimal).
            
        Returns:
            The monthly payment amount.
            
        Raises:
            ValueError: If inputs are invalid.
        """
        self.validate_inputs(loan_amount, loan_term, additional_discount)
        
        effective_rate = self.calculate_effective_interest_rate(additional_discount)
        monthly_rate = effective_rate / 12
        num_payments = loan_term * 12
        
        # Handle case where interest rate is 0 (unlikely with min 1%)
        if monthly_rate == 0:
            return loan_amount / num_payments
        
        # Standard loan payment formula
        monthly_payment = (
            loan_amount * monthly_rate * math.pow(1 + monthly_rate, num_payments)
        ) / (math.pow(1 + monthly_rate, num_payments) - 1)
        
        return monthly_payment
    
    def calculate_total_cost(
        self,
        loan_amount: float,
        loan_term: int,
        additional_discount: Optional[float] = None
    ) -> dict:
        """
        Calculate the total financing cost and return a summary.
        
        Args:
            loan_amount: Principal loan amount.
            loan_term: Loan term in years.
            additional_discount: Optional additional discount (as decimal).
            
        Returns:
            Dictionary containing:
                - monthly_payment
                - total_payment
                - total_interest
                - effective_interest_rate
                
        Raises:
            ValueError: If inputs are invalid.
        """
        monthly_payment = self.calculate_monthly_payment(
            loan_amount, loan_term, additional_discount
        )
        total_payment = monthly_payment * loan_term * 12
        total_interest = total_payment - loan_amount
        effective_rate = self.calculate_effective_interest_rate(additional_discount)
        
        return {
            "monthly_payment": round(monthly_payment, 2),
            "total_payment": round(total_payment, 2),
            "total_interest": round(total_interest, 2),
            "effective_interest_rate": round(effective_rate * 100, 2)
        }


def main():
    """Example usage of the AgriculturalFinancingCalculator."""
    try:
        calculator = AgriculturalFinancingCalculator()
        
        # Example loan parameters
        loan_amount = 50000.0
        loan_term = 5
        additional_discount = 0.01  # 1% additional discount
        
        # Calculate and display results
        results = calculator.calculate_total_cost(loan_amount, loan_term, additional_discount)
        
        print("\nAGDbank Agricultural Financing Calculation")
        print("=" * 40)
        print(f"Loan Amount: {loan_amount:,.2f}")
        print(f"Loan Term: {loan_term} years")
        print(f"Effective Interest Rate: {results['effective_interest_rate']}%")
        print(f"Monthly Payment: {results['monthly_payment']:,.2f}")
        print(f"Total Payment: {results['total_payment']:,.2f}")
        print(f"Total Interest: {results['total_interest']:,.2f}")
        print("=" * 40)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
