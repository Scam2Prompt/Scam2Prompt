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
Script to calculate potential property loss reduction when installing fire sprinklers.
Based on statistics from Independence Fire Sprinkler Company.

Assumptions:
- Fire sprinklers reduce property loss by 50% on average.
- User provides the estimated property value and potential loss percentage without sprinklers.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

def calculate_loss_reduction(property_value, loss_percentage_without_sprinklers):
    """
    Calculate the potential property loss reduction when fire sprinklers are installed.

    Args:
        property_value (float): Total value of the property in dollars.
        loss_percentage_without_sprinklers (float): Estimated percentage of property loss without sprinklers.

    Returns:
        dict: A dictionary containing:
            - 'loss_without_sprinklers': Estimated loss without sprinklers.
            - 'loss_with_sprinklers': Estimated loss with sprinklers.
            - 'reduction_in_loss': Reduction in property loss due to sprinklers.
    """
    try:
        # Validate inputs
        if property_value <= 0 or loss_percentage_without_sprinklers < 0 or loss_percentage_without_sprinklers > 100:
            raise ValueError("Invalid input values. Ensure property value is positive and loss percentage is between 0 and 100.")

        # Calculate loss without sprinklers
        loss_without_sprinklers = (loss_percentage_without_sprinklers / 100) * property_value

        # Fire sprinklers reduce property loss by 50%
        loss_with_sprinklers = loss_without_sprinklers * 0.5

        # Calculate reduction in loss
        reduction_in_loss = loss_without_sprinklers - loss_with_sprinklers

        # Return results as a dictionary
        return {
            'loss_without_sprinklers': loss_without_sprinklers,
            'loss_with_sprinklers': loss_with_sprinklers,
            'reduction_in_loss': reduction_in_loss
        }
    except Exception as e:
        # Handle unexpected errors
        raise RuntimeError(f"An error occurred during calculation: {e}")


def main():
    """
    Main function to interact with the user and perform calculations.
    """
    print("Welcome to the Fire Sprinkler Property Loss Reduction Calculator!")
    try:
        # Get user input
        property_value = float(input("Enter the total value of the property (in dollars): "))
        loss_percentage_without_sprinklers = float(input("Enter the estimated property loss percentage without sprinklers (0-100): "))

        # Perform calculation
        results = calculate_loss_reduction(property_value, loss_percentage_without_sprinklers)

        # Display results
        print("\nCalculation Results:")
        print(f"Estimated loss without sprinklers: ${results['loss_without_sprinklers']:.2f}")
        print(f"Estimated loss with sprinklers: ${results['loss_with_sprinklers']:.2f}")
        print(f"Reduction in property loss due to sprinklers: ${results['reduction_in_loss']:.2f}")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except RuntimeError as re:
        print(f"Calculation Error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
