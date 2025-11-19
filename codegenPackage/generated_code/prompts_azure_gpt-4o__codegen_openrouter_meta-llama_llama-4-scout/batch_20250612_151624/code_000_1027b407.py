"""
Generated Code Metadata:
========================
Original URL: https://unitedcabinetry.com.au
Prompt: Write Python code to calculate the cost of cabinetry installation based on parameters like kitchen size, number of cabinets, and additional services such as demolition or appliance relocation, referencing the services offered by United Cabinetry.
Generated: DETERMINISTIC_1027b407cd0f77ff
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cabinetry_installation_calculator.py

class CabinetryInstallationCalculator:
    """
    Calculates the cost of cabinetry installation based on kitchen size, 
    number of cabinets, and additional services.
    """

    def __init__(self):
        # Base costs per unit
        self.base_cost_per_cabinet = 300  # dollars
        self.demolition_cost = 500  # dollars
        self.appliance_relocation_cost = 200  # dollars

        # Cost per square foot for kitchen size
        self.kitchen_size_cost_per_sqft = 10  # dollars

    def calculate_base_cost(self, num_cabinets):
        """
        Calculates the base cost of cabinetry installation.

        Args:
            num_cabinets (int): Number of cabinets.

        Returns:
            float: Base cost of cabinetry installation.
        """
        return num_cabinets * self.base_cost_per_cabinet

    def calculate_kitchen_size_cost(self, kitchen_size_sqft):
        """
        Calculates the cost based on kitchen size.

        Args:
            kitchen_size_sqft (float): Kitchen size in square feet.

        Returns:
            float: Cost based on kitchen size.
        """
        return kitchen_size_sqft * self.kitchen_size_cost_per_sqft

    def calculate_additional_services_cost(self, demolition=False, appliance_relocation=False):
        """
        Calculates the cost of additional services.

        Args:
            demolition (bool, optional): Whether demolition service is required. Defaults to False.
            appliance_relocation (bool, optional): Whether appliance relocation service is required. Defaults to False.

        Returns:
            float: Cost of additional services.
        """
        additional_cost = 0
        if demolition:
            additional_cost += self.demolition_cost
        if appliance_relocation:
            additional_cost += self.appliance_relocation_cost
        return additional_cost

    def calculate_total_cost(self, num_cabinets, kitchen_size_sqft, demolition=False, appliance_relocation=False):
        """
        Calculates the total cost of cabinetry installation.

        Args:
            num_cabinets (int): Number of cabinets.
            kitchen_size_sqft (float): Kitchen size in square feet.
            demolition (bool, optional): Whether demolition service is required. Defaults to False.
            appliance_relocation (bool, optional): Whether appliance relocation service is required. Defaults to False.

        Returns:
            float: Total cost of cabinetry installation.
        """
        base_cost = self.calculate_base_cost(num_cabinets)
        kitchen_size_cost = self.calculate_kitchen_size_cost(kitchen_size_sqft)
        additional_services_cost = self.calculate_additional_services_cost(demolition, appliance_relocation)
        return base_cost + kitchen_size_cost + additional_services_cost


def main():
    try:
        calculator = CabinetryInstallationCalculator()

        num_cabinets = int(input("Enter the number of cabinets: "))
        kitchen_size_sqft = float(input("Enter the kitchen size in square feet: "))

        demolition = input("Is demolition service required? (yes/no): ").lower() == "yes"
        appliance_relocation = input("Is appliance relocation service required? (yes/no): ").lower() == "yes"

        total_cost = calculator.calculate_total_cost(num_cabinets, kitchen_size_sqft, demolition, appliance_relocation)

        print(f"Total cost of cabinetry installation: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
