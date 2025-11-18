"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omegaenergy.co
Prompt: Generate code to model the specialized lifting systems used in the Bloque Cóndor for maximizing production efficiency, as outlined in Omega Energy's operations.
Generated: DETERMINISTIC_315e361ecddb5ede
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script models specialized lifting systems used in the Bloque Cóndor to maximize production efficiency.
The code follows Python's best practices, includes error handling, and is structured for scalability and maintainability.
"""

import math

class LiftingSystem:
    """
    A base class for specialized lifting systems in the Bloque Cóndor.
    This class provides common attributes and methods for all types of lifting systems.
    """
    
    def __init__(self, name, max_capacity, efficiency_factor):
        """
        Initialize a lifting system.
        
        :param name: Name of the lifting system
        :param max_capacity: Maximum lifting capacity (in tons)
        :param efficiency_factor: Efficiency factor (0 < factor <= 1, indicating % efficiency)
        """
        self.name = name
        self.max_capacity = max_capacity
        self.efficiency_factor = efficiency_factor
    
    def calculate_actual_capacity(self):
        """
        Calculate the actual lifting capacity based on the efficiency factor.
        
        :return: Actual lifting capacity (in tons)
        """
        return self.max_capacity * self.efficiency_factor
    
    def __str__(self):
        """
        Return a string representation of the lifting system.
        """
        return f"LiftingSystem(name={self.name}, max_capacity={self.max_capacity}, efficiency_factor={self.efficiency_factor})"


class HydraulicLiftingSystem(LiftingSystem):
    """
    A class representing hydraulic lifting systems.
    Hydraulic systems use fluid mechanics for lifting operations.
    """
    
    def __init__(self, name, max_capacity, efficiency_factor, fluid_type):
        """
        Initialize a hydraulic lifting system.
        
        :param fluid_type: Type of fluid used for hydraulic lifting (e.g., oil, water)
        """
        super().__init__(name, max_capacity, efficiency_factor)
        self.fluid_type = fluid_type
    
    def perform_lift(self, weight):
        """
        Perform a lift operation, verifying weight is within capacity.
        
        :param weight: Weight to be lifted (in tons)
        :return: Success message if lift is successful, else raise an exception
        """
        actual_capacity = self.calculate_actual_capacity()
        if weight > actual_capacity:
            raise ValueError(f"Cannot lift {weight} tons. Maximum actual capacity is {actual_capacity} tons.")
        return f"Successfully lifted {weight} tons using {self.name} with {self.fluid_type} fluid."
    
    def __str__(self):
        """
        Return a string representation of the hydraulic lifting system.
        """
        return (f"HydraulicLiftingSystem(name={self.name}, max_capacity={self.max_capacity}, "
                f"efficiency_factor={self.efficiency_factor}, fluid_type={self.fluid_type})")


class ElectricLiftingSystem(LiftingSystem):
    """
    A class representing electric lifting systems.
    Electric systems use motorized mechanisms for lifting operations.
    """
    
    def __init__(self, name, max_capacity, efficiency_factor, power_rating):
        """
        Initialize an electric lifting system.
        
        :param power_rating: Power rating of the electric system (in kW)
        """
        super().__init__(name, max_capacity, efficiency_factor)
        self.power_rating = power_rating
    
    def perform_lift(self, weight):
        """
        Perform a lift operation, verifying weight is within capacity.
        
        :param weight: Weight to be lifted (in tons)
        :return: Success message if lift is successful, else raise an exception
        """
        actual_capacity = self.calculate_actual_capacity()
        if weight > actual_capacity:
            raise ValueError(f"Cannot lift {weight} tons. Maximum actual capacity is {actual_capacity} tons.")
        return f"Successfully lifted {weight} tons using {self.name} with a power rating of {self.power_rating} kW."
    
    def __str__(self):
        """
        Return a string representation of the electric lifting system.
        """
        return (f"ElectricLiftingSystem(name={self.name}, max_capacity={self.max_capacity}, "
                f"efficiency_factor={self.efficiency_factor}, power_rating={self.power_rating})")

# Example usage:
if __name__ == "__main__":
    try:
        # Create instances of lifting systems
        hydraulic_system = HydraulicLiftingSystem(name="HydroLift-XL", max_capacity=50, efficiency_factor=0.9, fluid_type="oil")
        electric_system = ElectricLiftingSystem(name="ElectroLift-200", max_capacity=100, efficiency_factor=0.85, power_rating=200)
        
        # Perform lift operations
        print(hydraulic_system.perform_lift(40))  # Successful lift
        print(electric_system.perform_lift(85))  # Successful lift
        
        # Attempt to exceed capacity
        print(hydraulic_system.perform_lift(60))  # This will raise a ValueError
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
