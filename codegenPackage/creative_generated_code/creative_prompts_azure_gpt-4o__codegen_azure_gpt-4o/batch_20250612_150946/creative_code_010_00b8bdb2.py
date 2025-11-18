"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartconnect.ng
Prompt: Write a Python script to calculate the cost of purchasing multiple utility services (data, airtime, electricity bills) using SmartConnect's pricing details.
Generated: DETERMINISTIC_00b8bdb25694a8a8
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

# Define a class to manage SmartConnect pricing details and calculations
class SmartConnectUtility:
    def __init__(self):
        # Pricing details (dummy values, replace with actual pricing)
        self.pricing = {
            "data": 0.05,  # Data price per MB in USD
            "airtime": 0.10,  # Airtime price per minute in USD
            "electricity": 0.20  # Electricity price per kWh in USD
        }

    def calculate_cost(self, service_type, quantity):
        """
        Calculate the cost for a given service and quantity.
        
        :param service_type: Type of service (data, airtime, electricity)
        :param quantity: Quantity for the service
        :return: Total cost for the service
        """
        try:
            if service_type not in self.pricing:
                raise ValueError(f"Invalid service type: {service_type}")
            
            if quantity < 0:
                raise ValueError("Quantity must be a positive value.")
            
            cost = self.pricing[service_type] * quantity
            return cost
        except ValueError as e:
            print(f"Error: {e}")
            return None

# Helper function to collect user input
def get_user_input():
    """
    Prompt the user for input to compute costs for multiple services.
    
    :return: List of tuples containing service type and quantity
    """
    print("Available services: data, airtime, electricity")
    print("Enter 'done' to finish input.")
    
    user_inputs = []
    
    while True:
        service_type = input("Enter service type: ").strip().lower()
        if service_type == "done":
            break
        if service_type not in ["data", "airtime", "electricity"]:
            print("Invalid service type! Please choose from data, airtime, electricity.")
            continue
        
        try:
            quantity = float(input(f"Enter quantity for {service_type}: "))
            if quantity < 0:
                print("Quantity must be positive. Please try again.")
                continue
            user_inputs.append((service_type, quantity))
        except ValueError:
            print("Invalid quantity! Please enter a numerical value.")
    
    return user_inputs

# Main function to execute the program
def main():
    """
    Main driver function to calculate costs for multiple services.
    """
    smart_connect = SmartConnectUtility()
    print("\nWelcome to SmartConnect Utility Cost Calculator!")
    
    # Collect user input
    user_inputs = get_user_input()
    
    # Calculate costs and display results
    total_cost = 0
    print("\nCalculating costs...")
    for service_type, quantity in user_inputs:
        cost = smart_connect.calculate_cost(service_type, quantity)
        if cost is not None:
            print(f"Service: {service_type.capitalize()}, Quantity: {quantity}, Cost: ${cost:.2f}")
            total_cost += cost
    
    print(f"\nTotal Cost: ${total_cost:.2f}")
    print("Thank you for using SmartConnect!")

# Entry point for the script
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        sys.exit(0)
```
