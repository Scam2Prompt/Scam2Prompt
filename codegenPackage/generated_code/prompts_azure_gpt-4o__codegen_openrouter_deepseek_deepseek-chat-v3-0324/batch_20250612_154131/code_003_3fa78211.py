"""
Generated Code Metadata:
========================
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Develop a program to calculate the cost of automatic garage door installations and repairs, incorporating Trimatic's approach of offering free studies and budgets.
Generated: DETERMINISTIC_3fa7821143ef9c8d
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Garage Door Cost Calculator for Trimatic Installations and Repairs
This program calculates the cost of garage door installations and repairs,
incorporating Trimatic's approach of offering free studies and budgets.
"""

class GarageDoorCalculator:
    """
    A class to calculate the cost of garage door installations and repairs.
    """
    
    def __init__(self):
        """
        Initialize the calculator with base prices and service options.
        """
        self.base_installation_cost = 500.00  # Base installation cost in dollars
        self.base_repair_cost = 150.00       # Base repair cost in dollars
        self.door_types = {
            'standard': 0.00,
            'insulated': 200.00,
            'custom': 500.00
        }
        self.additional_services = {
            'opener': 250.00,
            'remote': 50.00,
            'keypad': 100.00,
            'warranty': 150.00
        }
    
    def calculate_installation_cost(self, door_type, width, height, services=None):
        """
        Calculate the total cost for a garage door installation.
        
        Args:
            door_type (str): Type of door ('standard', 'insulated', 'custom')
            width (float): Width of the door in feet
            height (float): Height of the door in feet
            services (list): List of additional services (optional)
            
        Returns:
            float: Total installation cost
        """
        try:
            if door_type not in self.door_types:
                raise ValueError("Invalid door type specified")
            
            if width <= 0 or height <= 0:
                raise ValueError("Door dimensions must be positive numbers")
            
            # Calculate base cost
            total_cost = self.base_installation_cost + self.door_types[door_type]
            
            # Add size adjustment (larger doors cost more)
            size_factor = width * height / 100  # Normalize to 100 sq ft
            total_cost *= (1 + size_factor)
            
            # Add additional services
            if services:
                for service in services:
                    if service in self.additional_services:
                        total_cost += self.additional_services[service]
                    else:
                        print(f"Warning: Unknown service '{service}' will be ignored")
            
            return round(total_cost, 2)
        
        except ValueError as e:
            print(f"Error in calculation: {e}")
            return None
    
    def calculate_repair_cost(self, repair_type, parts_cost=0.0):
        """
        Calculate the cost for garage door repairs.
        
        Args:
            repair_type (str): Type of repair ('minor', 'major', 'emergency')
            parts_cost (float): Cost of replacement parts (optional)
            
        Returns:
            float: Total repair cost
        """
        try:
            repair_multipliers = {
                'minor': 1.0,
                'major': 1.5,
                'emergency': 2.0
            }
            
            if repair_type not in repair_multipliers:
                raise ValueError("Invalid repair type specified")
            
            if parts_cost < 0:
                raise ValueError("Parts cost cannot be negative")
            
            total_cost = self.base_repair_cost * repair_multipliers[repair_type] + parts_cost
            return round(total_cost, 2)
        
        except ValueError as e:
            print(f"Error in calculation: {e}")
            return None
    
    def generate_free_budget(self, installation=True, repair=False):
        """
        Generate a free budget proposal as per Trimatic's approach.
        
        Args:
            installation (bool): Include installation estimate
            repair (bool): Include repair estimate
            
        Returns:
            dict: Budget proposal with cost breakdown
        """
        budget = {
            'free_study': True,
            'installation_included': installation,
            'repair_included': repair,
            'notes': "This is a free budget proposal from Trimatic"
        }
        
        if installation:
            budget['installation_estimate'] = {
                'standard_door': self.calculate_installation_cost('standard', 8, 7),
                'insulated_door': self.calculate_installation_cost('insulated', 8, 7),
                'custom_door': self.calculate_installation_cost('custom', 8, 7)
            }
        
        if repair:
            budget['repair_estimate'] = {
                'minor_repair': self.calculate_repair_cost('minor'),
                'major_repair': self.calculate_repair_cost('major'),
                'emergency_repair': self.calculate_repair_cost('emergency')
            }
        
        return budget


def main():
    """
    Main function to demonstrate the calculator functionality.
    """
    calculator = GarageDoorCalculator()
    
    # Example installation calculation
    installation_cost = calculator.calculate_installation_cost(
        'insulated', 16, 8, ['opener', 'remote']
    )
    print(f"Installation Cost: ${installation_cost if installation_cost else 'Error'}")
    
    # Example repair calculation
    repair_cost = calculator.calculate_repair_cost('major', 75.50)
    print(f"Repair Cost: ${repair_cost if repair_cost else 'Error'}")
    
    # Generate free budget
    budget = calculator.generate_free_budget(installation=True, repair=True)
    print("\nFree Budget Proposal:")
    print(budget)


if __name__ == "__main__":
    main()
```
