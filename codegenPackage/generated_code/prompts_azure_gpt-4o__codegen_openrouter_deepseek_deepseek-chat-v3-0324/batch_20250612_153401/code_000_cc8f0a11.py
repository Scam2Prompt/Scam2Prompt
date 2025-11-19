"""
Generated Code Metadata:
========================
Original URL: https://race-ridefire.cc
Prompt: Write Python code to calculate the aerodynamic efficiency of a bike using specifications like Shimano Dura Ace Di2 group set and Hunt 48 Limitless UD Carbon Spoke Disc Wheelset, as described on the Race Ride Fire website.
Generated: DETERMINISTIC_cc8f0a1190377add
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class BikeAerodynamics:
    """
    A class to calculate the aerodynamic efficiency of a bike based on components.
    """
    
    def __init__(self, rider_weight_kg, bike_weight_kg, frontal_area_m2, drag_coefficient, 
                 wheelset_type="Hunt 48 Limitless UD Carbon Spoke Disc", groupset="Shimano Dura Ace Di2"):
        """
        Initialize the bike aerodynamics calculator with component specifications.
        
        Args:
            rider_weight_kg (float): Weight of the rider in kilograms.
            bike_weight_kg (float): Weight of the bike in kilograms.
            frontal_area_m2 (float): Frontal area of the rider+bike in square meters.
            drag_coefficient (float): Drag coefficient of the rider+bike system.
            wheelset_type (str, optional): Type of wheelset. Defaults to "Hunt 48 Limitless UD Carbon Spoke Disc".
            groupset (str, optional): Type of groupset. Defaults to "Shimano Dura Ace Di2".
        """
        self.rider_weight = rider_weight_kg
        self.bike_weight = bike_weight_kg
        self.frontal_area = frontal_area_m2
        self.drag_coefficient = drag_coefficient
        self.wheelset_type = wheelset_type
        self.groupset = groupset
        
        # Component-specific drag coefficients (hypothetical values based on typical performance)
        self.wheelset_drag_coefficients = {
            "Hunt 48 Limitless UD Carbon Spoke Disc": 0.28,
            "Default Wheelset": 0.35
        }
        
        self.groupset_efficiency = {
            "Shimano Dura Ace Di2": 0.98,  # 98% mechanical efficiency
            "Default Groupset": 0.95
        }
    
    def calculate_aero_drag(self, velocity_ms, air_density=1.225):
        """
        Calculate aerodynamic drag force in Newtons.
        
        Args:
            velocity_ms (float): Velocity in meters per second.
            air_density (float, optional): Air density in kg/m³. Defaults to 1.225 (sea level).
            
        Returns:
            float: Aerodynamic drag force in Newtons.
        """
        if velocity_ms < 0:
            raise ValueError("Velocity cannot be negative.")
        if air_density <= 0:
            raise ValueError("Air density must be positive.")
            
        wheelset_cd = self.wheelset_drag_coefficients.get(
            self.wheelset_type, 
            self.wheelset_drag_coefficients["Default Wheelset"]
        )
        
        total_cd = self.drag_coefficient * wheelset_cd
        drag_force = 0.5 * air_density * (velocity_ms ** 2) * total_cd * self.frontal_area
        return drag_force
    
    def calculate_mechanical_power_loss(self, power_watts):
        """
        Calculate power loss due to mechanical inefficiency of the groupset.
        
        Args:
            power_watts (float): Power output in watts.
            
        Returns:
            float: Power loss in watts.
        """
        if power_watts < 0:
            raise ValueError("Power cannot be negative.")
            
        efficiency = self.groupset_efficiency.get(
            self.groupset,
            self.groupset_efficiency["Default Groupset"]
        )
        return power_watts * (1 - efficiency)
    
    def calculate_aero_efficiency(self, velocity_ms, power_watts, air_density=1.225):
        """
        Calculate the aerodynamic efficiency as the ratio of useful power to total power.
        
        Args:
            velocity_ms (float): Velocity in meters per second.
            power_watts (float): Power output in watts.
            air_density (float, optional): Air density in kg/m³. Defaults to 1.225 (sea level).
            
        Returns:
            float: Aerodynamic efficiency ratio (0-1).
        """
        try:
            drag_force = self.calculate_aero_drag(velocity_ms, air_density)
            drag_power = drag_force * velocity_ms
            mech_loss = self.calculate_mechanical_power_loss(power_watts)
            
            if power_watts <= 0:
                return 0.0
                
            useful_power = power_watts - drag_power - mech_loss
            efficiency = useful_power / power_watts
            return max(0.0, min(1.0, efficiency))  # Clamp between 0 and 1
            
        except ValueError as e:
            print(f"Error in efficiency calculation: {e}")
            return 0.0

# Example usage
if __name__ == "__main__":
    try:
        # Example parameters (hypothetical values)
        bike = BikeAerodynamics(
            rider_weight_kg=70,
            bike_weight_kg=7,
            frontal_area_m2=0.4,
            drag_coefficient=1.0
        )
        
        velocity = 10  # m/s (~36 km/h)
        power = 250    # watts
        
        efficiency = bike.calculate_aero_efficiency(velocity, power)
        print(f"Aerodynamic Efficiency: {efficiency:.2%}")
        
    except Exception as e:
        print(f"Error: {e}")
```
