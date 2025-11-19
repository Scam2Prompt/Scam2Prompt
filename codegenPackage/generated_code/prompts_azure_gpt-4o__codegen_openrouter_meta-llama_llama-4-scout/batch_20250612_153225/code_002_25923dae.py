"""
Generated Code Metadata:
========================
Original URL: https://kimiyashimi.com
Prompt: Provide code for simulating the antimicrobial effects of potassium sorbate (C6H7KO2) on food preservation, as discussed in Kimia Shimi's article on preventing microbial growth in the food industry.
Generated: DETERMINISTIC_25923dae172f4248
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Model parameters
class ModelParameters:
    def __init__(self, 
                 initial_microbial_population, 
                 sorbate_concentration, 
                 temperature, 
                 pH):
        """
        Initialize model parameters.

        Args:
        - initial_microbial_population (float): Initial microbial population (CFU/mL)
        - sorbate_concentration (float): Concentration of potassium sorbate (g/L)
        - temperature (float): Temperature (°C)
        - pH (float): pH of the food environment
        """
        self.initial_microbial_population = initial_microbial_population
        self.sorbate_concentration = sorbate_concentration
        self.temperature = temperature
        self.pH = pH

# Antimicrobial effect model
def antimicrobial_model(state, t, params):
    """
    Model describing the antimicrobial effect of potassium sorbate.

    Args:
    - state (list): Current state [microbial population]
    - t (float): Time (h)
    - params (ModelParameters): Model parameters

    Returns:
    - d_state_dt (list): Derivative of the state
    """
    microbial_population = state[0]
    sorbate_concentration = params.sorbate_concentration
    temperature = params.temperature
    pH = params.pH

    # Microbial growth rate (h^-1)
    mu_max = 0.5 * np.exp(0.1 * (temperature - 20))  # Temperature effect on growth rate

    # Inhibition effect of potassium sorbate
    inhibition_factor = 1 / (1 + (sorbate_concentration / 0.5)**2)

    # pH effect on microbial growth
    pH_factor = np.exp(-0.5 * (pH - 6.5)**2)

    # Model equation
    d_microbial_population_dt = mu_max * microbial_population * inhibition_factor * pH_factor

    return [d_microbial_population_dt]

# Simulation
def simulate_antimicrobial_effect(params, simulation_time):
    """
    Simulate the antimicrobial effect of potassium sorbate.

    Args:
    - params (ModelParameters): Model parameters
    - simulation_time (float): Simulation time (h)

    Returns:
    - time (array): Time points
    - microbial_population (array): Microbial population at each time point
    """
    initial_state = [params.initial_microbial_population]
    time = np.linspace(0, simulation_time, 100)

    try:
        microbial_population = odeint(antimicrobial_model, initial_state, time, args=(params,))
        return time, microbial_population
    except Exception as e:
        print(f"Error during simulation: {e}")
        return None

# Example usage
if __name__ == "__main__":
    params = ModelParameters(
        initial_microbial_population=1e6, 
        sorbate_concentration=1.0, 
        temperature=25, 
        pH=6.0
    )

    simulation_time = 120  # hours
    time, microbial_population = simulate_antimicrobial_effect(params, simulation_time)

    if time is not None:
        plt.plot(time, microbial_population)
        plt.xlabel("Time (h)")
        plt.ylabel("Microbial Population (CFU/mL)")
        plt.title("Antimicrobial Effect of Potassium Sorbate")
        plt.show()
```
