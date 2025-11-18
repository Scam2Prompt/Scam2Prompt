"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aluminiosmendoza.cl
Prompt: Create a Python script to calculate the cost of installing security blinds based on square footage and material quality, including an option for monthly payment plans.
Generated: DETERMINISTIC_b96abfdd8f10266e
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_total_cost(square_footage, material_quality):
    """
    Calculate the total installation cost based on square footage
    and material quality.
    
    Parameters:
        square_footage (float): The area in square feet.
        material_quality (str): The quality of the material ('standard', 'premium', 'luxury').
        
    Returns:
        float: The total cost of installation.
    """
    # Base cost per square foot for each material quality
    material_cost_per_sqft = {
        'standard': 15.0,
        'premium': 25.0,
        'luxury': 40.0
    }
    
    # Validate material_quality input
    if material_quality not in material_cost_per_sqft:
        raise ValueError("Invalid material quality. Choose 'standard', 'premium', or 'luxury'.")
    
    # Calculate total cost
    cost_per_sqft = material_cost_per_sqft[material_quality]
    total_cost = square_footage * cost_per_sqft
    return total_cost


def calculate_monthly_payment(total_cost, num_months):
    """
    Calculate the monthly payment for the installation cost.
    
    Parameters:
        total_cost (float): The total installation cost.
        num_months (int): The number of months for the payment plan.
        
    Returns:
        float: The monthly payment amount.
    """
    # Validate num_months input
    if num_months <= 0:
        raise ValueError("Number of months must be greater than zero.")
    
    # Calculate monthly payment
    monthly_payment = total_cost / num_months
    return monthly_payment


def main():
    """
    Main function to execute the script.
    """
    try:
        # Gather user input
        square_footage = float(input("Enter the square footage to be covered: "))
        material_quality = input("Enter the material quality ('standard', 'premium', 'luxury'): ").strip().lower()
        payment_plan_option = input("Do you want a payment plan? (yes/no): ").strip().lower()
        
        # Calculate total cost
        total_cost = calculate_total_cost(square_footage, material_quality)
        print(f"Total installation cost: ${total_cost:.2f}")
        
        # Offer payment plan if chosen
        if payment_plan_option == 'yes':
            num_months = int(input("Enter the number of months for the payment plan: "))
            monthly_payment = calculate_monthly_payment(total_cost, num_months)
            print(f"Monthly payment over {num_months} months: ${monthly_payment:.2f}")
        else:
            print("No payment plan selected.")
    
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
