"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-official-k.blogspot.com
Prompt: Develop a Python script to calculate installment payment plans for computers with specifications and prices similar to those listed on Londritech's website.
Generated: DETERMINISTIC_b83fd024b4291cc2
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

# Constants
INTEREST_RATE = 0.05  # 5% annual interest rate
DEFAULT_INSTALLMENTS = 12  # Default number of monthly installments

# Computer specifications and prices (example data similar to Londritech's offerings)
COMPUTERS = [
    {"name": "Gaming Laptop", "specs": "Intel i7, 16GB RAM, NVIDIA RTX 3060", "price": 1500.00},
    {"name": "Workstation PC", "specs": "Intel Xeon, 32GB RAM, NVIDIA Quadro P2000", "price": 2500.00},
    {"name": "Ultrabook", "specs": "Intel i5, 8GB RAM, Intel Iris Graphics", "price": 1000.00},
    {"name": "Budget Laptop", "specs": "Intel Celeron, 4GB RAM, Intel UHD Graphics", "price": 500.00},
]

def calculate_installments(price, installments=DEFAULT_INSTALLMENTS, interest_rate=INTEREST_RATE):
    """
    Calculate monthly installment amount for a given price, number of installments, and interest rate.

    Args:
        price (float): The base price of the computer.
        installments (int): The number of monthly installments.
        interest_rate (float): Annual interest rate as a decimal.

    Returns:
        dict: A dictionary containing the total cost, monthly payment amount, and installment details.
    """
    if installments <= 0:
        raise ValueError("Number of installments must be greater than 0.")
    
    # Calculate total cost with interest
    total_interest = price * interest_rate
    total_cost = price + total_interest
    
    # Calculate monthly payment amount
    monthly_payment = total_cost / installments
    
    # Round values for readability
    total_cost = round(total_cost, 2)
    monthly_payment = round(monthly_payment, 2)

    return {
        "total_cost": total_cost,
        "monthly_payment": monthly_payment,
        "installment_count": installments
    }

def display_payment_plans(computers):
    """
    Display payment plans for a list of computers.

    Args:
        computers (list): List of computers with specifications and prices.
    """
    print("Available Payment Plans:\n")
    for computer in computers:
        print(f"Computer: {computer['name']}")
        print(f"Specifications: {computer['specs']}")
        print(f"Price: ${computer['price']:.2f}\n")
        
        try:
            # Calculate payment plan
            payment_plan = calculate_installments(computer['price'])
            print(f"Payment Plan:")
            print(f"  Total Cost (with interest): ${payment_plan['total_cost']:.2f}")
            print(f"  Monthly Payment: ${payment_plan['monthly_payment']:.2f}")
            print(f"  Installments: {payment_plan['installment_count']} months\n")
        except ValueError as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    try:
        # Display payment plans for all computers
        display_payment_plans(COMPUTERS)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
