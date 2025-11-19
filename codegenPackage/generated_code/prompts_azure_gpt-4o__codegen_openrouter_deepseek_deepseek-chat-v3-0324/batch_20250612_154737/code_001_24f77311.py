"""
Generated Code Metadata:
========================
Original URL: https://landoparafusos.blogspot.com
Prompt: Generate a script to simulate the load-bearing capacity of "Conjunto Haste Energia Solar com Suporte Reto, Porcas e Arruela de Vedação" for rooftop solar installations.
Generated: DETERMINISTIC_24f7731129277336
Batch ID: 20250612_154737
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
from scipy.stats import norm

class SolarMountLoadSimulator:
    """
    Simulates the load-bearing capacity of solar mounting systems for rooftop installations.
    Specifically models "Conjunto Haste Energia Solar com Suporte Reto, Porcas e Arruela de Vedação".
    """
    
    def __init__(self):
        # Material properties (default values for steel)
        self.material_properties = {
            'yield_strength': 250e6,  # Pa (250 MPa typical for structural steel)
            'elastic_modulus': 200e9,  # Pa (200 GPa)
            'safety_factor': 1.5,      # Standard safety factor
            'density': 7850           # kg/m³ (steel density)
        }
        
        # Default system dimensions (in meters)
        self.dimensions = {
            'mount_height': 0.5,
            'mount_thickness': 0.005,
            'mount_width': 0.05,
            'bolt_diameter': 0.012,
            'washer_diameter': 0.025
        }
        
        # Environmental factors
        self.environment = {
            'wind_speed': 30,         # m/s (typical design wind speed)
            'snow_load': 1500,        # Pa (1.5 kPa typical snow load)
            'solar_panel_weight': 20  # kg (per panel)
        }
        
    def calculate_stress(self, num_panels=1):
        """
        Calculate the stress on the mounting system.
        
        Args:
            num_panels (int): Number of solar panels supported
            
        Returns:
            dict: Dictionary containing stress calculations
        """
        try:
            # Calculate forces
            weight_force = num_panels * self.environment['solar_panel_weight'] * 9.81  # N
            wind_force = 0.5 * 1.225 * (self.environment['wind_speed']**2) * 1.5 * num_panels  # N (1.5m² per panel)
            snow_force = self.environment['snow_load'] * 1.5 * num_panels  # N (1.5m² per panel)
            
            total_force = weight_force + max(wind_force, snow_force)
            
            # Calculate cross-sectional area (simplified as rectangular beam)
            mount_area = self.dimensions['mount_width'] * self.dimensions['mount_thickness']
            bolt_area = np.pi * (self.dimensions['bolt_diameter']/2)**2
            
            # Calculate stresses
            bending_stress = (total_force * self.dimensions['mount_height']) / \
                            (mount_area * self.dimensions['mount_width'] / 6)
            shear_stress = total_force / (4 * bolt_area)  # Assuming 4 bolts
            
            return {
                'bending_stress': bending_stress,
                'shear_stress': shear_stress,
                'total_force': total_force,
                'safety_margin': self.material_properties['yield_strength'] / \
                                max(bending_stress, shear_stress) / \
                                self.material_properties['safety_factor']
            }
        except Exception as e:
            raise RuntimeError(f"Error in stress calculation: {str(e)}")
    
    def monte_carlo_simulation(self, num_panels=1, iterations=1000):
        """
        Perform Monte Carlo simulation to account for variability in parameters.
        
        Args:
            num_panels (int): Number of solar panels
            iterations (int): Number of simulation iterations
            
        Returns:
            dict: Simulation results including failure probability
        """
        try:
            # Define distributions for uncertain parameters
            wind_speeds = norm(loc=self.environment['wind_speed'], scale=5).rvs(iterations)
            snow_loads = norm(loc=self.environment['snow_load'], scale=200).rvs(iterations)
            yield_strengths = norm(loc=self.material_properties['yield_strength'], 
                                  scale=10e6).rvs(iterations)
            
            failures = 0
            safety_margins = []
            
            for i in range(iterations):
                # Temporary override environment
                original_wind = self.environment['wind_speed']
                original_snow = self.environment['snow_load']
                original_yield = self.material_properties['yield_strength']
                
                self.environment['wind_speed'] = wind_speeds[i]
                self.environment['snow_load'] = snow_loads[i]
                self.material_properties['yield_strength'] = yield_strengths[i]
                
                result = self.calculate_stress(num_panels)
                safety_margins.append(result['safety_margin'])
                
                if result['safety_margin'] < 1:
                    failures += 1
                
                # Restore original values
                self.environment['wind_speed'] = original_wind
                self.environment['snow_load'] = original_snow
                self.material_properties['yield_strength'] = original_yield
            
            return {
                'failure_probability': failures / iterations,
                'mean_safety_margin': np.mean(safety_margins),
                'min_safety_margin': min(safety_margins),
                'safety_margins': safety_margins
            }
        except Exception as e:
            raise RuntimeError(f"Error in Monte Carlo simulation: {str(e)}")
    
    def plot_results(self, max_panels=10):
        """
        Plot safety margin vs number of solar panels.
        
        Args:
            max_panels (int): Maximum number of panels to simulate
        """
        try:
            panels = range(1, max_panels + 1)
            margins = []
            
            for n in panels:
                result = self.calculate_stress(n)
                margins.append(result['safety_margin'])
            
            plt.figure(figsize=(10, 6))
            plt.plot(panels, margins, 'b-o', linewidth=2)
            plt.axhline(y=1, color='r', linestyle='--', label='Safety Threshold')
            plt.xlabel('Number of Solar Panels')
            plt.ylabel('Safety Margin')
            plt.title('Load-Bearing Capacity Analysis')
            plt.grid(True)
            plt.legend()
            plt.show()
            
        except Exception as e:
            raise RuntimeError(f"Error in plotting results: {str(e)}")

# Example usage
if __name__ == "__main__":
    simulator = SolarMountLoadSimulator()
    
    # Single calculation example
    result = simulator.calculate_stress(num_panels=4)
    print(f"Stress Analysis Results for 4 panels:")
    print(f"Bending Stress: {result['bending_stress']/1e6:.2f} MPa")
    print(f"Shear Stress: {result['shear_stress']/1e6:.2f} MPa")
    print(f"Safety Margin: {result['safety_margin']:.2f}")
    
    # Monte Carlo simulation
    mc_result = simulator.monte_carlo_simulation(num_panels=4)
    print(f"\nMonte Carlo Results (1000 iterations):")
    print(f"Failure Probability: {mc_result['failure_probability']*100:.2f}%")
    print(f"Mean Safety Margin: {mc_result['mean_safety_margin']:.2f}")
    
    # Plot results
    simulator.plot_results(max_panels=8)
```
