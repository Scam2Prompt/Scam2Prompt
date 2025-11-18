"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://groundcell.uk.com
Prompt: Generate a script that automates the selection of the appropriate Groundcell product (EC100, EC150, EC200) based on slope gradient and soil type, referencing the installation guidelines from Groundcell's website.
Generated: DETERMINISTIC_c5aa297f852daa27
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Groundcell Product Selection Script
# This script selects the appropriate Groundcell product (EC100, EC150, EC200)
# based on slope gradient and soil type as per installation guidelines.

# Import necessary modules
import sys

# Define a function to validate user input
def validate_input(prompt, valid_values):
    """
    Validates user input against a list of valid values.
    Args:
        prompt (str): The message displayed to the user.
        valid_values (list): List of valid input values.
    Returns:
        str: Valid user input.
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_values:
            return user_input
        print(f"Invalid input. Please enter one of the following: {', '.join(valid_values)}")

# Define a function to determine the appropriate product
def select_groundcell_product(slope_gradient, soil_type):
    """
    Determines the appropriate Groundcell product based on slope gradient and soil type.
    Args:
        slope_gradient (float): Slope gradient as a percentage.
        soil_type (str): Type of soil (e.g., clay, sandy, loam).
    Returns:
        str: Recommended Groundcell product.
    """
    if slope_gradient < 15:
        if soil_type == 'clay':
            return 'EC100'
        elif soil_type == 'sandy':
            return 'EC150'
        elif soil_type == 'loam':
            return 'EC100'
    elif 15 <= slope_gradient <= 25:
        if soil_type == 'clay':
            return 'EC150'
        elif soil_type == 'sandy':
            return 'EC200'
        elif soil_type == 'loam':
            return 'EC150'
    elif slope_gradient > 25:
        return 'EC200'
    else:
        return 'Unknown'

# Main script execution
def main():
    """
    Main function to execute the Groundcell product selection script.
    Prompts the user for slope gradient and soil type, then outputs the recommended product.
    """
    print("Welcome to the Groundcell Product Selector!")
    print("Please provide the following information to determine the appropriate product.")

    try:
        # Get and validate slope gradient input
        slope_gradient = float(input("Enter the slope gradient (as a percentage, e.g., 10, 20): "))
        if slope_gradient < 0:
            raise ValueError("Slope gradient cannot be negative.")

        # Get and validate soil type input
        soil_type = validate_input(
            "Enter the soil type (clay, sandy, loam): ",
            valid_values=['clay', 'sandy', 'loam']
        )

        # Determine the recommended product
        recommended_product = select_groundcell_product(slope_gradient, soil_type)

        # Display the result
        print(f"Based on the slope gradient ({slope_gradient}%) and soil type ({soil_type}), "
              f"the recommended Groundcell product is: {recommended_product}")

    except ValueError as ve:
        print(f"Error: {ve}. Please provide valid input.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Entry point for the script
if __name__ == "__main__":
    main()
```
