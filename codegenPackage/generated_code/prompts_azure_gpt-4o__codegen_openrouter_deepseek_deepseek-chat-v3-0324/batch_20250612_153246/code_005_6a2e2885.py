"""
Generated Code Metadata:
========================
Original URL: https://metis-investment.gr
Prompt: Write code to analyze the economic parameters of energy recovery systems, incorporating the principles of profitability and accessibility emphasized by Metis Investment.
Generated: DETERMINISTIC_6a2e2885af12f21b
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
from dataclasses import dataclass
import matplotlib.pyplot as plt

@dataclass
class EnergySystemParameters:
    """Dataclass to store energy system parameters."""
    initial_investment: float  # USD
    operational_cost: float  # USD/year
    maintenance_cost: float  # USD/year
    energy_output: float  # kWh/year
    energy_price: float  # USD/kWh
    system_lifetime: int  # years
    discount_rate: float  # decimal (e.g., 0.05 for 5%)
    accessibility_factor: float  # 0-1 scale (1 = fully accessible)

class EnergySystemAnalyzer:
    """Analyzes economic parameters of energy recovery systems based on Metis Investment principles."""
    
    def __init__(self, system_params: EnergySystemParameters):
        self.params = system_params
        
    def calculate_npv(self) -> float:
        """Calculate Net Present Value (NPV) of the energy system."""
        cash_flows = []
        for year in range(1, self.params.system_lifetime + 1):
            annual_revenue = self.params.energy_output * self.params.energy_price
            annual_cost = self.params.operational_cost + self.params.maintenance_cost
            net_cash_flow = annual_revenue - annual_cost
            discounted_cash_flow = net_cash_flow / ((1 + self.params.discount_rate) ** year)
            cash_flows.append(discounted_cash_flow)
        
        total_cash_flows = sum(cash_flows)
        npv = total_cash_flows - self.params.initial_investment
        return npv
    
    def calculate_payback_period(self) -> float:
        """Calculate payback period in years."""
        annual_revenue = self.params.energy_output * self.params.energy_price
        annual_cost = self.params.operational_cost + self.params.maintenance_cost
        annual_net_cash_flow = annual_revenue - annual_cost
        
        if annual_net_cash_flow <= 0:
            return float('inf')  # Never pays back
        
        payback_period = self.params.initial_investment / annual_net_cash_flow
        return payback_period
    
    def calculate_profitability_index(self) -> float:
        """Calculate profitability index (PI)."""
        npv = self.calculate_npv()
        if self.params.initial_investment == 0:
            return float('inf')
        pi = (npv + self.params.initial_investment) / self.params.initial_investment
        return pi
    
    def calculate_accessibility_score(self) -> float:
        """Calculate accessibility score based on Metis principles."""
        # Accessibility score combines financial and technical accessibility
        payback_period = self.calculate_payback_period()
        
        # Normalize payback period (shorter is better)
        max_payback = 20  # years (arbitrary max for normalization)
        normalized_payback = 1 - min(payback_period / max_payback, 1)
        
        # Combine with accessibility factor
        accessibility_score = (normalized_payback + self.params.accessibility_factor) / 2
        return accessibility_score
    
    def analyze_system(self) -> Dict[str, float]:
        """Run complete analysis and return results dictionary."""
        return {
            "NPV": self.calculate_npv(),
            "Payback_Period": self.calculate_payback_period(),
            "Profitability_Index": self.calculate_profitability_index(),
            "Accessibility_Score": self.calculate_accessibility_score()
        }
    
    def generate_report(self, results: Dict[str, float]) -> None:
        """Generate a formatted report of the analysis."""
        print("\nEnergy Recovery System Economic Analysis Report")
        print("="*50)
        print(f"Initial Investment: ${self.params.initial_investment:,.2f}")
        print(f"System Lifetime: {self.params.system_lifetime} years")
        print(f"Discount Rate: {self.params.discount_rate*100:.2f}%")
        print("\nResults:")
        print(f"- Net Present Value (NPV): ${results['NPV']:,.2f}")
        print(f"- Payback Period: {results['Payback_Period']:.2f} years")
        print(f"- Profitability Index: {results['Profitability_Index']:.2f}")
        print(f"- Accessibility Score: {results['Accessibility_Score']:.2f}/1.0")
        
        # Interpretation
        print("\nInterpretation:")
        if results['NPV'] > 0:
            print("✅ The project is economically viable (positive NPV)")
        else:
            print("❌ The project is not economically viable (negative NPV)")
            
        if results['Payback_Period'] <= 5:
            print("✅ Fast payback period (≤5 years)")
        elif results['Payback_Period'] <= 10:
            print("⚠️ Moderate payback period (5-10 years)")
        else:
            print("❌ Long payback period (>10 years)")
            
        if results['Accessibility_Score'] >= 0.7:
            print("✅ High accessibility score (≥0.7)")
        elif results['Accessibility_Score'] >= 0.5:
            print("⚠️ Moderate accessibility score (0.5-0.7)")
        else:
            print("❌ Low accessibility score (<0.5)")

def sensitivity_analysis(
    base_params: EnergySystemParameters,
    parameter_ranges: Dict[str, Tuple[float, float]],
    num_points: int = 10
) -> pd.DataFrame:
    """
    Perform sensitivity analysis on key parameters.
    
    Args:
        base_params: Base parameters for the system
        parameter_ranges: Dictionary of parameter ranges to test
        num_points: Number of points to test in each range
        
    Returns:
        DataFrame with sensitivity analysis results
    """
    results = []
    
    for param_name, (min_val, max_val) in parameter_ranges.items():
        values = np.linspace(min_val, max_val, num_points)
        for value in values:
            modified_params = EnergySystemParameters(
                initial_investment=value if param_name == "initial_investment" else base_params.initial_investment,
                operational_cost=value if param_name == "operational_cost" else base_params.operational_cost,
                maintenance_cost=value if param_name == "maintenance_cost" else base_params.maintenance_cost,
                energy_output=value if param_name == "energy_output" else base_params.energy_output,
                energy_price=value if param_name == "energy_price" else base_params.energy_price,
                system_lifetime=value if param_name == "system_lifetime" else base_params.system_lifetime,
                discount_rate=value if param_name == "discount_rate" else base_params.discount_rate,
                accessibility_factor=value if param_name == "accessibility_factor" else base_params.accessibility_factor
            )
            
            analyzer = EnergySystemAnalyzer(modified_params)
            analysis = analyzer.analyze_system()
            results.append({
                "Parameter": param_name,
                "Value": value,
                "NPV": analysis["NPV"],
                "Payback_Period": analysis["Payback_Period"],
                "Profitability_Index": analysis["Profitability_Index"],
                "Accessibility_Score": analysis["Accessibility_Score"]
            })
    
    return pd.DataFrame(results)

def plot_sensitivity_results(df: pd.DataFrame, output_file: Optional[str] = None) -> None:
    """
    Plot sensitivity analysis results.
    
    Args:
        df: DataFrame from sensitivity_analysis function
        output_file: Optional file path to save the plot
    """
    parameters = df["Parameter"].unique()
    num_params = len(parameters)
    
    fig, axes = plt.subplots(num_params, 3, figsize=(18, 4*num_params))
    if num_params == 1:
        axes = axes.reshape(1, -1)
    
    for i, param in enumerate(parameters):
        param_data = df[df["Parameter"] == param]
        
        # NPV plot
        axes[i, 0].plot(param_data["Value"], param_data["NPV"])
        axes[i, 0].set_title(f"NPV vs {param}")
        axes[i, 0].set_xlabel(param)
        axes[i, 0].set_ylabel("NPV (USD)")
        axes[i, 0].axhline(0, color='r', linestyle='--')
        axes[i, 0].grid(True)
        
        # Payback Period plot
        axes[i, 1].plot(param_data["Value"], param_data["Payback_Period"])
        axes[i, 1].set_title(f"Payback Period vs {param}")
        axes[i, 1].set_xlabel(param)
        axes[i, 1].set_ylabel("Payback Period (years)")
        axes[i, 1].grid(True)
        
        # Accessibility Score plot
        axes[i, 2].plot(param_data["Value"], param_data["Accessibility_Score"])
        axes[i,
