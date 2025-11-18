"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingroofing.com
Prompt: Write code to implement a discount system for veterans, applying King Roofing's specific discount percentages for repairs and replacements.
Generated: DETERMINISTIC_2946b1a153569128
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Discount System for Veterans - King Roofing Company
# This script calculates discounts for veterans based on specific percentages for repairs and replacements.

def calculate_discount(service_type, original_price, is_veteran):
    """
    Calculate the total price after applying discounts for veterans.

    Args:
        service_type (str): The type of service ('repair' or 'replacement').
        original_price (float): The original price of the service.
        is_veteran (bool): Whether the customer is a veteran.

    Returns:
        float: The final price after applying the discount.
    """
    # Validate input
    if service_type not in ['repair', 'replacement']:
        raise ValueError("Invalid service type. Must be 'repair' or 'replacement'.")
    if original_price < 0:
        raise ValueError("Original price must be a non-negative number.")
    
    # Discount percentages for veterans
    repair_discount = 0.15  # 15% discount for repairs
    replacement_discount = 0.20  # 20% discount for replacements

    # Calculate discount
    if is_veteran:
        if service_type == 'repair':
            discount = original_price * repair_discount
        elif service_type == 'replacement':
            discount = original_price * replacement_discount
    else:
        discount = 0  # No discount for non-veterans

    # Calculate final price
    final_price = original_price - discount
    return round(final_price, 2)  # Round to 2 decimal places for currency

def main():
    """
    Main function to demonstrate the discount system.
    """
    print("Welcome to King Roofing's Discount System!")
    try:
        # Input collection
        service_type = input("Enter the service type (repair/replacement): ").strip().lower()
        original_price = float(input("Enter the original price of the service: ").strip())
        is_veteran = input("Is the customer a veteran? (yes/no): ").strip().lower() == 'yes'

        # Calculate final price
        final_price = calculate_discount(service_type, original_price, is_veteran)
        print(f"The final price after discounts (if applicable) is: ${final_price}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the script
if __name__ == "__main__":
    main()
```
