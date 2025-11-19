"""
Generated Code Metadata:
========================
Original URL: https://libointeriors.net
Prompt: "Design a partition system for an educational institute using drywall and glass partitions."
Generated: DETERMINISTIC_15ccd0aca133d758
Batch ID: 20250622_210802
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
    A class to represent a partition in an educational institute.
    
    Attributes:
        material (str): The material of the partition (e.g., drywall, glass).
        height (float): The height of the partition in meters.
        width (float): The width of the partition in meters.
        is_soundproof (bool): Indicates if the partition is soundproof.
    """

    def __init__(self, material: str, height: float, width: float, is_soundproof: bool = False):
        """
        Initializes a new Partition instance.

        Args:
            material (str): The material of the partition.
            height (float): The height of the partition.
            width (float): The width of the partition.
            is_soundproof (bool): Whether the partition is soundproof. Defaults to False.
        
        Raises:
            ValueError: If height or width is not positive.
        """
        if height <= 0 or width <= 0:
            raise ValueError("Height and width must be positive values.")
        
        self.material = material
        self.height = height
        self.width = width
        self.is_soundproof = is_soundproof

    def area(self) -> float:
        """
        Calculates the area of the partition.

        Returns:
            float: The area of the partition in square meters.
        """
        return self.height * self.width

    def __str__(self) -> str:
        """
        Returns a string representation of the Partition instance.

        Returns:
            str: A description of the partition.
        """
        soundproof_status = "Soundproof" if self.is_soundproof else "Not soundproof"
        return f"Partition(Material: {self.material}, Height: {self.height}m, Width: {self.width}m, {soundproof_status})"


class PartitionSystem:
    """
    A class to manage a system of partitions in an educational institute.
    
    Attributes:
        partitions (list): A list of Partition instances.
    """

    def __init__(self):
        """Initializes the PartitionSystem with an empty list of partitions."""
        self.partitions = []

    def add_partition(self, partition: Partition):
        """
        Adds a new partition to the system.

        Args:
            partition (Partition): The partition to be added.
        """
        self.partitions.append(partition)

    def total_area(self) -> float:
        """
        Calculates the total area of all partitions in the system.

        Returns:
            float: The total area of all partitions in square meters.
        """
        return sum(partition.area() for partition in self.partitions)

    def __str__(self) -> str:
        """
        Returns a string representation of the PartitionSystem instance.

        Returns:
            str: A description of all partitions in the system.
        """
        return "\n".join(str(partition) for partition in self.partitions)


# Example usage
if __name__ == "__main__":
    try:
        # Create a partition system
        partition_system = PartitionSystem()

        # Add drywall partition
        drywall_partition = Partition(material="Drywall", height=2.5, width=3.0, is_soundproof=False)
        partition_system.add_partition(drywall_partition)

        # Add glass partition
        glass_partition = Partition(material="Glass", height=2.5, width=4.0, is_soundproof=True)
        partition_system.add_partition(glass_partition)

        # Print the total area of partitions
        print("Total area of partitions:", partition_system.total_area(), "square meters")

        # Print details of all partitions
        print("Partitions in the system:")
        print(partition_system)

    except ValueError as e:
        print(f"Error: {e}")
```
