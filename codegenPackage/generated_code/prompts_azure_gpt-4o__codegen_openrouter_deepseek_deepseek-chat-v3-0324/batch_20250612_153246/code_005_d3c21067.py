"""
Generated Code Metadata:
========================
Original URL: https://lenderlibrary.ca
Prompt: Develop a tool in Python to calculate equity loan amounts based on Dominion Lending's guidelines for different property types and borrower scenarios.
Generated: DETERMINISTIC_d3c2106700362ef4
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from enum import Enum
from typing import Optional, Union

class PropertyType(Enum):
    """Enum representing different property types."""
    PRIMARY_RESIDENCE = "Primary Residence"
    SECONDARY_RESIDENCE = "Secondary Residence"
    RENTAL_PROPERTY = "Rental Property"
    COMMERCIAL_PROPERTY = "Commercial Property"

class BorrowerScenario(Enum):
    """Enum representing different borrower scenarios."""
    STANDARD = "Standard"
    SELF_EMPLOYED = "Self-Employed"
    NEW_IMMIGRANT = "New Immigrant"
    CREDIT_CHALLENGED = "Credit Challenged"

class EquityLoanCalculator:
    """
    A calculator for determining equity loan amounts based on Dominion Lending's guidelines.
    
    Attributes:
        property_value (float): Current market value of the property
        outstanding_mortgage (float): Outstanding mortgage balance
        property_type (PropertyType): Type of property
        borrower_scenario (BorrowerScenario): Borrower's financial scenario
    """
    
    MAX_LTV_PRIMARY = 0.80
    MAX_LTV_SECONDARY = 0.75
    MAX_LTV_RENTAL = 0.65
    MAX_LTV_COMMERCIAL = 0.60
    
    SCENARIO_ADJUSTMENTS = {
        BorrowerScenario.STANDARD: 1.0,
        BorrowerScenario.SELF_EMPLOYED: 0.95,
        BorrowerScenario.NEW_IMMIGRANT: 0.90,
        BorrowerScenario.CREDIT_CHALLENGED: 0.85
    }
    
    def __init__(
        self,
        property_value: float,
        outstanding_mortgage: float,
        property_type: PropertyType,
        borrower_scenario: BorrowerScenario = BorrowerScenario.STANDARD
    ):
        """
        Initialize the calculator with property and borrower details.
        
        Args:
            property_value: Current market value of the property
            outstanding_mortgage: Outstanding mortgage balance
            property_type: Type of property
            borrower_scenario: Borrower's financial scenario (default: STANDARD)
            
        Raises:
            ValueError: If property_value or outstanding_mortgage are negative
        """
        if property_value < 0:
            raise ValueError("Property value cannot be negative")
        if outstanding_mortgage < 0:
            raise ValueError("Outstanding mortgage cannot be negative")
            
        self.property_value = property_value
        self.outstanding_mortgage = outstanding_mortgage
        self.property_type = property_type
        self.borrower_scenario = borrower_scenario
    
    def get_max_ltv(self) -> float:
        """
        Get the maximum Loan-to-Value ratio based on property type.
        
        Returns:
            float: Maximum LTV ratio for the property type
        """
        if self.property_type == PropertyType.PRIMARY_RESIDENCE:
            return self.MAX_LTV_PRIMARY
        elif self.property_type == PropertyType.SECONDARY_RESIDENCE:
            return self.MAX_LTV_SECONDARY
        elif self.property_type == PropertyType.RENTAL_PROPERTY:
            return self.MAX_LTV_RENTAL
        elif self.property_type == PropertyType.COMMERCIAL_PROPERTY:
            return self.MAX_LTV_COMMERCIAL
        else:
            raise ValueError("Invalid property type")
    
    def calculate_max_loan_amount(self) -> float:
        """
        Calculate the maximum loan amount based on Dominion Lending's guidelines.
        
        Returns:
            float: Maximum loan amount available
            
        Raises:
            ValueError: If property value is insufficient for the outstanding mortgage
        """
        max_ltv = self.get_max_ltv()
        scenario_adjustment = self.SCENARIO_ADJUSTMENTS[self.borrower_scenario]
        
        max_loan_based_on_value = self.property_value * max_ltv * scenario_adjustment
        
        if max_loan_based_on_value < self.outstanding_mortgage:
            raise ValueError("Property value is insufficient for the outstanding mortgage")
        
        available_equity = max_loan_based_on_value - self.outstanding_mortgage
        return max(0, available_equity)
    
    def calculate_monthly_payment(
        self,
        loan_amount: float,
        amortization_period: int,
        interest_rate: float,
        payment_frequency: int = 12
    ) -> float:
        """
        Calculate the monthly payment for the loan.
        
        Args:
            loan_amount: Amount to be borrowed
            amortization_period: Amortization period in years
            interest_rate: Annual interest rate (as decimal)
            payment_frequency: Number of payments per year (default: 12)
            
        Returns:
            float: Calculated monthly payment
            
        Raises:
            ValueError: If any parameter is invalid
        """
        if loan_amount <= 0:
            raise ValueError("Loan amount must be positive")
        if amortization_period <= 0:
            raise ValueError("Amortization period must be positive")
        if interest_rate <= 0:
            raise ValueError("Interest rate must be positive")
        if payment_frequency <= 0:
            raise ValueError("Payment frequency must be positive")
            
        monthly_rate = interest_rate / payment_frequency
        total_payments = amortization_period * payment_frequency
        
        if monthly_rate == 0:
            return loan_amount / total_payments
            
        payment = (loan_amount * monthly_rate) / (1 - (1 + monthly_rate) ** -total_payments)
        return payment

def main():
    """Example usage of the EquityLoanCalculator."""
    try:
        # Example property details
        property_value = 500000
        outstanding_mortgage = 200000
        property_type = PropertyType.PRIMARY_RESIDENCE
        borrower_scenario = BorrowerScenario.SELF_EMPLOYED
        
        # Create calculator instance
        calculator = EquityLoanCalculator(
            property_value=property_value,
            outstanding_mortgage=outstanding_mortgage,
            property_type=property_type,
            borrower_scenario=borrower_scenario
        )
        
        # Calculate maximum loan amount
        max_loan = calculator.calculate_max_loan_amount()
        print(f"Maximum available loan amount: ${max_loan:,.2f}")
        
        # Example payment calculation
        loan_amount = min(300000, max_loan)  # Example: borrower wants up to $300k
        amortization_period = 25  # years
        interest_rate = 0.05  # 5% annual
        
        monthly_payment = calculator.calculate_monthly_payment(
            loan_amount=loan_amount,
            amortization_period=amortization_period,
            interest_rate=interest_rate
        )
        print(f"Monthly payment for ${loan_amount:,.2f}: ${monthly_payment:,.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
