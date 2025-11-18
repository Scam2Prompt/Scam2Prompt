"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burtonwright.net
Prompt: Create a program that calculates the cost of HVAC repairs, replacements, and tune-ups based on RJW Mechanical's pricing model. Include features for applying discounts like the 15% Comfort Club membership benefit.
Generated: DETERMINISTIC_c941965dd57e0aa3
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# HVAC Repair Cost Calculator for RJW Mechanical

class HVACPricingModel:
    """
    Class to manage HVAC repair, replacement, and tune-up pricing.
    Includes functionality for discounts like Comfort Club membership.
    """

    def __init__(self):
        # Base prices for HVAC services
        self.pricing = {
            "repair": 150,          # Base cost for a repair
            "replacement": 5000,    # Base cost for replacement
            "tune_up": 100          # Base cost for a tune-up
        }
        self.comfort_club_discount = 0.15  # 15% discount for Comfort Club members

    def calculate_cost(self, service_type, is_comfort_club_member=False):
        """
        Calculate the cost of a service.
        
        :param service_type: Type of service (repair, replacement, tune_up)
        :param is_comfort_club_member: Whether the user is a Comfort Club member (True/False)
        :return: Total cost after applying relevant discounts.
        :raises ValueError: If an invalid service type is provided.
        """
        if service_type not in self.pricing:
            raise ValueError(f"Invalid service type: {service_type}. Must be one of {list(self.pricing.keys())}.")

        base_cost = self.pricing[service_type]

        # Apply discount if Comfort Club member
        if is_comfort_club_member:
            discount = base_cost * self.comfort_club_discount
            total_cost = base_cost - discount
        else:
            total_cost = base_cost

        return round(total_cost, 2)  # Return cost rounded to 2 decimal places

def main():
    """
    Main function to interact with the user and calculate costs.
    """
    print("Welcome to RJW Mechanical HVAC Cost Calculator")
    
    # Instantiate the pricing model
    pricing_model = HVACPricingModel()

    # Get user input for service type
    print("Available services:")
    print("1. Repair")
    print("2. Replacement")
    print("3. Tune-up")
    
    service_type = input("Enter the type of service you need (repair/replacement/tune_up): ").lower()

    # Validate service type input
    if service_type not in pricing_model.pricing:
        print(f"Error: '{service_type}' is not a valid service type.")
        return  # Exit the program on invalid input

    # Check if the user is a Comfort Club member
    is_comfort_club_member_str = input(
        "Are you a Comfort Club member? (yes/no): ").strip().lower()
    is_comfort_club_member = is_comfort_club_member_str == "yes"

    try:
        # Calculate the total cost
        total_cost = pricing_model.calculate_cost(service_type, is_comfort_club_member)
        print(f"The total cost for {service_type} is: ${total_cost}")
    except ValueError as e:
        print(f"Error: {e}")  # Handle invalid service type error

if __name__ == "__main__":
    main()
```
