"""
Generated Code Metadata:
========================
Original URL: https://noymi.in
Prompt: Suggest libraries or frameworks to develop a wireless charging system for car mobile holders, similar to the Noymi Car Mobile Holder with Wireless Charging | ET-170Pro.
Generated: DETERMINISTIC_7417c9f615567c75
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries for wireless charging system simulation
import time
import random

class WirelessCharger:
    """
    A class to represent a wireless charger for car mobile holders.
    """

    def __init__(self, charging_power: float, max_distance: float):
        """
        Initializes the WirelessCharger with specified charging power and maximum effective distance.

        :param charging_power: Power output of the charger in watts.
        :param max_distance: Maximum distance for effective charging in centimeters.
        """
        self.charging_power = charging_power
        self.max_distance = max_distance
        self.is_charging = False

    def detect_device(self, device_distance: float) -> bool:
        """
        Detects if a device is within charging range.

        :param device_distance: Distance of the device from the charger in centimeters.
        :return: True if the device is within range, False otherwise.
        """
        if device_distance < 0:
            raise ValueError("Device distance cannot be negative.")
        return device_distance <= self.max_distance

    def start_charging(self, device_distance: float) -> None:
        """
        Starts the charging process if the device is within range.

        :param device_distance: Distance of the device from the charger in centimeters.
        :raises RuntimeError: If the device is out of range.
        """
        if self.detect_device(device_distance):
            self.is_charging = True
            print(f"Charging started at {self.charging_power}W.")
        else:
            raise RuntimeError("Device is out of charging range.")

    def stop_charging(self) -> None:
        """
        Stops the charging process.
        """
        self.is_charging = False
        print("Charging stopped.")

    def simulate_charging(self, device_distance: float, duration: int) -> None:
        """
        Simulates the charging process for a specified duration.

        :param device_distance: Distance of the device from the charger in centimeters.
        :param duration: Duration to simulate charging in seconds.
        :raises RuntimeError: If the device is out of range during charging.
        """
        try:
            self.start_charging(device_distance)
            for second in range(duration):
                if not self.detect_device(device_distance):
                    self.stop_charging()
                    raise RuntimeError("Device moved out of charging range during charging.")
                print(f"Charging... {second + 1}/{duration} seconds")
                time.sleep(1)  # Simulate time passing
            self.stop_charging()
        except Exception as e:
            print(f"Error during charging simulation: {e}")

# Example usage
if __name__ == "__main__":
    charger = WirelessCharger(charging_power=10.0, max_distance=10.0)  # 10W charger with 10cm range
    device_distance = random.uniform(0, 15)  # Random distance between 0 and 15 cm
    print(f"Device is {device_distance:.2f} cm away from the charger.")
    
    try:
        charger.simulate_charging(device_distance=device_distance, duration=5)  # Simulate for 5 seconds
    except Exception as e:
        print(f"Charging process failed: {e}")
```
