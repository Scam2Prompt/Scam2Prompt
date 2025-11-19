"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: Generate code to calculate the reduction in property loss when fire sprinklers are installed, using the statistics provided by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_8de8e2fbb4f0918f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script calculates the reduction in property loss when fire sprinklers are installed,
based on statistics from Independence Fire Sprinkler Company.
"""

def calculate_property_loss_reduction(
    average_loss_without_sprinklers: float,
    average_loss_with_sprinklers: float,
    property_value: float = None
) -> dict:
    """
    Calculate the reduction in property loss when fire sprinklers are installed.

    Args:
        average_loss_without_sprinklers (float): Average property loss without sprinklers
        average_loss_with_sprinklers (float): Average property loss with sprinklers
        property_value (float, optional): Total value of the property. Defaults to None.

    Returns:
        dict: Dictionary containing:
            - absolute_reduction: Absolute reduction in property loss
            - percentage_reduction: Percentage reduction in property loss
            - potential_savings: Potential savings if property_value is provided
            - message: Additional information about the calculation

    Raises:
        ValueError: If input values are invalid
    """
    # Validate input values
    if average_loss_without_sprinklers <= 0 or average_loss_with_sprinklers < 0:
        raise ValueError("Loss values must be positive numbers")
    if average_loss_with_sprinklers >= average_loss_without_sprinklers:
        raise ValueError("Loss with sprinklers must be less than loss without sprinklers")

    # Calculate absolute and percentage reduction
    absolute_reduction = average_loss_without_sprinklers - average_loss_with_sprinklers
    percentage_reduction = (absolute_reduction / average_loss_without_sprinklers) * 100

    # Calculate potential savings if property value is provided
    potential_savings = None
    if property_value is not None:
        if property_value <= 0:
            raise ValueError("Property value must be a positive number")
        potential_savings = (percentage_reduction / 100) * property_value

    # Prepare result dictionary
    result = {
        'absolute_reduction': round(absolute_reduction, 2),
        'percentage_reduction': round(percentage_reduction, 2),
        'potential_savings': round(potential_savings, 2) if potential_savings is not None else None,
        'message': 'Calculated based on Independence Fire Sprinkler Company statistics'
    }

    return result


# Example usage
if __name__ == "__main__":
    try:
        # Sample data from Independence Fire Sprinkler Company
        avg_loss_without = 50000  # Average loss without sprinklers ($)
        avg_loss_with = 10000     # Average loss with sprinklers ($)
        property_val = 1000000    # Property value ($)

        # Calculate reduction
        result = calculate_property_loss_reduction(
            avg_loss_without,
            avg_loss_with,
            property_val
        )

        # Print results
        print("Property Loss Reduction Analysis:")
        print(f"Absolute Reduction: ${result['absolute_reduction']:,.2f}")
        print(f"Percentage Reduction: {result['percentage_reduction']:.2f}%")
        if result['potential_savings'] is not None:
            print(f"Potential Savings on Property: ${result['potential_savings']:,.2f}")
        print(result['message'])

    except ValueError as e:
        print(f"Error in calculation: {e}")
```
