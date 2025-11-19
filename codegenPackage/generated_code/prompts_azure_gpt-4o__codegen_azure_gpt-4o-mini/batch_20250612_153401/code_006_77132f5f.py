"""
Generated Code Metadata:
========================
Original URL: https://libointeriors.net
Prompt: Write code in Python to design a partition system layout for an office space using drywall partitions, including options for acoustical and moisture-resistant partitions.
Generated: DETERMINISTIC_77132f5f74b9091f
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Partition:
    """
    A class to represent a drywall partition in an office space.
    
    Attributes:
        name (str): The name of the partition type.
        acoustical (bool): Indicates if the partition is acoustical.
        moisture_resistant (bool): Indicates if the partition is moisture-resistant.
        height (float): The height of the partition in meters.
        width (float): The width of the partition in meters.
    """

    def __init__(self, name, acoustical=False, moisture_resistant=False, height=2.4, width=0.1):
        """
        Initializes a new Partition instance.

        Parameters:
            name (str): The name of the partition type.
            acoustical (bool): Indicates if the partition is acoustical.
            moisture_resistant (bool): Indicates if the partition is moisture-resistant.
            height (float): The height of the partition in meters.
            width (float): The width of the partition in meters.
        """
        self.name = name
        self.acoustical = acoustical
        self.moisture_resistant = moisture_resistant
        self.height = height
        self.width = width

    def area(self):
        """
        Calculates the area of the partition.

        Returns:
            float: The area of the partition in square meters.
        """
        return self.height * self.width

    def __str__(self):
        """
        Returns a string representation of the Partition instance.

        Returns:
            str: A description of the partition.
        """
        return (f"Partition(name={self.name}, acoustical={self.acoustical}, "
                f"moisture_resistant={self.moisture_resistant}, "
                f"height={self.height}, width={self.width})")


class OfficeLayout:
    """
    A class to represent an office layout consisting of multiple partitions.

    Attributes:
        partitions (list): A list of Partition instances in the office layout.
    """

    def __init__(self):
        """Initializes an empty OfficeLayout."""
        self.partitions = []

    def add_partition(self, partition):
        """
        Adds a partition to the office layout.

        Parameters:
            partition (Partition): The partition to be added.
        """
        if not isinstance(partition, Partition):
            raise ValueError("Only Partition instances can be added.")
        self.partitions.append(partition)

    def total_area(self):
        """
        Calculates the total area of all partitions in the layout.

        Returns:
            float: The total area of the partitions in square meters.
        """
        return sum(partition.area() for partition in self.partitions)

    def __str__(self):
        """
        Returns a string representation of the OfficeLayout instance.

        Returns:
            str: A description of the office layout.
        """
        return f"OfficeLayout with {len(self.partitions)} partitions."


# Example usage
if __name__ == "__main__":
    try:
        # Create an office layout
        office_layout = OfficeLayout()

        # Create different types of partitions
        partition1 = Partition(name="Standard Drywall", acoustical=False, moisture_resistant=False)
        partition2 = Partition(name="Acoustical Drywall", acoustical=True, moisture_resistant=False)
        partition3 = Partition(name="Moisture-Resistant Drywall", acoustical=False, moisture_resistant=True)

        # Add partitions to the office layout
        office_layout.add_partition(partition1)
        office_layout.add_partition(partition2)
        office_layout.add_partition(partition3)

        # Print the total area of the office layout
        print(f"Total area of office layout: {office_layout.total_area()} m²")
        print(office_layout)

    except Exception as e:
        print(f"An error occurred: {e}")
```
