"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://climax-polska.pl
Prompt: Develop a simulation for a mini tractor used in warehouse logistics, incorporating features similar to those described in the Climax Polska product range.
Generated: DETERMINISTIC_ecabdfc5c4d7e2e7
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class MiniTractor:
    """
    A class to simulate a mini tractor used in warehouse logistics.
    """

    def __init__(self, name, max_speed, max_load_capacity, battery_capacity):
        """
        Initialize the Mini Tractor object.

        Parameters:
        - name (str): The name or model of the tractor.
        - max_speed (float): Maximum speed of the tractor in km/h.
        - max_load_capacity (float): Maximum load capacity of the tractor in kilograms.
        - battery_capacity (float): Battery capacity of the tractor in percentage.
        """
        self.name = name
        self.max_speed = max_speed
        self.max_load_capacity = max_load_capacity
        self.battery_capacity = battery_capacity  # Percentage (0-100)
        self.current_speed = 0
        self.current_load = 0
        self.battery_usage_rate = 0.1  # Battery consumption per second of movement
        self.is_operational = True

    def load_cargo(self, weight):
        """
        Load cargo onto the tractor.

        Parameters:
        - weight (float): The weight of the cargo to be loaded in kilograms.

        Returns:
        - bool: True if the cargo is successfully loaded, False otherwise.
        """
        if weight <= 0:
            print("[Error] Weight must be greater than zero.")
            return False
        if self.current_load + weight > self.max_load_capacity:
            print("[Warning] Load exceeds maximum capacity! Cannot load cargo.")
            return False
        self.current_load += weight
        print(f"[Info] Cargo loaded. Current load: {self.current_load} kg.")
        return True

    def unload_cargo(self, weight):
        """
        Unload cargo from the tractor.

        Parameters:
        - weight (float): The weight of the cargo to be unloaded in kilograms.

        Returns:
        - bool: True if the cargo is successfully unloaded, False otherwise.
        """
        if weight <= 0:
            print("[Error] Weight must be greater than zero.")
            return False
        if weight > self.current_load:
            print("[Warning] Attempt to unload more than the current load! Cannot unload cargo.")
            return False
        self.current_load -= weight
        print(f"[Info] Cargo unloaded. Current load: {self.current_load} kg.")
        return True

    def move(self, speed, duration):
        """
        Move the tractor at a specified speed for a certain duration.

        Parameters:
        - speed (float): The speed of the tractor in km/h.
        - duration (float): Movement duration in seconds.

        Returns:
        - None
        """
        if speed <= 0:
            print("[Error] Speed must be greater than zero.")
            return
        if speed > self.max_speed:
            print("[Warning] Speed exceeds maximum capacity! Reducing to max speed.")
            speed = self.max_speed
        if self.battery_capacity <= 0:
            print("[Error] Battery depleted. Tractor cannot move.")
            self.is_operational = False
            return
        
        battery_required = self.battery_usage_rate * duration
        if battery_required > self.battery_capacity:
            print("[Warning] Battery insufficient for the duration. Reducing movement time.")
            duration = self.battery_capacity / self.battery_usage_rate

        self.current_speed = speed
        print(f"[Info] Tractor moving at {self.current_speed} km/h for {duration} seconds.")
        time.sleep(duration)  # Simulate movement
        self.battery_capacity -= self.battery_usage_rate * duration
        self.current_speed = 0
        print(f"[Info] Movement complete. Remaining battery: {self.battery_capacity:.2f}%.")

    def recharge_battery(self):
        """
        Recharge the battery to full capacity.

        Returns:
        - None
        """
        self.battery_capacity = 100
        self.is_operational = True
        print("[Info] Battery fully recharged.")

    def display_status(self):
        """
        Display the current status of the tractor.

        Returns:
        - None
        """
        print("\n--- Tractor Status ---")
        print(f"Name: {self.name}")
        print(f"Max Speed: {self.max_speed} km/h")
        print(f"Max Load Capacity: {self.max_load_capacity} kg")
        print(f"Current Load: {self.current_load} kg")
        print(f"Battery Capacity: {self.battery_capacity:.2f}%")
        print(f"Operational: {'Yes' if self.is_operational else 'No'}")
        print("-----------------------")

# Example usage of the MiniTractor class
if __name__ == "__main__":
    tractor = MiniTractor(name="Climax MiniTractor Model X", max_speed=15, max_load_capacity=500, battery_capacity=100)

    tractor.display_status()
    tractor.load_cargo(200)
    tractor.move(speed=10, duration=5)
    tractor.unload_cargo(100)
    tractor.recharge_battery()
    tractor.display_status()
```
