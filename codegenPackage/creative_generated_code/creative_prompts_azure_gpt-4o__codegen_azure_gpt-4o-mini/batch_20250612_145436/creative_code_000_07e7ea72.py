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
class PressureWasher:
    """A class to simulate the operation of a Karcher K7 Pressure Washer."""

    def __init__(self, power: int, pressure: int, flow_rate: float):
        """
        Initializes the pressure washer with specified power, pressure, and flow rate.

        :param power: Power of the pressure washer in watts.
        :param pressure: Maximum pressure in bar.
        :param flow_rate: Water flow rate in liters per hour.
        """
        self.power = power  # Power in watts
        self.pressure = pressure  # Pressure in bar
        self.flow_rate = flow_rate  # Flow rate in liters per hour
        self.is_running = False  # State of the pressure washer

    def start(self):
        """Starts the pressure washer."""
        if not self.is_running:
            self.is_running = True
            print("Pressure washer started.")
        else:
            print("Pressure washer is already running.")

    def stop(self):
        """Stops the pressure washer."""
        if self.is_running:
            self.is_running = False
            print("Pressure washer stopped.")
        else:
            print("Pressure washer is not running.")

    def spray(self, duration: int):
        """
        Simulates the spraying operation for a given duration.

        :param duration: Duration to spray in seconds.
        """
        if not self.is_running:
            print("Cannot spray. Pressure washer is not running.")
            return
        
        if duration <= 0:
            print("Duration must be a positive number.")
            return

        water_used = self.calculate_water_usage(duration)
        print(f"Spraying for {duration} seconds...")
        print(f"Water used: {water_used:.2f} liters")

    def calculate_water_usage(self, duration: int) -> float:
        """
        Calculates the amount of water used during spraying.

        :param duration: Duration of spraying in seconds.
        :return: Amount of water used in liters.
        """
        # Calculate the amount of water used (liters)
        hours = duration / 3600  # Convert seconds to hours
        water_used = (self.flow_rate / 1000) * hours  # Convert L/h to L/s
        return water_used

    def __str__(self):
        """Returns a string representation of the pressure washer's specifications."""
        return (f"Karcher K7 Pressure Washer:\n"
                f"Power: {self.power} W\n"
                f"Pressure: {self.pressure} bar\n"
                f"Flow Rate: {self.flow_rate} L/h\n"
                f"Running State: {'Running' if self.is_running else 'Stopped'}")


def main():
    """Main function to simulate the pressure washer operation."""
    try:
        # Specifications based on Karcher K7
        karcher_k7 = PressureWasher(power=3000, pressure=160, flow_rate=600)
        
        print(karcher_k7)  # Print initial specifications
        
        karcher_k7.start()  # Start the pressure washer
        karcher_k7.spray(10)  # Spray for 10 seconds
        karcher_k7.stop()  # Stop the pressure washer

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
