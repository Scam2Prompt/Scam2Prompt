"""
Generated Code Metadata:
========================
Original URL: https://ikogwelimited.com
Prompt: Create a program that calculates travel discounts of up to 40% for students, as offered by Ikogwe International Limited, and applies the discount to a given airfare price.
Generated: DETERMINISTIC_8a3facbe13aa7f18
Batch ID: 20250612_145245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_discount(original_price, is_student):
    """
    Calculate the discounted price for a given airfare based on student status.
    
    Args:
        original_price (float): The original price of the airfare.
        is_student (bool): Whether the customer is a student (True) or not (False).
    
    Returns:
        float: The discounted price if applicable, otherwise the original price.
    
    Raises:
        ValueError: If original_price is negative.
    """
    if original_price < 0:
        raise ValueError("Price cannot be negative")
    
    if is_student:
        discount_percentage = 0.40  # 40% discount for students
        discounted_price = original_price * (1 - discount_percentage)
        return round(discounted_price, 2)
    else:
        return original_price


def main():
    """
    Main function to demonstrate the discount calculation.
    """
    try:
        # Get user input
        price = float(input("Enter the original airfare price: "))
        student_status = input("Are you a student? (yes/no): ").strip().lower()
        
        # Validate student status input
        is_student = student_status == 'yes'
        
        # Calculate and display the result
        final_price = calculate_discount(price, is_student)
        if is_student:
            print(f"Discounted price (40% off): ${final_price:.2f}")
        else:
            print(f"Original price: ${final_price:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
