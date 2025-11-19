"""
Generated Code Metadata:
========================
Original URL: https://immediate-orbirex.org
Prompt: Develop a Python script to calculate key investment metrics, such as return on investment (ROI), net present value (NPV), and internal rate of return (IRR), for a given investment opportunity.
Generated: DETERMINISTIC_d03f333a41d40ba3
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.optimize import fsolve

def calculate_roi(cost, gain):
    """
    Calculate the return on investment (ROI).

    Args:
        cost (float): The cost of the investment.
        gain (float): The gain from the investment.

    Returns:
        float: The ROI as a decimal value.

    Raises:
        ValueError: If the cost is zero or negative.
    """
    if cost <= 0:
        raise ValueError("Cost must be greater than zero.")
    return (gain - cost) / cost


def calculate_npv(rate, cash_flow, time):
    """
    Calculate the net present value (NPV).

    Args:
        rate (float): The discount rate.
        cash_flow (list[float]): A list of cash flows.
        time (list[int]): A list of time periods corresponding to the cash flows.

    Returns:
        float: The NPV.

    Raises:
        ValueError: If the lengths of cash_flow and time do not match.
    """
    if len(cash_flow) != len(time):
        raise ValueError("Cash flow and time must have the same length.")
    npv = 0
    for i in range(len(cash_flow)):
        npv += cash_flow[i] / (1 + rate) ** time[i]
    return npv


def calculate_irr(cash_flow, initial_guess=0.1):
    """
    Calculate the internal rate of return (IRR).

    Args:
        cash_flow (list[float]): A list of cash flows.
        initial_guess (float, optional): The initial guess for the IRR. Defaults to 0.1.

    Returns:
        float: The IRR.

    Raises:
        ValueError: If the cash flow list is empty.
    """
    if not cash_flow:
        raise ValueError("Cash flow must not be empty.")

    def npv(rate):
        return calculate_npv(rate, cash_flow, list(range(len(cash_flow))))

    try:
        irr = fsolve(npv, initial_guess)[0]
    except RuntimeError:
        raise ValueError("Failed to converge to a solution.")
    return irr


def main():
    try:
        # Example usage
        investment_cost = 10000
        investment_gain = 12000
        roi = calculate_roi(investment_cost, investment_gain)
        print(f"Return on Investment (ROI): {roi * 100:.2f}%")

        cash_flow = [-10000, 3000, 4000, 5000]
        time = [0, 1, 2, 3]
        discount_rate = 0.05
        npv = calculate_npv(discount_rate, cash_flow, time)
        print(f"Net Present Value (NPV) at {discount_rate * 100:.2f}% discount rate: ${npv:.2f}")

        irr = calculate_irr(cash_flow)
        print(f"Internal Rate of Return (IRR): {irr * 100:.2f}%")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
