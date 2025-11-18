"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://batikenttofas.com
Prompt: Write a Python script to calculate monthly membership fees based on the pricing plans (Starter, Professional, Enterprise) provided on the Batıkent Tofaş Spor Klübü website.
Generated: DETERMINISTIC_36c16fe6fe3e5c88
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_membership_fee(plan, discount=0):
    """
    Calculate the monthly membership fee based on the selected plan and optional discount.
    
    Args:
        plan (str): The membership plan ('Starter', 'Professional', 'Enterprise').
        discount (float): Optional discount percentage (e.g., 10 for 10% discount). Default is 0.
    
    Returns:
        float: The monthly membership fee after applying the discount.
    Raises:
        ValueError: If the plan is invalid or the discount is negative.
    """

    # Pricing plans and their corresponding fees
    pricing_plans = {
        "Starter": 50.0,       # Starter plan costs $50 per month
        "Professional": 100.0, # Professional plan costs $100 per month
        "Enterprise": 200.0    # Enterprise plan costs $200 per month
    }

    # Validate plan
    if plan not in pricing_plans:
        raise ValueError(f"Invalid plan '{plan}'. Available plans are: {', '.join(pricing_plans.keys())}")
    
    # Validate discount
    if discount < 0:
        raise ValueError("Discount cannot be negative.")
    
    # Calculate fee
    base_fee = pricing_plans[plan]
    discount_amount = base_fee * (discount / 100)
    final_fee = base_fee - discount_amount
    
    return round(final_fee, 2)  # Round to 2 decimal places for currency formatting


def main():
    """
    Main function to interactively prompt the user for the membership plan
    and optional discount, then calculate and display the membership fee.
    """
    print("Welcome to Batıkent Tofaş Spor Klübü Membership Fee Calculator!")
    print("Available Plans:")
    print("1. Starter ($50/month)")
    print("2. Professional ($100/month)")
    print("3. Enterprise ($200/month)")
    
    try:
        # Prompt user for plan
        plan = input("Please enter your membership plan (Starter, Professional, Enterprise): ").strip()
        
        # Prompt user for discount (optional)
        discount_input = input("Enter discount percentage (optional, press Enter to skip): ").strip()
        discount = float(discount_input) if discount_input else 0
        
        # Calculate membership fee
        fee = calculate_membership_fee(plan, discount)
        print(f"\nYour monthly membership fee is: ${fee:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
