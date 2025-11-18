"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ikogwelimited.com
Prompt: Create a program that calculates travel discounts of up to 40% for students, as offered by Ikogwe International Limited, and applies the discount to a given airfare price.
Generated: DETERMINISTIC_8a3facbe13aa7f18
Batch ID: 20250612_145245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to calculate travel discounts for students offered by Ikogwe International Limited.
Students are eligible for up to a 40% discount on airfare.
"""

def calculate_discounted_price(airfare, discount_percentage):
    """
    Calculates the discounted price for a given airfare.
    
    Parameters:
        airfare (float): The original airfare price.
        discount_percentage (float): The percentage discount to apply.
    
    Returns:
        float: The discounted airfare price.
    """
    try:
        # Ensure airfare and discount_percentage are valid inputs
        if airfare < 0:
            raise ValueError("Airfare price must be a positive number.")
        if not (0 <= discount_percentage <= 40):
            raise ValueError("Discount percentage must be between 0% and 40%.")
        
        # Calculate the discounted price
        discount_amount = airfare * (discount_percentage / 100)
        discounted_price = airfare - discount_amount
        
        return round(discounted_price, 2)  # Return rounded price for better readability
    except TypeError:
        raise TypeError("Invalid input: Airfare and discount percentage must be numbers.")

def main():
    """
    Main function to interact with the user and calculate the discounted airfare.
    """
    try:
        print("Welcome to Ikogwe International Limited Travel Discounts for Students!")
        
        # Get the airfare price from the user
        airfare = float(input("Enter the original airfare price: $"))
        
        # Get the discount percentage (up to 40%) from the user
        discount_percentage = float(input("Enter the discount percentage (up to 40%): "))
        
        # Calculate the discounted price
        discounted_price = calculate_discounted_price(airfare, discount_percentage)
        
        # Display the result
        print(f"\nOriginal Airfare Price: ${airfare:.2f}")
        print(f"Discount Percentage: {discount_percentage}%")
        print(f"Discounted Airfare Price: ${discounted_price:.2f}")
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except TypeError as te:
        print(f"Error: {te}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the program
if __name__ == "__main__":
    main()
```
