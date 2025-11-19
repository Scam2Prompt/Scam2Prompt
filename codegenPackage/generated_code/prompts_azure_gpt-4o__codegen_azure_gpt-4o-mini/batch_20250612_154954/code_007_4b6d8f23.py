"""
Generated Code Metadata:
========================
Original URL: https://mechanosolutions.in
Prompt: Generate Python code to calculate the efficiency of a heat exchanger in a paddy dryer system, incorporating the components mentioned on Mechano Solutions' webpage.
Generated: DETERMINISTIC_4b6d8f235dcd3149
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HeatExchanger:
    """
    A class to represent a heat exchanger in a paddy dryer system.
    """

    def __init__(self, inlet_temp_hot, outlet_temp_hot, inlet_temp_cold, outlet_temp_cold, mass_flow_rate_hot, mass_flow_rate_cold):
        """
        Initializes the heat exchanger with the given parameters.

        Parameters:
        inlet_temp_hot (float): Inlet temperature of the hot fluid (°C)
        outlet_temp_hot (float): Outlet temperature of the hot fluid (°C)
        inlet_temp_cold (float): Inlet temperature of the cold fluid (°C)
        outlet_temp_cold (float): Outlet temperature of the cold fluid (°C)
        mass_flow_rate_hot (float): Mass flow rate of the hot fluid (kg/s)
        mass_flow_rate_cold (float): Mass flow rate of the cold fluid (kg/s)
        """
        self.inlet_temp_hot = inlet_temp_hot
        self.outlet_temp_hot = outlet_temp_hot
        self.inlet_temp_cold = inlet_temp_cold
        self.outlet_temp_cold = outlet_temp_cold
        self.mass_flow_rate_hot = mass_flow_rate_hot
        self.mass_flow_rate_cold = mass_flow_rate_cold

    def calculate_heat_transfer(self):
        """
        Calculates the heat transfer rate of the heat exchanger.

        Returns:
        float: Heat transfer rate (kW)
        """
        # Specific heat capacity of water (kJ/kg·°C)
        specific_heat_capacity = 4.186

        # Calculate heat transfer for hot fluid
        heat_transfer_hot = self.mass_flow_rate_hot * specific_heat_capacity * (self.inlet_temp_hot - self.outlet_temp_hot)

        # Calculate heat transfer for cold fluid
        heat_transfer_cold = self.mass_flow_rate_cold * specific_heat_capacity * (self.outlet_temp_cold - self.inlet_temp_cold)

        # Return the minimum of the two heat transfers (in kW)
        return min(heat_transfer_hot, heat_transfer_cold) / 1000  # Convert from kJ/s to kW

    def calculate_efficiency(self):
        """
        Calculates the efficiency of the heat exchanger.

        Returns:
        float: Efficiency of the heat exchanger (percentage)
        """
        try:
            heat_transfer = self.calculate_heat_transfer()
            # Maximum possible heat transfer based on the hot fluid
            max_heat_transfer = self.mass_flow_rate_hot * 4.186 * (self.inlet_temp_hot - self.inlet_temp_cold) / 1000  # Convert to kW

            # Efficiency calculation
            efficiency = (heat_transfer / max_heat_transfer) * 100 if max_heat_transfer > 0 else 0
            return efficiency
        except ZeroDivisionError:
            print("Error: Division by zero encountered in efficiency calculation.")
            return 0
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0

# Example usage
if __name__ == "__main__":
    # Initialize the heat exchanger with example parameters
    heat_exchanger = HeatExchanger(
        inlet_temp_hot=80,  # °C
        outlet_temp_hot=60,  # °C
        inlet_temp_cold=20,  # °C
        outlet_temp_cold=40,  # °C
        mass_flow_rate_hot=2,  # kg/s
        mass_flow_rate_cold=1.5  # kg/s
    )

    # Calculate and print the efficiency
    efficiency = heat_exchanger.calculate_efficiency()
    print(f"Heat Exchanger Efficiency: {efficiency:.2f}%")
```
