"""
Generated Code Metadata:
========================
Original URL: https://ethx-ai.com
Prompt: Write Python code to compare the ROI of implementing predictive AI tools versus generative AI tools for a small business, using the steps outlined by ETHX-AI Consulting.
Generated: DETERMINISTIC_3873b09721c960b7
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Tuple, List

class AIToolROIAnalyzer:
    """
    A class to analyze and compare ROI of predictive vs generative AI tools for small businesses.
    Follows ETHX-AI Consulting's methodology.
    """
    
    def __init__(self, business_params: Dict[str, float]):
        """
        Initialize with business-specific parameters.
        
        Args:
            business_params: Dictionary containing business parameters:
                - initial_investment_predictive: float
                - initial_investment_generative: float
                - monthly_revenue: float
                - predictive_efficiency_gain: float (0-1)
                - generative_content_boost: float (0-1)
                - operational_cost_reduction_predictive: float
                - operational_cost_reduction_generative: float
                - time_horizon: int (months)
                - discount_rate: float (annual)
        """
        self.params = business_params
        self.validate_parameters()
        
    def validate_parameters(self) -> None:
        """Validate input parameters."""
        required_keys = [
            'initial_investment_predictive',
            'initial_investment_generative',
            'monthly_revenue',
            'predictive_efficiency_gain',
            'generative_content_boost',
            'operational_cost_reduction_predictive',
            'operational_cost_reduction_generative',
            'time_horizon',
            'discount_rate'
        ]
        
        for key in required_keys:
            if key not in self.params:
                raise ValueError(f"Missing required parameter: {key}")
                
        if not 0 <= self.params['predictive_efficiency_gain'] <= 1:
            raise ValueError("predictive_efficiency_gain must be between 0 and 1")
            
        if not 0 <= self.params['generative_content_boost'] <= 1:
            raise ValueError("generative_content_boost must be between 0 and 1")
            
        if self.params['time_horizon'] <= 0:
            raise ValueError("time_horizon must be positive")
    
    def calculate_monthly_cash_flows(self) -> Tuple[List[float], List[float]]:
        """
        Calculate monthly cash flows for both AI tools.
        
        Returns:
            Tuple of (predictive_cash_flows, generative_cash_flows)
        """
        monthly_discount = (1 + self.params['discount_rate']/12) ** (1/12) - 1
        
        predictive_cash_flows = [-self.params['initial_investment_predictive']]
        generative_cash_flows = [-self.params['initial_investment_generative']]
        
        for month in range(1, self.params['time_horizon'] + 1):
            # Predictive AI benefits
            efficiency_gain = self.params['monthly_revenue'] * self.params['predictive_efficiency_gain']
            cost_reduction = self.params['operational_cost_reduction_predictive']
            predictive_cf = efficiency_gain + cost_reduction
            predictive_cf /= (1 + monthly_discount) ** month
            predictive_cash_flows.append(predictive_cf)
            
            # Generative AI benefits
            content_boost = self.params['monthly_revenue'] * self.params['generative_content_boost']
            cost_reduction = self.params['operational_cost_reduction_generative']
            generative_cf = content_boost + cost_reduction
            generative_cf /= (1 + monthly_discount) ** month
            generative_cash_flows.append(generative_cf)
            
        return predictive_cash_flows, generative_cash_flows
    
    def calculate_roi(self, cash_flows: List[float], initial_investment: float) -> float:
        """
        Calculate ROI given cash flows and initial investment.
        
        Args:
            cash_flows: List of monthly cash flows
            initial_investment: Initial investment amount
            
        Returns:
            ROI as a percentage
        """
        total_return = sum(cash_flows[1:])  # Exclude initial investment
        return (total_return - initial_investment) / initial_investment * 100
    
    def calculate_npv(self, cash_flows: List[float]) -> float:
        """
        Calculate Net Present Value of cash flows.
        
        Args:
            cash_flows: List of monthly cash flows
            
        Returns:
            NPV value
        """
        return sum(cash_flows)
    
    def compare_roi(self) -> Dict[str, Dict[str, float]]:
        """
        Compare ROI of predictive vs generative AI tools.
        
        Returns:
            Dictionary containing comparison metrics:
                - predictive: ROI, NPV, payback_period
                - generative: ROI, NPV, payback_period
        """
        predictive_cf, generative_cf = self.calculate_monthly_cash_flows()
        
        results = {
            'predictive': {
                'roi': self.calculate_roi(predictive_cf, self.params['initial_investment_predictive']),
                'npv': self.calculate_npv(predictive_cf),
                'payback_period': self.calculate_payback_period(predictive_cf)
            },
            'generative': {
                'roi': self.calculate_roi(generative_cf, self.params['initial_investment_generative']),
                'npv': self.calculate_npv(generative_cf),
                'payback_period': self.calculate_payback_period(generative_cf)
            }
        }
        
        return results
    
    def calculate_payback_period(self, cash_flows: List[float]) -> float:
        """
        Calculate payback period in months.
        
        Args:
            cash_flows: List of monthly cash flows
            
        Returns:
            Payback period in months
        """
        cumulative = 0
        for month, cf in enumerate(cash_flows):
            cumulative += cf
            if cumulative >= 0:
                return month
        return float('inf')  # Never pays back
    
    def visualize_comparison(self, results: Dict[str, Dict[str, float]]) -> None:
        """
        Visualize the comparison results.
        
        Args:
            results: Dictionary containing comparison metrics
        """
        labels = ['ROI (%)', 'NPV ($)', 'Payback Period (months)']
        predictive_values = [
            results['predictive']['roi'],
            results['predictive']['npv'],
            results['predictive']['payback_period']
        ]
        generative_values = [
            results['generative']['roi'],
            results['generative']['npv'],
            results['generative']['payback_period']
        ]
        
        x = np.arange(len(labels))
        width = 0.35
        
        fig, ax = plt.subplots(figsize=(10, 6))
        rects1 = ax.bar(x - width/2, predictive_values, width, label='Predictive AI')
        rects2 = ax.bar(x + width/2, generative_values, width, label='Generative AI')
        
        ax.set_ylabel('Value')
        ax.set_title('AI Tools ROI Comparison')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()
        
        fig.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Sample business parameters
    business_params = {
        'initial_investment_predictive': 20000,
        'initial_investment_generative': 25000,
        'monthly_revenue': 50000,
        'predictive_efficiency_gain': 0.15,  # 15% efficiency gain
        'generative_content_boost': 0.10,    # 10% content boost
        'operational_cost_reduction_predictive': 2000,
        'operational_cost_reduction_generative': 1500,
        'time_horizon': 24,  # 2 years
        'discount_rate': 0.05  # 5% annual
    }
    
    try:
        analyzer = AIToolROIAnalyzer(business_params)
        results = analyzer.compare_roi()
        print("ROI Comparison Results:")
        print("Predictive AI:", results['predictive'])
        print("Generative AI:", results['generative'])
        analyzer.visualize_comparison(results)
    except ValueError as e:
        print(f"Error in analysis: {e}")
```
