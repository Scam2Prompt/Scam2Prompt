"""
Generated Code Metadata:
========================
Original URL: https://soltec-solutions.de
Prompt: "Create a basic financial model in Excel or Google Sheets to evaluate the feasibility of investing in a solar panel system for a small business, including calculations for payback period, ROI, and net present value."
Generated: DETERMINISTIC_e4bf1c2d55ceeec1
Batch ID: 20250622_210650
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
import matplotlib.pyplot as plt
from datetime import datetime

class SolarInvestmentModel:
    """
    A financial model to evaluate the feasibility of investing in a solar panel system.
    Calculates payback period, ROI, and NPV.
    """
    
    def __init__(self, system_cost, annual_savings, system_life, discount_rate):
        """
        Initialize the solar investment model with financial parameters.
        
        Args:
            system_cost (float): Total cost of the solar panel system
            annual_savings (float): Expected annual savings from the system
            system_life (int): Expected lifespan of the system in years
            discount_rate (float): Discount rate for NPV calculation (e.g., 0.08 for 8%)
        """
        self.system_cost = system_cost
        self.annual_savings = annual_savings
        self.system_life = system_life
        self.discount_rate = discount_rate
        
    def calculate_cash_flows(self):
        """Calculate annual cash flows over the system's lifespan."""
        years = np.arange(1, self.system_life + 1)
        cash_flows = np.array([-self.system_cost] + [self.annual_savings] * self.system_life)
        cumulative_cash_flows = np.cumsum(cash_flows)
        return years, cash_flows, cumulative_cash_flows
    
    def calculate_payback_period(self):
        """Calculate the payback period in years."""
        _, _, cumulative_cash_flows = self.calculate_cash_flows()
        payback_period = None
        
        for year, cumulative in enumerate(cumulative_cash_flows):
            if cumulative >= 0:
                payback_period = year
                break
                
        if payback_period is None:
            return self.system_life  # Never pays back within system life
            
        # Interpolate for partial years
        if payback_period > 0:
            prev_cumulative = cumulative_cash_flows[payback_period - 1]
            fraction = (0 - prev_cumulative) / (cumulative_cash_flows[payback_period] - prev_cumulative)
            payback_period = payback_period - 1 + fraction
            
        return payback_period
    
    def calculate_roi(self):
        """Calculate Return on Investment (ROI) as a percentage."""
        total_return = self.annual_savings * self.system_life
        roi = ((total_return - self.system_cost) / self.system_cost) * 100
        return roi
    
    def calculate_npv(self):
        """Calculate Net Present Value (NPV) of the investment."""
        years = np.arange(0, self.system_life + 1)
        cash_flows = np.array([-self.system_cost] + [self.annual_savings] * self.system_life)
        discount_factors = 1 / (1 + self.discount_rate) ** years
        npv = np.sum(cash_flows * discount_factors)
        return npv
    
    def generate_report(self):
        """Generate a comprehensive financial report."""
        payback_period = self.calculate_payback_period()
        roi = self.calculate_roi()
        npv = self.calculate_npv()
        years, cash_flows, cumulative_cash_flows = self.calculate_cash_flows()
        
        report = {
            "System Cost": f"${self.system_cost:,.2f}",
            "Annual Savings": f"${self.annual_savings:,.2f}",
            "System Life": f"{self.system_life} years",
            "Discount Rate": f"{self.discount_rate*100:.2f}%",
            "Payback Period": f"{payback_period:.2f} years",
            "ROI": f"{roi:.2f}%",
            "NPV": f"${npv:,.2f}",
            "Positive NPV": npv > 0
        }
        
        # Create DataFrame for cash flow table
        cash_flow_table = pd.DataFrame({
            "Year": np.arange(0, self.system_life + 1),
            "Cash Flow": cash_flows,
            "Cumulative Cash Flow": cumulative_cash_flows
        })
        
        return report, cash_flow_table
    
    def plot_cash_flows(self):
        """Plot annual and cumulative cash flows."""
        years, cash_flows, cumulative_cash_flows = self.calculate_cash_flows()
        
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.bar(years, cash_flows[1:], color='green')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.title("Annual Cash Flows")
        plt.xlabel("Year")
        plt.ylabel("Amount ($)")
        
        plt.subplot(1, 2, 2)
        plt.plot(years, cumulative_cash_flows[1:], marker='o', color='blue')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.title("Cumulative Cash Flows")
        plt.xlabel("Year")
        plt.ylabel("Amount ($)")
        
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        # Example parameters
        model = SolarInvestmentModel(
            system_cost=50000,
            annual_savings=12000,
            system_life=10,
            discount_rate=0.08
        )
        
        report, cash_flow_table = model.generate_report()
        
        print("\nSolar Investment Financial Analysis:")
        print("="*40)
        for key, value in report.items():
            print(f"{key}: {value}")
            
        print("\nCash Flow Table:")
        print(cash_flow_table.to_string(index=False))
        
        model.plot_cash_flows()
        
    except Exception as e:
        print(f"Error in financial analysis: {str(e)}")
```
