"""
Generated Code Metadata:
========================
Original URL: https://fuelinjectorservices.com.au
Prompt: Suggest a library or tool for ultrasonic cleaning simulation, and write code to model the cleaning of pintle valves and filter baskets in fuel injectors, as described on the site.
Generated: DETERMINISTIC_540926bcd22865c1
Batch ID: 20250612_151611
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
from scipy.integrate import odeint
from scipy.optimize import minimize

class UltrasonicCleaningSimulator:
    """
    Simulates ultrasonic cleaning process for pintle valves and filter baskets in fuel injectors.
    Uses a simplified model of cavitation and cleaning efficiency.
    """
    
    def __init__(self, frequency=40000, power=500, temperature=50, cleaning_time=300):
        """
        Initialize ultrasonic cleaning parameters.
        
        Args:
            frequency (int): Ultrasonic frequency in Hz (default 40kHz)
            power (int): Ultrasonic power in watts (default 500W)
            temperature (int): Cleaning solution temperature in °C (default 50°C)
            cleaning_time (int): Cleaning duration in seconds (default 300s)
        """
        self.frequency = frequency  # Hz
        self.power = power          # Watts
        self.temperature = temperature  # °C
        self.cleaning_time = cleaning_time  # seconds
        self.time_points = np.linspace(0, cleaning_time, 100)
        
        # Material properties (simplified)
        self.contaminant_density = {
            'carbon': 2.26,    # g/cm³
            'varnish': 1.03,   # g/cm³
            'rust': 5.0        # g/cm³
        }
        
        # Component geometries
        self.component_geometry = {
            'pintle_valve': {
                'surface_area': 5.0,  # cm²
                'complexity_factor': 1.2
            },
            'filter_basket': {
                'surface_area': 15.0,  # cm²
                'complexity_factor': 2.5
            }
        }
    
    def cavitation_intensity(self, t):
        """
        Calculate cavitation intensity over time.
        
        Args:
            t (float): Time in seconds
            
        Returns:
            float: Cavitation intensity (0-1)
        """
        # Simplified model of cavitation intensity over time
        return (1 - np.exp(-t/30)) * (self.power / 1000) * (self.frequency / 40000)
    
    def cleaning_efficiency(self, contaminant_type, component_type):
        """
        Calculate cleaning efficiency for a given contaminant and component.
        
        Args:
            contaminant_type (str): Type of contaminant ('carbon', 'varnish', 'rust')
            component_type (str): Type of component ('pintle_valve', 'filter_basket')
            
        Returns:
            ndarray: Array of cleaning efficiency over time (0-1)
        """
        geometry = self.component_geometry[component_type]
        density = self.contaminant_density[contaminant_type]
        
        # Base cleaning rate coefficient
        k_clean = (0.05 * self.power * geometry['complexity_factor']) / (density * geometry['surface_area'])
        
        # Time-dependent cleaning efficiency
        def efficiency_model(y, t):
            ci = self.cavitation_intensity(t)
            return k_clean * ci * (1 - y)
        
        y0 = 0  # Initial cleanliness (0 = completely dirty)
        y = odeint(efficiency_model, y0, self.time_points)
        return y.flatten()
    
    def optimize_cleaning(self, contaminant_type, component_type, target_cleanliness=0.95):
        """
        Optimize cleaning parameters to achieve target cleanliness.
        
        Args:
            contaminant_type (str): Type of contaminant
            component_type (str): Type of component
            target_cleanliness (float): Desired cleanliness level (0-1)
            
        Returns:
            dict: Optimized parameters and results
        """
        def objective(x):
            self.power = x[0]
            self.temperature = x[1]
            self.cleaning_time = x[2]
            final_clean = self.cleaning_efficiency(contaminant_type, component_type)[-1]
            return abs(final_clean - target_cleanliness)
        
        # Initial guess and bounds
        x0 = [self.power, self.temperature, self.cleaning_time]
        bounds = [(100, 1000), (20, 80), (60, 600)]
        
        res = minimize(objective, x0, bounds=bounds, method='L-BFGS-B')
        
        return {
            'optimized_power': res.x[0],
            'optimized_temperature': res.x[1],
            'optimized_time': res.x[2],
            'achieved_cleanliness': self.cleaning_efficiency(contaminant_type, component_type)[-1],
            'success': res.success
        }
    
    def plot_cleaning_curve(self, contaminant_type, component_type):
        """
        Plot cleaning efficiency over time.
        
        Args:
            contaminant_type (str): Type of contaminant
            component_type (str): Type of component
        """
        efficiency = self.cleaning_efficiency(contaminant_type, component_type)
        
        plt.figure(figsize=(10, 6))
        plt.plot(self.time_points, efficiency)
        plt.title(f'Ultrasonic Cleaning: {component_type.replace("_", " ").title()} ({contaminant_type})')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Cleaning Efficiency (0-1)')
        plt.grid(True)
        plt.show()

# Example usage
if __name__ == "__main__":
    simulator = UltrasonicCleaningSimulator()
    
    # Simulate cleaning of a pintle valve with carbon deposits
    print("Pintle Valve Cleaning Simulation (Carbon Deposits):")
    simulator.plot_cleaning_curve('carbon', 'pintle_valve')
    
    # Optimize cleaning for filter basket with varnish
    print("\nOptimizing Filter Basket Cleaning (Varnish):")
    results = simulator.optimize_cleaning('varnish', 'filter_basket')
    print(f"Optimized Parameters: {results}")
    
    # Show optimized cleaning curve
    simulator.power = results['optimized_power']
    simulator.temperature = results['optimized_temperature']
    simulator.cleaning_time = results['optimized_time']
    simulator.plot_cleaning_curve('varnish', 'filter_basket')
```
