"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Write a script to calculate the cost of cleaning air conditioners based on labor specialization and equipment usage, as highlighted by شركة انجاز's cleaning services.
Generated: DETERMINISTIC_fd5465d0a3a35912
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the cost of cleaning air conditioners based on labor specialization and equipment usage.
"""

class AirConditionerCleaningCostCalculator:
    """
    A class to calculate the cost of cleaning air conditioners based on various factors.
    """
    
    def __init__(self):
        """
        Initialize the calculator with default rates and equipment costs.
        """
        self.labor_rates = {
            'standard': 50,      # per hour
            'specialized': 75,   # per hour
            'expert': 100        # per hour
        }
        
        self.equipment_costs = {
            'basic': 20,         # per use
            'advanced': 50,      # per use
            'premium': 100       # per use
        }
        
        self.base_time = 1.5     # hours (base time for standard cleaning)
    
    def calculate_cost(self, labor_type, equipment_type, units=1, additional_time=0):
        """
        Calculate the total cost for cleaning air conditioners.
        
        Args:
            labor_type (str): Type of labor ('standard', 'specialized', 'expert')
            equipment_type (str): Type of equipment ('basic', 'advanced', 'premium')
            units (int): Number of air conditioner units to clean (default: 1)
            additional_time (float): Additional time required in hours (default: 0)
            
        Returns:
            float: Total cost for the cleaning service
            
        Raises:
            ValueError: If invalid labor_type or equipment_type is provided
        """
        # Validate input parameters
        if labor_type not in self.labor_rates:
            raise ValueError(f"Invalid labor type: {labor_type}. Must be one of {list(self.labor_rates.keys())}")
            
        if equipment_type not in self.equipment_costs:
            raise ValueError(f"Invalid equipment type: {equipment_type}. Must be one of {list(self.equipment_costs.keys())}")
            
        if units <= 0:
            raise ValueError("Number of units must be positive")
            
        if additional_time < 0:
            raise ValueError("Additional time cannot be negative")
        
        # Calculate total time (base time + additional time)
        total_time = self.base_time + additional_time
        
        # Calculate labor cost
        labor_cost = self.labor_rates[labor_type] * total_time
        
        # Calculate equipment cost
        equipment_cost = self.equipment_costs[equipment_type]
        
        # Calculate total cost per unit
        cost_per_unit = labor_cost + equipment_cost
        
        # Calculate total cost for all units
        total_cost = cost_per_unit * units
        
        return total_cost
    
    def get_available_labor_types(self):
        """Return available labor types."""
        return list(self.labor_rates.keys())
    
    def get_available_equipment_types(self):
        """Return available equipment types."""
        return list(self.equipment_costs.keys())


# Example usage
if __name__ == "__main__":
    try:
        calculator = AirConditionerCleaningCostCalculator()
        
        # Get user input
        print("Available labor types:", calculator.get_available_labor_types())
        labor = input("Enter labor type: ").lower()
        
        print("Available equipment types:", calculator.get_available_equipment_types())
        equipment = input("Enter equipment type: ").lower()
        
        units = int(input("Enter number of units: "))
        additional_time = float(input("Enter additional time required (hours): "))
        
        # Calculate and display cost
        total_cost = calculator.calculate_cost(labor, equipment, units, additional_time)
        print(f"\nTotal cleaning cost: ${total_cost:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
