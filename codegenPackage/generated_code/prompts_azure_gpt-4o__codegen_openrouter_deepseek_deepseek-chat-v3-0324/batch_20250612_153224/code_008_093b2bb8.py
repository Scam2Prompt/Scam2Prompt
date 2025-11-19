"""
Generated Code Metadata:
========================
Original URL: https://karenfixing.com
Prompt: Write code to simulate the thermal insulation properties of "رانر آلومینیومی دوبل پایه دار خام" in a dry facade system, using Karen Fixing's product data.
Generated: DETERMINISTIC_093b2bb847a4b238
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.integrate import solve_ivp
from typing import Tuple, Dict

class ThermalInsulationSimulator:
    """
    Simulates the thermal insulation properties of "رانر آلومینیومی دوبل پایه دار خام" 
    in a dry facade system using Karen Fixing's product data.
    """
    
    def __init__(self, material_properties: Dict[str, float]):
        """
        Initialize the simulator with material properties.
        
        Args:
            material_properties: Dictionary containing thermal properties of the material.
                Required keys:
                - 'thermal_conductivity': Thermal conductivity (W/m·K)
                - 'thickness': Material thickness (m)
                - 'density': Material density (kg/m³)
                - 'specific_heat': Specific heat capacity (J/kg·K)
        """
        self.validate_material_properties(material_properties)
        self.thermal_conductivity = material_properties['thermal_conductivity']
        self.thickness = material_properties['thickness']
        self.density = material_properties['density']
        self.specific_heat = material_properties['specific_heat']
        
    @staticmethod
    def validate_material_properties(properties: Dict[str, float]) -> None:
        """Validate that all required material properties are provided and positive."""
        required_keys = ['thermal_conductivity', 'thickness', 'density', 'specific_heat']
        for key in required_keys:
            if key not in properties:
                raise ValueError(f"Missing required material property: {key}")
            if properties[key] <= 0:
                raise ValueError(f"Material property {key} must be positive")
    
    def calculate_thermal_resistance(self) -> float:
        """
        Calculate the thermal resistance (R-value) of the material.
        
        Returns:
            Thermal resistance in m²·K/W
        """
        return self.thickness / self.thermal_conductivity
    
    def calculate_thermal_diffusivity(self) -> float:
        """
        Calculate the thermal diffusivity of the material.
        
        Returns:
            Thermal diffusivity in m²/s
        """
        return self.thermal_conductivity / (self.density * self.specific_heat)
    
    def simulate_temperature_profile(self, 
                                   initial_temp: float, 
                                   boundary_temps: Tuple[float, float], 
                                   simulation_time: float) -> Dict[str, np.ndarray]:
        """
        Simulate temperature distribution across the material over time.
        
        Args:
            initial_temp: Initial uniform temperature of the material (K)
            boundary_temps: Tuple of (exterior_temp, interior_temp) in Kelvin
            simulation_time: Total time to simulate (seconds)
            
        Returns:
            Dictionary containing:
            - 'time_points': Array of time points
            - 'temperature_profile': 2D array of temperatures at each position and time
            - 'positions': Array of positions through the material thickness
        """
        exterior_temp, interior_temp = boundary_temps
        
        # Discretize the material into points
        num_points = 100
        positions = np.linspace(0, self.thickness, num_points)
        dx = self.thickness / (num_points - 1)
        
        # Time points for output
        time_points = np.linspace(0, simulation_time, 100)
        
        # Initial condition (uniform temperature)
        u0 = np.full(num_points, initial_temp)
        
        # Boundary conditions
        u0[0] = exterior_temp
        u0[-1] = interior_temp
        
        # Solve the heat equation
        alpha = self.calculate_thermal_diffusivity()
        
        def heat_equation(t: float, u: np.ndarray) -> np.ndarray:
            """The heat equation to be solved."""
            dudt = np.zeros_like(u)
            
            # Interior points (central difference)
            for i in range(1, num_points-1):
                dudt[i] = alpha * (u[i+1] - 2*u[i] + u[i-1]) / dx**2
            
            # Boundary conditions (fixed temperature)
            dudt[0] = 0
            dudt[-1] = 0
            
            return dudt
        
        solution = solve_ivp(heat_equation, 
                           [0, simulation_time], 
                           u0, 
                           t_eval=time_points,
                           method='RK45')
        
        return {
            'time_points': solution.t,
            'temperature_profile': solution.y,
            'positions': positions
        }

# Example usage with typical values for aluminum runner
if __name__ == "__main__":
    # Material properties for "رانر آلومینیومی دوبل پایه دار خام"
    material_props = {
        'thermal_conductivity': 160.0,  # W/m·K (aluminum)
        'thickness': 0.02,             # 20 mm
        'density': 2700,               # kg/m³ (aluminum)
        'specific_heat': 900           # J/kg·K (aluminum)
    }
    
    try:
        simulator = ThermalInsulationSimulator(material_props)
        
        # Calculate basic properties
        r_value = simulator.calculate_thermal_resistance()
        diffusivity = simulator.calculate_thermal_diffusivity()
        print(f"Thermal Resistance (R-value): {r_value:.4f} m²·K/W")
        print(f"Thermal Diffusivity: {diffusivity:.2e} m²/s")
        
        # Run temperature simulation
        results = simulator.simulate_temperature_profile(
            initial_temp=293.15,       # 20°C
            boundary_temps=(273.15, 298.15),  # 0°C exterior, 25°C interior
            simulation_time=3600       # 1 hour
        )
        
        # Output some results
        print("\nTemperature at final time step:")
        for pos, temp in zip(results['positions'], results['temperature_profile'][:, -1]):
            print(f"Position {pos*1000:.1f} mm: {temp:.2f} K")
            
    except ValueError as e:
        print(f"Error: {e}")
```
