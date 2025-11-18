"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alghanim-capital.com
Prompt: Write a function to calculate returns on private equity investments, incorporating strategic planning and prudent investment management principles as highlighted by Alghanim Capital.
Generated: DETERMINISTIC_7b299feb2e27fa59
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import numpy as np

def calculate_pe_returns(initial_investment, cash_flows, discount_rate):
    """
    Calculate the internal rate of return (IRR) and net present value (NPV) 
    of private equity investments based on prudent investment management principles.

    Parameters:
    initial_investment (float): The initial investment amount (negative value for cash outflow).
    cash_flows (list of floats): List of annual cash inflows or outflows from the investment.
    discount_rate (float): The discount rate (expressed as a decimal, e.g., 0.1 for 10%).

    Returns:
    dict: A dictionary containing the calculated IRR and NPV of the investment.
    """
    try:
        # Validate inputs
        if not isinstance(initial_investment, (int, float)) or initial_investment >= 0:
            raise ValueError("Initial investment must be a negative float or integer (cash outflow).")
        if not isinstance(cash_flows, list) or not all(isinstance(cf, (int, float)) for cf in cash_flows):
            raise ValueError("Cash flows must be a list of floats or integers.")
        if not isinstance(discount_rate, (int, float)) or discount_rate < 0 or discount_rate > 1:
            raise ValueError("Discount rate must be a float between 0 and 1.")
        
        # Combine initial investment and cash flows into a single list
        cash_flow_series = [initial_investment] + cash_flows

        # Calculate Internal Rate of Return (IRR)
        irr = np.irr(cash_flow_series)

        # Calculate Net Present Value (NPV)
        npv = np.npv(discount_rate, cash_flow_series)

        # Return results in a dictionary
        return {
            "IRR": irr,
            "NPV": npv
        }

    except Exception as e:
        # Handle any unexpected errors
        return {
            "error": str(e)
        }

# Example usage
if __name__ == "__main__":
    # Test data
    initial_investment = -1000000  # $1,000,000 investment (cash outflow)
    cash_flows = [200000, 300000, 500000, 600000, 800000]  # Cash inflows over 5 years
    discount_rate = 0.1  # 10% discount rate

    # Calculate returns
    result = calculate_pe_returns(initial_investment, cash_flows, discount_rate)

    # Display results
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"Internal Rate of Return (IRR): {result['IRR']:.2%}")
        print(f"Net Present Value (NPV): ${result['NPV']:.2f}")
```
