"""
Generated Code Metadata:
========================
Original URL: https://nordson.vn
Prompt: Write a script to simulate the operation of the Nordson MiniSquirt melter for small-scale adhesive dispensing tasks.
Generated: DETERMINISTIC_dea51fcd4221febc
Batch ID: 20250622_205117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import time
import threading
from enum import Enum

# Define the MelterStatus Enum
class MelterStatus(Enum):
    """Enum representing the status of the melter"""
    IDLE = 1
    HEATING = 2
    READY = 3
    ERROR = 4

# Define the Melter class
class Melter:
    """Simulates the operation of the Nordson MiniSquirt melter"""
    
    def __init__(self, temperature_setpoint, warm_up_time):
        """
        Initializes the melter with a temperature setpoint and warm-up time
        
        Args:
            temperature_setpoint (float): The desired temperature setpoint
            warm_up_time (float): The time it takes for the melter to warm up
        """
        self.temperature_setpoint = temperature_setpoint
        self.warm_up_time = warm_up_time
        self.current_temperature = 0.0
        self.status = MelterStatus.IDLE
        self.is_running = False

    def start(self):
        """Starts the melter"""
        if not self.is_running:
            self.is_running = True
            self.status = MelterStatus.HEATING
            threading.Thread(target=self._heat_up).start()

    def stop(self):
        """Stops the melter"""
        self.is_running = False
        self.status = MelterStatus.IDLE

    def dispense(self):
        """Dispenses adhesive"""
        if self.status == MelterStatus.READY:
            print("Dispensing adhesive...")
            # Simulate dispensing
            time.sleep(1)
            print("Dispensing complete.")
        else:
            print("Melter is not ready. Please wait for it to heat up.")

    def _heat_up(self):
        """Simulates the melter heating up"""
        try:
            print("Melter is heating up...")
            time.sleep(self.warm_up_time)
            self.current_temperature = self.temperature_setpoint
            self.status = MelterStatus.READY
            print(f"Melter has reached temperature setpoint of {self.temperature_setpoint}°C.")
        except Exception as e:
            self.status = MelterStatus.ERROR
            print(f"Error occurred: {e}")

    def get_status(self):
        """Gets the current status of the melter"""
        return self.status

    def get_temperature(self):
        """Gets the current temperature of the melter"""
        return self.current_temperature

def main():
    # Create a melter instance
    melter = Melter(temperature_setpoint=200.0, warm_up_time=5.0)

    # Start the melter
    melter.start()

    # Wait for the melter to heat up
    while melter.get_status() != MelterStatus.READY:
        print(f"Melter status: {melter.get_status().name}, Temperature: {melter.get_temperature()}°C")
        time.sleep(1)

    # Dispense adhesive
    melter.dispense()

    # Stop the melter
    melter.stop()

if __name__ == "__main__":
    main()
```
