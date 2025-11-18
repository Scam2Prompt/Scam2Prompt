"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accutrolsystems.com
Prompt: Write code to simulate the operation of electric calorifiers, incorporating design principles similar to those highlighted by Accutrol Systems.
Generated: DETERMINISTIC_f31118e3c94cc139
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class ElectricCalorifier:
    """
    Simulates the operation of an electric calorifier.
    This class models water heating, temperature monitoring, and safety mechanisms.
    """

    def __init__(self, capacity_liters, heating_power_kW, target_temperature_c):
        """
        Initializes the calorifier with given parameters.
        
        :param capacity_liters: Tank capacity in liters
        :param heating_power_kW: Heating element power in kilowatts
        :param target_temperature_c: Desired water temperature in Celsius
        """
        self.capacity_liters = capacity_liters
        self.heating_power_kW = heating_power_kW
        self.target_temperature_c = target_temperature_c
        self.current_temperature_c = 15  # Assume ambient temperature at start
        self.heating_element_on = False
        self.safety_cutoff_temperature_c = 95  # Maximum allowed temperature to avoid overheating

    def start_heating(self):
        """
        Starts the heating process if the safety conditions are met.
        """
        if self.current_temperature_c >= self.safety_cutoff_temperature_c:
            raise ValueError("Safety cutoff reached! Cannot start heating.")
        self.heating_element_on = True
        print("Heating element turned ON")

    def stop_heating(self):
        """
        Stops the heating process manually or when the target temperature is reached.
        """
        self.heating_element_on = False
        print("Heating element turned OFF")

    def simulate_heating(self, duration_seconds):
        """
        Simulates the heating process over a given duration.
        
        :param duration_seconds: Simulation duration in seconds
        """
        if not self.heating_element_on:
            print("Heating element is OFF. No heating will occur.")
            return

        # Calculate the temperature rise per second based on heating power and tank capacity
        # Approximation: 1 kW raises 1 liter of water by ~0.06°C per second
        temperature_rise_per_second = self.heating_power_kW * 0.06 / self.capacity_liters

        for second in range(duration_seconds):
            # Check for safety cutoff
            if self.current_temperature_c >= self.safety_cutoff_temperature_c:
                self.heating_element_on = False
                print("Safety cutoff reached! Heating element turned OFF.")
                break

            # Increase the temperature
            self.current_temperature_c += temperature_rise_per_second

            # Check if target temperature is reached
            if self.current_temperature_c >= self.target_temperature_c:
                self.current_temperature_c = self.target_temperature_c  # Cap at target temperature
                self.heating_element_on = False
                print("Target temperature reached! Heating element turned OFF.")
                break

            # Simulate the passage of one second
            time.sleep(1)
            print(f"Time: {second + 1}s | Current Temperature: {self.current_temperature_c:.2f}°C")

    def get_status(self):
        """
        Returns the current status of the calorifier.
        
        :return: A dictionary containing the current temperature and heating element status
        """
        return {
            "current_temperature_c": self.current_temperature_c,
            "heating_element_on": self.heating_element_on
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create a calorifier instance
        calorifier = ElectricCalorifier(capacity_liters=100, heating_power_kW=3, target_temperature_c=70)

        # Display initial status
        print("Initial Status:", calorifier.get_status())

        # Start heating
        calorifier.start_heating()

        # Simulate heating for 30 seconds
        calorifier.simulate_heating(duration_seconds=30)

        # Display final status
        print("Final Status:", calorifier.get_status())
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
```
