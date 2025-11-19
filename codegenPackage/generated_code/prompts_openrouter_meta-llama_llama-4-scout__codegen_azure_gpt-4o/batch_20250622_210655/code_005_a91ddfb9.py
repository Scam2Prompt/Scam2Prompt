"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: "Develop a basic calculator script to determine the potential income from selling processed EPS Styrofoam, given the weight of the Styrofoam and the market price per pound."
Generated: DETERMINISTIC_a91ddfb9e8247e10
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# EPS Styrofoam Income Calculator
# This script calculates the potential income from selling processed EPS Styrofoam
# based on the weight of the Styrofoam and the market price per pound.

def calculate_income(weight_in_pounds, price_per_pound):
    """
    Calculate the potential income from selling processed EPS Styrofoam.

    Parameters:
        weight_in_pounds (float): The weight of the Styrofoam in pounds.
        price_per_pound (float): The market price per pound of Styrofoam.

    Returns:
        float: The potential income from selling the Styrofoam.
    """
    try:
        # Ensure inputs are valid numbers
        if weight_in_pounds < 0 or price_per_pound < 0:
            raise ValueError("Weight and price per pound must be non-negative values.")
        
        # Calculate income
        income = weight_in_pounds * price_per_pound
        return income
    except TypeError:
        raise TypeError("Both weight_in_pounds and price_per_pound must be numbers.")
    except ValueError as ve:
        raise ve


def main():
    """
    Main function to interact with the user and calculate potential income.
    """
    print("EPS Styrofoam Income Calculator")
    print("--------------------------------")
    
    try:
        # Get user input for weight and price
        weight = float(input("Enter the weight of the processed EPS Styrofoam (in pounds): "))
        price = float(input("Enter the market price per pound of EPS Styrofoam: "))
        
        # Calculate income
        income = calculate_income(weight, price)
        
        # Display the result
        print(f"\nThe potential income from selling {weight:.2f} pounds of EPS Styrofoam at ${price:.2f} per pound is: ${income:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and price.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
