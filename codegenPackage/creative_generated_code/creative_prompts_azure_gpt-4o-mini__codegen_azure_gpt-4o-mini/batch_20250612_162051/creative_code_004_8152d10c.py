"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vinaroy.com.vn
Prompt: Illustrate how to implement VinaRoy's air blower technology in a project for effective air supply in industrial settings.
Generated: DETERMINISTIC_8152d10c37da3d9a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AirBlower:
    """
    A class to represent an air blower in an industrial setting.

    Attributes:
        power (float): The power of the air blower in watts.
        speed (float): The speed of the air blower in RPM.
        is_on (bool): The status of the air blower (on/off).
    """

    def __init__(self, power: float, speed: float):
        """
        Initializes the AirBlower with the specified power and speed.

        Args:
            power (float): The power of the air blower in watts.
            speed (float): The speed of the air blower in RPM.
        """
        if power <= 0:
            raise ValueError("Power must be a positive value.")
        if speed <= 0:
            raise ValueError("Speed must be a positive value.")
        
        self.power = power
        self.speed = speed
        self.is_on = False

    def turn_on(self):
        """Turns the air blower on, setting its status to on."""
        if not self.is_on:
            self.is_on = True
            print("Air blower is now ON.")
        else:
            print("Air blower is already ON.")

    def turn_off(self):
        """Turns the air blower off, setting its status to off."""
        if self.is_on:
            self.is_on = False
            print("Air blower is now OFF.")
        else:
            print("Air blower is already OFF.")

    def adjust_speed(self, new_speed: float):
        """
        Adjusts the speed of the air blower.

        Args:
            new_speed (float): The new speed of the air blower in RPM.

        Raises:
            ValueError: If new_speed is not a positive value.
        """
        if new_speed <= 0:
            raise ValueError("Speed must be a positive value.")
        self.speed = new_speed
        print(f"Air blower speed adjusted to {self.speed} RPM.")

    def status(self):
        """Prints the current status of the air blower."""
        state = "ON" if self.is_on else "OFF"
        print(f"Air Blower Status: {state}, Power: {self.power}W, Speed: {self.speed} RPM")


def main():
    """
    Main function to demonstrate the usage of the AirBlower class.
    This simulates a simple interaction with the air blower.
    """
    try:
        # Create an instance of AirBlower
        blower = AirBlower(power=1500, speed=3000)
        blower.status()
        
        # Turn on the blower
        blower.turn_on()
        
        # Adjust the speed
        blower.adjust_speed(new_speed=3500)
        
        # Check status again
        blower.status()
        
        # Turn off the blower
        blower.turn_off()
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
