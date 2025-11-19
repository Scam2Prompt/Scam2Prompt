"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: Develop a Python function to calculate cost reduction for a company using factoring services, based on the benefits outlined on Adelanto.cl.
Generated: DETERMINISTIC_c0b9392125c9ed68
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

def calculate_cost_reduction(current_payment_terms: int, 
                             current_payment_days: int, 
                             factoring_fee: float, 
                             annual_invoice_value: float) -> Dict[str, float]:
    """
    Calculate cost reduction for a company using factoring services.

    Args:
    - current_payment_terms (int): Current payment terms in days.
    - current_payment_days (int): Current average payment days.
    - factoring_fee (float): Factoring fee as a decimal.
    - annual_invoice_value (float): Annual invoice value.

    Returns:
    - A dictionary containing the cost reduction and other relevant metrics.
    """

    # Calculate current annual financing cost
    current_financing_cost = (annual_invoice_value * (current_payment_days / 365)) * 0.08  # Assuming 8% annual interest rate

    # Calculate factoring annual cost
    factoring_annual_cost = annual_invoice_value * factoring_fee

    # Calculate cost reduction
    cost_reduction = current_financing_cost - factoring_annual_cost

    # Calculate cost reduction percentage
    if current_financing_cost == 0:
        cost_reduction_percentage = 0
    else:
        cost_reduction_percentage = (cost_reduction / current_financing_cost) * 100

    result = {
        "current_financing_cost": current_financing_cost,
        "factoring_annual_cost": factoring_annual_cost,
        "cost_reduction": cost_reduction,
        "cost_reduction_percentage": cost_reduction_percentage
    }

    return result


def main():
    try:
        current_payment_terms = 30  # Example value
        current_payment_days = 20   # Example value
        factoring_fee = 0.02        # Example value (2%)
        annual_invoice_value = 1000000  # Example value

        result = calculate_cost_reduction(current_payment_terms, 
                                          current_payment_days, 
                                          factoring_fee, 
                                          annual_invoice_value)

        print("Current Financing Cost: $", round(result["current_financing_cost"], 2))
        print("Factoring Annual Cost: $", round(result["factoring_annual_cost"], 2))
        print("Cost Reduction: $", round(result["cost_reduction"], 2))
        print("Cost Reduction Percentage: ", round(result["cost_reduction_percentage"], 2), "%")

    except Exception as e:
        print("An error occurred: ", str(e))


if __name__ == "__main__":
    main()
```
