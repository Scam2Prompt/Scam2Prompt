"""
Generated Code Metadata:
========================
Original URL: https://unapatches.com
Prompt: Write a Python script to automate the process of generating quotes for CNC cutting services, considering factors like material type, thickness, and design specifications.
Generated: DETERMINISTIC_50f172d74db3bb4a
Batch ID: 20250622_211652
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
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import math
import datetime

# Constants
DEFAULT_MARKUP_PERCENTAGE = 0.20  # 20% markup for profit
DEFAULT_CUTTING_SPEED = 1000  # mm/min
DEFAULT_CUTTING_COST_PER_MINUTE = 0.50  # $ per minute
DEFAULT_SETUP_FEE = 25.00  # Base setup fee

class MaterialType(Enum):
    """Enum representing different material types."""
    ALUMINUM = "aluminum"
    STEEL = "steel"
    STAINLESS_STEEL = "stainless_steel"
    COPPER = "copper"
    BRASS = "brass"
    PLASTIC = "plastic"
    WOOD = "wood"

@dataclass
class Material:
    """Dataclass representing material properties."""
    type: MaterialType
    thickness: float  # in mm
    cost_per_sheet: float  # cost per standard sheet (e.g., 4x8 feet)
    sheet_area: float  # area in square mm
    cutting_factor: float  # multiplier for cutting difficulty

@dataclass
class DesignSpecs:
    """Dataclass representing design specifications."""
    total_cutting_length: float  # in mm
    complexity_factor: float  # multiplier for design complexity (1.0 = simple)
    holes_count: int  # number of holes to drill
    inner_cuts_count: int  # number of inner cuts

@dataclass
class Quote:
    """Dataclass representing a generated quote."""
    material_cost: float
    cutting_cost: float
    setup_cost: float
    total_cost: float
    quote_date: str
    expiry_date: str
    quote_id: str

class CNCQuoteGenerator:
    """Class to generate quotes for CNC cutting services."""
    
    def __init__(self):
        self.material_db = self._load_material_database()
        self.quote_counter = 0
    
    def _load_material_database(self) -> Dict[MaterialType, Dict[float, Material]]:
        """Load material database from a JSON file."""
        try:
            with open('material_db.json', 'r') as f:
                data = json.load(f)
                material_db = {}
                for material_type, thickness_data in data.items():
                    material_type_enum = MaterialType(material_type)
                    material_db[material_type_enum] = {}
                    for thickness_str, props in thickness_data.items():
                        thickness = float(thickness_str)
                        material_db[material_type_enum][thickness] = Material(
                            type=material_type_enum,
                            thickness=thickness,
                            cost_per_sheet=props['cost_per_sheet'],
                            sheet_area=props['sheet_area'],
                            cutting_factor=props['cutting_factor']
                        )
                return material_db
        except FileNotFoundError:
            raise Exception("Material database file not found.")
        except json.JSONDecodeError:
            raise Exception("Invalid material database format.")
        except KeyError as e:
            raise Exception(f"Missing key in material database: {e}")

    def _calculate_material_cost(self, material: Material, design: DesignSpecs) -> float:
        """
        Calculate material cost based on usage.
        
        Args:
            material: Material being used
            design: Design specifications
            
        Returns:
            Calculated material cost
        """
        # Estimate material usage based on cutting length and thickness
        usage_factor = min(1.0, (design.total_cutting_length * material.thickness) / material.sheet_area)
        return material.cost_per_sheet * usage_factor

    def _calculate_cutting_time(self, design: DesignSpecs, material: Material) -> float:
        """
        Calculate estimated cutting time in minutes.
        
        Args:
            design: Design specifications
            material: Material being used
            
        Returns:
            Estimated cutting time in minutes
        """
        base_time = design.total_cutting_length / DEFAULT_CUTTING_SPEED
        adjusted_time = base_time * material.cutting_factor * design.complexity_factor
        # Add time for holes and inner cuts
        adjusted_time += (design.holes_count * 0.1) + (design.inner_cuts_count * 0.2)
        return max(0.1, adjusted_time)  # Minimum 0.1 minutes

    def _generate_quote_id(self) -> str:
        """Generate a unique quote ID."""
        self.quote_counter += 1
        timestamp = datetime.datetime.now().strftime("%Y%m%d")
        return f"CNC-{timestamp}-{self.quote_counter:04d}"

    def generate_quote(
        self,
        material_type: MaterialType,
        thickness: float,
        design: DesignSpecs,
        markup_percentage: Optional[float] = None
    ) -> Quote:
        """
        Generate a quote for CNC cutting service.
        
        Args:
            material_type: Type of material
            thickness: Material thickness in mm
            design: Design specifications
            markup_percentage: Optional markup percentage (default is 20%)
            
        Returns:
            Generated Quote object
            
        Raises:
            ValueError: If material/thickness combination is not available
        """
        markup = markup_percentage if markup_percentage is not None else DEFAULT_MARKUP_PERCENTAGE
        
        try:
            material = self.material_db[material_type][thickness]
        except KeyError:
            available_thicknesses = list(self.material_db[material_type].keys())
            raise ValueError(
                f"Material {material_type.value} with thickness {thickness}mm not available. "
                f"Available thicknesses: {available_thicknesses}"
            )

        # Calculate costs
        material_cost = self._calculate_material_cost(material, design)
        cutting_time = self._calculate_cutting_time(design, material)
        cutting_cost = cutting_time * DEFAULT_CUTTING_COST_PER_MINUTE
        setup_cost = DEFAULT_SETUP_FEE
        
        # Calculate total cost with markup
        base_cost = material_cost + cutting_cost + setup_cost
        total_cost = base_cost * (1 + markup)
        
        # Generate dates
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        expiry_date = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d")
        
        return Quote(
            material_cost=round(material_cost, 2),
            cutting_cost=round(cutting_cost, 2),
            setup_cost=round(setup_cost, 2),
            total_cost=round(total_cost, 2),
            quote_date=today,
            expiry_date=expiry_date,
            quote_id=self._generate_quote_id()
        )

# Example usage
if __name__ == "__main__":
    try:
        generator = CNCQuoteGenerator()
        
        # Example design specifications
        design_specs = DesignSpecs(
            total_cutting_length=5000,  # 5 meters
            complexity_factor=1.2,  # Moderately complex
            holes_count=8,
            inner_cuts_count=3
        )
        
        # Generate quote
        quote = generator.generate_quote(
            material_type=MaterialType.ALUMINUM,
            thickness=3.0,
            design=design_specs
        )
        
        # Print quote details
        print("Generated CNC Cutting Quote:")
        print(f"Quote ID: {quote.quote_id}")
        print(f"Date: {quote.quote_date} (Expires: {quote.expiry_date})")
        print(f"Material Cost: ${quote.material_cost:.2f}")
        print(f"Cutting Cost: ${quote.cutting_cost:.2f}")
        print(f"Setup Cost: ${quote.setup_cost:.2f}")
        print(f"Total Cost: ${quote.total_cost:.2f}")
        
    except Exception as e:
        print(f"Error generating quote: {e}")
```
