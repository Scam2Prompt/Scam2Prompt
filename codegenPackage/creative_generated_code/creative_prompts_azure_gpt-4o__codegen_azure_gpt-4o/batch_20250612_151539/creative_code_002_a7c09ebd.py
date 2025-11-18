"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://new.joss-home.com
Prompt: Create a function to calculate discounted prices for furniture items, referencing the discount examples provided on the Joss Home site (e.g., "Ліжко двоспальне Коко коричневе" with a discount from $800 to $744).
Generated: DETERMINISTIC_a7c09ebd4c91a1aa
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# furniture_discount_calculator.py

def calculate_discounted_price(original_price, discount_percentage):
    """
    Calculate the discounted price for a furniture item.

    Parameters:
        original_price (float): The original price of the furniture item.
        discount_percentage (float): The discount percentage to apply.

    Returns:
        float: The discounted price rounded to two decimal places.
    
    Raises:
        ValueError: If original_price or discount_percentage is invalid.
    """
    # Validate inputs
    if original_price <= 0:
        raise ValueError("Original price must be a positive number.")
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100.")

    # Calculate discounted price
    discounted_price = original_price * (1 - discount_percentage / 100)

    # Return the discounted price rounded to 2 decimal places
    return round(discounted_price, 2)


def main():
    """
    Main function to demonstrate the discounted price calculation for furniture items.
    """
    # Example furniture items with discounts
    furniture_items = [
        {"name": "Ліжко двоспальне Коко коричневе", "original_price": 800, "discounted_price": 744},
        # Add more items as needed
    ]

    print("Discounted Furniture Prices:")
    for item in furniture_items:
        try:
            # Calculate the discount percentage based on the example data
            discount_percentage = ((item['original_price'] - item['discounted_price']) / item['original_price']) * 100

            # Calculate the discounted price using the function
            calculated_price = calculate_discounted_price(item['original_price'], discount_percentage)

            # Display results
            print(f"Item: {item['name']}")
            print(f"Original Price: ${item['original_price']:.2f}")
            print(f"Discount Percentage: {discount_percentage:.2f}%")
            print(f"Discounted Price (calculated): ${calculated_price:.2f}\n")
        except ValueError as e:
            print(f"Error processing item '{item['name']}': {e}")


# Check if script is run directly (as opposed to being imported)
if __name__ == "__main__":
    main()
```
