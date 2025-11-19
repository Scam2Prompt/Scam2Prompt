"""
Generated Code Metadata:
========================
Original URL: https://blendbit.org
Prompt: Develop a function that calculates the potential savings from using non-public tariffs compared to standard rates offered by mobile operators.
Generated: DETERMINISTIC_f2598af854f719e3
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List

def calculate_potential_savings(
    standard_rates: Dict[str, float], 
    non_public_tariffs: Dict[str, float], 
    usage: Dict[str, int]
) -> float:
    """
    Calculate the potential savings from using non-public tariffs compared to standard rates.

    Args:
    - standard_rates (Dict[str, float]): A dictionary of standard rates offered by mobile operators.
    - non_public_tariffs (Dict[str, float]): A dictionary of non-public tariffs.
    - usage (Dict[str, int]): A dictionary of usage for each service.

    Returns:
    - float: The potential savings.

    Raises:
    - ValueError: If the input dictionaries do not have the same keys.
    """

    # Check if the input dictionaries have the same keys
    if set(standard_rates.keys()) != set(non_public_tariffs.keys()) or set(standard_rates.keys()) != set(usage.keys()):
        raise ValueError("Input dictionaries must have the same keys")

    # Initialize the total cost with standard rates and non-public tariffs
    total_standard_cost = 0
    total_non_public_cost = 0

    # Calculate the total cost for standard rates and non-public tariffs
    for service, rate in standard_rates.items():
        usage_quantity = usage[service]
        total_standard_cost += rate * usage_quantity

    for service, rate in non_public_tariffs.items():
        usage_quantity = usage[service]
        total_non_public_cost += rate * usage_quantity

    # Calculate the potential savings
    potential_savings = total_standard_cost - total_non_public_cost

    # Return the potential savings if it's positive, otherwise return 0
    return max(potential_savings, 0)


def main():
    # Example usage
    standard_rates = {
        "voice": 0.20,
        "sms": 0.10,
        "data": 0.05
    }

    non_public_tariffs = {
        "voice": 0.15,
        "sms": 0.05,
        "data": 0.03
    }

    usage = {
        "voice": 100,
        "sms": 50,
        "data": 1000
    }

    try:
        potential_savings = calculate_potential_savings(standard_rates, non_public_tariffs, usage)
        print(f"The potential savings is: ${potential_savings:.2f}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
