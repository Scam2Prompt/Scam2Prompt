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
class LiftingTable:
    """
    A class to model a lifting table mechanism with adjustable height.
    """

    def __init__(self, min_height: float, max_height: float):
        """
        Initializes the LiftingTable with a minimum and maximum height.

        :param min_height: The minimum height of the lifting table in centimeters.
        :param max_height: The maximum height of the lifting table in centimeters.
        :raises ValueError: If min_height is greater than max_height.
        """
        if min_height > max_height:
            raise ValueError("Minimum height cannot be greater than maximum height.")

        self.min_height = min_height
        self.max_height = max_height
        self.current_height = min_height  # Start at minimum height

    def raise_table(self, increment: float):
        """
        Raises the table by a specified increment, ensuring it does not exceed max height.

        :param increment: The amount to raise the table in centimeters.
        :raises ValueError: If the increment would raise the table above max height.
        """
        if self.current_height + increment > self.max_height:
            raise ValueError("Cannot raise table; exceeds maximum height.")

        self.current_height += increment

    def lower_table(self, decrement: float):
        """
        Lowers the table by a specified decrement, ensuring it does not drop below min height.

        :param decrement: The amount to lower the table in centimeters.
        :raises ValueError: If the decrement would lower the table below min height.
        """
        if self.current_height - decrement < self.min_height:
            raise ValueError("Cannot lower table; exceeds minimum height.")

        self.current_height -= decrement

    def set_height(self, new_height: float):
        """
        Sets the table to a specific height within the defined limits.

        :param new_height: The desired height of the table in centimeters.
        :raises ValueError: If new_height is not within the min and max height.
        """
        if new_height < self.min_height or new_height > self.max_height:
            raise ValueError(f"Height must be between {self.min_height} and {self.max_height} cm.")

        self.current_height = new_height

    def get_current_height(self) -> float:
        """
        Returns the current height of the table.

        :return: Current height in centimeters.
        """
        return self.current_height

    def __str__(self):
        """
        Returns a string representation of the LiftingTable state.
        """
        return f"Lifting Table - Current Height: {self.current_height} cm (Min: {self.min_height} cm, Max: {self.max_height} cm)"


# Example usage of the LiftingTable class
if __name__ == "__main__":
    try:
        # Initialize a lifting table with a height range of 30 to 120 cm
        lifting_table = LiftingTable(min_height=30, max_height=120)

        # Adjust the height of the table
        lifting_table.raise_table(20)  # Raise by 20 cm
        print(lifting_table)

        lifting_table.lower_table(10)  # Lower by 10 cm
        print(lifting_table)

        lifting_table.set_height(100)  # Set to 100 cm
        print(lifting_table)

        # Attempt to set the height beyond limits to demonstrate error handling
        lifting_table.lower_table(80)  # This will raise an error
    except ValueError as e:
        print(f"Error: {e}")
```
