"""
Generated Code Metadata:
========================
Original URL: https://www.ablakvaros.hu
Prompt: Write a code snippet to simulate the airflow through the résszellőzős vasalat (ventilation fittings) of Aluplast ablak profiles.
Generated: DETERMINISTIC_4967879e10cc8a5a
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
from scipy.integrate import solve_ivp
from typing import Tuple, Callable

class VentilationSimulation:
    """
    Simulates airflow through Aluplast window profile ventilation fittings.
    Models pressure differentials and airflow rates based on physical properties.
    """
    
    def __init__(self, 
                 fitting_diameter: float = 0.005,  # meters
                 fitting_length: float = 0.02,    # meters
                 num_fittings: int = 4,
                 air_density: float = 1.225,      # kg/m³
                 air_viscosity: float = 1.81e-5,  # Pa·s
                 pressure_diff_range: Tuple[float, float] = (0, 50)):  # Pa
        
        self.fitting_diameter = fitting_diameter
        self.fitting_length = fitting_length
        self.num_fittings = num_fittings
        self.air_density = air_density
        self.air_viscosity = air_viscosity
        self.pressure_diff_range = pressure_diff_range
        
        # Cross-sectional area of one fitting
        self.fitting_area = np.pi * (fitting_diameter / 2)**2
        
    def _calculate_reynolds(self, velocity: float) -> float:
        """Calculate Reynolds number for given flow velocity."""
        return (self.air_density * velocity * self.fitting_diameter) / self.air_viscosity
    
    def _calculate_friction_factor(self, reynolds: float) -> float:
        """
        Calculate Darcy friction factor using Churchill's equation.
        Valid for all flow regimes (laminar, transitional, turbulent).
        """
        if reynolds == 0:
            return 0
            
        A = (2.457 * np.log(1 / ((7/reynolds)**0.9 + 0.27*(0.0001/self.fitting_diameter))))**16
        B = (37530/reynolds)**16
        return 8 * ((8/reynolds)**12 + 1/((A+B)**1.5))**(1/12)
    
    def _pressure_loss(self, velocity: float) -> float:
        """
        Calculate pressure loss through fittings using Darcy-Weisbach equation.
        Includes minor losses (entrance/exit effects) approximated as 1.5 velocity heads.
        """
        if velocity == 0:
            return 0
            
        reynolds = self._calculate_reynolds(velocity)
        friction_factor = self._calculate_friction_factor(reynolds)
        
        # Major losses + minor losses (K=1.5)
        pressure_loss = (friction_factor * (self.fitting_length/self.fitting_diameter) + 1.5) * \
                       (0.5 * self.air_density * velocity**2)
        
        return pressure_loss * self.num_fittings
    
    def calculate_flow_rate(self, pressure_diff: float) -> float:
        """
        Calculate volumetric flow rate through all fittings for given pressure difference.
        Uses iterative solution to Darcy-Weisbach equation.
        """
        if pressure_diff <= 0:
            return 0.0
            
        # Initial guess using simplified Bernoulli
        v_guess = np.sqrt(2 * pressure_diff / self.air_density)
        
        # Solve iteratively
        tolerance = 1e-6
        max_iter = 100
        for _ in range(max_iter):
            loss = self._pressure_loss(v_guess)
            error = pressure_diff - loss
            
            if abs(error) < tolerance:
                break
                
            # Newton-Raphson adjustment
            dv = 0.001 * v_guess
            loss_derivative = (self._pressure_loss(v_guess + dv) - loss) / dv
            v_guess += error / loss_derivative if loss_derivative != 0 else 0
        else:
            raise ValueError("Flow rate calculation did not converge")
        
        return v_guess * self.fitting_area * self.num_fittings
    
    def simulate_airflow(self, 
                         external_pressure_fn: Callable[[float], float],
                         time_span: Tuple[float, float] = (0, 3600),
                         initial_conditions: float = 0.0) -> dict:
        """
        Simulate dynamic airflow response to changing external pressure conditions.
        
        Args:
            external_pressure_fn: Function that returns external pressure difference (Pa) at time t
            time_span: Simulation time range (seconds)
            initial_conditions: Initial flow rate (m³/s)
            
        Returns:
            Dictionary with time points and corresponding flow rates
        """
        def system_ode(t: float, q: float) -> float:
            """ODE representing the rate of change of flow rate."""
            current_pressure = external_pressure_fn(t)
            target_flow = self.calculate_flow_rate(current_pressure)
            
            # Simple first-order response model (time constant ~0.1s)
            tau = 0.1  # seconds
            return (target_flow - q) / tau
            
        # Solve the ODE
        solution = solve_ivp(system_ode, 
                            time_span, 
                            [initial_conditions], 
                            t_eval=np.linspace(time_span[0], time_span[1], 1000))
        
        return {
            'time': solution.t,
            'flow_rate': solution.y[0],
            'pressure': [external_pressure_fn(t) for t in solution.t]
        }

# Example usage
if __name__ == "__main__":
    # Create simulation for standard Aluplast fittings
    sim = VentilationSimulation()
    
    # Define a sample pressure variation (e.g., wind gust)
    def pressure_variation(t):
        if t < 1:
            return 5  # Pa
        elif t < 2:
            return 20  # Pa (gust)
        else:
            return 10  # Pa
            
    # Run simulation
    results = sim.simulate_airflow(pressure_variation, time_span=(0, 5))
    
    # Output results (in production, would save to file or visualize)
    print("Time (s)\tFlow Rate (m³/s)\tPressure (Pa)")
    for t, q, p in zip(results['time'], results['flow_rate'], results['pressure']):
        print(f"{t:.2f}\t{q:.6f}\t{p:.2f}")
```
