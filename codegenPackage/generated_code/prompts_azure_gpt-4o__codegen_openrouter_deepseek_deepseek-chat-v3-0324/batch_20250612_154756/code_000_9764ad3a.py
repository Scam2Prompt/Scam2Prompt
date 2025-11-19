"""
Generated Code Metadata:
========================
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Write a Python script to calculate monthly installment payments for Chevrolet Consórcio plans, using parameters like vehicle price, administrative fee percentage, and financing term as described on the Consórcio Chevrolet website.
Generated: DETERMINISTIC_9764ad3a6f54e61b
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_monthly_installment(
    vehicle_price: float,
    admin_fee_percentage: float,
    term_months: int,
    interest_rate: float = 0.0
) -> dict:
    """
    Calculate monthly installment payments for Chevrolet Consórcio plans.
    
    Args:
        vehicle_price (float): Total price of the vehicle
        admin_fee_percentage (float): Administrative fee as percentage (e.g., 15 for 15%)
        term_months (int): Financing term in months
        interest_rate (float, optional): Annual interest rate (if applicable). Defaults to 0.0.
        
    Returns:
        dict: Dictionary containing calculated values with keys:
            - 'monthly_installment'
            - 'total_admin_fee'
            - 'total_cost'
            - 'total_interest' (if interest_rate > 0)
            
    Raises:
        ValueError: If any input parameter is invalid
    """
    # Validate input parameters
    if vehicle_price <= 0:
        raise ValueError("Vehicle price must be positive")
    if admin_fee_percentage < 0:
        raise ValueError("Administrative fee percentage cannot be negative")
    if term_months <= 0:
        raise ValueError("Term in months must be positive")
    if interest_rate < 0:
        raise ValueError("Interest rate cannot be negative")
    
    # Calculate administrative fee
    admin_fee = vehicle_price * (admin_fee_percentage / 100)
    total_amount = vehicle_price + admin_fee
    
    # Calculate monthly installment (simple division if no interest)
    if interest_rate == 0:
        monthly_installment = total_amount / term_months
        total_interest = 0.0
    else:
        # Convert annual rate to monthly and calculate compound interest
        monthly_rate = (interest_rate / 100) / 12
        monthly_installment = (total_amount * monthly_rate * math.pow(1 + monthly_rate, term_months)) / (math.pow(1 + monthly_rate, term_months) - 1)
        total_interest = (monthly_installment * term_months) - total_amount
    
    # Prepare result dictionary
    result = {
        'monthly_installment': round(monthly_installment, 2),
        'total_admin_fee': round(admin_fee, 2),
        'total_cost': round(monthly_installment * term_months, 2),
        'vehicle_price': round(vehicle_price, 2),
        'admin_fee_percentage': admin_fee_percentage,
        'term_months': term_months,
        'interest_rate': interest_rate
    }
    
    if interest_rate > 0:
        result['total_interest'] = round(total_interest, 2)
    
    return result

def main():
    """Example usage of the installment calculator."""
    try:
        # Get user input
        vehicle_price = float(input("Enter vehicle price (R$): "))
        admin_fee = float(input("Enter administrative fee percentage (%): "))
        term = int(input("Enter financing term in months: "))
        has_interest = input("Does the plan have interest? (y/n): ").lower() == 'y'
        
        interest_rate = 0.0
        if has_interest:
            interest_rate = float(input("Enter annual interest rate (%): "))
        
        # Calculate installment
        result = calculate_monthly_installment(
            vehicle_price=vehicle_price,
            admin_fee_percentage=admin_fee,
            term_months=term,
            interest_rate=interest_rate
        )
        
        # Display results
        print("\n--- Calculation Results ---")
        print(f"Vehicle Price: R$ {result['vehicle_price']:,.2f}")
        print(f"Administrative Fee ({result['admin_fee_percentage']}%): R$ {result['total_admin_fee']:,.2f}")
        if interest_rate > 0:
            print(f"Total Interest ({interest_rate}% p.a.): R$ {result['total_interest']:,.2f}")
        print(f"Monthly Installment ({term} months): R$ {result['monthly_installment']:,.2f}")
        print(f"Total Cost: R$ {result['total_cost']:,.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
