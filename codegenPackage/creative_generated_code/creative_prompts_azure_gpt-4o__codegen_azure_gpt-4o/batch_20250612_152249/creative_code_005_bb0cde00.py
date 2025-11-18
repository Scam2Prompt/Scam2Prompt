"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://novaforma.hr
Prompt: Write code to simulate thermal processing of plexiglass for creating custom signage, referencing Nova Forma's capabilities and equipment.
Generated: DETERMINISTIC_bb0cde007bf926be
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Simulates thermal processing of plexiglass for creating custom signage, referencing Nova Forma's capabilities and equipment.
This script models temperature control, timing, and quality checks during the process.
"""

import time
import random

class ThermalProcessor:
    """
    A class to simulate the thermal processing of plexiglass.
    """
    def __init__(self, max_temperature, duration, equipment_name):
        """
        Initialize the thermal processor.

        :param max_temperature: The maximum allowable temperature for processing (in degrees Celsius).
        :param duration: The time (in seconds) to process the plexiglass.
        :param equipment_name: Name of the equipment used in processing.
        """
        self.max_temperature = max_temperature
        self.duration = duration
        self.equipment_name = equipment_name
        self.current_temperature = 0

    def heat_up(self):
        """
        Gradually heats up the plexiglass to the target temperature.
        Includes safety checks to ensure it doesn't exceed the maximum temperature.
        """
        print(f"Heating up plexiglass using {self.equipment_name}...")
        try:
            while self.current_temperature < self.max_temperature:
                self.current_temperature += random.randint(5, 10)  # Simulating temperature increase
                if self.current_temperature > self.max_temperature:
                    raise ValueError("Temperature exceeded maximum limit! Shutting down for safety.")
                print(f"Current Temperature: {self.current_temperature}°C")
                time.sleep(0.5)  # Simulating real-time processing
        except ValueError as e:
            print(e)
            self.shutdown()
            return False
        return True

    def maintain_temperature(self):
        """
        Maintains the target temperature for the specified duration.
        """
        print(f"Maintaining temperature at {self.max_temperature}°C for {self.duration} seconds...")
        start_time = time.time()
        while time.time() - start_time < self.duration:
            time.sleep(1)  # Simulating real-time processing
            # Random fluctuation simulation
            fluctuation = random.randint(-2, 2)
            self.current_temperature += fluctuation
            # Safety check
            if self.current_temperature > self.max_temperature:
                print("Temperature exceeded maximum limit during maintenance! Shutting down...")
                self.shutdown()
                return False
            elif self.current_temperature < self.max_temperature - 10:
                print("Temperature dropped too low during maintenance! Shutting down...")
                self.shutdown()
                return False
            print(f"Current Temperature: {self.current_temperature}°C")
        return True

    def cooldown(self):
        """
        Gradually cools down the plexiglass to room temperature.
        """
        print("Cooling down plexiglass...")
        try:
            while self.current_temperature > 25:  # Assuming room temperature is 25°C
                self.current_temperature -= random.randint(5, 10)  # Simulating temperature decrease
                if self.current_temperature < 25:
                    self.current_temperature = 25  # Avoid dropping below room temperature
                print(f"Current Temperature: {self.current_temperature}°C")
                time.sleep(0.5)
        except Exception as e:
            print(f"Error during cooldown: {e}")
            self.shutdown()
            return False
        print("Cooldown complete. Plexiglass is ready for next processing step.")
        return True

    def shutdown(self):
        """
        Safely shuts down the equipment in case of an error or manual stop.
        """
        print(f"Shutting down {self.equipment_name}...")
        self.current_temperature = 0
        print("Equipment safely shut down.")

def simulate_thermal_processing():
    """
    Simulates the complete thermal processing workflow for plexiglass.
    """
    # Nova Forma's sample equipment capabilities
    equipment_name = "Nova Forma Thermal Processor Model X"
    max_temperature = 160  # Maximum temperature in degrees Celsius
    duration = 30  # Duration to maintain maximum temperature (in seconds)

    processor = ThermalProcessor(max_temperature, duration, equipment_name)

    # Step 1: Heat up the plexiglass
    if not processor.heat_up():
        return

    # Step 2: Maintain temperature
    if not processor.maintain_temperature():
        return

    # Step 3: Cool down the plexiglass
    if not processor.cooldown():
        return

    print("Thermal processing completed successfully!")

# Run the simulation
if __name__ == "__main__":
    simulate_thermal_processing()
```
