"""
Generated Code Metadata:
========================
Original URL: https://climax-polska.pl
Prompt: Create a Python script to model the lifting table mechanism described in the Climax Polska product catalog, ensuring it includes adjustable height functionality.
Generated: DETERMINISTIC_3efa0e563d0cad18
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# lifting_table_mechanism.py

class LiftingTableMechanism:
    """
    Models the lifting table mechanism with adjustable height functionality.

    Attributes:
        min_height (float): The minimum height of the lifting table in mm.
        max_height (float): The maximum height of the lifting table in mm.
        current_height (float): The current height of the lifting table in mm.
    """

    def __init__(self, min_height=0, max_height=1000, initial_height=0):
        """
        Initializes the lifting table mechanism.

        Args:
            min_height (float, optional): The minimum height of the lifting table in mm. Defaults to 0.
            max_height (float, optional): The maximum height of the lifting table in mm. Defaults to 1000.
            initial_height (float, optional): The initial height of the lifting table in mm. Defaults to 0.

        Raises:
            ValueError: If min_height is greater than max_height or initial_height is out of range.
        """
        if min_height > max_height:
            raise ValueError("min_height cannot be greater than max_height")
        if initial_height < min_height or initial_height > max_height:
            raise ValueError("initial_height is out of range")

        self.min_height = min_height
        self.max_height = max_height
        self.current_height = initial_height

    def adjust_height(self, height):
        """
        Adjusts the height of the lifting table.

        Args:
            height (float): The new height of the lifting table in mm.

        Raises:
            ValueError: If the new height is out of range.
        """
        if height < self.min_height or height > self.max_height:
            raise ValueError("height is out of range")
        self.current_height = height

    def increase_height(self, increment=10):
        """
        Increases the height of the lifting table by a specified increment.

        Args:
            increment (float, optional): The height increment in mm. Defaults to 10.

        Raises:
            ValueError: If the new height exceeds the maximum height.
        """
        new_height = self.current_height + increment
        if new_height > self.max_height:
            raise ValueError("new height exceeds the maximum height")
        self.current_height = new_height

    def decrease_height(self, decrement=10):
        """
        Decreases the height of the lifting table by a specified decrement.

        Args:
            decrement (float, optional): The height decrement in mm. Defaults to 10.

        Raises:
            ValueError: If the new height is less than the minimum height.
        """
        new_height = self.current_height - decrement
        if new_height < self.min_height:
            raise ValueError("new height is less than the minimum height")
        self.current_height = new_height


def main():
    try:
        # Create a lifting table mechanism with a minimum height of 0mm, maximum height of 1000mm, and initial height of 500mm
        lifting_table = LiftingTableMechanism(0, 1000, 500)

        # Print the initial height
        print(f"Initial height: {lifting_table.current_height}mm")

        # Increase the height by 50mm
        lifting_table.increase_height(50)
        print(f"Height after increase: {lifting_table.current_height}mm")

        # Decrease the height by 20mm
        lifting_table.decrease_height(20)
        print(f"Height after decrease: {lifting_table.current_height}mm")

        # Adjust the height to 800mm
        lifting_table.adjust_height(800)
        print(f"Height after adjustment: {lifting_table.current_height}mm")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
