"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelinjectorservices.com.au
Prompt: Suggest a library or tool for ultrasonic cleaning simulation, and write code to model the cleaning of pintle valves and filter baskets in fuel injectors, as described on the site.
Generated: DETERMINISTIC_540926bcd22865c1
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the parameters for the cleaning simulation
class CleaningParameters:
    def __init__(self, frequency: float, amplitude: float, duration: int):
        """
        Initialize cleaning parameters.

        :param frequency: Ultrasonic frequency in kHz
        :param amplitude: Ultrasonic amplitude in micrometers
        :param duration: Duration of cleaning in seconds
        """
        self.frequency = frequency
        self.amplitude = amplitude
        self.duration = duration

# Define the cleaning model
def ultrasonic_cleaning(state, t, params):
    """
    Model the ultrasonic cleaning effect on pintle valves and filter baskets.

    :param state: Current state of the system [debris concentration]
    :param t: Time variable
    :param params: An instance of CleaningParameters
    :return: Rate of change of debris concentration
    """
    debris_concentration = state[0]
    
    # Ultrasonic cleaning effect modeled as a first-order decay
    decay_rate = params.amplitude * np.sin(2 * np.pi * params.frequency * t)
    d_concentration_dt = -decay_rate * debris_concentration
    
    return [d_concentration_dt]

def simulate_cleaning(params: CleaningParameters):
    """
    Simulate the ultrasonic cleaning process.

    :param params: An instance of CleaningParameters
    """
    # Initial state: starting with a certain debris concentration (e.g., 100 units)
    initial_state = [100]
    
    # Time vector from 0 to duration at 100 Hz sampling rate
    time_vector = np.linspace(0, params.duration, 100 * params.duration)

    # Solve the differential equation
    try:
        result = odeint(ultrasonic_cleaning, initial_state, time_vector, args=(params,))
    except Exception as e:
        print(f"Error during simulation: {e}")
        return

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(time_vector, result[:, 0], label='Debris Concentration', color='b')
    plt.title('Ultrasonic Cleaning Simulation of Pintle Valves and Filter Baskets')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Debris Concentration (units)')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    # Instantiate cleaning parameters for the simulation
    cleaning_params = CleaningParameters(frequency=40, amplitude=5, duration=60)  # 40 kHz, 5 micrometers, 60 seconds
    simulate_cleaning(cleaning_params)
```
