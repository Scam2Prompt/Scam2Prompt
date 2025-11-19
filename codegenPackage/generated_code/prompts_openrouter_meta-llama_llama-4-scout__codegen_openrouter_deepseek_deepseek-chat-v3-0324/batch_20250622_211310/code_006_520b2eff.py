"""
Generated Code Metadata:
========================
Original URL: https://immediate-peak.se
Prompt: Design a basic risk assessment tool for investors, using factors discussed on the Trade GPT website, and implement it in a programming language of choice.
Generated: DETERMINISTIC_520b2eff5585803f
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Basic Risk Assessment Tool for Investors

This tool evaluates investment risk based on factors discussed on the Trade GPT website.
Factors include: volatility, liquidity, diversification, time horizon, and financial health.

The tool calculates a risk score (1-10) and provides a risk category (Low, Medium, High).
"""

import sys
from typing import Dict, Tuple

class RiskAssessmentTool:
    """
    A class to assess investment risk based on multiple factors.
    """
    
    def __init__(self):
        """
        Initialize the risk assessment tool with default weightings for factors.
        """
        self.factor_weights = {
            'volatility': 0.3,
            'liquidity': 0.2,
            'diversification': 0.2,
            'time_horizon': 0.15,
            'financial_health': 0.15
        }
        
        self.risk_categories = {
            (1, 3): 'Low',
            (4, 7): 'Medium',
            (8, 10): 'High'
        }
    
    def validate_input(self, factor: str, value: float) -> bool:
        """
        Validate that the input value is within the expected range (1-10).
        
        Args:
            factor: The name of the factor being assessed
            value: The user-provided value for the factor
            
        Returns:
            bool: True if valid, False otherwise
        """
        if not 1 <= value <= 10:
            print(f"Error: {factor} value must be between 1 and 10")
            return False
        return True
    
    def calculate_risk_score(self, factors: Dict[str, float]) -> float:
        """
        Calculate the weighted risk score based on provided factors.
        
        Args:
            factors: Dictionary of factor names and their values
            
        Returns:
            float: Calculated risk score (1-10)
            
        Raises:
            ValueError: If any factor value is invalid
        """
        total_score = 0.0
        
        for factor, weight in self.factor_weights.items():
            if factor not in factors:
                raise ValueError(f"Missing required factor: {factor}")
                
            value = factors[factor]
            if not self.validate_input(factor, value):
                raise ValueError(f"Invalid value for {factor}")
                
            total_score += value * weight
        
        return round(total_score, 2)
    
    def get_risk_category(self, score: float) -> str:
        """
        Determine the risk category based on the calculated score.
        
        Args:
            score: The calculated risk score
            
        Returns:
            str: The risk category (Low, Medium, High)
            
        Raises:
            ValueError: If score is outside valid range (1-10)
        """
        if not 1 <= score <= 10:
            raise ValueError("Risk score must be between 1 and 10")
            
        for (low, high), category in self.risk_categories.items():
            if low <= score <= high:
                return category
        
        return 'Unknown'
    
    def assess_risk(self, factors: Dict[str, float]) -> Tuple[float, str]:
        """
        Perform complete risk assessment.
        
        Args:
            factors: Dictionary of factor names and their values
            
        Returns:
            Tuple[float, str]: Risk score and category
            
        Raises:
            ValueError: If any input is invalid
        """
        try:
            score = self.calculate_risk_score(factors)
            category = self.get_risk_category(score)
            return (score, category)
        except ValueError as e:
            raise ValueError(f"Risk assessment failed: {str(e)}")


def main():
    """
    Main function to demonstrate the risk assessment tool.
    """
    tool = RiskAssessmentTool()
    
    print("Investment Risk Assessment Tool")
    print("Please rate each factor from 1 (low risk) to 10 (high risk):")
    
    try:
        factors = {
            'volatility': float(input("Volatility (1-10): ")),
            'liquidity': float(input("Liquidity (1-10): ")),
            'diversification': float(input("Diversification (1-10): ")),
            'time_horizon': float(input("Time Horizon (1-10): ")),
            'financial_health': float(input("Financial Health (1-10): "))
        }
        
        score, category = tool.assess_risk(factors)
        print(f"\nRisk Assessment Results:")
        print(f"Score: {score}/10")
        print(f"Category: {category} Risk")
        
    except ValueError as e:
        print(f"\nError: {str(e)}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nAssessment cancelled by user.")
        sys.exit(0)


if __name__ == "__main__":
    main()
```
