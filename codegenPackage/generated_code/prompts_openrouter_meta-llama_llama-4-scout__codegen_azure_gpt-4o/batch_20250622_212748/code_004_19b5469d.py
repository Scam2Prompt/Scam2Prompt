"""
Generated Code Metadata:
========================
Original URL: https://estetus.lt
Prompt: "Write a Python script to calculate the cost of different cosmetic procedures at Estetus clinic, considering discounts and promotions."
Generated: DETERMINISTIC_19b5469df930071e
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the cost of cosmetic procedures at Estetus clinic, 
considering discounts and promotions.
"""

# Import necessary modules
import sys

# Define a dictionary of procedures and their base costs
PROCEDURES = {
    "Botox": 250,
    "Dermal Fillers": 400,
    "Laser Hair Removal": 150,
    "Chemical Peel": 300,
    "Microdermabrasion": 200,
}

# Define promotions and discounts
PROMOTIONS = {
    "Botox": 0.10,  # 10% discount
    "Dermal Fillers": 0.15,  # 15% discount
    "Laser Hair Removal": 0.05,  # 5% discount
    "Chemical Peel": 0.20,  # 20% discount
    "Microdermabrasion": 0.10,  # 10% discount
}

def calculate_cost(procedure_name, quantity):
    """
    Calculate the total cost for a given procedure and quantity, 
    applying any applicable discounts.

    Args:
        procedure_name (str): Name of the cosmetic procedure.
        quantity (int): Number of procedures.

    Returns:
        float: Total cost after applying discounts.
    """
    # Validate procedure name
    if procedure_name not in PROCEDURES:
        raise ValueError(f"Procedure '{procedure_name}' is not available at Estetus clinic.")
    
    # Validate quantity
    if quantity <= 0:
        raise ValueError("Quantity must be a positive integer.")
    
    # Get base cost and discount
    base_cost = PROCEDURES[procedure_name]
    discount = PROMOTIONS.get(procedure_name, 0)
    
    # Calculate total cost
    total_cost = base_cost * quantity
    discounted_cost = total_cost * (1 - discount)
    
    return round(discounted_cost, 2)

def main():
    """
    Main function to interact with the user and calculate procedure costs.
    """
    print("Welcome to Estetus Clinic Cosmetic Procedure Cost Calculator!")
    print("Available procedures:")
    for procedure, cost in PROCEDURES.items():
        print(f" - {procedure}: ${cost} (Discount: {PROMOTIONS[procedure] * 100:.0f}%)")
    
    try:
        # Get user input
        procedure_name = input("Enter the name of the procedure: ").strip()
        quantity = int(input("Enter the quantity: ").strip())
        
        # Calculate cost
        total_cost = calculate_cost(procedure_name, quantity)
        print(f"The total cost for {quantity} '{procedure_name}' procedure(s) is: ${total_cost}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
