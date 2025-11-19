"""
Generated Code Metadata:
========================
Original URL: https://cartoriojustiniano.com.br
Prompt: Write a Python script that calculates the fees for various notarial services, including union stable and apostilamento, based on the provided tabela de emolumentos.
Generated: DETERMINISTIC_317784a3fc3e3da4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate fees for various notarial services based on a provided fee table (tabela de emolumentos).
This script supports services like 'union stable' and 'apostilamento'.
"""

# Import necessary modules
import sys

# Define the fee table (tabela de emolumentos)
FEE_TABLE = {
    "union_stable": 150.00,  # Fee for union stable service
    "apostilamento": 75.00,  # Fee for apostilamento service
}

def calculate_fee(service_type, quantity=1):
    """
    Calculate the total fee for a given notarial service.

    Args:
        service_type (str): The type of notarial service (e.g., 'union_stable', 'apostilamento').
        quantity (int): The number of services requested (default is 1).

    Returns:
        float: The total fee for the requested service.
    """
    try:
        # Validate service type
        if service_type not in FEE_TABLE:
            raise ValueError(f"Invalid service type: '{service_type}'. Available services: {list(FEE_TABLE.keys())}")
        
        # Validate quantity
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        # Calculate total fee
        fee_per_service = FEE_TABLE[service_type]
        total_fee = fee_per_service * quantity
        return total_fee
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    """
    Main function to interact with the user and calculate fees.
    """
    print("Welcome to the Notarial Fee Calculator!")
    print("Available services:")
    for service, fee in FEE_TABLE.items():
        print(f" - {service}: ${fee:.2f} per service")
    
    # Get user input
    service_type = input("Enter the type of service you need: ").strip().lower()
    try:
        quantity = int(input("Enter the quantity of services: ").strip())
    except ValueError:
        print("Error: Quantity must be a valid integer.")
        sys.exit(1)
    
    # Calculate and display the fee
    total_fee = calculate_fee(service_type, quantity)
    print(f"The total fee for {quantity} '{service_type}' service(s) is: ${total_fee:.2f}")

if __name__ == "__main__":
    main()
```
