"""
Generated Code Metadata:
========================
Original URL: https://kubitz.com.br
Prompt: "Write a Python code snippet to calculate the cost-benefit analysis of implementing a recycling program, including factors like waste reduction, job creation, and energy savings."
Generated: DETERMINISTIC_dec99986dd8542b0
Batch ID: 20250622_205440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from typing import Dict, Tuple, Optional

class RecyclingCostBenefitAnalyzer:
    """
    A class to perform cost-benefit analysis of a recycling program.
    Calculates net benefits considering waste reduction, job creation, and energy savings.
    """
    
    def __init__(self):
        """
        Initialize with default values for cost and benefit factors.
        All monetary values are in USD.
        """
        self.default_params = {
            # Costs
            'initial_investment': 100000,  # Initial setup cost
            'annual_operating_cost': 50000,  # Yearly maintenance/operations
            'collection_cost_per_ton': 50,  # Cost to collect recyclables per ton
            
            # Benefits
            'waste_reduction_per_ton': 30,  # Savings from reduced landfill fees per ton
            'job_creation_per_ton': 0.5,  # Jobs created per ton recycled
            'avg_job_salary': 35000,  # Average salary per created job
            'energy_savings_per_ton': 100,  # Energy savings per ton recycled
            'carbon_credit_per_ton': 20,  # Value of carbon credits per ton
            
            # Program metrics
            'tons_recycled_annually': 1000,  # Estimated tons recycled per year
            'program_duration': 5  # Duration of program in years
        }
    
    def calculate_net_benefits(self, custom_params: Optional[Dict] = None) -> Tuple[pd.DataFrame, float]:
        """
        Calculate the net present value (NPV) of the recycling program over its duration.
        
        Args:
            custom_params: Dictionary of custom parameters to override defaults
            
        Returns:
            Tuple containing:
                - DataFrame with yearly cost/benefit breakdown
                - Net present value (NPV) of the program
        """
        try:
            # Merge default and custom parameters
            params = {**self.default_params, **(custom_params or {})}
            
            # Validate parameters
            if any(value < 0 for value in params.values()):
                raise ValueError("All parameters must be non-negative")
            
            years = np.arange(1, params['program_duration'] + 1)
            data = []
            
            for year in years:
                # Calculate costs
                operating_cost = params['annual_operating_cost']
                collection_cost = params['collection_cost_per_ton'] * params['tons_recycled_annually']
                total_costs = operating_cost + collection_cost
                
                # Calculate benefits
                waste_reduction = params['waste_reduction_per_ton'] * params['tons_recycled_annually']
                jobs_created = params['job_creation_per_ton'] * params['tons_recycled_annually']
                job_benefit = jobs_created * params['avg_job_salary']
                energy_savings = params['energy_savings_per_ton'] * params['tons_recycled_annually']
                carbon_credits = params['carbon_credit_per_ton'] * params['tons_recycled_annually']
                total_benefits = waste_reduction + job_benefit + energy_savings + carbon_credits
                
                # Net benefit for the year
                net_benefit = total_benefits - total_costs
                
                # Only include initial investment in first year
                if year == 1:
                    total_costs += params['initial_investment']
                    net_benefit -= params['initial_investment']
                
                data.append({
                    'Year': year,
                    'Total Costs': total_costs,
                    'Total Benefits': total_benefits,
                    'Net Benefit': net_benefit,
                    'Jobs Created': jobs_created
                })
            
            # Create DataFrame with results
            results_df = pd.DataFrame(data)
            
            # Calculate NPV (assuming 5% discount rate)
            discount_rate = 0.05
            npv = sum(results_df['Net Benefit'] / (1 + discount_rate) ** results_df['Year'])
            
            return results_df, npv
        
        except Exception as e:
            print(f"Error in calculation: {str(e)}")
            return pd.DataFrame(), 0.0

# Example usage
if __name__ == "__main__":
    analyzer = RecyclingCostBenefitAnalyzer()
    
    # Run with default parameters
    results, npv = analyzer.calculate_net_benefits()
    print("\nYearly Cost-Benefit Analysis:")
    print(results.to_string(index=False))
    print(f"\nNet Present Value (NPV): ${npv:,.2f}")
    
    # Example with custom parameters
    custom_params = {
        'initial_investment': 150000,
        'tons_recycled_annually': 1500,
        'program_duration': 7
    }
    custom_results, custom_npv = analyzer.calculate_net_benefits(custom_params)
    print("\nCustom Scenario Analysis:")
    print(custom_results.to_string(index=False))
    print(f"\nNet Present Value (NPV): ${custom_npv:,.2f}")
```
