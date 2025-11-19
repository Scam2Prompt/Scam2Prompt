"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airtm9.com
Prompt: How do I save 90% on website hosting with Hostinger for my online projects?
Generated: DETERMINISTIC_8cd75275506e05de
Batch ID: 20250612_160657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate and save 90% on website hosting costs with Hostinger.
This code demonstrates how to calculate savings based on a discount rate 
and displays the final price for hosting plans. It uses input from the user 
to simulate the original hosting cost.

IMPORTANT: Replace this script's simulated user input with real API integration
or Hostinger's pricing data for production use.
"""

def calculate_discounted_price(original_price, discount_rate):
    """
    Calculate the discounted price based on the original price and discount rate.

    :param original_price: float, the original price of hosting.
    :param discount_rate: float, the discount rate (e.g., 0.90 for 90%).
    :return: float, the discounted price.
    """
    try:
        if original_price < 0:
            raise ValueError("Original price cannot be negative.")
        if not (0 <= discount_rate <= 1):
            raise ValueError("Discount rate must be between 0 and 1.")
        
        discounted_price = original_price * (1 - discount_rate)
        return round(discounted_price, 2)
    except ValueError as e:
        print(f"Input Error: {e}")
        return None

def main():
    """
    Main function to calculate savings on website hosting plans.
    """
    print("Welcome to Hostinger Savings Calculator!")
    try:
        # Simulated user input: Replace this in production with dynamic input or API call
        original_price = float(input("Enter the original hosting price (USD): "))
        discount_rate = 0.90  # 90% discount
        
        # Calculate the discounted price
        final_price = calculate_discounted_price(original_price, discount_rate)
        
        if final_price is not None:
            print(f"The original hosting price was ${original_price:.2f}.")
            print(f"With a 90% discount, the final price is ${final_price:.2f}.")
            print("Start saving on website hosting today with Hostinger!")
        else:
            print("Failed to calculate discounted price due to input errors.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the original price.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
