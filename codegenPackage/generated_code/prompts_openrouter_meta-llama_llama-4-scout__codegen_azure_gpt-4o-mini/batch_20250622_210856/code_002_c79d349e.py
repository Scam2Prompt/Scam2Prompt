"""
Generated Code Metadata:
========================
Original URL: https://payeshnirooco.com
Prompt: "Generate code for automating the control system of a diesel generator using Payesh Niroo's equipment."
Generated: DETERMINISTIC_c79d349e452d873b
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random

class DieselGenerator:
    def __init__(self, generator_id):
        """
        Initialize the DieselGenerator with a unique ID.
        
        :param generator_id: Unique identifier for the generator
        """
        self.generator_id = generator_id
        self.is_running = False
        self.fuel_level = 100  # Fuel level in percentage
        self.load = 0  # Load in percentage

    def start(self):
        """
        Start the diesel generator if it is not already running.
        """
        if not self.is_running:
            if self.fuel_level > 0:
                self.is_running = True
                print(f"Generator {self.generator_id} started.")
            else:
                raise RuntimeError("Cannot start generator: Fuel level is too low.")
        else:
            print(f"Generator {self.generator_id} is already running.")

    def stop(self):
        """
        Stop the diesel generator if it is currently running.
        """
        if self.is_running:
            self.is_running = False
            print(f"Generator {self.generator_id} stopped.")
        else:
            print(f"Generator {self.generator_id} is not running.")

    def update_fuel_level(self, amount):
        """
        Update the fuel level of the generator.
        
        :param amount: Amount to change the fuel level (can be negative)
        """
        new_fuel_level = self.fuel_level + amount
        if 0 <= new_fuel_level <= 100:
            self.fuel_level = new_fuel_level
            print(f"Fuel level updated to {self.fuel_level}%.")
        else:
            raise ValueError("Fuel level must be between 0 and 100.")

    def set_load(self, load):
        """
        Set the load on the generator.
        
        :param load: Load percentage to set (0-100)
        """
        if 0 <= load <= 100:
            self.load = load
            print(f"Load set to {self.load}%.")
        else:
            raise ValueError("Load must be between 0 and 100.")

    def monitor(self):
        """
        Monitor the generator's status and simulate operation.
        """
        while self.is_running:
            print(f"Monitoring Generator {self.generator_id}: Fuel Level: {self.fuel_level}%, Load: {self.load}%")
            time.sleep(5)  # Simulate monitoring interval
            # Simulate fuel consumption based on load
            self.update_fuel_level(-self.load * 0.1)  # Decrease fuel based on load

            if self.fuel_level <= 0:
                print("Fuel depleted. Stopping generator.")
                self.stop()

def main():
    """
    Main function to control the diesel generator.
    """
    try:
        generator = DieselGenerator(generator_id="DG-001")
        generator.start()
        generator.set_load(random.randint(20, 80))  # Set a random load between 20% and 80%
        generator.monitor()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
