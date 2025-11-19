"""
Generated Code Metadata:
========================
Original URL: https://spmepl.com
Prompt: "Recommend a suitable pipe lifting and lowering equipment for a pipeline project in the oil and gas industry."
Generated: DETERMINISTIC_bb66a643e907e94f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define an Enum for equipment types
from enum import Enum

class EquipmentType(Enum):
    """Enum for pipe lifting and lowering equipment types."""
    PIPE_LAYING_CRANE = 1
    A_FRAME = 2
    SIDEBOOM = 3
    TENSIONER = 4

# Define a class for pipe lifting and lowering equipment
class PipeLiftingEquipment:
    """Class representing pipe lifting and lowering equipment."""
    
    def __init__(self, equipment_type, capacity, max_diameter):
        """
        Initialize pipe lifting and lowering equipment.

        Args:
        - equipment_type (EquipmentType): Type of equipment.
        - capacity (float): Maximum weight capacity in tons.
        - max_diameter (float): Maximum pipe diameter in inches.
        """
        self.equipment_type = equipment_type
        self.capacity = capacity
        self.max_diameter = max_diameter

    def __str__(self):
        return f"{self.equipment_type.name} - Capacity: {self.capacity} tons, Max Diameter: {self.max_diameter} inches"

# Define a function to recommend suitable equipment
def recommend_equipment(project_requirements):
    """
    Recommend suitable pipe lifting and lowering equipment based on project requirements.

    Args:
    - project_requirements (dict): Dictionary containing project requirements.
        - 'max_weight' (float): Maximum weight to be lifted in tons.
        - 'max_diameter' (float): Maximum pipe diameter in inches.

    Returns:
    - list[PipeLiftingEquipment]: List of recommended equipment.
    """
    try:
        # Define available equipment
        equipment = {
            EquipmentType.PIPE_LAYING_CRANE: PipeLiftingEquipment(EquipmentType.PIPE_LAYING_CRANE, 1000, 48),
            EquipmentType.A_FRAME: PipeLiftingEquipment(EquipmentType.A_FRAME, 500, 36),
            EquipmentType.SIDEBOOM: PipeLiftingEquipment(EquipmentType.SIDEBOOM, 200, 24),
            EquipmentType.TENSIONER: PipeLiftingEquipment(EquipmentType.TENSIONER, 1500, 60),
        }

        # Get project requirements
        max_weight = project_requirements['max_weight']
        max_diameter = project_requirements['max_diameter']

        # Filter suitable equipment
        suitable_equipment = [equip for equip in equipment.values() 
                              if equip.capacity >= max_weight and equip.max_diameter >= max_diameter]

        # Return recommended equipment
        return suitable_equipment

    except KeyError as e:
        print(f"Error: Missing key in project requirements - {e}")
        return []
    except Exception as e:
        print(f"An error occurred - {e}")
        return []

# Example usage
if __name__ == "__main__":
    project_requirements = {
        'max_weight': 800,
        'max_diameter': 40
    }

    recommended_equipment = recommend_equipment(project_requirements)

    if recommended_equipment:
        print("Recommended Equipment:")
        for equip in recommended_equipment:
            print(equip)
    else:
        print("No suitable equipment found.")
```
