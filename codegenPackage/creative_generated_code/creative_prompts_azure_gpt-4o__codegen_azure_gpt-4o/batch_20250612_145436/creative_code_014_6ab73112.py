"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dotcomachinery.co.tz
Prompt: Generate a script to calculate discounts for promotional items like the PALLET STACKER JECK 1.5TON, as described on Dotcom Machinery's website.
Generated: DETERMINISTIC_6ab73112b6e5daaf
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_discount(item_name, original_price, discount_percentage):
    """
    Calculate the discounted price for a given item.

    Args:
        item_name (str): Name of the item.
        original_price (float): Original price of the item in dollars.
        discount_percentage (float): Discount percentage to be applied.

    Returns:
        dict: A dictionary containing item details and calculated prices.
    """
    try:
        # Validate inputs
        if original_price < 0:
            raise ValueError("Original price cannot be negative.")
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")

        # Calculate discounted price
        discount_amount = (original_price * discount_percentage) / 100
        discounted_price = original_price - discount_amount

        # Return result as a dictionary
        return {
            "item_name": item_name,
            "original_price": round(original_price, 2),
            "discount_percentage": round(discount_percentage, 2),
            "discount_amount": round(discount_amount, 2),
            "discounted_price": round(discounted_price, 2),
        }
    except ValueError as ve:
        return {"error": str(ve)}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}


def main():
    """
    Main function to handle user inputs and display the discount calculation.
    """
    print("** Discount Calculator **")

    try:
        # Gather user inputs
        item_name = input("Enter the item name: ").strip()
        if not item_name:
            raise ValueError("Item name cannot be empty.")

        original_price = float(input("Enter the original price of the item (in dollars): ").strip())
        discount_percentage = float(input("Enter the discount percentage: ").strip())

        # Calculate discount
        result = calculate_discount(item_name, original_price, discount_percentage)

        # Check for errors in the result
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            # Print the results
            print("\n** Discount Details **")
            print(f"Item Name: {result['item_name']}")
            print(f"Original Price: ${result['original_price']:.2f}")
            print(f"Discount Percentage: {result['discount_percentage']:.2f}%")
            print(f"Discount Amount: ${result['discount_amount']:.2f}")
            print(f"Discounted Price: ${result['discounted_price']:.2f}")

    except ValueError as ve:
        print(f"Input Error: {str(ve)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
    finally:
        print("\nThank you for using the Discount Calculator!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user. Exiting...")
        sys.exit(0)
```
