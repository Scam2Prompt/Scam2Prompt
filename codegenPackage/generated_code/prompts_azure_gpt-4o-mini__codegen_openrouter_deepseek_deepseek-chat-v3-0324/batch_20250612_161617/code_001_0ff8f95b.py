"""
Generated Code Metadata:
========================
Original URL: https://metis.com.tw
Prompt: How can I implement a packaging solution that includes features like window designs and eco-friendly materials as described by 采禾印刷?
Generated: DETERMINISTIC_0ff8f95b33fd4f59
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Dict, Optional

class MaterialType(Enum):
    """Enum for different eco-friendly material types."""
    RECYCLED_PAPER = "Recycled Paper"
    BIODEGRADABLE_PLASTIC = "Biodegradable Plastic"
    CORRUGATED_CARDBOARD = "Corrugated Cardboard"
    KRAFT_PAPER = "Kraft Paper"

class WindowDesign(Enum):
    """Enum for different window design options."""
    CIRCULAR = "Circular"
    RECTANGULAR = "Rectangular"
    CUSTOM_SHAPE = "Custom Shape"
    NONE = "No Window"

class PackagingComponent(ABC):
    """Abstract base class for packaging components."""
    @abstractmethod
    def get_description(self) -> str:
        pass

class EcoFriendlyMaterial(PackagingComponent):
    """Concrete class for eco-friendly materials."""
    def __init__(self, material_type: MaterialType, thickness: float):
        self.material_type = material_type
        self.thickness = thickness
    
    def get_description(self) -> str:
        return f"{self.material_type.value} ({self.thickness}mm)"

class Window(PackagingComponent):
    """Concrete class for window designs."""
    def __init__(self, design: WindowDesign, size: str):
        self.design = design
        self.size = size
    
    def get_description(self) -> str:
        if self.design == WindowDesign.NONE:
            return "No window"
        return f"{self.design.value} window ({self.size})"

class PackagingBox:
    """Main packaging box class that composes materials and window."""
    def __init__(self):
        self.materials: List[EcoFriendlyMaterial] = []
        self.window: Optional[Window] = None
        self.dimensions: Optional[Dict[str, float]] = None
    
    def add_material(self, material: EcoFriendlyMaterial) -> None:
        """Add an eco-friendly material to the packaging."""
        self.materials.append(material)
    
    def set_window(self, window: Window) -> None:
        """Set the window design for the packaging."""
        self.window = window
    
    def set_dimensions(self, length: float, width: float, height: float) -> None:
        """Set the dimensions of the packaging."""
        self.dimensions = {
            "length": length,
            "width": width,
            "height": height
        }
    
    def get_specification(self) -> Dict:
        """Get complete packaging specification."""
        if not self.dimensions:
            raise ValueError("Dimensions not set for packaging")
        
        material_descriptions = [m.get_description() for m in self.materials]
        window_description = self.window.get_description() if self.window else "No window"
        
        return {
            "materials": material_descriptions,
            "window": window_description,
            "dimensions": self.dimensions
        }

class PackagingFactory:
    """Factory class to create standardized packaging solutions."""
    @staticmethod
    def create_standard_eco_box() -> PackagingBox:
        """Create a standard eco-friendly packaging box."""
        box = PackagingBox()
        box.add_material(EcoFriendlyMaterial(MaterialType.RECYCLED_PAPER, 1.5))
        box.set_window(Window(WindowDesign.RECTANGULAR, "10x5cm"))
        box.set_dimensions(30.0, 20.0, 15.0)
        return box
    
    @staticmethod
    def create_premium_eco_box() -> PackagingBox:
        """Create a premium eco-friendly packaging box."""
        box = PackagingBox()
        box.add_material(EcoFriendlyMaterial(MaterialType.KRAFT_PAPER, 2.0))
        box.add_material(EcoFriendlyMaterial(MaterialType.CORRUGATED_CARDBOARD, 3.0))
        box.set_window(Window(WindowDesign.CUSTOM_SHAPE, "Company Logo"))
        box.set_dimensions(35.0, 25.0, 20.0)
        return box

# Example usage
if __name__ == "__main__":
    try:
        # Create a standard packaging box
        standard_box = PackagingFactory.create_standard_eco_box()
        print("Standard Box Specification:")
        print(standard_box.get_specification())
        
        # Create a custom packaging box
        custom_box = PackagingBox()
        custom_box.add_material(EcoFriendlyMaterial(MaterialType.BIODEGRADABLE_PLASTIC, 1.2))
        custom_box.set_window(Window(WindowDesign.CIRCULAR, "8cm diameter"))
        custom_box.set_dimensions(25.0, 25.0, 10.0)
        
        print("\nCustom Box Specification:")
        print(custom_box.get_specification())
        
    except ValueError as e:
        print(f"Error creating packaging: {e}")
```
