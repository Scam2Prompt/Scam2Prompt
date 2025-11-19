"""
Generated Code Metadata:
========================
Original URL: https://guardian-associates.com
Prompt: Develop a script that calculates the optimal Rolling Reserve percentage for a business, factoring in transaction volume and risk profile, based on Guardian Associates' risk assessment approach.
Generated: DETERMINISTIC_55321844a3be1697
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from typing import Dict, Tuple, Union

class RollingReserveCalculator:
    """
    Calculates the optimal rolling reserve percentage for a business based on:
    - Transaction volume
    - Risk profile factors
    - Guardian Associates' risk assessment approach
    """
    
    def __init__(self):
        # Risk factor weights based on Guardian Associates' methodology
        self.risk_weights = {
            'chargeback_rate': 0.35,
            'refund_rate': 0.25,
            'business_age': 0.15,
            'industry_risk': 0.15,
            'transaction_consistency': 0.10
        }
        
        # Base reserve percentages by risk category
        self.base_reserves = {
            'low': 5.0,
            'medium': 10.0,
            'high': 15.0
        }
        
        # Volume adjustment factors (percentage points)
        self.volume_adjustments = {
            'low': {'adjustment': 2.0, 'threshold': 10000},
            'medium': {'adjustment': 0.0, 'threshold': 50000},
            'high': {'adjustment': -1.0, 'threshold': 100000}
        }
    
    def calculate_risk_score(self, risk_factors: Dict[str, float]) -> float:
        """
        Calculate weighted risk score based on provided factors.
        
        Args:
            risk_factors: Dictionary containing risk metrics:
                - chargeback_rate: Percentage of chargebacks (0-100)
                - refund_rate: Percentage of refunds (0-100)
                - business_age: Years in business
                - industry_risk: Industry risk score (1-10, 10=highest risk)
                - transaction_consistency: Monthly variation in transactions (0-100)
        
        Returns:
            Weighted risk score (0-100)
        """
        try:
            # Validate input factors
            for factor, weight in self.risk_weights.items():
                if factor not in risk_factors:
                    raise ValueError(f"Missing required risk factor: {factor}")
                
                value = risk_factors[factor]
                if not (0 <= value <= 100 if factor != 'business_age' else value >= 0):
                    raise ValueError(f"Invalid value for {factor}: {value}")
            
            # Calculate weighted score
            weighted_score = sum(
                risk_factors[factor] * weight 
                for factor, weight in self.risk_weights.items()
            )
            
            return min(max(weighted_score, 0), 100)  # Clamp between 0-100
            
        except Exception as e:
            raise ValueError(f"Error calculating risk score: {str(e)}")
    
    def get_risk_category(self, risk_score: float) -> str:
        """
        Determine risk category based on score.
        
        Args:
            risk_score: Calculated risk score (0-100)
        
        Returns:
            Risk category ('low', 'medium', or 'high')
        """
        if not 0 <= risk_score <= 100:
            raise ValueError("Risk score must be between 0 and 100")
            
        if risk_score <= 40:
            return 'low'
        elif risk_score <= 70:
            return 'medium'
        else:
            return 'high'
    
    def get_volume_category(self, monthly_volume: float) -> str:
        """
        Determine volume category based on monthly transaction amount.
        
        Args:
            monthly_volume: Average monthly transaction volume in USD
        
        Returns:
            Volume category ('low', 'medium', or 'high')
        """
        if monthly_volume < 0:
            raise ValueError("Monthly volume cannot be negative")
            
        if monthly_volume < self.volume_adjustments['low']['threshold']:
            return 'low'
        elif monthly_volume < self.volume_adjustments['medium']['threshold']:
            return 'medium'
        else:
            return 'high'
    
    def calculate_reserve_percentage(
        self, 
        risk_factors: Dict[str, float], 
        monthly_volume: float
    ) -> Tuple[float, Dict[str, Union[str, float]]]:
        """
        Calculate optimal rolling reserve percentage.
        
        Args:
            risk_factors: Dictionary of risk metrics
            monthly_volume: Average monthly transaction volume in USD
        
        Returns:
            Tuple of (reserve_percentage, calculation_details)
        """
        try:
            # Calculate risk components
            risk_score = self.calculate_risk_score(risk_factors)
            risk_category = self.get_risk_category(risk_score)
            base_reserve = self.base_reserves[risk_category]
            
            # Apply volume adjustment
            volume_category = self.get_volume_category(monthly_volume)
            volume_adjustment = self.volume_adjustments[volume_category]['adjustment']
            adjusted_reserve = base_reserve + volume_adjustment
            
            # Ensure reserve is within reasonable bounds (1-25%)
            final_reserve = min(max(adjusted_reserve, 1.0), 25.0)
            
            # Prepare calculation details
            details = {
                'risk_score': risk_score,
                'risk_category': risk_category,
                'base_reserve': base_reserve,
                'volume_category': volume_category,
                'volume_adjustment': volume_adjustment,
                'adjusted_reserve': adjusted_reserve,
                'final_reserve': final_reserve
            }
            
            return final_reserve, details
            
        except Exception as e:
            raise ValueError(f"Error calculating reserve percentage: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        calculator = RollingReserveCalculator()
        
        # Sample business data
        risk_factors = {
            'chargeback_rate': 2.5,    # 2.5%
            'refund_rate': 8.0,       # 8%
            'business_age': 3,        # 3 years
            'industry_risk': 6,       # 6/10
            'transaction_consistency': 20  # 20% monthly variation
        }
        monthly_volume = 75000.00     # $75,000/month
        
        reserve, details = calculator.calculate_reserve_percentage(risk_factors, monthly_volume)
        
        print(f"Optimal Rolling Reserve Percentage: {reserve:.2f}%")
        print("\nCalculation Details:")
        for key, value in details.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
