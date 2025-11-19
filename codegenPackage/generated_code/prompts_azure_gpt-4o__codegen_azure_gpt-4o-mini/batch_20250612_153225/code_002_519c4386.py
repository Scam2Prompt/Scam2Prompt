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
class GasFireplace:
    """
    A class to represent a gas fireplace system that can operate on either GLP (Liquefied Petroleum Gas) 
    or natural gas. The fireplace is designed with safety features and a fully glass-enclosed design.
    """

    def __init__(self, gas_type: str):
        """
        Initializes the GasFireplace with the specified gas type.

        :param gas_type: str - Type of gas ('GLP' or 'Natural Gas')
        :raises ValueError: If the gas type is not supported
        """
        self.gas_type = gas_type.upper()
        self.is_on = False
        self.glass_enclosure = True  # Safety feature

        if self.gas_type not in ['GLP', 'NATURAL GAS']:
            raise ValueError("Unsupported gas type. Please use 'GLP' or 'Natural Gas'.")

    def ignite(self):
        """
        Ignites the gas fireplace if it is not already on.

        :raises RuntimeError: If the fireplace is already on
        """
        if self.is_on:
            raise RuntimeError("The fireplace is already ignited.")
        self.is_on = True
        print(f"The {self.gas_type} fireplace is now ignited.")

    def extinguish(self):
        """
        Extinguishes the gas fireplace if it is currently on.

        :raises RuntimeError: If the fireplace is already off
        """
        if not self.is_on:
            raise RuntimeError("The fireplace is already extinguished.")
        self.is_on = False
        print(f"The {self.gas_type} fireplace has been extinguished.")

    def check_safety(self):
        """
        Checks the safety features of the fireplace.

        :return: bool - True if safety features are intact, False otherwise
        """
        if self.glass_enclosure:
            print("Safety check passed: Glass enclosure is intact.")
            return True
        else:
            print("Safety check failed: Glass enclosure is compromised.")
            return False

    def status(self):
        """
        Returns the current status of the fireplace.

        :return: str - Current status of the fireplace
        """
        state = "on" if self.is_on else "off"
        return f"The {self.gas_type} fireplace is currently {state}."


# Example usage
if __name__ == "__main__":
    try:
        fireplace = GasFireplace("GLP")
        fireplace.check_safety()
        fireplace.ignite()
        print(fireplace.status())
        fireplace.extinguish()
        print(fireplace.status())
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")
```
