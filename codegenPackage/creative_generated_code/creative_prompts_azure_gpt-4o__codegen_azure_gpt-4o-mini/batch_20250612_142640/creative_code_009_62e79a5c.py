"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinoag.com
Prompt: Write code to simulate the flex-wing functionality of heavy-duty mowers, inspired by the 4125 model described on RhinoAg's site.
Generated: DETERMINISTIC_62e79a5c9eb07598
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FlexWingMower:
    """
    A class to simulate the flex-wing functionality of heavy-duty mowers.
    Inspired by the 4125 model described on RhinoAg's site.
    """

    def __init__(self, width: float, height: float):
        """
        Initializes a new FlexWingMower instance.

        :param width: The cutting width of the mower in feet.
        :param height: The cutting height of the mower in inches.
        """
        self.width = width
        self.height = height
        self.is_operational = False  # Status of the mower

    def start(self):
        """
        Starts the mower if it is not already operational.
        Raises an exception if the mower is already running.
        """
        if self.is_operational:
            raise RuntimeError("Mower is already running.")
        self.is_operational = True
        print("Mower started.")

    def stop(self):
        """
        Stops the mower if it is operational.
        Raises an exception if the mower is not running.
        """
        if not self.is_operational:
            raise RuntimeError("Mower is not running.")
        self.is_operational = False
        print("Mower stopped.")

    def adjust_height(self, new_height: float):
        """
        Adjusts the cutting height of the mower.

        :param new_height: The new cutting height in inches.
        :raises ValueError: If new_height is not positive.
        """
        if new_height <= 0:
            raise ValueError("Cutting height must be a positive value.")
        self.height = new_height
        print(f"Cutting height adjusted to {self.height} inches.")

    def cut_grass(self):
        """
        Simulates the grass cutting functionality of the mower.
        Raises an exception if the mower is not operational.
        """
        if not self.is_operational:
            raise RuntimeError("Mower must be started before cutting grass.")
        print(f"Cutting grass at {self.height} inches with a width of {self.width} feet.")

    def get_specs(self) -> str:
        """
        Returns a string with the specifications of the mower.

        :return: Specifications of the mower.
        """
        operational_status = "Operational" if self.is_operational else "Not Operational"
        return (f"Flex-Wing Mower Specs:\n"
                f"Width: {self.width} feet\n"
                f"Height: {self.height} inches\n"
                f"Status: {operational_status}")


if __name__ == "__main__":
    try:
        # Example usage of the FlexWingMower class
        mower = FlexWingMower(width=12.0, height=3.0)
        print(mower.get_specs())
        
        mower.start()
        mower.cut_grass()
        mower.adjust_height(4.0)
        mower.cut_grass()
        mower.stop()
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
