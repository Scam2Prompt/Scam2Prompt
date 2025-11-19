"""
Generated Code Metadata:
========================
Original URL: https://carolinacapitalre.com
Prompt: Write a Python code snippet to calculate the returns on investment for a real estate project, similar to Carolina Capital's strategy, assuming an initial land acquisition cost and projected development revenue.
Generated: DETERMINISTIC_25d6c312ca29cd15
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import numpy_financial as npf

class RealEstateInvestment:
    """
    A class to calculate the returns on investment for a real estate project.
    Similar to Carolina Capital's strategy, it models initial land acquisition
    costs and projected development revenue.
    """
    
    def __init__(self, initial_investment, development_costs, holding_period_years, 
                 annual_operating_costs, projected_revenue, discount_rate=0.1):
        """
        Initialize the investment parameters.
        
        Args:
            initial_investment (float): Initial land acquisition cost
            development_costs (list): List of development costs per period
            holding_period_years (int): Number of years to hold the property
            annual_operating_costs (float): Annual operating costs
            projected_revenue (list): List of projected revenue per period
            discount_rate (float, optional): Discount rate for NPV calculation. Defaults to 0.1 (10%).
        """
        self.initial_investment = initial_investment
        self.development_costs = development_costs
        self.holding_period_years = holding_period_years
        self.annual_operating_costs = annual_operating_costs
        self.projected_revenue = projected_revenue
        self.discount_rate = discount_rate
        
        # Validate inputs
        if len(development_costs) != holding_period_years:
            raise ValueError("Development costs list length must match holding period")
        if len(projected_revenue) != holding_period_years:
            raise ValueError("Projected revenue list length must match holding period")
        if any(cost < 0 for cost in development_costs):
            raise ValueError("Development costs cannot be negative")
        if any(revenue < 0 for revenue in projected_revenue):
            raise ValueError("Projected revenue cannot be negative")
    
    def calculate_cash_flows(self):
        """
        Calculate annual cash flows for the investment.
        
        Returns:
            list: List of annual cash flows (negative for outflows, positive for inflows)
        """
        cash_flows = [-self.initial_investment]
        
        for year in range(self.holding_period_years):
            net_cash_flow = (self.projected_revenue[year] - 
                             self.development_costs[year] - 
                             self.annual_operating_costs)
            cash_flows.append(net_cash_flow)
            
        return cash_flows
    
    def calculate_npv(self):
        """
        Calculate the Net Present Value (NPV) of the investment.
        
        Returns:
            float: NPV of the investment
        """
        cash_flows = self.calculate_cash_flows()
        return npf.npv(self.discount_rate, cash_flows)
    
    def calculate_irr(self):
        """
        Calculate the Internal Rate of Return (IRR) of the investment.
        
        Returns:
            float: IRR of the investment
        """
        cash_flows = self.calculate_cash_flows()
        return npf.irr(cash_flows)
    
    def calculate_roi(self):
        """
        Calculate the Return on Investment (ROI) percentage.
        
        Returns:
            float: ROI percentage
        """
        cash_flows = self.calculate_cash_flows()
        total_investment = self.initial_investment + sum(self.development_costs)
        total_return = sum(cash_flows[1:])  # Exclude initial investment
        return (total_return / total_investment) * 100
    
    def calculate_payback_period(self):
        """
        Calculate the payback period in years.
        
        Returns:
            float: Payback period in years
        """
        cash_flows = self.calculate_cash_flows()
        cumulative_cash_flow = 0
        payback_period = 0
        
        for i, flow in enumerate(cash_flows):
            cumulative_cash_flow += flow
            if cumulative_cash_flow >= 0:
                if i == 0:
                    return 0
                # Linear interpolation for fractional years
                last_negative = cumulative_cash_flow - flow
                fractional_year = abs(last_negative) / flow
                payback_period = i - 1 + fractional_year
                return payback_period
        
        return float('inf')  # Investment never pays back

# Example usage
if __name__ == "__main__":
    try:
        # Example parameters
        investment = RealEstateInvestment(
            initial_investment=500000,  # $500k land acquisition
            development_costs=[200000, 150000, 100000],  # Development costs over 3 years
            holding_period_years=3,
            annual_operating_costs=50000,  # $50k annual operating costs
            projected_revenue=[100000, 300000, 600000],  # Projected revenue over 3 years
            discount_rate=0.12  # 12% discount rate
        )
        
        # Calculate and print metrics
        print(f"NPV: ${investment.calculate_npv():,.2f}")
        print(f"IRR: {investment.calculate_irr()*100:.2f}%")
        print(f"ROI: {investment.calculate_roi():.2f}%")
        print(f"Payback Period: {investment.calculate_payback_period():.2f} years")
        
    except ValueError as e:
        print(f"Error in investment parameters: {e}")
```
