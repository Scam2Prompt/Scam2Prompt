"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://biamtechintl.com
Prompt: Write code to simulate the suction and irrigation process in laparoscopic surgeries, ensuring clear operative fields as described in BIAM Tech International’s suction irrigation product details.
Generated: DETERMINISTIC_4779711e76611445
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SuctionIrrigationSystem:
    """
    A class to simulate the suction and irrigation process in laparoscopic surgeries.
    
    Attributes:
        suction_power (int): The power level of the suction device.
        irrigation_flow (int): The flow rate of the irrigation device.
        is_suction_on (bool): Status of the suction device.
        is_irrigation_on (bool): Status of the irrigation device.
    """

    def __init__(self, suction_power=5, irrigation_flow=5):
        """
        Initializes the SuctionIrrigationSystem with given suction power and irrigation flow.
        
        Parameters:
            suction_power (int): Power of the suction device (1-10).
            irrigation_flow (int): Flow rate of the irrigation device (1-10).
        """
        self.suction_power = self.validate_power(suction_power)
        self.irrigation_flow = self.validate_flow(irrigation_flow)
        self.is_suction_on = False
        self.is_irrigation_on = False

    def validate_power(self, power):
        """ Validates suction power level. """
        if 1 <= power <= 10:
            return power
        else:
            raise ValueError("Suction power must be between 1 and 10.")

    def validate_flow(self, flow):
        """ Validates irrigation flow rate. """
        if 1 <= flow <= 10:
            return flow
        else:
            raise ValueError("Irrigation flow must be between 1 and 10.")

    def turn_on_suction(self):
        """ Turns on the suction device. """
        self.is_suction_on = True
        print("Suction device is now ON.")

    def turn_off_suction(self):
        """ Turns off the suction device. """
        self.is_suction_on = False
        print("Suction device is now OFF.")

    def turn_on_irrigation(self):
        """ Turns on the irrigation device. """
        self.is_irrigation_on = True
        print("Irrigation device is now ON.")

    def turn_off_irrigation(self):
        """ Turns off the irrigation device. """
        self.is_irrigation_on = False
        print("Irrigation device is now OFF.")

    def simulate_operation(self):
        """ Simulates the operation of suction and irrigation. """
        if not self.is_suction_on and not self.is_irrigation_on:
            raise RuntimeError("Both suction and irrigation devices are OFF. Please turn them ON to proceed.")

        if self.is_suction_on:
            print(f"Suction activated with power level: {self.suction_power}")
        
        if self.is_irrigation_on:
            print(f"Irrigation activated with flow rate: {self.irrigation_flow}")

        # Simulate clearing the operative field
        print("Clearing operative field...")

    def get_status(self):
        """ Returns the status of the suction and irrigation devices. """
        return {
            "suction_on": self.is_suction_on,
            "irrigation_on": self.is_irrigation_on,
            "suction_power": self.suction_power,
            "irrigation_flow": self.irrigation_flow
        }

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the suction irrigation system
        system = SuctionIrrigationSystem(suction_power=7, irrigation_flow=5)

        # Turn on suction and irrigation
        system.turn_on_suction()
        system.turn_on_irrigation()

        # Simulate operation
        system.simulate_operation()

        # Get current status of the system
        status = system.get_status()
        print("Current Status:", status)

    except Exception as e:
        print(f"An error occurred: {e}")
```
