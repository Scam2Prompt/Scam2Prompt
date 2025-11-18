"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dotcomachinery.co.tz
Prompt: Write Python code to simulate the operation of a pressure washer, referencing the specifications of the Karcher K7 Pressure Washer listed on Dotcom Machinery's website.
Generated: DETERMINISTIC_07e7ea72a4a7e540
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class PressureWasher:
    """
    A class to simulate the operation of a pressure washer.
    This implementation references the specifications of the Karcher K7 Pressure Washer.
    """

    def __init__(self, max_pressure_bar, water_flow_rate_lpm, power_rating_w):
        """
        Initialize the pressure washer with its specifications.

        Args:
            max_pressure_bar (int): Maximum pressure in bars.
            water_flow_rate_lpm (int): Water flow rate in liters per minute.
            power_rating_w (int): Power rating in watts.
        """
        self.max_pressure_bar = max_pressure_bar
        self.water_flow_rate_lpm = water_flow_rate_lpm
        self.power_rating_w = power_rating_w
        self.is_running = False

    def start(self):
        """
        Start the pressure washer. Simulates the motor and system powering up.
        """
        if self.is_running:
            print("Pressure washer is already running.")
            return

        print("Starting the pressure washer...")
        time.sleep(1)  # Simulate startup delay
        self.is_running = True
        print(f"Pressure washer started. Max Pressure: {self.max_pressure_bar} bar, "
              f"Water Flow Rate: {self.water_flow_rate_lpm} L/min, Power Rating: {self.power_rating_w} W.")

    def stop(self):
        """
        Stop the pressure washer. Simulates the motor powering down.
        """
        if not self.is_running:
            print("Pressure washer is not running.")
            return

        print("Stopping the pressure washer...")
        time.sleep(1)  # Simulate shutdown delay
        self.is_running = False
        print("Pressure washer stopped.")

    def simulate_cleaning(self, duration_seconds):
        """
        Simulate a cleaning operation.

        Args:
            duration_seconds (int): Duration of the cleaning operation in seconds.
        """
        if not self.is_running:
            print("Cannot start cleaning. The pressure washer is not running.")
            return

        print(f"Starting cleaning operation for {duration_seconds} seconds...")
        for i in range(duration_seconds):
            if not self.is_running:
                print("Cleaning operation stopped prematurely.")
                return

            # Simulate cleaning progress with random efficiency
            cleaning_efficiency = round(random.uniform(0.8, 1.0), 2)
            print(f"Cleaning in progress... Efficiency: {cleaning_efficiency * 100:.2f}%")
            time.sleep(1)  # Simulate one second of work

        print("Cleaning operation completed.")

    def get_status(self):
        """
        Get the current status of the pressure washer.

        Returns:
            dict: A dictionary containing the current status of the pressure washer.
        """
        return {
            "is_running": self.is_running,
            "max_pressure_bar": self.max_pressure_bar,
            "water_flow_rate_lpm": self.water_flow_rate_lpm,
            "power_rating_w": self.power_rating_w
        }

# Main function to demonstrate the simulation
if __name__ == "__main__":
    try:
        # Karcher K7 Pressure Washer specifications
        MAX_PRESSURE_BAR = 180  # Maximum pressure in bars
        WATER_FLOW_RATE_LPM = 600  # Water flow rate in liters per minute
        POWER_RATING_W = 3000  # Power rating in watts

        # Instantiate the pressure washer object
        karcher_k7 = PressureWasher(MAX_PRESSURE_BAR, WATER_FLOW_RATE_LPM, POWER_RATING_W)

        # Start the pressure washer
        karcher_k7.start()

        # Simulate a cleaning operation for 10 seconds
        karcher_k7.simulate_cleaning(10)

        # Get and display the current status
        status = karcher_k7.get_status()
        print(f"Pressure Washer Status: {status}")

        # Stop the pressure washer
        karcher_k7.stop()

    except Exception as e:
        # Handle any unexpected errors gracefully
        print(f"An error occurred: {e}")
```
