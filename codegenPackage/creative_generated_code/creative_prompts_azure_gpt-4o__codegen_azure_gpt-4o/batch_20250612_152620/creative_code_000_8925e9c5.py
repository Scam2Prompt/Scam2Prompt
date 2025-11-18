"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adygeya.propiski-net.ru
Prompt: Write a Python script to calculate the cost of temporary registration in Adygea based on the pricing details provided on the website, including discounts for minors.
Generated: DETERMINISTIC_8925e9c508c80ecb
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the cost of temporary registration in Adygea based on pricing details and discounts for minors.
"""

# Import necessary libraries
import sys

def calculate_registration_cost(age: int, base_cost: float, minor_discount: float) -> float:
    """
    Calculate the cost of temporary registration based on age and pricing details.

    Parameters:
        age (int): Age of the person registering.
        base_cost (float): The standard cost of registration.
        minor_discount (float): Discount percentage for minors (0-18 years).

    Returns:
        float: The final cost of registration.
    """
    try:
        # Validate input
        if age < 0 or base_cost < 0 or minor_discount < 0 or minor_discount > 100:
            raise ValueError("Invalid input values provided.")
        
        # Apply discount if the person is a minor
        if age < 18:
            final_cost = base_cost * (1 - minor_discount / 100)
        else:
            final_cost = base_cost
        
        return round(final_cost, 2)
    except Exception as e:
        print(f"Error calculating registration cost: {e}", file=sys.stderr)
        return None

def main():
    """
    Main function to handle user input and calculate registration cost.
    """
    try:
        # Prompt user for inputs
        print("Welcome to the Adygea Temporary Registration Cost Calculator!")
        age = int(input("Please enter the age of the person registering: "))
        base_cost = float(input("Please enter the base cost of registration: "))
        minor_discount = float(input("Please enter the discount percentage for minors: "))

        # Calculate the cost
        cost = calculate_registration_cost(age, base_cost, minor_discount)

        if cost is not None:
            print(f"The final cost of registration is: {cost} RUB")
        else:
            print("Failed to calculate registration cost due to invalid input.")
    except ValueError:
        print("Error: Invalid input. Please provide numeric values for age, base cost, and discount.", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
