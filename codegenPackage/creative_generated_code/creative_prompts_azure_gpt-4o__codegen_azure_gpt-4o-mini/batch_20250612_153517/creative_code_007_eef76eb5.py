"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://payeshnirooco.com
Prompt: Generate code for calculating the efficiency of a CCHP (Combined Cooling, Heat, and Power) system, incorporating the technical specifications provided by پایش نیرو.
Generated: DETERMINISTIC_eef76eb55f66ea97
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CCHPSystem:
    """
    A class to represent a Combined Cooling, Heat, and Power (CCHP) system.
    
    Attributes
    ----------
    electrical_power_output : float
        The electrical power output of the system in kW.
    thermal_power_output : float
        The thermal power output of the system in kW.
    cooling_power_output : float
        The cooling power output of the system in kW.
    fuel_input : float
        The amount of fuel input to the system in kW.
    
    Methods
    -------
    calculate_total_efficiency() -> float:
        Calculates the total efficiency of the CCHP system.
    """

    def __init__(self, electrical_power_output: float, thermal_power_output: float,
                 cooling_power_output: float, fuel_input: float):
        """
        Parameters
        ----------
        electrical_power_output : float
            The electrical power output in kW.
        thermal_power_output : float
            The thermal power output in kW.
        cooling_power_output : float
            The cooling power output in kW.
        fuel_input : float
            The amount of fuel input in kW.
        """
        if fuel_input <= 0:
            raise ValueError("Fuel input must be greater than zero.")
        
        self.electrical_power_output = electrical_power_output
        self.thermal_power_output = thermal_power_output
        self.cooling_power_output = cooling_power_output
        self.fuel_input = fuel_input

    def calculate_total_efficiency(self) -> float:
        """
        Calculates the total efficiency of the CCHP system.
        
        Total efficiency is defined as the sum of electrical, thermal, and cooling outputs 
        divided by the fuel input.

        Returns
        -------
        float
            The total efficiency of the CCHP system in percentage.
        """
        try:
            total_output = (self.electrical_power_output + 
                            self.thermal_power_output + 
                            self.cooling_power_output)
            efficiency = (total_output / self.fuel_input) * 100
            
            return round(efficiency, 2)  # Round to two decimal places for readability
        except ZeroDivisionError:
            raise RuntimeError("Error in calculating efficiency: fuel input cannot be zero.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating efficiency: {str(e)}")


# Example usage (to be executed outside this module)
if __name__ == "__main__":
    try:
        cchp = CCHPSystem(electrical_power_output=100, 
                          thermal_power_output=50, 
                          cooling_power_output=30, 
                          fuel_input=200)
        efficiency = cchp.calculate_total_efficiency()
        print(f"The total efficiency of the CCHP system is {efficiency}%")
    except Exception as e:
        print(f"Error: {e}")
```
