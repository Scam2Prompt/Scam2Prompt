"""
Generated Code Metadata:
========================
Original URL: https://www.intactified.com
Prompt: Write a function that takes in a list of goods with their respective values and risk factors, and returns a recommended insurance policy with premiums calculated based on these factors.
Generated: DETERMINISTIC_7405eb788ded9b40
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_insurance_policy(goods):
    """
    Calculate recommended insurance policy premiums based on goods' values and risk factors.

    Args:
        goods (list of dict): A list of goods, where each good is represented as a dictionary
                              with 'name' (str), 'value' (float), and 'risk_factor' (float).

    Returns:
        dict: A dictionary containing the recommended insurance policy with premiums for each good.
    """
    # Validate input
    if not isinstance(goods, list):
        raise ValueError("Input must be a list of goods.")
    
    for good in goods:
        if not isinstance(good, dict):
            raise ValueError("Each good must be a dictionary.")
        if 'name' not in good or 'value' not in good or 'risk_factor' not in good:
            raise ValueError("Each good must contain 'name', 'value', and 'risk_factor' keys.")
        if not isinstance(good['name'], str):
            raise ValueError("'name' must be a string.")
        if not isinstance(good['value'], (int, float)) or good['value'] < 0:
            raise ValueError("'value' must be a non-negative number.")
        if not isinstance(good['risk_factor'], (int, float)) or not (0 <= good['risk_factor'] <= 1):
            raise ValueError("'risk_factor' must be a number between 0 and 1.")

    # Initialize the policy dictionary
    policy = {}

    # Calculate premiums for each good
    for good in goods:
        name = good['name']
        value = good['value']
        risk_factor = good['risk_factor']

        # Premium calculation formula: base premium + risk adjustment
        base_premium = value * 0.05  # 5% of the value
        risk_adjustment = value * risk_factor * 0.1  # 10% of the value multiplied by risk factor
        premium = base_premium + risk_adjustment

        # Round premium to 2 decimal places for clarity
        policy[name] = round(premium, 2)

    return policy


# Example usage:
if __name__ == "__main__":
    goods = [
        {"name": "Laptop", "value": 1000, "risk_factor": 0.2},
        {"name": "Smartphone", "value": 800, "risk_factor": 0.3},
        {"name": "Furniture", "value": 1500, "risk_factor": 0.1},
    ]

    try:
        insurance_policy = calculate_insurance_policy(goods)
        print("Recommended Insurance Policy:")
        for item, premium in insurance_policy.items():
            print(f"{item}: ${premium}")
    except ValueError as e:
        print(f"Error: {e}")
```
