"""
Generated Code Metadata:
========================
Original URL: https://www.marodconsultores.com.pe
Prompt: Write a function to evaluate the economic feasibility of an electrical distribution system project, incorporating MAROD Consultores SAC's methodology for pre-investment evaluations.
Generated: DETERMINISTIC_cd27dd1b0894aa74
Batch ID: 20250612_153246
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
from typing import Dict, Tuple, Optional

class EconomicFeasibilityAnalyzer:
    """
    Evaluates the economic feasibility of an electrical distribution system project
    using MAROD Consultores SAC's methodology for pre-investment evaluations.
    """
    
    def __init__(self, project_lifetime: int, discount_rate: float):
        """
        Initialize the analyzer with project parameters.
        
        Args:
            project_lifetime: Project lifetime in years
            discount_rate: Discount rate for NPV calculation (decimal, e.g., 0.08 for 8%)
        """
        self.project_lifetime = project_lifetime
        self.discount_rate = discount_rate
        
    def calculate_npv(self, initial_investment: float, annual_cash_flows: np.ndarray) -> float:
        """
        Calculate Net Present Value (NPV) of the project.
        
        Args:
            initial_investment: Initial capital expenditure (negative value)
            annual_cash_flows: Array of annual cash flows (positive values)
            
        Returns:
            NPV value
        """
        if len(annual_cash_flows) != self.project_lifetime:
            raise ValueError("Length of annual_cash_flows must match project_lifetime")
            
        cash_flows = np.insert(annual_cash_flows, 0, initial_investment)
        discount_factors = [(1 + self.discount_rate) ** -i for i in range(len(cash_flows))]
        npv = np.sum(cash_flows * discount_factors)
        
        return npv
    
    def calculate_irr(self, initial_investment: float, annual_cash_flows: np.ndarray) -> float:
        """
        Calculate Internal Rate of Return (IRR) of the project.
        
        Args:
            initial_investment: Initial capital expenditure (negative value)
            annual_cash_flows: Array of annual cash flows (positive values)
            
        Returns:
            IRR value (decimal)
        """
        if len(annual_cash_flows) != self.project_lifetime:
            raise ValueError("Length of annual_cash_flows must match project_lifetime")
            
        cash_flows = np.insert(annual_cash_flows, 0, initial_investment)
        irr = np.irr(cash_flows)
        
        return irr
    
    def calculate_payback_period(self, initial_investment: float, annual_cash_flows: np.ndarray) -> float:
        """
        Calculate payback period in years.
        
        Args:
            initial_investment: Initial capital expenditure (positive value)
            annual_cash_flows: Array of annual cash flows (positive values)
            
        Returns:
            Payback period in years (can be fractional)
        """
        cumulative_cash_flow = 0
        payback_period = None
        
        for year, cash_flow in enumerate(annual_cash_flows, 1):
            cumulative_cash_flow += cash_flow
            if cumulative_cash_flow >= initial_investment:
                payback_period = year - 1 + (initial_investment - (cumulative_cash_flow - cash_flow)) / cash_flow
                break
                
        if payback_period is None:
            raise ValueError("Payback period exceeds project lifetime")
            
        return payback_period
    
    def calculate_bcr(self, initial_investment: float, annual_benefits: np.ndarray, annual_costs: np.ndarray) -> float:
        """
        Calculate Benefit-Cost Ratio (BCR).
        
        Args:
            initial_investment: Initial capital expenditure (positive value)
            annual_benefits: Array of annual benefits (positive values)
            annual_costs: Array of annual costs (positive values, excluding initial investment)
            
        Returns:
            Benefit-Cost Ratio
        """
        if len(annual_benefits) != self.project_lifetime or len(annual_costs) != self.project_lifetime:
            raise ValueError("Length of annual arrays must match project_lifetime")
            
        discount_factors = [(1 + self.discount_rate) ** -i for i in range(1, self.project_lifetime + 1)]
        pv_benefits = np.sum(annual_benefits * discount_factors)
        pv_costs = initial_investment + np.sum(annual_costs * discount_factors)
        
        return pv_benefits / pv_costs
    
    def evaluate_project(
        self,
        initial_investment: float,
        annual_cash_flows: np.ndarray,
        annual_benefits: Optional[np.ndarray] = None,
        annual_costs: Optional[np.ndarray] = None
    ) -> Dict[str, float]:
        """
        Comprehensive project evaluation.
        
        Args:
            initial_investment: Initial capital expenditure (positive value)
            annual_cash_flows: Array of annual cash flows (positive values)
            annual_benefits: Optional array of annual benefits for BCR calculation
            annual_costs: Optional array of annual costs for BCR calculation
            
        Returns:
            Dictionary containing all evaluation metrics
        """
        results = {
            'NPV': self.calculate_npv(-initial_investment, annual_cash_flows),
            'IRR': self.calculate_irr(-initial_investment, annual_cash_flows),
            'Payback_Period': self.calculate_payback_period(initial_investment, annual_cash_flows)
        }
        
        if annual_benefits is not None and annual_costs is not None:
            results['BCR'] = self.calculate_bcr(initial_investment, annual_benefits, annual_costs)
            
        return results
    
    def generate_report(self, evaluation_results: Dict[str, float]) -> str:
        """
        Generate a human-readable evaluation report.
        
        Args:
            evaluation_results: Dictionary of evaluation metrics
            
        Returns:
            Formatted report string
        """
        report = "MAROD Consultores SAC - Project Economic Feasibility Report\n"
        report += "=" * 60 + "\n"
        report += f"Project Lifetime: {self.project_lifetime} years\n"
        report += f"Discount Rate: {self.discount_rate * 100:.2f}%\n\n"
        report += "Evaluation Metrics:\n"
        
        for metric, value in evaluation_results.items():
            if metric == 'NPV':
                report += f"- Net Present Value: ${value:,.2f}\n"
            elif metric == 'IRR':
                report += f"- Internal Rate of Return: {value * 100:.2f}%\n"
            elif metric == 'Payback_Period':
                report += f"- Payback Period: {value:.2f} years\n"
            elif metric == 'BCR':
                report += f"- Benefit-Cost Ratio: {value:.2f}\n"
                
        # Add interpretation
        report += "\nInterpretation:\n"
        if evaluation_results['NPV'] > 0:
            report += "- NPV > 0: Project is economically viable\n"
        else:
            report += "- NPV ≤ 0: Project is not economically viable\n"
            
        if 'IRR' in evaluation_results:
            if evaluation_results['IRR'] > self.discount_rate:
                report += f"- IRR ({evaluation_results['IRR'] * 100:.2f}%) > Discount Rate ({self.discount_rate * 100:.2f}%): Project is acceptable\n"
            else:
                report += f"- IRR ({evaluation_results['IRR'] * 100:.2f}%) ≤ Discount Rate ({self.discount_rate * 100:.2f}%): Project is not acceptable\n"
                
        if 'BCR' in evaluation_results:
            if evaluation_results['BCR'] > 1:
                report += f"- BCR ({evaluation_results['BCR']:.2f}) > 1: Benefits outweigh costs\n"
            else:
                report += f"- BCR ({evaluation_results['BCR']:.2f}) ≤ 1: Costs outweigh benefits\n"
                
        return report
```
