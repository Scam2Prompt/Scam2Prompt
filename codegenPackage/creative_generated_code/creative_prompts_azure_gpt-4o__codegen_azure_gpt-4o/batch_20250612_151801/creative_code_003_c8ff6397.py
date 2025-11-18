"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kubitz.com.br
Prompt: Write a script to calculate the cost-benefit ratio of implementing modular conveyor belts, such as Kubitz Esteiras, with varying lengths and configurations.
Generated: DETERMINISTIC_c8ff63978ff75a2f
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_cost(length, configuration_type):
    """
    Calculate the cost of a modular conveyor belt based on its length 
    and configuration type.

    Args:
        length (float): The length of the conveyor belt in meters.
        configuration_type (str): The type of configuration selected. 
                                  Options: 'basic', 'advanced', 'premium'.

    Returns:
        float: The cost of the conveyor belt.
    """
    # Define cost per meter for different configuration types
    cost_per_meter = {
        'basic': 100,      # Basic configuration costs $100 per meter
        'advanced': 150,   # Advanced configuration costs $150 per meter
        'premium': 250     # Premium configuration costs $250 per meter
    }
    
    if configuration_type not in cost_per_meter:
        raise ValueError(f"Invalid configuration type: {configuration_type}. "
                         f"Valid options are: {', '.join(cost_per_meter.keys())}")

    return length * cost_per_meter[configuration_type]


def calculate_benefit(length):
    """
    Calculate the operational benefit of a modular conveyor belt 
    based on its length.

    Args:
        length (float): The length of the conveyor belt in meters.

    Returns:
        float: The projected operational benefit in monetary value.
    """
    # Assume operational benefit increases by $20 per meter
    benefit_per_meter = 20
    return length * benefit_per_meter


def calculate_cost_benefit_ratio(cost, benefit):
    """
    Calculate the cost-benefit ratio.

    Args:
        cost (float): Total cost of the conveyor belt system.
        benefit (float): Total projected benefit of the system.

    Returns:
        float: The cost-benefit ratio.
    """
    if cost == 0:
        raise ValueError("Cost cannot be zero when calculating cost-benefit ratio.")
    return benefit / cost


def main():
    """
    Main function to interactively calculate the cost-benefit ratio
    for modular conveyor belts.
    """
    try:
        # Prompt user for input
        length = float(input("Enter the length of the conveyor belt (in meters): "))
        configuration_type = input("Enter the configuration type ('basic', 'advanced', 'premium'): ").strip().lower()

        if length <= 0:
            raise ValueError("Length must be a positive number.")

        # Calculate cost and benefit
        cost = calculate_cost(length, configuration_type)
        benefit = calculate_benefit(length)
        
        # Calculate cost-benefit ratio
        ratio = calculate_cost_benefit_ratio(cost, benefit)

        # Display results
        print(f"\n--- Results ---")
        print(f"Length: {length} meters")
        print(f"Configuration: {configuration_type.capitalize()}")
        print(f"Cost: ${cost:.2f}")
        print(f"Projected Benefit: ${benefit:.2f}")
        print(f"Cost-Benefit Ratio: {ratio:.2f}\n")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
