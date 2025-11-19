"""
Generated Code Metadata:
========================
Original URL: https://engenhariawpj.com
Prompt: Write code to simulate the thermal performance of a building using StoTherm systems, referencing the insulation properties described on the Engenharia WPJ website.
Generated: DETERMINISTIC_b42e56a6bbebc513
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

class BuildingThermalModel:
    """
    Simulates the thermal performance of a building using StoTherm insulation systems.
    References insulation properties from Engenharia WPJ website.
    
    Attributes:
        area (float): Building surface area in m².
        volume (float): Building volume in m³.
        insulation_thickness (float): Insulation thickness in meters.
        initial_temp (float): Initial indoor temperature in °C.
        outside_temp (float): Outside temperature in °C.
        heat_capacity (float): Heat capacity of air in J/(kg·K).
        air_density (float): Density of air in kg/m³.
        u_value (float): Overall heat transfer coefficient in W/(m²·K).
    """
    
    def __init__(self, area, volume, insulation_thickness, initial_temp=20.0, outside_temp=10.0):
        """
        Initialize the building thermal model with given parameters.
        
        Args:
            area (float): Building surface area in m².
            volume (float): Building volume in m³.
            insulation_thickness (float): Insulation thickness in meters.
            initial_temp (float, optional): Initial indoor temperature in °C. Defaults to 20.0.
            outside_temp (float, optional): Outside temperature in °C. Defaults to 10.0.
        """
        self.area = area
        self.volume = volume
        self.insulation_thickness = insulation_thickness
        self.initial_temp = initial_temp
        self.outside_temp = outside_temp
        
        # Physical constants
        self.heat_capacity = 1005.0  # J/(kg·K)
        self.air_density = 1.225     # kg/m³
        
        # Calculate U-value based on StoTherm insulation properties (reference: Engenharia WPJ)
        # Typical lambda (thermal conductivity) for StoTherm is ~0.035 W/(m·K)
        self.u_value = 0.035 / insulation_thickness  # W/(m²·K)
    
    def heat_loss_rate(self, temp_inside):
        """
        Calculate the heat loss rate through the building envelope.
        
        Args:
            temp_inside (float): Current indoor temperature in °C.
            
        Returns:
            float: Heat loss rate in Watts.
        """
        return self.u_value * self.area * (temp_inside - self.outside_temp)
    
    def thermal_model(self, t, temp_inside):
        """
        Differential equation representing the thermal dynamics of the building.
        
        Args:
            t (float): Time (unused, required by solver).
            temp_inside (float): Current indoor temperature in °C.
            
        Returns:
            float: Rate of temperature change in °C/s.
        """
        mass_air = self.air_density * self.volume
        heat_loss = self.heat_loss_rate(temp_inside)
        dTdt = -heat_loss / (mass_air * self.heat_capacity)
        return dTdt
    
    def simulate(self, duration_hours, time_step_minutes=1):
        """
        Simulate the thermal performance over a given duration.
        
        Args:
            duration_hours (float): Simulation duration in hours.
            time_step_minutes (int, optional): Time step for output in minutes. Defaults to 1.
            
        Returns:
            tuple: (time_points, temperature_points) arrays.
        """
        try:
            duration_seconds = duration_hours * 3600
            t_eval = np.arange(0, duration_seconds, time_step_minutes * 60)
            
            solution = solve_ivp(
                fun=self.thermal_model,
                t_span=(0, duration_seconds),
                y0=[self.initial_temp],
                t_eval=t_eval,
                method='RK45'
            )
            
            return solution.t / 3600, solution.y[0]  # Convert time to hours
            
        except Exception as e:
            print(f"Error during simulation: {str(e)}")
            raise
    
    def plot_results(self, time_points, temperature_points):
        """
        Plot the simulation results.
        
        Args:
            time_points (array): Time points in hours.
            temperature_points (array): Temperature points in °C.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(time_points, temperature_points, label='Indoor Temperature')
        plt.axhline(y=self.outside_temp, color='r', linestyle='--', label='Outside Temperature')
        plt.xlabel('Time (hours)')
        plt.ylabel('Temperature (°C)')
        plt.title('Building Thermal Performance Simulation')
        plt.legend()
        plt.grid(True)
        plt.show()


# Example usage
if __name__ == "__main__":
    try:
        # Parameters for a small building (50 m² surface area, 150 m³ volume)
        model = BuildingThermalModel(
            area=50.0,
            volume=150.0,
            insulation_thickness=0.1,  # 10 cm insulation
            initial_temp=22.0,
            outside_temp=5.0
        )
        
        # Simulate for 24 hours with 5-minute time steps
        time, temperature = model.simulate(duration_hours=24, time_step_minutes=5)
        
        # Plot results
        model.plot_results(time, temperature)
        
    except Exception as e:
        print(f"Error in simulation: {str(e)}")
```
