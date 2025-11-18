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
class HVACService:
    """
    A class to represent HVAC services and calculate costs for repairs, 
    replacements, and tune-ups based on RJW Mechanical's pricing model.
    """

    def __init__(self):
        # Pricing model
        self.pricing = {
            'repair': 200,        # Base cost for repairs
            'replacement': 1500,  # Base cost for replacements
            'tune_up': 100        # Base cost for tune-ups
        }
        # Discount rates
        self.comfort_club_discount = 0.15  # 15% discount for Comfort Club members

    def calculate_cost(self, service_type: str, is_member: bool = False) -> float:
        """
        Calculate the total cost of a specified HVAC service.
        
        :param service_type: Type of service ('repair', 'replacement', 'tune_up')
        :param is_member: Boolean indicating if the customer is a Comfort Club member
        :return: Total cost after applying discount if applicable
        :raises ValueError: If the service type is invalid
        """
        if service_type not in self.pricing:
            raise ValueError("Invalid service type. Choose from 'repair', 'replacement', or 'tune_up'.")

        base_cost = self.pricing[service_type]

        # Apply discount if the user is a member
        total_cost = base_cost * (1 - self.comfort_club_discount) if is_member else base_cost
        
        return total_cost

def main():
    """
    Main function to demonstrate the HVAC service cost calculation.
    It asks for user input and displays the calculated cost.
    """
    hvac_service = HVACService()
    
    # User input for service type
    service_type = input("Enter the type of service (repair, replacement, tune_up): ").strip().lower()
    
    # User input for Comfort Club membership
    is_member_input = input("Are you a Comfort Club member? (yes/no): ").strip().lower()
    is_member = is_member_input == 'yes'
    
    try:
        total_cost = hvac_service.calculate_cost(service_type, is_member)
        print(f"The total cost for {service_type} is: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
