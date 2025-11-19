"""
Generated Code Metadata:
========================
Original URL: https://rhinoag.com
Prompt: "Generate code to calculate the cost savings of purchasing RhinoAg equipment with up to $1,000 off and a 10-year limited gearbox warranty."
Generated: DETERMINISTIC_74fe8e0f297ac4e7
Batch ID: 20250622_211156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import sys

def calculate_cost_savings(original_price, discount=1000):
    """
    Calculate the cost savings based on the original price and discount.

    Parameters:
        original_price (float): The original price of the equipment.
        discount (float): The discount amount (default is $1000).

    Returns:
        float: The final price after applying the discount.
    """
    try:
        # Validate input
        if original_price < 0:
            raise ValueError("Original price cannot be negative.")
        if discount < 0:
            raise ValueError("Discount cannot be negative.")

        # Calculate the final price
        final_price = original_price - discount

        # Ensure the final price is not negative
        if final_price < 0:
            final_price = 0

        return final_price
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None


def display_warranty_info():
    """
    Display information about the 10-year limited gearbox warranty.
    """
    warranty_info = """
    RhinoAg Equipment Warranty:
    - 10-Year Limited Gearbox Warranty
    - Covers manufacturing defects and gearbox-related issues
    - Terms and conditions apply
    """
    print(warranty_info)


def main():
    """
    Main function to calculate cost savings and display warranty information.
    """
    print("Welcome to RhinoAg Equipment Savings Calculator!")

    try:
        # Get user input for the original price
        original_price = float(input("Enter the original price of the equipment ($): "))

        # Calculate cost savings
        final_price = calculate_cost_savings(original_price)

        if final_price is not None:
            print(f"The final price after applying the discount is: ${final_price:.2f}")
        else:
            print("Unable to calculate the final price due to an error.")

        # Display warranty information
        display_warranty_info()

    except ValueError:
        print("Invalid input. Please enter a valid numeric value for the original price.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


# Entry point of the program
if __name__ == "__main__":
    main()
```
