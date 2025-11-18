"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cemnazmakine.com
Prompt: Write a Python script to simulate the cooling process in a "Soğutma ve Şoklama Makinesi," using parameters like temperature and cooling time, as described on the CEMNAZ Makine website.
Generated: DETERMINISTIC_7aeea8c00b10493d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class CoolingMachine:
    def __init__(self, initial_temperature: float, target_temperature: float, cooling_time: float):
        """
        Initializes the CoolingMachine with the given parameters.

        :param initial_temperature: The starting temperature of the material (in Celsius).
        :param target_temperature: The target temperature to reach (in Celsius).
        :param cooling_time: The estimated time to achieve the target temperature (in seconds).
        """
        self.initial_temperature = initial_temperature
        self.target_temperature = target_temperature
        self.cooling_time = cooling_time

    def validate_parameters(self):
        """
        Validates the input parameters to ensure they are reasonable.
        
        :raises ValueError: If the parameters are not valid.
        """
        if self.initial_temperature < self.target_temperature:
            raise ValueError("Initial temperature must be greater than target temperature.")
        if self.cooling_time <= 0:
            raise ValueError("Cooling time must be a positive number.")

    def simulate_cooling(self):
        """
        Simulates the cooling process, printing the temperature at regular intervals
        until the target temperature is reached.
        """
        self.validate_parameters()

        # Calculate the temperature decrement per interval
        temperature_difference = self.initial_temperature - self.target_temperature
        time_intervals = 10  # Number of intervals for the simulation
        interval_time = self.cooling_time / time_intervals
        temperature_decrement = temperature_difference / time_intervals

        current_temperature = self.initial_temperature

        print(f"Starting cooling process from {self.initial_temperature}°C to {self.target_temperature}°C.")
        
        for i in range(time_intervals):
            time.sleep(interval_time)  # Simulate time passing
            current_temperature -= temperature_decrement
            
            # Ensure we do not go below the target temperature
            if current_temperature < self.target_temperature:
                current_temperature = self.target_temperature

            print(f"Current temperature: {current_temperature:.2f}°C")

        print("Cooling process completed.")

if __name__ == "__main__":
    try:
        # Example parameters, these can be modified as per requirements
        initial_temp = 100.0  # Starting temperature in Celsius
        target_temp = -18.0    # Target temperature in Celsius
        cooling_duration = 60.0 # Duration in seconds to reach the target
        
        # Create an instance of CoolingMachine
        cooling_machine = CoolingMachine(initial_temp, target_temp, cooling_duration)

        # Start the cooling simulation
        cooling_machine.simulate_cooling()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
