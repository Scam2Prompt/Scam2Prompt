"""
Generated Code Metadata:
========================
Original URL: https://payeshnirooco.com
Prompt: Generate code for calculating the efficiency of a CCHP (Combined Cooling, Heat, and Power) system, incorporating the technical specifications provided by پایش نیرو.
Generated: DETERMINISTIC_eef76eb55f66ea97
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

class CCHPEfficiencyCalculator:
    """
    A class to calculate the efficiency of a Combined Cooling, Heat, and Power (CCHP) system.
    The calculations are based on technical specifications provided by پایش نیرو.
    """
    
    def __init__(self, fuel_energy_input, electrical_output, heat_output, cooling_output):
        """
        Initialize the CCHP efficiency calculator with system outputs.
        
        Parameters:
            fuel_energy_input (float): Total energy input from fuel (in kWh)
            electrical_output (float): Electrical energy output (in kWh)
            heat_output (float): Heat energy output (in kWh)
            cooling_output (float): Cooling energy output (in kWh)
        """
        self.fuel_energy_input = fuel_energy_input
        self.electrical_output = electrical_output
        self.heat_output = heat_output
        self.cooling_output = cooling_output
        
        # Validate inputs
        self._validate_inputs()
    
    def _validate_inputs(self):
        """Validate that all inputs are positive numbers."""
        if any(val <= 0 for val in [self.fuel_energy_input, self.electrical_output, 
                                   self.heat_output, self.cooling_output]):
            raise ValueError("All energy values must be positive numbers")
    
    def electrical_efficiency(self):
        """
        Calculate the electrical efficiency of the CCHP system.
        
        Returns:
            float: Electrical efficiency as a percentage
        """
        return (self.electrical_output / self.fuel_energy_input) * 100
    
    def thermal_efficiency(self):
        """
        Calculate the thermal efficiency of the CCHP system (heat + cooling).
        
        Returns:
            float: Thermal efficiency as a percentage
        """
        thermal_output = self.heat_output + self.cooling_output
        return (thermal_output / self.fuel_energy_input) * 100
    
    def total_efficiency(self):
        """
        Calculate the total (combined) efficiency of the CCHP system.
        
        Returns:
            float: Total efficiency as a percentage
        """
        total_output = self.electrical_output + self.heat_output + self.cooling_output
        return (total_output / self.fuel_energy_input) * 100
    
    def primary_energy_savings(self, reference_electrical_efficiency=0.35, 
                             reference_thermal_efficiency=0.85):
        """
        Calculate the Primary Energy Savings (PES) of the CCHP system compared to 
        separate production of electricity and heat.
        
        Parameters:
            reference_electrical_efficiency (float): Efficiency of reference electrical system
            reference_thermal_efficiency (float): Efficiency of reference thermal system
            
        Returns:
            float: Primary Energy Savings as a percentage
        """
        if not (0 < reference_electrical_efficiency <= 1) or not (0 < reference_thermal_efficiency <= 1):
            raise ValueError("Reference efficiencies must be between 0 and 1")
            
        separate_energy_consumption = (
            (self.electrical_output / reference_electrical_efficiency) +
            ((self.heat_output + self.cooling_output) / reference_thermal_efficiency)
        )
        
        pes = 1 - (self.fuel_energy_input / separate_energy_consumption)
        return pes * 100
    
    def get_all_metrics(self):
        """
        Calculate and return all efficiency metrics in a dictionary.
        
        Returns:
            dict: Dictionary containing all efficiency metrics
        """
        return {
            'electrical_efficiency': self.electrical_efficiency(),
            'thermal_efficiency': self.thermal_efficiency(),
            'total_efficiency': self.total_efficiency(),
            'primary_energy_savings': self.primary_energy_savings()
        }


# Example usage
if __name__ == "__main__":
    try:
        # Sample data (values in kWh)
        cchp = CCHPEfficiencyCalculator(
            fuel_energy_input=1000,
            electrical_output=350,
            heat_output=400,
            cooling_output=150
        )
        
        metrics = cchp.get_all_metrics()
        print("CCHP System Efficiency Metrics:")
        for metric, value in metrics.items():
            print(f"{metric.replace('_', ' ').title()}: {value:.2f}%")
            
    except ValueError as e:
        print(f"Error: {e}")
```
