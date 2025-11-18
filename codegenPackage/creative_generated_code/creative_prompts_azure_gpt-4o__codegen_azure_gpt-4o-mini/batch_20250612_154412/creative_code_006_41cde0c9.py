"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unapatches.com
Prompt: Write a program to design shale shaker screens and pipe supports for oil field applications, incorporating the unique fabrication expertise of Jupiter Design & Manufacturing.
Generated: DETERMINISTIC_41cde0c987ed531b
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ShaleShakerScreen:
    """Class to represent a shale shaker screen design."""
    
    def __init__(self, width: float, length: float, mesh_type: str):
        """
        Initializes a shale shaker screen with specified dimensions and mesh type.

        Parameters:
            width (float): The width of the screen in inches.
            length (float): The length of the screen in inches.
            mesh_type (str): The type of mesh used for the screen.
        """
        self.width = width
        self.length = length
        self.mesh_type = mesh_type

    def calculate_area(self) -> float:
        """Calculates the area of the shaker screen."""
        return self.width * self.length

    def to_dict(self) -> Dict[str, Any]:
        """Converts the screen object to a dictionary for JSON serialization."""
        return {
            "width": self.width,
            "length": self.length,
            "mesh_type": self.mesh_type,
            "area": self.calculate_area()
        }

class PipeSupport:
    """Class to represent pipe support design."""
    
    def __init__(self, diameter: float, height: float, material: str):
        """
        Initializes a pipe support with specified diameter, height, and material.

        Parameters:
            diameter (float): The diameter of the pipe in inches.
            height (float): The height of the support in inches.
            material (str): The material used for the support.
        """
        self.diameter = diameter
        self.height = height
        self.material = material

    def calculate_load_capacity(self) -> float:
        """Calculates the load capacity based on material and dimensions."""
        # Placeholder for a more complex calculation based on material properties
        return self.diameter * self.height * 10  # Example load capacity formula

    def to_dict(self) -> Dict[str, Any]:
        """Converts the pipe support object to a dictionary for JSON serialization."""
        return {
            "diameter": self.diameter,
            "height": self.height,
            "material": self.material,
            "load_capacity": self.calculate_load_capacity()
        }

def save_designs_to_file(designs: List[Dict[str, Any]], filename: str) -> None:
    """
    Saves the designs to a JSON file.

    Parameters:
        designs (List[Dict[str, Any]]): The list of design dictionaries to save.
        filename (str): The filename where the designs will be saved.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(designs, file, indent=4)
            logging.info(f"Designs saved successfully to {filename}")
    except IOError as e:
        logging.error(f"Error saving designs to file: {e}")

def main():
    """Main function to create designs and save to a file."""
    try:
        # Create shale shaker screen designs
        screens = [
            ShaleShakerScreen(width=48.0, length=60.0, mesh_type="API 200"),
            ShaleShakerScreen(width=36.0, length=72.0, mesh_type="API 100")
        ]

        # Create pipe support designs
        supports = [
            PipeSupport(diameter=12.0, height=24.0, material="Steel"),
            PipeSupport(diameter=10.0, height=20.0, material="Aluminum")
        ]

        # Aggregate designs into a single list
        designs = {
            "shale_shaker_screens": [screen.to_dict() for screen in screens],
            "pipe_supports": [support.to_dict() for support in supports]
        }

        # Save designs to a JSON file
        save_designs_to_file(designs, 'designs.json')

    except Exception as e:
        logging.error(f"An error occurred in the main execution: {e}")

if __name__ == "__main__":
    main()
```
