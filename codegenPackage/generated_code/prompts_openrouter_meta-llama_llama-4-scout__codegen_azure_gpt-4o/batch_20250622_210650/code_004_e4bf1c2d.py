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

# Define the financial model for solar panel investment
def solar_panel_financial_model(initial_investment, annual_savings, lifespan_years, discount_rate):
    """
    Evaluates the feasibility of investing in a solar panel system.
    
    Parameters:
        initial_investment (float): The upfront cost of the solar panel system.
        annual_savings (float): The yearly savings from reduced energy costs.
        lifespan_years (int): The expected lifespan of the solar panel system in years.
        discount_rate (float): The discount rate for NPV calculation (as a decimal, e.g., 0.05 for 5%).

    Returns:
        dict: A dictionary containing payback period, ROI, and NPV.
    """
    # Initialize variables
    cash_flows = [-initial_investment]  # Year 0 cash flow (negative due to investment)
    for year in range(1, lifespan_years + 1):
        cash_flows.append(annual_savings)  # Positive cash flows for each year

    # Calculate Payback Period
    cumulative_cash_flow = 0
    payback_period = None
    for year, cash_flow in enumerate(cash_flows):
        cumulative_cash_flow += cash_flow
        if cumulative_cash_flow >= 0:
            payback_period = year
            break

    # Calculate ROI (Return on Investment)
    total_savings = sum(cash_flows[1:])  # Exclude initial investment
    roi = (total_savings - initial_investment) / initial_investment * 100  # ROI as a percentage

    # Calculate NPV (Net Present Value)
    npv = sum(cash_flow / (1 + discount_rate) ** year for year, cash_flow in enumerate(cash_flows))

    # Return results
    return {
        "Payback Period (years)": payback_period,
        "ROI (%)": roi,
        "NPV ($)": npv
    }

# Example usage
if __name__ == "__main__":
    # Input parameters
    initial_investment = 20000  # Example: $20,000 upfront cost
    annual_savings = 3000       # Example: $3,000 annual savings
    lifespan_years = 25         # Example: 25 years lifespan
    discount_rate = 0.05        # Example: 5% discount rate

    # Run the financial model
    results = solar_panel_financial_model(initial_investment, annual_savings, lifespan_years, discount_rate)

    # Display results
    print("Solar Panel Investment Financial Model Results:")
    for key, value in results.items():
        print(f"{key}: {value}")
```

This Python script calculates the payback period, ROI, and NPV for a solar panel investment. It is designed to be run in a Python environment and outputs the results to the console.
