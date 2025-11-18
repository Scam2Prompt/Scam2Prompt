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
import json


class Partition:
    """
    Represents a generic drywall partition.
    Includes options for acoustical and moisture resistance.
    """

    def __init__(self, name, length, height, acoustical=False, moisture_resistant=False):
        """
        Initializes a partition with given attributes.

        :param name: Name of the partition
        :param length: Length of the partition in meters
        :param height: Height of the partition in meters
        :param acoustical: Whether the partition is acoustical
        :param moisture_resistant: Whether the partition is moisture-resistant
        """
        self.name = name
        self.length = length
        self.height = height
        self.acoustical = acoustical
        self.moisture_resistant = moisture_resistant

    def calculate_area(self):
        """
        Calculates the area of the partition.

        :return: Area of the partition in square meters
        """
        return self.length * self.height

    def get_details(self):
        """
        Returns a dictionary containing the partition's details.

        :return: Dictionary of partition attributes
        """
        return {
            "name": self.name,
            "length": self.length,
            "height": self.height,
            "area": self.calculate_area(),
            "acoustical": self.acoustical,
            "moisture_resistant": self.moisture_resistant,
        }


class PartitionSystem:
    """
    Represents a layout of partitions in an office space.
    Allows adding, removing, and viewing partitions.
    """

    def __init__(self):
        """
        Initializes an empty partition system.
        """
        self.partitions = []

    def add_partition(self, partition):
        """
        Adds a partition to the system.

        :param partition: Partition object to add
        """
        if not isinstance(partition, Partition):
            raise TypeError("Invalid partition object. Must be of type Partition.")
        self.partitions.append(partition)

    def remove_partition(self, name):
        """
        Removes a partition from the system by name.

        :param name: Name of the partition to remove
        """
        self.partitions = [p for p in self.partitions if p.name != name]

    def get_partition_details(self):
        """
        Retrieves details for all partitions in the system.

        :return: List of dictionaries containing partition details
        """
        return [partition.get_details() for partition in self.partitions]

    def save_to_file(self, filename="partition_system.json"):
        """
        Saves the partition system details to a JSON file.

        :param filename: Name of the file to save (default: "partition_system.json")
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.get_partition_details(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename="partition_system.json"):
        """
        Loads partition system details from a JSON file.

        :param filename: Name of the file to load (default: "partition_system.json")
        """
        try:
            with open(filename, "r") as file:
                partitions_data = json.load(file)
                self.partitions = [
                    Partition(
                        name=data["name"],
                        length=data["length"],
                        height=data["height"],
                        acoustical=data["acoustical"],
                        moisture_resistant=data["moisture_resistant"],
                    )
                    for data in partitions_data
                ]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")


# Example usage:
if __name__ == "__main__":
    # Create a partition system
    system = PartitionSystem()

    # Add partitions
    system.add_partition(Partition("Partition A", 5, 3, acoustical=True, moisture_resistant=False))
    system.add_partition(Partition("Partition B", 4, 2.5, acoustical=False, moisture_resistant=True))

    # Get details of all partitions
    print("Partition Details:")
    for partition in system.get_partition_details():
        print(partition)

    # Save partition system to file
    system.save_to_file()

    # Load partition system from file
    system.load_from_file()
    print("\nLoaded Partition Details:")
    for partition in system.get_partition_details():
        print(partition)
```
