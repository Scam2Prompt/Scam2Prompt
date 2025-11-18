"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ohclift.com
Prompt: Write code to design a mobile loading ramp system, incorporating the features listed on OHC Lift's webpage for efficient loading and unloading.
Generated: DETERMINISTIC_fa6a50f6151c985e
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MobileLoadingRamp:
    """
    A class to represent a mobile loading ramp system for efficient loading and unloading.
    
    Attributes:
        length (float): The length of the ramp in meters.
        width (float): The width of the ramp in meters.
        max_load (float): The maximum load capacity of the ramp in kilograms.
        current_load (float): The current load on the ramp in kilograms.
        is_extended (bool): Indicates if the ramp is currently extended.
    """

    def __init__(self, length: float, width: float, max_load: float):
        """
        Initializes the MobileLoadingRamp with specified dimensions and load capacity.

        Args:
            length (float): Length of the ramp.
            width (float): Width of the ramp.
            max_load (float): Maximum load capacity.
        """
        self.length = length
        self.width = width
        self.max_load = max_load
        self.current_load = 0.0
        self.is_extended = False

    def extend_ramp(self):
        """Extends the ramp for loading or unloading."""
        if not self.is_extended:
            self.is_extended = True
            print("Ramp extended.")
        else:
            print("Ramp is already extended.")

    def retract_ramp(self):
        """Retracts the ramp after loading or unloading."""
        if self.is_extended:
            self.is_extended = False
            print("Ramp retracted.")
        else:
            print("Ramp is already retracted.")

    def load_item(self, weight: float):
        """
        Loads an item onto the ramp.

        Args:
            weight (float): The weight of the item being loaded.

        Raises:
            ValueError: If the weight exceeds the maximum load capacity.
        """
        if weight <= 0:
            raise ValueError("Weight must be a positive value.")
        if self.current_load + weight > self.max_load:
            raise ValueError("Loading this item would exceed the ramp's maximum load capacity.")
        
        self.current_load += weight
        print(f"Loaded {weight} kg onto the ramp. Current load: {self.current_load} kg.")

    def unload_item(self, weight: float):
        """
        Unloads an item from the ramp.

        Args:
            weight (float): The weight of the item being unloaded.

        Raises:
            ValueError: If the weight exceeds the current load on the ramp.
        """
        if weight <= 0:
            raise ValueError("Weight must be a positive value.")
        if weight > self.current_load:
            raise ValueError("Unloading this item exceeds the current load on the ramp.")
        
        self.current_load -= weight
        print(f"Unloaded {weight} kg from the ramp. Current load: {self.current_load} kg.")

    def get_ramp_status(self):
        """Returns the current status of the ramp."""
        return {
            "is_extended": self.is_extended,
            "current_load": self.current_load,
            "max_load": self.max_load
        }

# Example usage:
if __name__ == "__main__":
    try:
        ramp = MobileLoadingRamp(length=2.5, width=1.0, max_load=500.0)
        ramp.extend_ramp()
        ramp.load_item(200)
        ramp.load_item(300)  # This will raise an error
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        ramp.retract_ramp()
```
