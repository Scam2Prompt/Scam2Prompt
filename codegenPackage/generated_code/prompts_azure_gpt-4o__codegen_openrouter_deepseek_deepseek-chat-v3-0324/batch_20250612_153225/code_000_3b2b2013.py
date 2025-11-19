"""
Generated Code Metadata:
========================
Original URL: https://shelterder.com
Prompt: Write code to design a custom fireplace configuration using Planika BEV Technology™ for bioethanol fireplaces, ensuring eco-friendly and odorless operation.
Generated: DETERMINISTIC_3b2b2013c71a8ae6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import List, Dict, Optional

class FuelType(Enum):
    """Enumeration for bioethanol fuel types."""
    BIOETHANOL = "Bioethanol"
    ECO_FRIENDLY = "Eco-Friendly Bioethanol"

class BurnerType(Enum):
    """Enumeration for burner types."""
    SINGLE = "Single"
    DOUBLE = "Double"
    TRIPLE = "Triple"

class FireplaceDesign:
    """Class representing a custom fireplace configuration."""
    
    def __init__(
        self,
        model_name: str,
        burner_type: BurnerType,
        fuel_type: FuelType,
        width: float,
        height: float,
        depth: float,
        features: Optional[List[str]] = None
    ):
        """
        Initialize a FireplaceDesign instance.
        
        Args:
            model_name (str): Name of the fireplace model.
            burner_type (BurnerType): Type of burner (SINGLE, DOUBLE, TRIPLE).
            fuel_type (FuelType): Type of fuel (BIOETHANOL, ECO_FRIENDLY).
            width (float): Width of the fireplace in cm.
            height (float): Height of the fireplace in cm.
            depth (float): Depth of the fireplace in cm.
            features (List[str], optional): List of additional features. Defaults to None.
        """
        self.model_name = model_name
        self.burner_type = burner_type
        self.fuel_type = fuel_type
        self.width = width
        self.height = height
        self.depth = depth
        self.features = features if features else []
    
    def validate_dimensions(self) -> bool:
        """Validate the fireplace dimensions."""
        if self.width <= 0 or self.height <= 0 or self.depth <= 0:
            raise ValueError("Dimensions must be positive numbers.")
        return True
    
    def add_feature(self, feature: str) -> None:
        """Add a feature to the fireplace configuration."""
        if feature not in self.features:
            self.features.append(feature)
    
    def to_dict(self) -> Dict:
        """Convert the fireplace configuration to a dictionary."""
        return {
            "model_name": self.model_name,
            "burner_type": self.burner_type.value,
            "fuel_type": self.fuel_type.value,
            "width": self.width,
            "height": self.height,
            "depth": self.depth,
            "features": self.features
        }
    
    def to_json(self) -> str:
        """Serialize the fireplace configuration to JSON."""
        return json.dumps(self.to_dict(), indent=2)

class FireplaceConfigurator:
    """Class to configure and manage custom fireplaces."""
    
    def __init__(self):
        self.designs: List[FireplaceDesign] = []
    
    def create_design(
        self,
        model_name: str,
        burner_type: BurnerType,
        fuel_type: FuelType,
        width: float,
        height: float,
        depth: float,
        features: Optional[List[str]] = None
    ) -> FireplaceDesign:
        """
        Create a new fireplace design.
        
        Args:
            model_name (str): Name of the fireplace model.
            burner_type (BurnerType): Type of burner.
            fuel_type (FuelType): Type of fuel.
            width (float): Width in cm.
            height (float): Height in cm.
            depth (float): Depth in cm.
            features (List[str], optional): List of features. Defaults to None.
        
        Returns:
            FireplaceDesign: The created fireplace design.
        """
        design = FireplaceDesign(
            model_name=model_name,
            burner_type=burner_type,
            fuel_type=fuel_type,
            width=width,
            height=height,
            depth=depth,
            features=features
        )
        design.validate_dimensions()
        self.designs.append(design)
        return design
    
    def get_design_by_name(self, model_name: str) -> Optional[FireplaceDesign]:
        """
        Retrieve a fireplace design by model name.
        
        Args:
            model_name (str): Name of the model to search for.
        
        Returns:
            Optional[FireplaceDesign]: The design if found, else None.
        """
        for design in self.designs:
            if design.model_name == model_name:
                return design
        return None
    
    def save_designs_to_file(self, filename: str) -> None:
        """
        Save all designs to a JSON file.
        
        Args:
            filename (str): Name of the file to save to.
        
        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            with open(filename, 'w') as f:
                json.dump([design.to_dict() for design in self.designs], f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to save designs to file: {e}")
    
    def load_designs_from_file(self, filename: str) -> None:
        """
        Load designs from a JSON file.
        
        Args:
            filename (str): Name of the file to load from.
        
        Raises:
            IOError: If there is an issue reading the file.
            ValueError: If the file contains invalid data.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for item in data:
                    design = FireplaceDesign(
                        model_name=item["model_name"],
                        burner_type=BurnerType(item["burner_type"]),
                        fuel_type=FuelType(item["fuel_type"]),
                        width=item["width"],
                        height=item["height"],
                        depth=item["depth"],
                        features=item["features"]
                    )
                    design.validate_dimensions()
                    self.designs.append(design)
        except IOError as e:
            raise IOError(f"Failed to load designs from file: {e}")
        except (KeyError, ValueError) as e:
            raise ValueError(f"Invalid data in file: {e}")

# Example usage
if __name__ == "__main__":
    configurator = FireplaceConfigurator()
    
    # Create a new design
    design = configurator.create_design(
        model_name="EcoFlame Pro",
        burner_type=BurnerType.DOUBLE,
        fuel_type=FuelType.ECO_FRIENDLY,
        width=120.0,
        height=80.0,
        depth=40.0,
        features=["Remote Control", "Safety Lock"]
    )
    
    # Add a feature
    design.add_feature("Adjustable Flame")
    
    # Save designs to file
    try:
        configurator.save_designs_to_file("fireplace_designs.json")
    except IOError as e:
        print(f"Error saving designs: {e}")
    
    # Load designs from file
    try:
        configurator.load_designs_from_file("fireplace_designs.json")
    except (IOError, ValueError) as e:
        print(f"Error loading designs: {e}")
    
    # Print a design as JSON
    print(design.to_json())
```
