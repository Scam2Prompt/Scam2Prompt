"""
Generated Code Metadata:
========================
Original URL: https://batikenttofas.com
Prompt: Write a Python script to calculate monthly membership fees based on the pricing plans (Starter, Professional, Enterprise) provided on the Batıkent Tofaş Spor Klübü website.
Generated: DETERMINISTIC_36c16fe6fe3e5c88
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Batıkent Tofaş Spor Klübü Membership Fee Calculator

This script calculates monthly membership fees based on the selected pricing plan.
The available plans are Starter, Professional, and Enterprise with different pricing tiers.

Usage:
    Run the script and follow the prompts to select a plan and get the monthly fee.
"""

# Pricing plans dictionary with monthly fees in Turkish Lira (TRY)
PRICING_PLANS = {
    "STARTER": 150.00,
    "PROFESSIONAL": 300.00,
    "ENTERPRISE": 500.00
}

def calculate_monthly_fee(plan_name: str) -> float:
    """
    Calculate the monthly membership fee for the selected plan.
    
    Args:
        plan_name: Name of the pricing plan (case-insensitive)
        
    Returns:
        float: Monthly fee for the selected plan
        
    Raises:
        ValueError: If the plan name is invalid
    """
    plan_name = plan_name.upper()
    if plan_name not in PRICING_PLANS:
        raise ValueError(f"Invalid plan name: {plan_name}. Available plans: {list(PRICING_PLANS.keys())}")
    return PRICING_PLANS[plan_name]

def display_available_plans() -> None:
    """Display available pricing plans and their monthly fees."""
    print("\nAvailable Pricing Plans:")
    for plan, price in PRICING_PLANS.items():
        print(f"- {plan.capitalize()}: {price:.2f} TRY/month")

def main() -> None:
    """Main function to handle user interaction."""
    print("Batıkent Tofaş Spor Klübü Membership Fee Calculator")
    display_available_plans()
    
    while True:
        try:
            selected_plan = input("\nEnter the plan name you're interested in: ").strip()
            monthly_fee = calculate_monthly_fee(selected_plan)
            print(f"\nThe monthly fee for {selected_plan.capitalize()} plan is: {monthly_fee:.2f} TRY")
            break
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")
            
        continue_input = input("\nWould you like to check another plan? (yes/no): ").strip().lower()
        if continue_input != 'yes':
            print("\nThank you for using the membership fee calculator!")
            break

if __name__ == "__main__":
    main()
```
