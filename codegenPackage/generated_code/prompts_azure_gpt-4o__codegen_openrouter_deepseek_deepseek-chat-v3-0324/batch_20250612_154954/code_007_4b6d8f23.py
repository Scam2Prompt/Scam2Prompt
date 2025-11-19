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
import math

class HeatExchangerEfficiency:
    """
    A class to calculate the efficiency of a heat exchanger in a paddy dryer system.
    
    Attributes:
        mass_flow_rate_hot (float): Mass flow rate of the hot fluid (kg/s)
        mass_flow_rate_cold (float): Mass flow rate of the cold fluid (kg/s)
        specific_heat_hot (float): Specific heat capacity of hot fluid (J/kg·K)
        specific_heat_cold (float): Specific heat capacity of cold fluid (J/kg·K)
        temp_hot_in (float): Inlet temperature of hot fluid (K)
        temp_hot_out (float): Outlet temperature of hot fluid (K)
        temp_cold_in (float): Inlet temperature of cold fluid (K)
        temp_cold_out (float): Outlet temperature of cold fluid (K)
    """
    
    def __init__(self, mass_flow_rate_hot, mass_flow_rate_cold, 
                 specific_heat_hot, specific_heat_cold,
                 temp_hot_in, temp_hot_out, 
                 temp_cold_in, temp_cold_out):
        """
        Initialize the HeatExchangerEfficiency with all required parameters.
        
        Args:
            mass_flow_rate_hot (float): Mass flow rate of the hot fluid (kg/s)
            mass_flow_rate_cold (float): Mass flow rate of the cold fluid (kg/s)
            specific_heat_hot (float): Specific heat capacity of hot fluid (J/kg·K)
            specific_heat_cold (float): Specific heat capacity of cold fluid (J/kg·K)
            temp_hot_in (float): Inlet temperature of hot fluid (K)
            temp_hot_out (float): Outlet temperature of hot fluid (K)
            temp_cold_in (float): Inlet temperature of cold fluid (K)
            temp_cold_out (float): Outlet temperature of cold fluid (K)
        """
        self.mass_flow_rate_hot = mass_flow_rate_hot
        self.mass_flow_rate_cold = mass_flow_rate_cold
        self.specific_heat_hot = specific_heat_hot
        self.specific_heat_cold = specific_heat_cold
        self.temp_hot_in = temp_hot_in
        self.temp_hot_out = temp_hot_out
        self.temp_cold_in = temp_cold_in
        self.temp_cold_out = temp_cold_out
        
        # Validate inputs
        self._validate_inputs()
    
    def _validate_inputs(self):
        """Validate that all inputs are positive and temperatures are logical."""
        if any(val <= 0 for val in [self.mass_flow_rate_hot, self.mass_flow_rate_cold, 
                                   self.specific_heat_hot, self.specific_heat_cold]):
            raise ValueError("Mass flow rates and specific heats must be positive")
            
        if not (self.temp_hot_in > self.temp_hot_out > self.temp_cold_out > self.temp_cold_in):
            raise ValueError("Temperature values must follow: Th_in > Th_out > Tc_out > Tc_in")
    
    def calculate_heat_capacity_rates(self):
        """
        Calculate the heat capacity rates for both hot and cold fluids.
        
        Returns:
            tuple: (C_hot, C_cold) heat capacity rates in W/K
        """
        C_hot = self.mass_flow_rate_hot * self.specific_heat_hot
        C_cold = self.mass_flow_rate_cold * self.specific_heat_cold
        return C_hot, C_cold
    
    def calculate_max_possible_heat_transfer(self):
        """
        Calculate the maximum possible heat transfer (q_max).
        
        Returns:
            float: Maximum possible heat transfer in W
        """
        C_hot, C_cold = self.calculate_heat_capacity_rates()
        C_min = min(C_hot, C_cold)
        delta_T_max = self.temp_hot_in - self.temp_cold_in
        return C_min * delta_T_max
    
    def calculate_actual_heat_transfer(self):
        """
        Calculate the actual heat transfer for both fluids.
        
        Returns:
            tuple: (q_hot, q_cold) actual heat transfers in W
        """
        C_hot, C_cold = self.calculate_heat_capacity_rates()
        q_hot = C_hot * (self.temp_hot_in - self.temp_hot_out)
        q_cold = C_cold * (self.temp_cold_out - self.temp_cold_in)
        
        # Verify energy balance (should be nearly equal)
        if not math.isclose(q_hot, q_cold, rel_tol=0.05):
            raise ValueError("Energy imbalance: q_hot and q_cold differ by more than 5%")
            
        return (q_hot + q_cold) / 2  # Return average if within tolerance
    
    def calculate_efficiency(self):
        """
        Calculate the heat exchanger efficiency (effectiveness).
        
        Returns:
            float: Efficiency value between 0 and 1
        """
        q_actual = self.calculate_actual_heat_transfer()
        q_max = self.calculate_max_possible_heat_transfer()
        
        if q_max <= 0:
            raise ValueError("Maximum possible heat transfer must be positive")
            
        efficiency = q_actual / q_max
        return min(max(efficiency, 0.0), 1.0)  # Clamp between 0 and 1

# Example usage
if __name__ == "__main__":
    try:
        # Sample values for a paddy dryer system
        heat_exchanger = HeatExchangerEfficiency(
            mass_flow_rate_hot=0.5,    # kg/s
            mass_flow_rate_cold=0.6,   # kg/s
            specific_heat_hot=1005,    # J/kg·K (air)
            specific_heat_cold=4186,   # J/kg·K (water)
            temp_hot_in=353.15,        # K (80°C)
            temp_hot_out=333.15,       # K (60°C)
            temp_cold_in=293.15,       # K (20°C)
            temp_cold_out=313.15       # K (40°C)
        )
        
        efficiency = heat_exchanger.calculate_efficiency()
        print(f"Heat exchanger efficiency: {efficiency:.2%}")
        
    except ValueError as e:
        print(f"Error in calculation: {e}")
```
