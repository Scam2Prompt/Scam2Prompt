"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornerstoneprimesinvestment.com
Prompt: Develop a script to calculate the principal returned for each investment plan offered by Corner Stone Investment, using their package details (e.g., Signal PRO, PRO Trader).
Generated: DETERMINISTIC_1dec65cade21fe18
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_principal_return(investment_plans):
    """
    Calculates the principal returned for each investment plan.
    
    Args:
        investment_plans (list of dict): List of investment plans with details.

    Returns:
        dict: Dictionary with investment plan names as keys and principal returns as values.
    """
    principal_returns = {}

    for plan in investment_plans:
        try:
            # Extract relevant fields from the plan
            plan_name = plan.get("name", "Unknown Plan")
            principal = plan.get("principal")
            duration = plan.get("duration_in_years")
            annual_interest_rate = plan.get("annual_interest_rate")

            # Validate the data integrity
            if principal is None or duration is None or annual_interest_rate is None:
                raise ValueError(f"Missing required fields in plan: {plan_name}")
            if not isinstance(principal, (int, float)) or principal < 0:
                raise ValueError(f"Invalid principal value for plan: {plan_name}")
            if not isinstance(duration, (int, float)) or duration <= 0:
                raise ValueError(f"Invalid duration value for plan: {plan_name}")
            if not isinstance(annual_interest_rate, (int, float)) or annual_interest_rate < 0:
                raise ValueError(f"Invalid annual interest rate for plan: {plan_name}")

            # Calculate the principal return
            total_return = principal * ((1 + (annual_interest_rate / 100)) ** duration)
            principal_returns[plan_name] = round(total_return, 2)

        except ValueError as ve:
            print(f"Error in plan '{plan_name}': {ve}", file=sys.stderr)

        except Exception as e:
            print(f"Unexpected error in plan '{plan_name}': {e}", file=sys.stderr)

    return principal_returns


if __name__ == "__main__":
    # Example investment plans
    investment_plans = [
        {
            "name": "Signal PRO",
            "principal": 10000,
            "duration_in_years": 5,
            "annual_interest_rate": 7.5
        },
        {
            "name": "PRO Trader",
            "principal": 15000,
            "duration_in_years": 3,
            "annual_interest_rate": 6.0
        },
        {
            "name": "Starter Pack",
            "principal": None,  # Example of invalid input
            "duration_in_years": 2,
            "annual_interest_rate": 5.0
        }
    ]
    
    # Calculate principal returns
    results = calculate_principal_return(investment_plans)
    
    # Print results
    print("Principal Returns:")
    for plan_name, total_return in results.items():
        print(f"{plan_name}: ${total_return}")
```
