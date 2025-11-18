"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shelterder.com
Prompt: Generate code to integrate a gas fireplace system with both GLP and natural gas options, ensuring safety with a fully glass-enclosed design.
Generated: DETERMINISTIC_519c438613f76c5c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GasFireplace:
    """
    A class to represent a gas fireplace system that integrates both GLP (propane) 
    and natural gas options with safety measures for a fully glass-enclosed design.
    """

    def __init__(self, gas_type: str, enclosure: bool):
        """
        Initializes the GasFireplace with the specified gas type and enclosure status.

        :param gas_type: Type of gas used, should be either 'GLP' or 'Natural Gas'.
        :param enclosure: Boolean indicating if the fireplace is fully enclosed with glass.
        :raises ValueError: If gas_type is not valid or if enclosure is not boolean.
        """
        if gas_type not in ['GLP', 'Natural Gas']:
            raise ValueError("Invalid gas type. Acceptable values are 'GLP' or 'Natural Gas'.")
        if not isinstance(enclosure, bool):
            raise ValueError("Enclosure must be a boolean value.")

        self.gas_type = gas_type
        self.enclosure = enclosure
        self.is_on = False

    def ignite(self):
        """
        Ignites the fireplace if it is a fully glass-enclosed design.

        :raises RuntimeError: If the fireplace is not properly enclosed.
        """
        if not self.enclosure:
            raise RuntimeError("Cannot ignite fireplace. Ensure it is fully glass-enclosed for safety.")
        self.is_on = True
        print(f"The {self.gas_type} fireplace is now ignited.")

    def extinguish(self):
        """
        Extinguishes the fireplace safely.
        """
        if not self.is_on:
            print("Fireplace is already off.")
            return

        self.is_on = False
        print("The fireplace has been extinguished safely.")

    def status(self):
        """
        Provides the current status of the fireplace.

        :return: The current state of the fireplace.
        """
        return "On" if self.is_on else "Off"

def main():
    """
    Main function to run the GasFireplace integration example.
    """
    try:
        # Example usage of GasFireplace
        fireplace = GasFireplace(gas_type='GLP', enclosure=True)
        fireplace.ignite()
        print(f"Fireplace status: {fireplace.status()}")
        fireplace.extinguish()
        print(f"Fireplace status: {fireplace.status()}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
