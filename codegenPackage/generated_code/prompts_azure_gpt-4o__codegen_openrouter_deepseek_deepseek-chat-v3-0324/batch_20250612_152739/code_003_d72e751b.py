"""
Generated Code Metadata:
========================
Original URL: https://aprisacv.com.mx
Prompt: Write a Python program to simulate heat transfer in a furnace wall using Aprisacv's ceramic paper (ApriPaper) as insulation, based on its thickness and thermal properties.
Generated: DETERMINISTIC_d72e751bcb655798
Batch ID: 20250612_152739
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

class FurnaceWallSimulator:
    """
    Simulates heat transfer through a furnace wall insulated with ApriPaper ceramic insulation.
    
    Attributes:
        thickness (float): Thickness of the ApriPaper insulation layer (meters).
        thermal_conductivity (float): Thermal conductivity of ApriPaper (W/m·K).
        inner_temp (float): Inner wall temperature (K).
        outer_temp (float): Outer wall temperature (K).
        area (float): Cross-sectional area of the wall (m²).
    """
    
    def __init__(self, thickness=0.05, thermal_conductivity=0.12, inner_temp=1000.0, outer_temp=300.0, area=1.0):
        """
        Initialize the furnace wall simulator with default or provided parameters.
        
        Args:
            thickness (float): Thickness of ApriPaper (m).
            thermal_conductivity (float): Thermal conductivity of ApriPaper (W/m·K).
            inner_temp (float): Inner wall temperature (K).
            outer_temp (float): Outer wall temperature (K).
            area (float): Cross-sectional area (m²).
        """
        self.thickness = thickness
        self.thermal_conductivity = thermal_conductivity
        self.inner_temp = inner_temp
        self.outer_temp = outer_temp
        self.area = area
        
        # Validate inputs
        if thickness <= 0:
            raise ValueError("Thickness must be positive.")
        if thermal_conductivity <= 0:
            raise ValueError("Thermal conductivity must be positive.")
        if inner_temp <= outer_temp:
            raise ValueError("Inner temperature must be greater than outer temperature.")
        if area <= 0:
            raise ValueError("Area must be positive.")
    
    def calculate_heat_flux(self):
        """
        Calculate heat flux through the wall using Fourier's law.
        
        Returns:
            float: Heat flux (W/m²).
        """
        delta_temp = self.inner_temp - self.outer_temp
        heat_flux = (self.thermal_conductivity * delta_temp) / self.thickness
        return heat_flux
    
    def calculate_total_heat_transfer(self):
        """
        Calculate total heat transfer rate through the wall.
        
        Returns:
            float: Total heat transfer rate (W).
        """
        heat_flux = self.calculate_heat_flux()
        total_heat = heat_flux * self.area
        return total_heat
    
    def temperature_profile(self, num_points=100):
        """
        Generate temperature profile across the wall thickness.
        
        Args:
            num_points (int): Number of points to calculate temperature.
            
        Returns:
            tuple: (positions, temperatures) arrays.
        """
        positions = np.linspace(0, self.thickness, num_points)
        temperatures = self.inner_temp - (self.inner_temp - self.outer_temp) * (positions / self.thickness)
        return positions, temperatures
    
    def plot_temperature_profile(self):
        """Plot the temperature profile across the wall thickness."""
        positions, temperatures = self.temperature_profile()
        
        plt.figure(figsize=(8, 6))
        plt.plot(positions, temperatures, 'r-', linewidth=2)
        plt.title('Temperature Profile Across Furnace Wall')
        plt.xlabel('Wall Thickness (m)')
        plt.ylabel('Temperature (K)')
        plt.grid(True)
        plt.show()
    
    def optimize_thickness(self, max_heat_flux, min_thickness=0.001, max_thickness=0.5, tolerance=1e-3):
        """
        Find the minimum thickness that keeps heat flux below a specified value.
        
        Args:
            max_heat_flux (float): Maximum allowed heat flux (W/m²).
            min_thickness (float): Minimum thickness to consider (m).
            max_thickness (float): Maximum thickness to consider (m).
            tolerance (float): Convergence tolerance.
            
        Returns:
            float: Optimal thickness (m).
        """
        if max_heat_flux <= 0:
            raise ValueError("Maximum heat flux must be positive.")
            
        def heat_flux_func(t):
            self.thickness = t
            return self.calculate_heat_flux() - max_heat_flux
        
        # Use bisection method to find optimal thickness
        a, b = min_thickness, max_thickness
        while (b - a) > tolerance:
            c = (a + b) / 2
            if heat_flux_func(c) < 0:
                b = c
            else:
                a = c
        
        optimal_thickness = (a + b) / 2
        return optimal_thickness

# Example usage
if __name__ == "__main__":
    try:
        # Create furnace wall simulator with default parameters
        simulator = FurnaceWallSimulator()
        
        # Calculate and print results
        heat_flux = simulator.calculate_heat_flux()
        total_heat = simulator.calculate_total_heat_transfer()
        
        print(f"Heat Flux: {heat_flux:.2f} W/m²")
        print(f"Total Heat Transfer: {total_heat:.2f} W")
        
        # Plot temperature profile
        simulator.plot_temperature_profile()
        
        # Find optimal thickness for a given heat flux constraint
        max_flux = 1000.0  # W/m²
        optimal_thickness = simulator.optimize_thickness(max_flux)
        print(f"Optimal thickness for max flux {max_flux} W/m²: {optimal_thickness:.4f} m")
        
    except ValueError as e:
        print(f"Error: {e}")
```
