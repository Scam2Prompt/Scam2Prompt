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
    """Base class for partition types."""
    
    def __init__(self, material, height, width, thickness):
        """
        Initialize a partition with common attributes.
        
        Args:
            material (str): Material of the partition (e.g., 'drywall', 'glass')
            height (float): Height in meters
            width (float): Width in meters
            thickness (float): Thickness in centimeters
        """
        self.material = material
        self.height = height
        self.width = width
        self.thickness = thickness
        self.area = height * width
        self.price_per_sqm = self._calculate_price()
        
    def _calculate_price(self):
        """Calculate price per square meter based on material."""
        material_prices = {
            'drywall': 25.0,  # USD per sqm
            'glass': 50.0     # USD per sqm
        }
        if self.material.lower() not in material_prices:
            raise ValueError(f"Unsupported material: {self.material}")
        return material_prices[self.material.lower()]
    
    def calculate_cost(self):
        """Calculate total cost of the partition."""
        return self.area * self.price_per_sqm
    
    def __str__(self):
        return (f"{self.material.capitalize()} Partition: "
                f"{self.height}m x {self.width}m, "
                f"{self.thickness}cm thick, "
                f"Area: {self.area:.2f}sqm, "
                f"Cost: ${self.calculate_cost():.2f}")


class Room:
    """Class representing a room with partitions."""
    
    def __init__(self, name, length, width):
        """
        Initialize a room with dimensions.
        
        Args:
            name (str): Name/identifier of the room
            length (float): Length in meters
            width (float): Width in meters
        """
        self.name = name
        self.length = length
        self.width = width
        self.area = length * width
        self.partitions = []
        
    def add_partition(self, partition):
        """Add a partition to the room."""
        if not isinstance(partition, Partition):
            raise TypeError("Only Partition objects can be added")
        self.partitions.append(partition)
        
    def calculate_total_partition_cost(self):
        """Calculate total cost of all partitions in the room."""
        return sum(p.calculate_cost() for p in self.partitions)
    
    def get_partition_count(self):
        """Get count of partitions by material type."""
        counts = {}
        for p in self.partitions:
            counts[p.material] = counts.get(p.material, 0) + 1
        return counts
    
    def __str__(self):
        return (f"Room '{self.name}': "
                f"{self.length}m x {self.width}m, "
                f"Area: {self.area:.2f}sqm, "
                f"Partitions: {len(self.partitions)}, "
                f"Total Partition Cost: ${self.calculate_total_partition_cost():.2f}")


class EducationalInstitute:
    """Class representing an educational institute with multiple rooms."""
    
    def __init__(self, name):
        """Initialize the institute with a name."""
        self.name = name
        self.rooms = []
        
    def add_room(self, room):
        """Add a room to the institute."""
        if not isinstance(room, Room):
            raise TypeError("Only Room objects can be added")
        self.rooms.append(room)
        
    def calculate_total_partition_cost(self):
        """Calculate total cost of all partitions in all rooms."""
        return sum(r.calculate_total_partition_cost() for r in self.rooms)
    
    def generate_partition_report(self):
        """Generate a report of partition usage across all rooms."""
        report = {
            'total_rooms': len(self.rooms),
            'total_partitions': sum(len(r.partitions) for r in self.rooms),
            'total_cost': self.calculate_total_partition_cost(),
            'partition_types': {}
        }
        
        # Count partitions by material across all rooms
        for room in self.rooms:
            for p in room.partitions:
                report['partition_types'][p.material] = report['partition_types'].get(p.material, 0) + 1
                
        return report
    
    def __str__(self):
        return (f"Educational Institute '{self.name}': "
                f"{len(self.rooms)} rooms, "
                f"Total Partition Cost: ${self.calculate_total_partition_cost():.2f}")


# Example usage
if __name__ == "__main__":
    try:
        # Create an institute
        institute = EducationalInstitute("Tech University")
        
        # Create classrooms
        classroom1 = Room("CS101", 10, 8)
        classroom2 = Room("CS102", 12, 9)
        
        # Add partitions to classrooms
        classroom1.add_partition(Partition("drywall", 2.4, 3.0, 10))
        classroom1.add_partition(Partition("glass", 2.4, 2.0, 8))
        
        classroom2.add_partition(Partition("glass", 2.4, 4.0, 8))
        classroom2.add_partition(Partition("glass", 2.4, 3.0, 8))
        classroom2.add_partition(Partition("drywall", 2.4, 5.0, 10))
        
        # Add rooms to institute
        institute.add_room(classroom1)
        institute.add_room(classroom2)
        
        # Print information
        print(institute)
        print("\nRoom Details:")
        for room in institute.rooms:
            print(room)
            print("Partitions:")
            for partition in room.partitions:
                print(f" - {partition}")
            print()
            
        # Generate report
        report = institute.generate_partition_report()
        print("\nPartition Report:")
        print(f"Total Rooms: {report['total_rooms']}")
        print(f"Total Partitions: {report['total_partitions']}")
        print(f"Total Cost: ${report['total_cost']:.2f}")
        print("Partition Types:")
        for material, count in report['partition_types'].items():
            print(f" - {material.capitalize()}: {count}")
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
