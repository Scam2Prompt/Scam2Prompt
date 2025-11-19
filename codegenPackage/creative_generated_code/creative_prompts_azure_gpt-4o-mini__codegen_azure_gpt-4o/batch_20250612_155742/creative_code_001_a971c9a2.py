"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcsprayfoamsolutions.com
Prompt: Write a Python script that calculates potential energy savings from installing commercial spray foam insulation based on user input for building size and energy costs.
Generated: DETERMINISTIC_a971c9a2b70b80dc
Batch ID: 20250612_155742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import sys

def calculate_energy_savings(building_size, energy_cost):
    """
    Calculate potential energy savings from installing spray foam insulation.

    Parameters:
    building_size (float): The size of the building in square feet.
    energy_cost (float): The monthly energy cost in dollars.

    Returns:
    float: Estimated monthly energy savings in dollars.
    """
    # Assumed energy savings factor (percentage reduction)
    savings_factor = 0.25  # 25% energy savings

    # Calculate potential savings
    potential_savings = energy_cost * savings_factor

    return potential_savings


def get_user_input(prompt, cast_type=float):
    """
    Get user input and convert it to the specified type.

    Parameters:
    prompt (str): The input prompt message.
    cast_type (type): The type to cast the input to (default is float).

    Returns:
    cast_type: User input cast to the specified type.

    Raises:
    ValueError: If the input cannot be cast to the specified type.
    """
    try:
        user_input = cast_type(input(prompt))
        if user_input <= 0:
            raise ValueError("Input must be a positive number.")
        return user_input
    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)


def main():
    """
    Main function to execute the script.
    Handles user input, calculates energy savings, and displays the result.
    """
    print("Commercial Spray Foam Insulation Savings Calculator")
    print("=" * 50)

    # Get user input for building size and energy costs
    building_size = get_user_input("Enter building size in square feet: ", float)
    energy_cost = get_user_input("Enter monthly energy cost in dollars: ", float)

    # Calculate potential energy savings
    savings = calculate_energy_savings(building_size, energy_cost)

    # Display the result
    print(f"\nFor a building of size {building_size} sq ft with monthly energy costs of ${energy_cost},")
    print(f"the estimated monthly energy savings from installing spray foam insulation is: ${savings:.2f}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
