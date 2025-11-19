"""
Generated Code Metadata:
========================
Original URL: https://rhinoassetfinance.com
Prompt: Generate a Python function that calculates seasonal payment options for asset financing deals tailored to different industries.
Generated: DETERMINISTIC_aeb1be606ffae913
Batch ID: 20250612_155712
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
from typing import Dict, List, Optional, Tuple

class Industry(Enum):
    """Enum representing different industries with their seasonal factors."""
    AGRICULTURE = "Agriculture"
    RETAIL = "Retail"
    CONSTRUCTION = "Construction"
    TOURISM = "Tourism"
    MANUFACTURING = "Manufacturing"

class SeasonalPaymentCalculator:
    """Calculates seasonal payment options for asset financing deals."""
    
    def __init__(self):
        # Define seasonal factors for each industry (percentage of annual payment per season)
        self.seasonal_factors = {
            Industry.AGRICULTURE: {
                "Q1": 0.10,  # Spring
                "Q2": 0.40,  # Summer
                "Q3": 0.40,  # Fall
                "Q4": 0.10   # Winter
            },
            Industry.RETAIL: {
                "Q1": 0.20,  # Post-holiday season
                "Q2": 0.20,  # Spring
                "Q3": 0.25,  # Summer
                "Q4": 0.35   # Holiday season
            },
            Industry.CONSTRUCTION: {
                "Q1": 0.15,  # Early construction season
                "Q2": 0.35,  # Peak construction season
                "Q3": 0.35,  # Late construction season
                "Q4": 0.15   # Winter slowdown
            },
            Industry.TOURISM: {
                "Q1": 0.15,  # Off-peak
                "Q2": 0.35,  # Spring travel
                "Q3": 0.40,  # Summer peak
                "Q4": 0.10   # Fall slowdown
            },
            Industry.MANUFACTURING: {
                "Q1": 0.25,  # Steady
                "Q2": 0.25,  # Steady
                "Q3": 0.25,  # Steady
                "Q4": 0.25   # Steady
            }
        }
    
    def calculate_seasonal_payments(
        self,
        principal: float,
        annual_interest_rate: float,
        term_years: int,
        industry: Industry,
        custom_factors: Optional[Dict[str, float]] = None
    ) -> Tuple[Dict[str, float], float]:
        """
        Calculate seasonal payment amounts based on industry factors.
        
        Args:
            principal: Total loan amount
            annual_interest_rate: Annual interest rate (e.g., 0.05 for 5%)
            term_years: Loan term in years
            industry: Industry type from Industry enum
            custom_factors: Optional custom seasonal factors (overrides default)
            
        Returns:
            Tuple containing:
                - Dictionary of seasonal payments (keys: Q1-Q4)
                - Total annual payment amount
                
        Raises:
            ValueError: If invalid input parameters are provided
        """
        # Validate inputs
        if principal <= 0:
            raise ValueError("Principal must be positive")
        if annual_interest_rate < 0:
            raise ValueError("Interest rate cannot be negative")
        if term_years <= 0:
            raise ValueError("Term must be positive")
        
        # Get seasonal factors (custom or default)
        factors = custom_factors if custom_factors else self.seasonal_factors.get(industry)
        if not factors or sum(factors.values()) != 1.0:
            raise ValueError("Seasonal factors must sum to 1.0")
        
        # Calculate total annual payment using standard amortization formula
        monthly_rate = annual_interest_rate / 12
        num_payments = term_years * 12
        if annual_interest_rate == 0:
            monthly_payment = principal / num_payments
        else:
            monthly_payment = principal * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)
        
        annual_payment = monthly_payment * 12
        
        # Calculate seasonal payments
        seasonal_payments = {
            quarter: round(annual_payment * factor, 2)
            for quarter, factor in factors.items()
        }
        
        return seasonal_payments, round(annual_payment, 2)
    
    def get_available_industries(self) -> List[str]:
        """Return list of available industry names."""
        return [industry.value for industry in Industry]
    
    def get_seasonal_factors(self, industry: Industry) -> Dict[str, float]:
        """Get default seasonal factors for a given industry."""
        return self.seasonal_factors.get(industry, {})

# Example usage (commented out for production)
# if __name__ == "__main__":
#     calculator = SeasonalPaymentCalculator()
#     payments, annual = calculator.calculate_seasonal_payments(
#         principal=100000,
#         annual_interest_rate=0.05,
#         term_years=5,
#         industry=Industry.AGRICULTURE
#     )
#     print(f"Annual payment: ${annual:,.2f}")
#     print("Seasonal payments:")
#     for quarter, amount in payments.items():
#         print(f"{quarter}: ${amount:,.2f}")
```
