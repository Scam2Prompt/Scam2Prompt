"""
Generated Code Metadata:
========================
Original URL: https://shelterder.com
Prompt: Generate code to integrate a gas fireplace system with both GLP and natural gas options, ensuring safety with a fully glass-enclosed design.
Generated: DETERMINISTIC_519c438613f76c5c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# gas_fireplace_system.py

class GasFireplaceSystem:
    """
    A class representing a gas fireplace system with GLP and natural gas options.

    Attributes:
        gas_type (str): The type of gas used (GLP or natural).
        is_on (bool): Whether the fireplace is currently on.
        temperature (int): The current temperature setting.
    """

    def __init__(self, gas_type):
        """
        Initializes a GasFireplaceSystem instance.

        Args:
            gas_type (str): The type of gas used (GLP or natural).

        Raises:
            ValueError: If the gas type is not GLP or natural.
        """
        if gas_type not in ["GLP", "natural"]:
            raise ValueError("Invalid gas type. Must be GLP or natural.")
        self.gas_type = gas_type
        self.is_on = False
        self.temperature = 20  # default temperature

    def turn_on(self):
        """
        Turns on the gas fireplace system.

        Raises:
            Exception: If the system is already on.
        """
        if self.is_on:
            raise Exception("Fireplace is already on.")
        self.is_on = True
        print(f"Gas fireplace system turned on with {self.gas_type} gas.")

    def turn_off(self):
        """
        Turns off the gas fireplace system.

        Raises:
            Exception: If the system is already off.
        """
        if not self.is_on:
            raise Exception("Fireplace is already off.")
        self.is_on = False
        print(f"Gas fireplace system turned off.")

    def set_temperature(self, temperature):
        """
        Sets the temperature of the gas fireplace system.

        Args:
            temperature (int): The desired temperature.

        Raises:
            ValueError: If the temperature is not between 15 and 30.
        """
        if temperature < 15 or temperature > 30:
            raise ValueError("Temperature must be between 15 and 30.")
        self.temperature = temperature
        print(f"Temperature set to {temperature}°C.")

    def safety_check(self):
        """
        Performs a safety check on the gas fireplace system.

        Raises:
            Exception: If the system is not in a safe state.
        """
        if not self.is_on:
            print("Fireplace is off. No safety issues.")
            return
        if self.temperature > 25:
            raise Exception("Temperature too high. Safety issue detected.")
        print("Safety check passed.")

def main():
    try:
        # Create a gas fireplace system with GLP gas
        fireplace = GasFireplaceSystem("GLP")

        # Turn on the fireplace
        fireplace.turn_on()

        # Set the temperature
        fireplace.set_temperature(22)

        # Perform a safety check
        fireplace.safety_check()

        # Turn off the fireplace
        fireplace.turn_off()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
