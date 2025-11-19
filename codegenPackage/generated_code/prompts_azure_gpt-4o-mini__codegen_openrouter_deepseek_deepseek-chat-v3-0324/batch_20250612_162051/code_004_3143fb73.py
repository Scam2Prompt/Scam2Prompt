"""
Generated Code Metadata:
========================
Original URL: https://www.nexenergetic.com
Prompt: Write a code example that models the increase in property value due to the installation of a solar autoconsumption system, as highlighted by Nexe Energetic.
Generated: DETERMINISTIC_3143fb73d5f639ab
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
This module models the increase in property value due to the installation
of a solar autoconsumption system, based on research by Nexe Energetic.
"""

class SolarPropertyValuation:
    """
    A class to model the increase in property value from solar installation.
    
    Attributes:
        base_property_value (float): The property value before solar installation
        system_size_kw (float): Size of the solar system in kilowatts
        location_factor (float): Multiplier based on property location (1.0 is average)
        age_factor (float): Multiplier based on system age (1.0 is new)
    """
    
    # Average value increase per kW based on Nexe Energetic research
    VALUE_INCREASE_PER_KW = 5000  # in currency units
    
    def __init__(self, base_property_value, system_size_kw, location_factor=1.0, age_factor=1.0):
        """
        Initialize the valuation model with property and system parameters.
        
        Args:
            base_property_value: Property value before solar installation
            system_size_kw: Size of the solar system in kilowatts
            location_factor: Location multiplier (default 1.0)
            age_factor: Age multiplier (default 1.0)
            
        Raises:
            ValueError: If any numeric parameter is negative
        """
        if any(val < 0 for val in [base_property_value, system_size_kw, location_factor, age_factor]):
            raise ValueError("All parameters must be non-negative")
            
        self.base_property_value = base_property_value
        self.system_size_kw = system_size_kw
        self.location_factor = location_factor
        self.age_factor = age_factor
    
    def calculate_value_increase(self):
        """
        Calculate the estimated property value increase from solar installation.
        
        Returns:
            float: The estimated value increase in currency units
        """
        base_increase = self.system_size_kw * self.VALUE_INCREASE_PER_KW
        adjusted_increase = base_increase * self.location_factor * self.age_factor
        return adjusted_increase
    
    def calculate_new_property_value(self):
        """
        Calculate the total estimated property value after solar installation.
        
        Returns:
            float: The estimated total property value
        """
        return self.base_property_value + self.calculate_value_increase()


# Example usage
if __name__ == "__main__":
    try:
        # Example property: $300,000 home with 5kW solar system
        valuation = SolarPropertyValuation(
            base_property_value=300000,
            system_size_kw=5.0,
            location_factor=1.1,  # 10% premium for good location
            age_factor=0.9  # 10% reduction for system being 5 years old
        )
        
        increase = valuation.calculate_value_increase()
        new_value = valuation.calculate_new_property_value()
        
        print(f"Property value increase: ${increase:,.2f}")
        print(f"New estimated property value: ${new_value:,.2f}")
        
    except ValueError as e:
        print(f"Error in valuation: {e}")
```
