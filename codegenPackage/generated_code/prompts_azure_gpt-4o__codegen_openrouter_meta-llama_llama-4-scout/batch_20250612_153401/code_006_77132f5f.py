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
from enum import Enum
from dataclasses import dataclass

class PartitionType(Enum):
    """Enum for partition types."""
    STANDARD = 1
    ACOUSTICAL = 2
    MOISTURE_RESISTANT = 3

@dataclass
class Partition:
    """Class to represent a partition."""
    type: PartitionType
    length: float  # in feet
    height: float  # in feet
    material: str

    def __post_init__(self):
        """Validate partition attributes."""
        if self.length <= 0 or self.height <= 0:
            raise ValueError("Length and height must be greater than zero.")

class PartitionSystem:
    """Class to design a partition system layout."""
    def __init__(self):
        self.partitions = []

    def add_partition(self, partition: Partition):
        """Add a partition to the system."""
        self.partitions.append(partition)

    def remove_partition(self, index: int):
        """Remove a partition from the system."""
        try:
            del self.partitions[index]
        except IndexError:
            print("Invalid partition index.")

    def calculate_total_area(self) -> float:
        """Calculate the total area of all partitions."""
        total_area = 0
        for partition in self.partitions:
            total_area += partition.length * partition.height
        return total_area

    def print_layout(self):
        """Print the partition system layout."""
        for i, partition in enumerate(self.partitions):
            print(f"Partition {i+1}:")
            print(f"Type: {partition.type.name}")
            print(f"Length: {partition.length} ft")
            print(f"Height: {partition.height} ft")
            print(f"Material: {partition.material}")
            print()

def main():
    # Create a partition system
    system = PartitionSystem()

    # Create partitions
    partition1 = Partition(PartitionType.STANDARD, 10, 8, "Drywall")
    partition2 = Partition(PartitionType.ACOUSTICAL, 12, 9, "Acoustical Drywall")
    partition3 = Partition(PartitionType.MOISTURE_RESISTANT, 8, 7, "Moisture-Resistant Drywall")

    # Add partitions to the system
    system.add_partition(partition1)
    system.add_partition(partition2)
    system.add_partition(partition3)

    # Print the partition system layout
    system.print_layout()

    # Calculate and print the total area
    total_area = system.calculate_total_area()
    print(f"Total Area: {total_area} sq ft")

if __name__ == "__main__":
    main()
```
