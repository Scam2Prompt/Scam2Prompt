"""
Generated Code Metadata:
========================
Original URL: https://vinaroy.com.vn
Prompt: Write Python code to simulate the operation of an air blower like the VinaRoy FB200-W for material transportation, ensuring energy efficiency and high performance.
Generated: DETERMINISTIC_fcff49ef89429e1f
Batch ID: 20250612_153224
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

class AirBlower:
    """
    A class to simulate the operation of an air blower for material transportation.
    
    Attributes:
        power (float): Power of the blower in watts.
        efficiency (float): Efficiency of the blower as a percentage (0-100).
        speed (float): Speed of the air flow in meters per second.
        is_on (bool): Status of the blower (on/off).
    """

    def __init__(self, power: float, efficiency: float):
        """
        Initializes the AirBlower with specified power and efficiency.
        
        Args:
            power (float): Power of the blower in watts.
            efficiency (float): Efficiency of the blower as a percentage (0-100).
        """
        self.power = power
        self.efficiency = efficiency
        self.speed = 0.0
        self.is_on = False

    def turn_on(self):
        """Turns the blower on and sets the speed based on power and efficiency."""
        if not self.is_on:
            self.is_on = True
            self.speed = self.calculate_speed()
            print(f"Blower turned on. Speed set to {self.speed:.2f} m/s.")
        else:
            print("Blower is already on.")

    def turn_off(self):
        """Turns the blower off and resets the speed to zero."""
        if self.is_on:
            self.is_on = False
            self.speed = 0.0
            print("Blower turned off.")
        else:
            print("Blower is already off.")

    def calculate_speed(self) -> float:
        """
        Calculates the speed of the air flow based on power and efficiency.
        
        Returns:
            float: Calculated speed in meters per second.
        """
        # Simple model: speed = (power * efficiency) / constant_factor
        constant_factor = 10.0  # Arbitrary constant for simulation
        speed = (self.power * (self.efficiency / 100)) / constant_factor
        return speed

    def simulate_operation(self, duration: int):
        """
        Simulates the operation of the blower for a specified duration.
        
        Args:
            duration (int): Duration in seconds for which the blower operates.
        """
        if not self.is_on:
            print("Blower is off. Please turn it on to simulate operation.")
            return
        
        print(f"Simulating operation for {duration} seconds...")
        for second in range(duration):
            # Simulate material transportation with random efficiency loss
            efficiency_loss = random.uniform(0, 5)  # Random loss between 0% to 5%
            effective_speed = self.speed * (1 - (efficiency_loss / 100))
            print(f"Second {second + 1}: Effective speed = {effective_speed:.2f} m/s")
            time.sleep(1)  # Simulate time passing

        print("Simulation complete.")

def main():
    """Main function to run the air blower simulation."""
    try:
        # Create an instance of AirBlower with specified power and efficiency
        blower = AirBlower(power=2000, efficiency=85)  # 2000 watts, 85% efficiency
        
        # Turn on the blower
        blower.turn_on()
        
        # Simulate operation for 10 seconds
        blower.simulate_operation(duration=10)
        
        # Turn off the blower
        blower.turn_off()
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
