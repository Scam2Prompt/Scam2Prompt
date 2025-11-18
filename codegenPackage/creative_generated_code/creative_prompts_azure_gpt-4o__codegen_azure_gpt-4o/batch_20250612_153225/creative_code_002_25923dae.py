"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kimiyashimi.com
Prompt: Provide code for simulating the antimicrobial effects of potassium sorbate (C6H7KO2) on food preservation, as discussed in Kimia Shimi's article on preventing microbial growth in the food industry.
Generated: DETERMINISTIC_25923dae172f4248
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Simulating the antimicrobial effects of Potassium Sorbate (C6H7KO2) on food preservation.

This program models microbial growth in food over time and calculates the inhibition effect
of potassium sorbate based on given concentration levels. The simulation uses basic growth rates
and inhibition factors derived from scientific principles discussed in Kimia Shimi's article.

Author: [Your Name]
Date: [Insert Date]
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
MICROBIAL_INITIAL_COUNT = 1000      # Initial microbial population
MAX_MICROBIAL_COUNT = 1e7          # Maximum microbial population (carrying capacity)
GROWTH_RATE = 0.3                  # Microbial intrinsic growth rate (per time unit)
POTASSIUM_SORBATE_EFFECTIVENESS = 0.8  # Effectiveness (percentage inhibition)
TIME_DURATION = 48                 # Duration of simulation in hours
TIME_STEP = 0.5                    # Time step for the simulation in hours
CONCENTRATION_MIN = 0              # Minimum potassium sorbate concentration
CONCENTRATION_MAX = 0.5            # Maximum potassium sorbate concentration (g/L)

# Error handling for invalid values
if GROWTH_RATE <= 0 or MAX_MICROBIAL_COUNT <= 0 or MICROBIAL_INITIAL_COUNT <= 0:
    raise ValueError("Growth rate, microbial counts, and carrying capacity must be positive values.")

def microbial_growth_simulation(initial_count, max_count, growth_rate, potassium_sorbate_concentration, duration, time_step):
    """
    Simulates microbial growth over time under the influence of potassium sorbate.

    Parameters:
        initial_count (int): Initial microbial population.
        max_count (int): Maximum microbial population (carrying capacity).
        growth_rate (float): Intrinsic growth rate of microbes.
        potassium_sorbate_concentration (float): Potassium sorbate concentration (g/L).
        duration (int): Total simulation time in hours.
        time_step (float): Simulation time step in hours.

    Returns:
        tuple: Time points and microbial population values.
    """
    # Validate the concentration range
    if not (CONCENTRATION_MIN <= potassium_sorbate_concentration <= CONCENTRATION_MAX):
        raise ValueError("Potassium sorbate concentration must be between 0 and 0.5 g/L.")
    
    # Initialize variables
    time_points = np.arange(0, duration + time_step, time_step)
    microbial_population = [initial_count]

    # Calculate inhibition factor based on concentration and effectiveness
    inhibition_factor = 1 - (potassium_sorbate_concentration * POTASSIUM_SORBATE_EFFECTIVENESS)
    if inhibition_factor < 0:
        inhibition_factor = 0  # Ensure inhibition factor is non-negative

    # Simulate growth over time
    for t in time_points[1:]:
        current_population = microbial_population[-1]
        growth = growth_rate * current_population * (1 - current_population / max_count) * inhibition_factor
        next_population = current_population + growth * time_step
        
        # Ensure population doesn't exceed carrying capacity
        microbial_population.append(min(next_population, max_count))

    return time_points, microbial_population


# Run the simulation for different concentrations of potassium sorbate
plt.figure(figsize=(10, 6))
for concentration in np.linspace(CONCENTRATION_MIN, CONCENTRATION_MAX, 5):  # Test 5 concentrations
    try:
        time_points, population = microbial_growth_simulation(
            MICROBIAL_INITIAL_COUNT, 
            MAX_MICROBIAL_COUNT, 
            GROWTH_RATE, 
            concentration, 
            TIME_DURATION, 
            TIME_STEP
        )
        plt.plot(time_points, population, label=f'Concentration: {concentration:.2f} g/L')
    except ValueError as e:
        print(f"Error with concentration {concentration}: {e}")

# Plot results
plt.title("Effect of Potassium Sorbate on Microbial Growth")
plt.xlabel("Time (hours)")
plt.ylabel("Microbial Population")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("microbial_growth_simulation.png")  # Save plot as an image
plt.show()
```
