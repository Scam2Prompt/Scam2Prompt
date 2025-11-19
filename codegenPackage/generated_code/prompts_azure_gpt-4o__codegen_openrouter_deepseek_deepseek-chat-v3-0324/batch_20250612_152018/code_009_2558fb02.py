"""
Generated Code Metadata:
========================
Original URL: https://cncrete.pages.dev
Prompt: Generate code for a feature that calculates higher yields for users in an appchain focused on improving debt and credit systems.
Generated: DETERMINISTIC_2558fb0216f49b0d
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-
"""
Yield Calculator Module for AppChain Debt/Credit System

This module provides functionality to calculate higher yields for users
based on their credit score, debt profile, and other financial metrics.
"""

from dataclasses import dataclass
from decimal import Decimal, getcontext
from typing import Optional, Dict, List
import logging

# Configure decimal precision
getcontext().prec = 6

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class UserFinancialProfile:
    """Data class representing a user's financial profile."""
    credit_score: int
    total_debt: Decimal
    total_assets: Decimal
    payment_history: List[bool]  # List of on-time payments (True) or late/missed (False)
    debt_to_income_ratio: Decimal
    account_age_months: int


class YieldCalculator:
    """Main class for calculating user yields based on financial metrics."""
    
    BASE_YIELD = Decimal('0.05')  # 5% base yield
    
    def __init__(self, risk_adjustment_factors: Optional[Dict[str, Decimal]] = None):
        """
        Initialize the yield calculator with optional risk adjustment factors.
        
        Args:
            risk_adjustment_factors: Dictionary of custom risk adjustment factors.
                If None, default factors will be used.
        """
        self.risk_factors = risk_adjustment_factors or {
            'credit_score': Decimal('0.0001'),
            'debt_to_assets': Decimal('0.2'),
            'payment_history': Decimal('0.15'),
            'dti_ratio': Decimal('0.1'),
            'account_age': Decimal('0.0005')
        }
        
    def _validate_financial_profile(self, profile: UserFinancialProfile) -> None:
        """Validate the user financial profile data."""
        if not (300 <= profile.credit_score <= 850):
            raise ValueError("Credit score must be between 300 and 850")
        if profile.total_debt < 0:
            raise ValueError("Total debt cannot be negative")
        if profile.total_assets < 0:
            raise ValueError("Total assets cannot be negative")
        if profile.debt_to_income_ratio < 0:
            raise ValueError("Debt-to-income ratio cannot be negative")
        if profile.account_age_months < 0:
            raise ValueError("Account age cannot be negative")
    
    def _calculate_risk_score(self, profile: UserFinancialProfile) -> Decimal:
        """Calculate a composite risk score based on financial metrics."""
        # Calculate payment history score (percentage of on-time payments)
        payment_score = (
            sum(profile.payment_history) / len(profile.payment_history) 
            if profile.payment_history 
            else Decimal('0.5')
        )
        
        # Calculate debt-to-assets ratio
        debt_to_assets = (
            profile.total_debt / profile.total_assets 
            if profile.total_assets > 0 
            else Decimal('1.0')
        )
        
        # Composite risk score calculation
        risk_score = (
            self.risk_factors['credit_score'] * profile.credit_score +
            self.risk_factors['payment_history'] * payment_score +
            self.risk_factors['account_age'] * profile.account_age_months -
            self.risk_factors['debt_to_assets'] * debt_to_assets -
            self.risk_factors['dti_ratio'] * profile.debt_to_income_ratio
        )
        
        return risk_score
    
    def calculate_yield(self, profile: UserFinancialProfile) -> Decimal:
        """
        Calculate the yield for a user based on their financial profile.
        
        Args:
            profile: UserFinancialProfile object containing financial metrics
            
        Returns:
            Decimal representing the calculated yield percentage
            
        Raises:
            ValueError: If the financial profile data is invalid
        """
        try:
            self._validate_financial_profile(profile)
            risk_score = self._calculate_risk_score(profile)
            
            # Calculate yield adjustment (higher risk score = higher yield)
            yield_adjustment = risk_score * Decimal('0.01')
            
            # Ensure yield doesn't go below base or above reasonable maximum
            calculated_yield = max(
                self.BASE_YIELD,
                min(self.BASE_YIELD + yield_adjustment, Decimal('0.20'))  # Cap at 20%
            )
            
            logger.info(
                f"Calculated yield: {calculated_yield:.4%} for user with "
                f"credit score {profile.credit_score}"
            )
            
            return calculated_yield
            
        except Exception as e:
            logger.error(f"Error calculating yield: {str(e)}")
            raise


# Example usage
if __name__ == "__main__":
    try:
        # Sample user profile
        user_profile = UserFinancialProfile(
            credit_score=750,
            total_debt=Decimal('25000'),
            total_assets=Decimal('100000'),
            payment_history=[True] * 23 + [False] * 2,  # 23 on-time, 2 late
            debt_to_income_ratio=Decimal('0.35'),
            account_age_months=36
        )
        
        calculator = YieldCalculator()
        yield_result = calculator.calculate_yield(user_profile)
        print(f"Calculated yield: {yield_result:.2%}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
