"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://climax-polska.pl
Prompt: Create a Python script to model the lifting table mechanism described in the Climax Polska product catalog, ensuring it includes adjustable height functionality.
Generated: DETERMINISTIC_3efa0e563d0cad18
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class LiftingTable:
    """
    A class to model a lifting table mechanism with adjustable height.
    """

    def __init__(self, min_height: float, max_height: float):
        """
        Initialize the LiftingTable with a minimum and maximum height.

        :param min_height: The minimum height of the lifting table in centimeters.
        :param max_height: The maximum height of the lifting table in centimeters.
        """
        if min_height <= 0 or max_height <= 0:
            raise ValueError("Height values must be positive numbers.")
        if min_height >= max_height:
            raise ValueError("Minimum height must be less than maximum height.")
        
        self.min_height = min_height
        self.max_height = max_height
        self.current_height = min_height  # Table starts at its minimum height

    def adjust_height(self, new_height: float):
        """
        Adjust the lifting table to a specific height.

        :param new_height: The desired height of the lifting table in centimeters.
        :raises ValueError: If the new height is outside the valid range.
        """
        if new_height < self.min_height or new_height > self.max_height:
            raise ValueError(f"Height must be between {self.min_height} and {self.max_height} cm.")
        
        self.current_height = new_height
        print(f"Lifting table height adjusted to {self.current_height} cm.")

    def increase_height(self, step: float):
        """
        Increase the table height by a specific step value.

        :param step: The amount to increase the height by in centimeters.
        :raises ValueError: If the resulting height exceeds the maximum height.
        """
        new_height = self.current_height + step
        if new_height > self.max_height:
            raise ValueError(f"Cannot exceed maximum height of {self.max_height} cm.")
        
        self.current_height = new_height
        print(f"Lifting table height increased to {self.current_height} cm.")

    def decrease_height(self, step: float):
        """
        Decrease the table height by a specific step value.

        :param step: The amount to decrease the height by in centimeters.
        :raises ValueError: If the resulting height falls below the minimum height.
        """
        new_height = self.current_height - step
        if new_height < self.min_height:
            raise ValueError(f"Cannot fall below minimum height of {self.min_height} cm.")
        
        self.current_height = new_height
        print(f"Lifting table height decreased to {self.current_height} cm.")

    def get_current_height(self) -> float:
        """
        Get the current height of the lifting table.

        :return: The current height in centimeters.
        """
        return self.current_height


def main():
    try:
        # Create a lifting table with a minimum height of 50 cm and a maximum height of 150 cm
        table = LiftingTable(min_height=50, max_height=150)
        
        # Adjust the table height
        table.adjust_height(100)
        
        # Increase the table height
        table.increase_height(20)
        
        # Decrease the table height
        table.decrease_height(30)
        
        # Print the current height
        print(f"Final table height: {table.get_current_height()} cm.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
