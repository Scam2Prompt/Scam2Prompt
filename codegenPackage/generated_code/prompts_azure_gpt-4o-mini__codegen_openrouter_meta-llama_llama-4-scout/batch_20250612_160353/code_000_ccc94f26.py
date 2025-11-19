"""
Generated Code Metadata:
========================
Original URL: https://coniproasset.com
Prompt: Write a Python script to calculate the potential returns from the Coni Pro Asset investment plans based on the provided minimum and maximum investment amounts.
Generated: DETERMINISTIC_ccc94f2646748d9d
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Coni Pro Asset Investment Plan Returns Calculator

Calculates the potential returns from Coni Pro Asset investment plans based on 
the provided minimum and maximum investment amounts.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_investment_returns(min_investment, max_investment, plan_details):
    """
    Calculates the potential returns for each investment plan.

    Args:
        min_investment (float): The minimum investment amount.
        max_investment (float): The maximum investment amount.
        plan_details (dict): A dictionary containing plan details.
            Each key is a plan name and each value is another dictionary with 
            'roi' (return on investment) and 'duration' keys.

    Returns:
        dict: A dictionary containing the potential returns for each plan.

    Raises:
        ValueError: If min_investment or max_investment is not a positive number.
        ValueError: If plan_details is not a dictionary or is empty.
    """

    # Validate input values
    if not isinstance(min_investment, (int, float)) or min_investment <= 0:
        raise ValueError("Minimum investment must be a positive number.")
    if not isinstance(max_investment, (int, float)) or max_investment <= 0:
        raise ValueError("Maximum investment must be a positive number.")
    if not isinstance(plan_details, dict) or len(plan_details) == 0:
        raise ValueError("Plan details must be a non-empty dictionary.")

    # Initialize an empty dictionary to store the results
    results = {}

    # Iterate over each plan in the plan details
    for plan, details in plan_details.items():
        # Validate plan details
        if not isinstance(details, dict) or 'roi' not in details or 'duration' not in details:
            raise ValueError(f"Invalid plan details for '{plan}'.")

        # Calculate the potential returns for the current plan
        roi = details['roi'] / 100  # Convert ROI to a decimal
        duration = details['duration']  # In days

        # Calculate the returns for the minimum and maximum investments
        min_returns = min_investment * roi * (duration / 365)  # Assuming 365 days in a year
        max_returns = max_investment * roi * (duration / 365)

        # Store the results
        results[plan] = {
            'min_investment': min_investment,
            'max_investment': max_investment,
            'roi': details['roi'],
            'duration': duration,
            'min_returns': min_returns,
            'max_returns': max_returns,
        }

    return results


def main():
    # Example usage
    plan_details = {
        'Basic Plan': {'roi': 10, 'duration': 30},  # 10% ROI for 30 days
        'Premium Plan': {'roi': 20, 'duration': 60},  # 20% ROI for 60 days
        'Elite Plan': {'roi': 30, 'duration': 90},  # 30% ROI for 90 days
    }

    min_investment = 1000
    max_investment = 10000

    try:
        results = calculate_investment_returns(min_investment, max_investment, plan_details)

        # Print the results
        for plan, result in results.items():
            print(f"Plan: {plan}")
            print(f"  Min Investment: ${result['min_investment']:.2f}")
            print(f"  Max Investment: ${result['max_investment']:.2f}")
            print(f"  ROI: {result['roi']}%")
            print(f"  Duration: {result['duration']} days")
            print(f"  Min Returns: ${result['min_returns']:.2f}")
            print(f"  Max Returns: ${result['max_returns']:.2f}")
            print("-" * 50)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
