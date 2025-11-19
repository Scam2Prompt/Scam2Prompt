"""
Generated Code Metadata:
========================
Original URL: https://libointeriors.net
Prompt: "Design a raised access flooring system for a data centre using calcium sulphate materials."
Generated: DETERMINISTIC_24236b5b3842a9e8
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Raised Access Flooring System Design for Data Centre using Calcium Sulphate Materials

This module provides a class to design and calculate specifications for a raised access flooring system
using calcium sulphate panels for data centre applications.
"""

import math
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, Tuple, List

class PanelType(Enum):
    """Enumeration of available calcium sulphate panel types"""
    STANDARD = auto()
    HIGH_LOAD = auto()
    ULTRA_LOAD = auto()

@dataclass
class PanelSpecs:
    """Dataclass containing specifications for a panel type"""
    type: PanelType
    thickness: float  # mm
    load_capacity: float  # kN/m²
    weight: float  # kg/m²
    fire_rating: str
    thermal_conductivity: float  # W/mK

class RaisedFloorDesign:
    """
    Class for designing a raised access flooring system using calcium sulphate panels.
    
    Attributes:
        panel_specs (dict): Dictionary mapping panel types to their specifications
        pedestal_height (float): Height of pedestals in mm
        grid_layout (Tuple[int, int]): Number of panels in x and y directions
        panel_size (float): Standard panel size in mm (typically 600x600mm)
    """
    
    def __init__(self):
        """Initialize with default panel specifications"""
        self.panel_specs = {
            PanelType.STANDARD: PanelSpecs(
                type=PanelType.STANDARD,
                thickness=32.0,
                load_capacity=12.5,
                weight=42.0,
                fire_rating="Class A1",
                thermal_conductivity=0.25
            ),
            PanelType.HIGH_LOAD: PanelSpecs(
                type=PanelType.HIGH_LOAD,
                thickness=40.0,
                load_capacity=20.0,
                weight=50.0,
                fire_rating="Class A1",
                thermal_conductivity=0.25
            ),
            PanelType.ULTRA_LOAD: PanelSpecs(
                type=PanelType.ULTRA_LOAD,
                thickness=50.0,
                load_capacity=30.0,
                weight=60.0,
                fire_rating="Class A1",
                thermal_conductivity=0.25
            )
        }
        self.pedestal_height = 300.0  # mm
        self.grid_layout = (0, 0)  # (x, y)
        self.panel_size = 600.0  # mm
        
    def set_pedestal_height(self, height: float) -> None:
        """Set the pedestal height for the raised floor system"""
        if height < 150 or height > 1000:
            raise ValueError("Pedestal height must be between 150mm and 1000mm")
        self.pedestal_height = height
        
    def set_grid_layout(self, x_panels: int, y_panels: int) -> None:
        """Set the grid layout dimensions"""
        if x_panels <= 0 or y_panels <= 0:
            raise ValueError("Number of panels must be positive integers")
        self.grid_layout = (x_panels, y_panels)
        
    def calculate_total_area(self) -> float:
        """Calculate total floor area in square meters"""
        if self.grid_layout == (0, 0):
            raise ValueError("Grid layout not set")
        x, y = self.grid_layout
        return (x * self.panel_size / 1000) * (y * self.panel_size / 1000)
        
    def calculate_total_panels(self) -> int:
        """Calculate total number of panels required"""
        if self.grid_layout == (0, 0):
            raise ValueError("Grid layout not set")
        x, y = self.grid_layout
        return x * y
        
    def calculate_total_weight(self, panel_type: PanelType) -> float:
        """
        Calculate total weight of all panels in kg
        
        Args:
            panel_type: Selected panel type from PanelType enum
            
        Returns:
            Total weight in kg
        """
        if panel_type not in self.panel_specs:
            raise ValueError("Invalid panel type")
        return self.calculate_total_panels() * (self.panel_size/1000)**2 * self.panel_specs[panel_type].weight
        
    def calculate_load_capacity(self, panel_type: PanelType) -> float:
        """
        Calculate total load capacity of the floor system in kN
        
        Args:
            panel_type: Selected panel type from PanelType enum
            
        Returns:
            Total load capacity in kN
        """
        if panel_type not in self.panel_specs:
            raise ValueError("Invalid panel type")
        return self.calculate_total_area() * self.panel_specs[panel_type].load_capacity
        
    def recommend_panel_type(self, expected_load: float) -> PanelType:
        """
        Recommend panel type based on expected load
        
        Args:
            expected_load: Expected load in kN/m²
            
        Returns:
            Recommended PanelType
        """
        if expected_load <= 0:
            raise ValueError("Expected load must be positive")
            
        for panel_type in [PanelType.ULTRA_LOAD, PanelType.HIGH_LOAD, PanelType.STANDARD]:
            if self.panel_specs[panel_type].load_capacity >= expected_load:
                return panel_type
                
        raise ValueError("No suitable panel type found for the expected load")
        
    def generate_materials_list(self, panel_type: PanelType) -> dict:
        """
        Generate a materials list for the flooring system
        
        Args:
            panel_type: Selected panel type from PanelType enum
            
        Returns:
            Dictionary containing materials quantities
        """
        if panel_type not in self.panel_specs:
            raise ValueError("Invalid panel type")
        if self.grid_layout == (0, 0):
            raise ValueError("Grid layout not set")
            
        x, y = self.grid_layout
        total_panels = x * y
        total_pedestals = (x + 1) * (y + 1)
        
        return {
            "calcium_sulphate_panels": {
                "type": panel_type.name,
                "quantity": total_panels,
                "size_mm": f"{self.panel_size}x{self.panel_size}",
                "thickness_mm": self.panel_specs[panel_type].thickness
            },
            "pedestals": {
                "quantity": total_pedestals,
                "height_mm": self.pedestal_height
            },
            "stringers": {
                "quantity": x * (y + 1) + y * (x + 1),
                "length_mm": self.panel_size
            }
        }
```
