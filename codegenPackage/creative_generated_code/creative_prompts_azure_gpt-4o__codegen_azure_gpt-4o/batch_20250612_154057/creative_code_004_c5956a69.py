"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ashlabs.xyz
Prompt: Create a script to calculate hosting plan costs and simulate saving 90% on Hostinger's website hosting plans.
Generated: DETERMINISTIC_c5956a6970e53665
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# hosting_plan_calculator.py

"""
This script calculates the hosting plan costs and simulates saving 
90% on Hostinger's website hosting plans. It is designed to be clean, 
efficient, and production-ready.
"""

# Define hosting plans and their original prices in USD
HOSTING_PLANS = {
    "Single Web Hosting": 9.99,
    "Premium Web Hosting": 15.99,
    "Business Web Hosting": 24.99
}

# Discount rate (90% off)
DISCOUNT_RATE = 0.90


def calculate_discounted_price(original_price, discount_rate):
    """
    Calculate the discounted price based on the original price and discount rate.
    
    Args:
        original_price (float): The original price of the hosting plan.
        discount_rate (float): The discount rate (e.g., 0.90 for 90% off).
    
    Returns:
        float: The discounted price.
    """
    if original_price < 0:
        raise ValueError("Original price cannot be negative.")
    if not (0 <= discount_rate <= 1):
        raise ValueError("Discount rate must be between 0 and 1.")

    discounted_price = original_price * (1 - discount_rate)
    return round(discounted_price, 2)


def display_hosting_plan_costs(plans, discount_rate):
    """
    Display the original and discounted prices for each hosting plan.
    
    Args:
        plans (dict): A dictionary of hosting plans and their original prices.
        discount_rate (float): The discount rate (e.g., 0.90 for 90% off).
    """
    print("=== Hosting Plans Pricing ===")
    for plan_name, original_price in plans.items():
        try:
            discounted_price = calculate_discounted_price(original_price, discount_rate)
            print(f"{plan_name}:\n- Original Price: ${original_price}\n- Discounted Price: ${discounted_price}\n")
        except ValueError as e:
            print(f"Error calculating price for {plan_name}: {e}")


def main():
    """
    Main function to calculate and display hosting plan costs with discounts applied.
    """
    try:
        display_hosting_plan_costs(HOSTING_PLANS, DISCOUNT_RATE)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
