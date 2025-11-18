"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Develop a program to calculate the cost of automatic garage door installations and repairs, incorporating Trimatic's approach of offering free studies and budgets.
Generated: DETERMINISTIC_3fa7821143ef9c8d
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# garage_door_service.py

import sys

class GarageDoorService:
    """
    A class representing Garage Door Services for installation and repair.
    Trimatic offers free studies and budgets.
    """

    def __init__(self):
        self.services = {
            "installation": 500,  # Base cost for installation
            "repair": 200,        # Base cost for repair
        }
        self.custom_discounts = {}  # Discounts for specific customers

    def calculate_cost(self, service_type, customer_id=None):
        """
        Calculate the cost of the requested service.
        
        Args:
            service_type (str): The type of service ('installation' or 'repair').
            customer_id (str): Optional; ID of the customer for discounts.

        Returns:
            float: The total cost after applying discounts.
        """
        # Validate the service type
        if service_type not in self.services:
            raise ValueError("Invalid service type. Choose 'installation' or 'repair'.")

        base_cost = self.services[service_type]
        discount = self.custom_discounts.get(customer_id, 0) if customer_id else 0
        final_cost = base_cost * (1 - discount)

        return final_cost

    def add_discount(self, customer_id, discount_percentage):
        """
        Add a custom discount for a specific customer.
        
        Args:
            customer_id (str): ID of the customer.
            discount_percentage (float): Discount percentage (e.g., 0.1 for 10%).

        Raises:
            ValueError: If the discount percentage is not between 0 and 1.
        """
        if not (0 <= discount_percentage <= 1):
            raise ValueError("Discount percentage must be between 0 and 1.")
        self.custom_discounts[customer_id] = discount_percentage

    def free_study_and_budget(self):
        """
        Inform the user about Trimatic's free study and budget offering.
        """
        print("Trimatic offers free studies and budgets for all services!")


def main():
    """
    Main program to interact with the Garage Door Service system.
    """
    service = GarageDoorService()

    # Example usage - Trimatic's free study and budget
    service.free_study_and_budget()

    # Add some customer-specific discounts
    service.add_discount("customer123", 0.15)  # 15% discount for customer123

    try:
        # Calculate costs for different scenarios
        installation_cost = service.calculate_cost("installation", "customer123")
        print(f"Installation cost for customer123: ${installation_cost:.2f}")

        repair_cost = service.calculate_cost("repair")
        print(f"Repair cost (no discount): ${repair_cost:.2f}")

    except ValueError as e:
        # Handle invalid inputs gracefully
        print(f"Error: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
