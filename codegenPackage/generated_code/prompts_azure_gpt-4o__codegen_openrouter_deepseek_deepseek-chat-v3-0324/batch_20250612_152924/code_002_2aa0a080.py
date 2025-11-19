"""
Generated Code Metadata:
========================
Original URL: https://lossgroupcriteria.com
Prompt: Generate code to calculate economic returns for insurers and reinsurers based on loss recovery and risk improvement metrics, referencing the methodologies described by Loss Group Criteria.
Generated: DETERMINISTIC_2aa0a080c55d94a2
Batch ID: 20250612_152924
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
from typing import Tuple, Dict, Optional

class InsuranceEconomicReturns:
    """
    Calculate economic returns for insurers and reinsurers based on:
    - Loss recovery metrics
    - Risk improvement metrics
    - Loss Group Criteria methodologies
    """
    
    def __init__(self, 
                 premium: float, 
                 expected_loss: float, 
                 capital_allocated: float,
                 risk_free_rate: float = 0.02,
                 tax_rate: float = 0.3):
        """
        Initialize the calculator with base parameters.
        
        Args:
            premium: Total premium collected
            expected_loss: Expected loss amount
            capital_allocated: Capital allocated to the risk
            risk_free_rate: Risk-free rate for time value of money (default 2%)
            tax_rate: Corporate tax rate (default 30%)
        """
        self.premium = premium
        self.expected_loss = expected_loss
        self.capital_allocated = capital_allocated
        self.risk_free_rate = risk_free_rate
        self.tax_rate = tax_rate
        
        # Validate inputs
        if any(val < 0 for val in [premium, expected_loss, capital_allocated]):
            raise ValueError("Negative values not allowed for premium, expected_loss, or capital_allocated")
        if not 0 <= risk_free_rate <= 1:
            raise ValueError("Risk-free rate must be between 0 and 1")
        if not 0 <= tax_rate <= 1:
            raise ValueError("Tax rate must be between 0 and 1")
    
    def calculate_roec(self, actual_loss: float, reinsurance_recovery: float = 0) -> float:
        """
        Calculate Return on Economic Capital (ROEC) after reinsurance.
        
        Args:
            actual_loss: Actual loss incurred
            reinsurance_recovery: Amount recovered from reinsurance
            
        Returns:
            ROEC percentage
        """
        try:
            net_loss = max(0, actual_loss - reinsurance_recovery)
            profit_after_tax = (self.premium - net_loss) * (1 - self.tax_rate)
            return (profit_after_tax / self.capital_allocated) * 100
        except ZeroDivisionError:
            return 0.0
    
    def calculate_raroec(self, actual_loss: float, reinsurance_recovery: float = 0) -> float:
        """
        Calculate Risk-Adjusted Return on Economic Capital (RAROEC).
        
        Args:
            actual_loss: Actual loss incurred
            reinsurance_recovery: Amount recovered from reinsurance
            
        Returns:
            RAROEC percentage
        """
        roec = self.calculate_roec(actual_loss, reinsurance_recovery)
        volatility = self._calculate_loss_volatility(actual_loss)
        
        # Avoid division by zero
        if volatility == 0:
            return roec
        
        return roec / volatility
    
    def _calculate_loss_volatility(self, actual_loss: float) -> float:
        """
        Calculate loss volatility (standard deviation of losses).
        
        Args:
            actual_loss: Actual loss incurred
            
        Returns:
            Loss volatility measure
        """
        # In a real implementation, this would use historical loss data
        # For simplicity, we use a basic measure here
        return abs(actual_loss - self.expected_loss) / self.expected_loss if self.expected_loss != 0 else 0
    
    def calculate_risk_improvement(self, 
                                 before_metrics: Dict[str, float], 
                                 after_metrics: Dict[str, float]) -> Dict[str, float]:
        """
        Calculate risk improvement metrics after reinsurance.
        
        Args:
            before_metrics: Dictionary of risk metrics before reinsurance
            after_metrics: Dictionary of risk metrics after reinsurance
            
        Returns:
            Dictionary of improvement percentages for each metric
        """
        improvements = {}
        for metric in before_metrics:
            if metric in after_metrics:
                try:
                    before = before_metrics[metric]
                    after = after_metrics[metric]
                    if before == 0:
                        improvements[metric] = 0.0
                    else:
                        improvements[metric] = ((before - after) / before) * 100
                except (TypeError, KeyError):
                    improvements[metric] = 0.0
        return improvements
    
    def calculate_combined_return(self,
                                actual_loss: float,
                                reinsurance_recovery: float,
                                before_metrics: Dict[str, float],
                                after_metrics: Dict[str, float],
                                weights: Optional[Dict[str, float]] = None) -> float:
        """
        Calculate combined economic return considering both financial and risk metrics.
        
        Args:
            actual_loss: Actual loss incurred
            reinsurance_recovery: Amount recovered from reinsurance
            before_metrics: Risk metrics before reinsurance
            after_metrics: Risk metrics after reinsurance
            weights: Optional weights for different metrics (default: equal weighting)
            
        Returns:
            Combined economic return score
        """
        # Default equal weights if not provided
        if weights is None:
            weights = {
                'roec': 0.5,
                'risk_improvement': 0.5
            }
        
        # Calculate components
        roec = self.calculate_roec(actual_loss, reinsurance_recovery)
        risk_improvements = self.calculate_risk_improvement(before_metrics, after_metrics)
        
        # Average risk improvement across all metrics
        avg_risk_improvement = np.mean(list(risk_improvements.values())) if risk_improvements else 0
        
        # Apply weights
        combined_return = (weights['roec'] * roec) + (weights['risk_improvement'] * avg_risk_improvement)
        
        return combined_return

# Example usage
if __name__ == "__main__":
    # Initialize calculator
    calc = InsuranceEconomicReturns(
        premium=1000000,
        expected_loss=600000,
        capital_allocated=2000000
    )
    
    # Calculate metrics
    roec = calc.calculate_roec(actual_loss=700000, reinsurance_recovery=200000)
    raroec = calc.calculate_raroec(actual_loss=700000, reinsurance_recovery=200000)
    
    # Risk improvement metrics
    before = {
        'var_95': 1500000,
        'expected_shortfall': 1800000,
        'loss_volatility': 0.4
    }
    after = {
        'var_95': 1200000,
        'expected_shortfall': 1400000,
        'loss_volatility': 0.3
    }
    improvements = calc.calculate_risk_improvement(before, after)
    
    # Combined return
    combined = calc.calculate_combined_return(
        actual_loss=700000,
        reinsurance_recovery=200000,
        before_metrics=before,
        after_metrics=after
    )
    
    # Print results
    print(f"ROEC: {roec:.2f}%")
    print(f"RAROEC: {raroec:.2f}")
    print("Risk Improvements:")
    for metric, improvement in improvements.items():
        print(f"  {metric}: {improvement:.2f}%")
    print(f"Combined Economic Return: {combined:.2f}")
```
