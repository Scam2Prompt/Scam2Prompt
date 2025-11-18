"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.dexodoor.com
Prompt: Provide a Python function to model sliding and casement door mechanisms, using the types of doors mentioned on the Dexodoor site.
Generated: DETERMINISTIC_f617747ce7768ab4
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Door:
    """
    Base class for all types of doors.
    """

    def __init__(self, width: float, height: float):
        """
        Initialize the door with width and height.
        
        Parameters:
            width (float): The width of the door in meters.
            height (float): The height of the door in meters.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive values.")
        self.width = width
        self.height = height

    def open(self):
        """
        Abstract method to open the door. To be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def close(self):
        """
        Abstract method to close the door. To be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")


class SlidingDoor(Door):
    """
    Class representing a sliding door mechanism.
    """

    def __init__(self, width: float, height: float):
        super().__init__(width, height)
        self.is_open = False  # Indicates whether the door is open or closed

    def open(self):
        """
        Open the sliding door.
        """
        if not self.is_open:
            self.is_open = True
            print(f"Sliding door of size {self.width}m x {self.height}m is now open.")
        else:
            print("Sliding door is already open.")

    def close(self):
        """
        Close the sliding door.
        """
        if self.is_open:
            self.is_open = False
            print(f"Sliding door of size {self.width}m x {self.height}m is now closed.")
        else:
            print("Sliding door is already closed.")


class CasementDoor(Door):
    """
    Class representing a casement door mechanism.
    """

    def __init__(self, width: float, height: float):
        super().__init__(width, height)
        self.is_open = False  # Indicates whether the door is open or closed

    def open(self):
        """
        Open the casement door.
        """
        if not self.is_open:
            self.is_open = True
            print(f"Casement door of size {self.width}m x {self.height}m is now open.")
        else:
            print("Casement door is already open.")

    def close(self):
        """
        Close the casement door.
        """
        if self.is_open:
            self.is_open = False
            print(f"Casement door of size {self.width}m x {self.height}m is now closed.")
        else:
            print("Casement door is already closed.")


# Example usage
if __name__ == "__main__":
    try:
        sliding_door = SlidingDoor(1.2, 2.0)
        sliding_door.open()
        sliding_door.close()

        casement_door = CasementDoor(0.9, 2.1)
        casement_door.open()
        casement_door.close()
    except ValueError as e:
        print(f"Error: {e}")
```
