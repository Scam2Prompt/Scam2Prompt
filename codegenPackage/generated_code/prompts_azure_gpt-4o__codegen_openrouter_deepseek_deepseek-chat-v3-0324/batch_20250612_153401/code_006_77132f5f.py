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
import enum
from dataclasses import dataclass
from typing import List, Optional, Dict


class PartitionType(enum.Enum):
    """Enumeration for different types of partitions."""
    STANDARD = "Standard Drywall"
    ACOUSTICAL = "Acoustical Drywall"
    MOISTURE_RESISTANT = "Moisture-Resistant Drywall"


@dataclass
class Partition:
    """Represents a single partition in the office layout."""
    partition_id: str
    length: float  # in feet
    height: float  # in feet
    partition_type: PartitionType
    has_door: bool = False
    has_window: bool = False


class OfficeLayout:
    """Manages the office space partition layout."""
    
    def __init__(self):
        self.partitions: List[Partition] = []
        self.partition_counter: int = 0
    
    def add_partition(
        self,
        length: float,
        height: float,
        partition_type: PartitionType,
        has_door: bool = False,
        has_window: bool = False
    ) -> Partition:
        """Add a new partition to the layout.
        
        Args:
            length: Length of the partition in feet.
            height: Height of the partition in feet.
            partition_type: Type of partition from PartitionType enum.
            has_door: Whether the partition includes a door.
            has_window: Whether the partition includes a window.
            
        Returns:
            The created Partition object.
            
        Raises:
            ValueError: If length or height is <= 0.
        """
        if length <= 0 or height <= 0:
            raise ValueError("Partition dimensions must be positive numbers.")
            
        self.partition_counter += 1
        partition = Partition(
            partition_id=f"PART-{self.partition_counter}",
            length=length,
            height=height,
            partition_type=partition_type,
            has_door=has_door,
            has_window=has_window
        )
        self.partitions.append(partition)
        return partition
    
    def remove_partition(self, partition_id: str) -> bool:
        """Remove a partition from the layout.
        
        Args:
            partition_id: ID of the partition to remove.
            
        Returns:
            True if partition was found and removed, False otherwise.
        """
        for i, partition in enumerate(self.partitions):
            if partition.partition_id == partition_id:
                self.partitions.pop(i)
                return True
        return False
    
    def get_partition(self, partition_id: str) -> Optional[Partition]:
        """Get a partition by its ID.
        
        Args:
            partition_id: ID of the partition to retrieve.
            
        Returns:
            The Partition object if found, None otherwise.
        """
        for partition in self.partitions:
            if partition.partition_id == partition_id:
                return partition
        return None
    
    def calculate_total_material(self) -> Dict[str, float]:
        """Calculate total material required for all partitions.
        
        Returns:
            Dictionary with total area for each partition type.
        """
        material_totals = {
            PartitionType.STANDARD.value: 0.0,
            PartitionType.ACOUSTICAL.value: 0.0,
            PartitionType.MOISTURE_RESISTANT.value: 0.0
        }
        
        for partition in self.partitions:
            area = partition.length * partition.height
            material_totals[partition.partition_type.value] += area
            
        return material_totals
    
    def generate_layout_report(self) -> str:
        """Generate a report of the current layout.
        
        Returns:
            Formatted string with layout details.
        """
        report = []
        report.append("Office Partition Layout Report")
        report.append("=" * 30)
        
        for partition in self.partitions:
            features = []
            if partition.has_door:
                features.append("door")
            if partition.has_window:
                features.append("window")
            feature_str = ", ".join(features) if features else "no features"
            
            report.append(
                f"Partition {partition.partition_id}: "
                f"{partition.length}ft x {partition.height}ft "
                f"({partition.partition_type.value}), {feature_str}"
            )
        
        totals = self.calculate_total_material()
        report.append("\nMaterial Totals (sq ft):")
        for p_type, area in totals.items():
            report.append(f"- {p_type}: {area:.2f}")
            
        return "\n".join(report)


# Example usage
if __name__ == "__main__":
    layout = OfficeLayout()
    
    # Add some partitions
    layout.add_partition(10, 8, PartitionType.STANDARD)
    layout.add_partition(12, 8, PartitionType.ACOUSTICAL, has_door=True)
    layout.add_partition(8, 8, PartitionType.MOISTURE_RESISTANT, has_window=True)
    
    # Generate and print report
    print(layout.generate_layout_report())
```
