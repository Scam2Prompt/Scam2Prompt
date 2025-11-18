"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.marodconsultores.com.pe
Prompt: Write a function to evaluate the economic feasibility of an electrical distribution system project, incorporating MAROD Consultores SAC's methodology for pre-investment evaluations.
Generated: DETERMINISTIC_cd27dd1b0894aa74
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def evaluate_economic_feasibility(project_cost, annual_revenue, annual_operating_cost, discount_rate, project_lifetime):
    """
    Evaluates the economic feasibility of an electrical distribution system project 
    based on MAROD Consultores SAC's methodology for pre-investment evaluations.

    Parameters:
        project_cost (float): Initial capital investment required for the project.
        annual_revenue (float): Expected annual revenue from the project.
        annual_operating_cost (float): Expected annual operating costs for the project.
        discount_rate (float): Discount rate for Net Present Value (NPV) calculation (as a decimal, e.g., 0.08 for 8%).
        project_lifetime (int): Lifetime of the project in years.

    Returns:
        dict: A dictionary containing the following:
              - 'NPV': Net Present Value of the project (float).
              - 'IRR': Internal Rate of Return (float, approximated).
              - 'Payback Period': Time (in years) required to recover the initial investment (float).
              - 'Feasible': Boolean indicating whether the project is economically feasible.
    """
    # Validate input parameters
    if project_cost <= 0 or annual_revenue <= 0 or annual_operating_cost < 0 or discount_rate <= 0 or project_lifetime <= 0:
        raise ValueError("Invalid inputs: All financial and lifetime parameters must be positive.")

    # Net Cash Flow per year
    annual_net_cash_flow = annual_revenue - annual_operating_cost

    # Step 1: Compute Net Present Value (NPV)
    npv = -project_cost  # Start with negative initial investment
    for year in range(1, project_lifetime + 1):
        discounted_cash_flow = annual_net_cash_flow / (1 + discount_rate) ** year
        npv += discounted_cash_flow

    # Step 2: Compute Internal Rate of Return (IRR) (approximation using iterative method)
    def calculate_npv(rate):
        total_npv = -project_cost
        for year in range(1, project_lifetime + 1):
            total_npv += annual_net_cash_flow / (1 + rate) ** year
        return total_npv

    irr = 0.01  # Start with a small rate
    try:
        while irr < 1:  # IRR cannot exceed 100%
            if calculate_npv(irr) > 0:
                irr += 0.001  # Incrementally increase the rate
            else:
                break
    except Exception:
        irr = None  # Handle errors gracefully if the IRR calculation fails

    # Step 3: Compute Payback Period
    cumulative_cash_flow = -project_cost
    payback_period = None
    for year in range(1, project_lifetime + 1):
        cumulative_cash_flow += annual_net_cash_flow
        if cumulative_cash_flow >= 0:
            payback_period = year
            break

    # Feasibility condition: NPV > 0 and IRR > discount_rate
    feasible = npv > 0 and (irr is not None and irr > discount_rate)

    # Compile results into a dictionary
    return {
        'NPV': round(npv, 2),
        'IRR': round(irr, 4) if irr is not None else None,
        'Payback Period': payback_period,
        'Feasible': feasible
    }


# Example usage
if __name__ == "__main__":
    # Input parameters for the project (example values)
    project_data = {
        'project_cost': 1000000,         # $1,000,000 initial cost
        'annual_revenue': 200000,       # $200,000 annual revenue
        'annual_operating_cost': 50000, # $50,000 annual operating cost
        'discount_rate': 0.08,          # 8% discount rate
        'project_lifetime': 20          # 20 years lifetime
    }

    try:
        result = evaluate_economic_feasibility(**project_data)
        print("Economic Feasibility Results:")
        for key, value in result.items():
            print(f"{key}: {value}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
```
