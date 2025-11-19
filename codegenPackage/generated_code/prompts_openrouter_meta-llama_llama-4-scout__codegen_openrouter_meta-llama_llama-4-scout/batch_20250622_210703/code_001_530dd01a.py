"""
Generated Code Metadata:
========================
Original URL: https://spmepl.com
Prompt: "What are the different types of pipe clamps used in oil and gas pipeline construction, and how do they work?"
Generated: DETERMINISTIC_530dd01aef1dc047
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class PipeClampType(str, Enum):
    """Enum representing different types of pipe clamps."""
    WELDING = "Welding Clamp"
    BOLTED = "Bolted Clamp"
    HYDRAULIC = "Hydraulic Clamp"
    PNEUMATIC = "Pneumatic Clamp"

class PipeClamp:
    """Class representing a pipe clamp."""
    def __init__(self, clamp_type: PipeClampType, size: str, material: str):
        """
        Initialize a PipeClamp object.

        Args:
        - clamp_type (PipeClampType): The type of pipe clamp.
        - size (str): The size of the pipe clamp.
        - material (str): The material of the pipe clamp.
        """
        self.clamp_type = clamp_type
        self.size = size
        self.material = material

    def __str__(self):
        return f"{self.clamp_type.value} - {self.size} - {self.material}"

class PipeClampGuide:
    """Class providing information on pipe clamps used in oil and gas pipeline construction."""
    def __init__(self):
        self.clamp_types: Dict[PipeClampType, str] = {
            PipeClampType.WELDING: "Used for welding pipes together, provides strong and permanent connection.",
            PipeClampType.BOLTED: "Used for bolting pipes together, provides secure and adjustable connection.",
            PipeClampType.HYDRAULIC: "Used for hydraulic testing and providing temporary connection.",
            PipeClampType.PNEUMATIC: "Used for pneumatic testing and providing temporary connection."
        }

    def get_clamp_types(self) -> Dict[PipeClampType, str]:
        """Get a dictionary of different pipe clamp types and their descriptions."""
        return self.clamp_types

    def get_clamp_working_principle(self, clamp_type: PipeClampType) -> str:
        """
        Get the working principle of a specific pipe clamp type.

        Args:
        - clamp_type (PipeClampType): The type of pipe clamp.

        Returns:
        - str: The working principle of the pipe clamp.

        Raises:
        - ValueError: If the clamp type is not found.
        """
        try:
            return self.clamp_types[clamp_type]
        except KeyError:
            raise ValueError("Invalid clamp type.")

def main():
    guide = PipeClampGuide()
    print("Pipe Clamp Types and Descriptions:")
    for clamp_type, description in guide.get_clamp_types().items():
        print(f"{clamp_type.value}: {description}")

    clamp_type = PipeClampType.WELDING
    print(f"\nWorking Principle of {clamp_type.value}:")
    print(guide.get_clamp_working_principle(clamp_type))

    try:
        invalid_clamp_type = PipeClampType("Invalid")
        print(guide.get_clamp_working_principle(invalid_clamp_type))
    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
```
