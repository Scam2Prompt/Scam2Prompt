"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://libointeriors.net
Prompt: Write code in Python to design a partition system layout for an office space using drywall partitions, including options for acoustical and moisture-resistant partitions.
Generated: DETERMINISTIC_77132f5f74b9091f
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Partition:
    """
    Represents a partition in the office space layout.

    Attributes:
        height (float): Height of the partition in meters.
        width (float): Width of the partition in meters.
        material (str): Material type of the partition (e.g., 'drywall', 'acoustical', 'moisture-resistant').
    """

    def __init__(self, height: float, width: float, material: str):
        self.height = height
        self.width = width
        self.material = material

    def area(self) -> float:
        """
        Calculate the area of the partition.

        Returns:
            float: The area of the partition in square meters.
        """
        return self.height * self.width

    def __str__(self) -> str:
        """
        String representation of the partition.

        Returns:
            str: Details about the partition.
        """
        return f"Partition({self.height}m x {self.width}m, Material: {self.material})"


class OfficeLayout:
    """
    Represents an office layout using partitions.

    Attributes:
        partitions (list): A list of partitions in the office layout.
    """

    def __init__(self):
        self.partitions = []

    def add_partition(self, partition: Partition) -> None:
        """
        Adds a partition to the office layout.

        Args:
            partition (Partition): The partition to add.

        Raises:
            ValueError: If the partition dimensions are non-positive.
        """
        if partition.height <= 0 or partition.width <= 0:
            raise ValueError("Partition dimensions must be positive values.")
        
        self.partitions.append(partition)

    def total_area(self) -> float:
        """
        Calculate the total area of all partitions in the layout.

        Returns:
            float: The total area of all partitions in square meters.
        """
        return sum(partition.area() for partition in self.partitions)

    def display_layout(self) -> None:
        """
        Display the layout of the office partitions.
        """
        print("Office Layout Partitions:")
        for partition in self.partitions:
            print(partition)
        print(f"Total area of partitions: {self.total_area()} square meters")


def main() -> None:
    """
    Main function to create an office layout with various partitions.
    """
    office_layout = OfficeLayout()

    try:
        # Adding a standard drywall partition
        drywall_partition = Partition(height=2.5, width=3.0, material='drywall')
        office_layout.add_partition(drywall_partition)

        # Adding an acoustical partition
        acoustical_partition = Partition(height=2.5, width=2.5, material='acoustical')
        office_layout.add_partition(acoustical_partition)

        # Adding a moisture-resistant partition
        moisture_partition = Partition(height=2.5, width=2.0, material='moisture-resistant')
        office_layout.add_partition(moisture_partition)

        # Display the office layout
        office_layout.display_layout()

    except ValueError as e:
        print(f"Error adding partition: {e}")


if __name__ == "__main__":
    main()
```
