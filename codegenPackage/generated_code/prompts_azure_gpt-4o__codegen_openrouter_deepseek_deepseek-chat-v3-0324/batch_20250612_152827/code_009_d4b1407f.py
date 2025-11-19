"""
Generated Code Metadata:
========================
Original URL: https://origineth.us
Prompt: Develop a tool to calculate the benefits of Crédit Agricole's "Livret Engagé Sociétaire" savings account based on its unique features.
Generated: DETERMINISTIC_d4b1407f21715a35
Batch ID: 20250612_152827
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
class SavingsParameters:
    """Data class to hold savings account parameters."""
    initial_deposit: float
    monthly_deposit: float
    duration_months: int
    base_interest_rate: float
    bonus_interest_rate: float
    bonus_threshold: float
    membership_duration_years: int

class SavingsCalculator:
    """
    Calculator for Crédit Agricole's "Livret Engagé Sociétaire" savings account.
    Computes projected savings with base interest and potential bonuses.
    """
    
    def __init__(self, params: SavingsParameters):
        """
        Initialize the calculator with account parameters.
        
        Args:
            params: SavingsParameters object containing account details
        """
        self.params = params
        self.validate_parameters()
    
    def validate_parameters(self) -> None:
        """Validate input parameters to ensure they are reasonable."""
        if self.params.initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative")
        if self.params.monthly_deposit < 0:
            raise ValueError("Monthly deposit cannot be negative")
        if self.params.duration_months <= 0:
            raise ValueError("Duration must be at least 1 month")
        if self.params.base_interest_rate < 0:
            raise ValueError("Base interest rate cannot be negative")
        if self.params.bonus_interest_rate < 0:
            raise ValueError("Bonus interest rate cannot be negative")
        if self.params.bonus_threshold < 0:
            raise ValueError("Bonus threshold cannot be negative")
        if self.params.membership_duration_years < 0:
            raise ValueError("Membership duration cannot be negative")
    
    def calculate_base_savings(self) -> Tuple[float, float]:
        """
        Calculate savings with base interest rate only.
        
        Returns:
            Tuple of (total_savings, total_interest)
        """
        balance = self.params.initial_deposit
        total_interest = 0.0
        
        for month in range(1, self.params.duration_months + 1):
            monthly_interest = balance * (self.params.base_interest_rate / 12 / 100)
            total_interest += monthly_interest
            balance += monthly_interest + self.params.monthly_deposit
        
        return balance, total_interest
    
    def calculate_with_bonus(self) -> Tuple[float, float, float]:
        """
        Calculate savings including potential bonus interest.
        
        Returns:
            Tuple of (total_savings, total_base_interest, total_bonus_interest)
        """
        balance = self.params.initial_deposit
        total_base_interest = 0.0
        total_bonus_interest = 0.0
        
        for month in range(1, self.params.duration_months + 1):
            # Calculate base interest
            monthly_base_interest = balance * (self.params.base_interest_rate / 12 / 100)
            total_base_interest += monthly_base_interest
            balance += monthly_base_interest
            
            # Calculate bonus interest if eligible
            if (self.params.membership_duration_years >= 5 and 
                balance >= self.params.bonus_threshold):
                monthly_bonus_interest = balance * (self.params.bonus_interest_rate / 12 / 100)
                total_bonus_interest += monthly_bonus_interest
                balance += monthly_bonus_interest
            
            # Add monthly deposit
            balance += self.params.monthly_deposit
        
        return balance, total_base_interest, total_bonus_interest
    
    def generate_report(self) -> dict:
        """
        Generate a comprehensive report of savings projections.
        
        Returns:
            Dictionary containing all calculation results
        """
        base_savings, base_interest = self.calculate_base_savings()
        bonus_savings, bonus_base_interest, bonus_interest = self.calculate_with_bonus()
        
        return {
            "base_scenario": {
                "final_balance": round(base_savings, 2),
                "total_interest": round(base_interest, 2),
                "total_deposits": round(
                    self.params.initial_deposit + 
                    (self.params.monthly_deposit * self.params.duration_months), 
                    2
                )
            },
            "bonus_scenario": {
                "final_balance": round(bonus_savings, 2),
                "base_interest": round(bonus_base_interest, 2),
                "bonus_interest": round(bonus_interest, 2),
                "total_interest": round(bonus_base_interest + bonus_interest, 2),
                "total_deposits": round(
                    self.params.initial_deposit + 
                    (self.params.monthly_deposit * self.params.duration_months), 
                    2
                )
            },
            "bonus_eligibility": self.params.membership_duration_years >= 5,
            "parameters": {
                "initial_deposit": self.params.initial_deposit,
                "monthly_deposit": self.params.monthly_deposit,
                "duration_months": self.params.duration_months,
                "base_interest_rate": self.params.base_interest_rate,
                "bonus_interest_rate": self.params.bonus_interest_rate,
                "bonus_threshold": self.params.bonus_threshold,
                "membership_duration_years": self.params.membership_duration_years
            }
        }

def main():
    """Command-line interface for the savings calculator."""
    try:
        # Example parameters (should be replaced with user input or config)
        params = SavingsParameters(
            initial_deposit=1000.0,
            monthly_deposit=100.0,
            duration_months=36,
            base_interest_rate=2.0,
            bonus_interest_rate=0.5,
            bonus_threshold=5000.0,
            membership_duration_years=5
        )
        
        calculator = SavingsCalculator(params)
        report = calculator.generate_report()
        
        # Print report (in a real app, this would be formatted nicely)
        print("Savings Projection Report:")
        print(f"Base Scenario Final Balance: €{report['base_scenario']['final_balance']:,.2f}")
        print(f"Bonus Scenario Final Balance: €{report['bonus_scenario']['final_balance']:,.2f}")
        print(f"Bonus Eligibility: {'Yes' if report['bonus_eligibility'] else 'No'}")
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
