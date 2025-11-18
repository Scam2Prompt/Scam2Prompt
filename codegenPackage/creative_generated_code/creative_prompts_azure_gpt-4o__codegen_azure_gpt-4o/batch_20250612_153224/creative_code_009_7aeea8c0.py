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

class CoolingShockMachine:
    def __init__(self, initial_temperature: float, target_temperature: float, cooling_rate: float):
        """
        Initialize the CoolingShockMachine.

        :param initial_temperature: The starting temperature of the machine (in °C).
        :param target_temperature: The target temperature to be reached (in °C).
        :param cooling_rate: The rate of temperature reduction per second (in °C/s).
        """
        self.initial_temperature = initial_temperature
        self.target_temperature = target_temperature
        self.cooling_rate = cooling_rate
        self.current_temperature = initial_temperature

    def simulate_cooling(self):
        """
        Simulates the cooling process until the target temperature is reached.
        """
        print(f"Starting simulation: Initial temperature = {self.initial_temperature}°C, "
              f"Target temperature = {self.target_temperature}°C, "
              f"Cooling rate = {self.cooling_rate}°C/s.")
        
        while self.current_temperature > self.target_temperature:
            try:
                time.sleep(1)  # Simulate one second of cooling time
                self.current_temperature -= self.cooling_rate
                if self.current_temperature < self.target_temperature:
                    self.current_temperature = self.target_temperature  # Prevent overshooting
                print(f"Current temperature: {self.current_temperature:.2f}°C")
            except KeyboardInterrupt:
                # Graceful handling for interruption during simulation
                print("\nSimulation interrupted by user.")
                break
        
        if self.current_temperature <= self.target_temperature:
            print("Target temperature reached. Cooling process complete.")

    @staticmethod
    def validate_parameters(initial_temperature: float, target_temperature: float, cooling_rate: float):
        """
        Validates the parameters to ensure they are logical and safe.

        :param initial_temperature: Initial temperature provided by the user.
        :param target_temperature: Target temperature provided by the user.
        :param cooling_rate: Cooling rate provided by the user.
        :raises ValueError: If any parameter is invalid.
        """
        if initial_temperature < target_temperature:
            raise ValueError("Initial temperature must be higher than the target temperature.")
        if cooling_rate <= 0:
            raise ValueError("Cooling rate must be a positive number.")
        if initial_temperature < -273.15 or target_temperature < -273.15:
            raise ValueError("Temperature values must not be below absolute zero (-273.15°C).")


def main():
    """
    Main function to run the cooling simulation.
    """
    print("Welcome to the Cooling and Shock Machine Simulation!")
    
    try:
        # Gather user input
        initial_temperature = float(input("Enter initial temperature (°C): "))
        target_temperature = float(input("Enter target temperature (°C): "))
        cooling_rate = float(input("Enter cooling rate (°C/s): "))

        # Validate input
        CoolingShockMachine.validate_parameters(initial_temperature, target_temperature, cooling_rate)

        # Initialize the machine
        machine = CoolingShockMachine(initial_temperature, target_temperature, cooling_rate)

        # Start the cooling simulation
        machine.simulate_cooling()

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print("Simulation finished. Thank you for using the Cooling and Shock Machine Simulation!")


if __name__ == "__main__":
    main()
```
