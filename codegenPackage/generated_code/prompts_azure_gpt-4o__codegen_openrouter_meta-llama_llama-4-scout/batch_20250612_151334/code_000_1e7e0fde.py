"""
Generated Code Metadata:
========================
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Write a Python script to filter tire products by width, height, and rim size, as described on the "Dal Cortivo Pneus" website, and display the filtered results.
Generated: DETERMINISTIC_1e7e0fdeeee3bb8e
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tire_filter.py

class Tire:
    def __init__(self, width, height, rim_size, description):
        """
        Initialize a Tire object.

        Args:
            width (int): The width of the tire.
            height (int): The height of the tire.
            rim_size (int): The rim size of the tire.
            description (str): A description of the tire.
        """
        self.width = width
        self.height = height
        self.rim_size = rim_size
        self.description = description

    def __repr__(self):
        return f"Tire(width={self.width}, height={self.height}, rim_size={self.rim_size}, description='{self.description}')"


class TireFilter:
    def __init__(self, tires):
        """
        Initialize a TireFilter object.

        Args:
            tires (list[Tire]): A list of Tire objects.
        """
        self.tires = tires

    def filter_by_width(self, width):
        """
        Filter tires by width.

        Args:
            width (int): The width to filter by.

        Returns:
            list[Tire]: A list of tires with the specified width.
        """
        return [tire for tire in self.tires if tire.width == width]

    def filter_by_height(self, height):
        """
        Filter tires by height.

        Args:
            height (int): The height to filter by.

        Returns:
            list[Tire]: A list of tires with the specified height.
        """
        return [tire for tire in self.tires if tire.height == height]

    def filter_by_rim_size(self, rim_size):
        """
        Filter tires by rim size.

        Args:
            rim_size (int): The rim size to filter by.

        Returns:
            list[Tire]: A list of tires with the specified rim size.
        """
        return [tire for tire in self.tires if tire.rim_size == rim_size]

    def filter(self, width=None, height=None, rim_size=None):
        """
        Filter tires by width, height, and rim size.

        Args:
            width (int, optional): The width to filter by. Defaults to None.
            height (int, optional): The height to filter by. Defaults to None.
            rim_size (int, optional): The rim size to filter by. Defaults to None.

        Returns:
            list[Tire]: A list of tires that match the specified filters.
        """
        filtered_tires = self.tires
        if width:
            filtered_tires = self.filter_by_width(width)
        if height:
            filtered_tires = self.filter_by_height(height)
        if rim_size:
            filtered_tires = self.filter_by_rim_size(rim_size)
        return filtered_tires


def main():
    try:
        # Example tires
        tires = [
            Tire(205, 55, 16, "Tire 1"),
            Tire(215, 60, 17, "Tire 2"),
            Tire(225, 65, 18, "Tire 3"),
            Tire(205, 55, 16, "Tire 4"),
            Tire(215, 60, 17, "Tire 5"),
        ]

        filter = TireFilter(tires)

        # Example usage
        width = 215
        height = 60
        rim_size = 17

        filtered_tires = filter.filter(width=width, height=height, rim_size=rim_size)

        print(f"Filtered Tires (Width: {width}, Height: {height}, Rim Size: {rim_size}):")
        for tire in filtered_tires:
            print(tire)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
