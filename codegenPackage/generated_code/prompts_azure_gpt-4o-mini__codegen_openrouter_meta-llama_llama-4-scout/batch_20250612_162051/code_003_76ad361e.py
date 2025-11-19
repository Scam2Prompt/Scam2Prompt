"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: Write a Python script that calculates the potential property loss reduction when installing fire sprinklers, based on statistics from Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_76ad361edb0369b8
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculates the potential property loss reduction when installing fire sprinklers.

Based on statistics from Independence Fire Sprinkler Company.
"""

import argparse

def calculate_loss_reduction(property_value, sprinkler_efficacy=0.97, fire_risk=0.05):
    """
    Calculates the potential property loss reduction.

    Args:
        property_value (float): The value of the property.
        sprinkler_efficacy (float, optional): The efficacy of the fire sprinkler system. Defaults to 0.97.
        fire_risk (float, optional): The risk of a fire occurring. Defaults to 0.05.

    Returns:
        float: The potential property loss reduction.
    """
    # Calculate the expected loss without sprinklers
    expected_loss_without_sprinklers = property_value * fire_risk * (1 - 0)

    # Calculate the expected loss with sprinklers
    expected_loss_with_sprinklers = property_value * fire_risk * (1 - sprinkler_efficacy)

    # Calculate the loss reduction
    loss_reduction = expected_loss_without_sprinklers - expected_loss_with_sprinklers

    return loss_reduction

def main():
    parser = argparse.ArgumentParser(description='Calculate potential property loss reduction')
    parser.add_argument('--property_value', type=float, required=True, help='The value of the property')
    parser.add_argument('--sprinkler_efficacy', type=float, default=0.97, help='The efficacy of the fire sprinkler system')
    parser.add_argument('--fire_risk', type=float, default=0.05, help='The risk of a fire occurring')

    args = parser.parse_args()

    try:
        loss_reduction = calculate_loss_reduction(args.property_value, args.sprinkler_efficacy, args.fire_risk)
        print(f'The potential property loss reduction is: ${loss_reduction:.2f}')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    main()
```
