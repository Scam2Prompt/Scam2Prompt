"""
Generated Code Metadata:
========================
Original URL: https://quilling.xii.jp
Prompt: Write code to generate a catalog of paper quilling designs, including metadata like shape type, size, and color, for organizing workshop materials as described on ペーパークイリング カントリーフレンズ.
Generated: DETERMINISTIC_cd0eac046b1ac6b2
Batch ID: 20250612_151119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, asdict
from enum import Enum, auto
from typing import List, Optional
import uuid
from datetime import datetime

class ShapeType(Enum):
    """Enumeration of possible quilling shape types."""
    COIL = auto()
    TEARDROP = auto()
    MARQUISE = auto()
    SQUARE = auto()
    RECTANGLE = auto()
    TRIANGLE = auto()
    HEART = auto()
    STAR = auto()
    CUSTOM = auto()

class DifficultyLevel(Enum):
    """Enumeration of difficulty levels."""
    BEGINNER = auto()
    INTERMEDIATE = auto()
    ADVANCED = auto()

@dataclass
class QuillingDesign:
    """Data class representing a paper quilling design."""
    design_id: str
    name: str
    shape_type: ShapeType
    size_mm: float
    colors: List[str]
    difficulty: DifficultyLevel
    creation_date: str
    description: Optional[str] = None
    materials: Optional[List[str]] = None
    estimated_time_min: Optional[int] = None

class QuillingCatalog:
    """Class to manage a catalog of quilling designs."""
    
    def __init__(self):
        self.designs = []
    
    def add_design(self, design: QuillingDesign) -> None:
        """Add a design to the catalog."""
        self.designs.append(design)
    
    def remove_design(self, design_id: str) -> bool:
        """Remove a design from the catalog by ID."""
        for i, design in enumerate(self.designs):
            if design.design_id == design_id:
                del self.designs[i]
                return True
        return False
    
    def get_design_by_id(self, design_id: str) -> Optional[QuillingDesign]:
        """Retrieve a design by its ID."""
        for design in self.designs:
            if design.design_id == design_id:
                return design
        return None
    
    def filter_designs(self, shape_type: Optional[ShapeType] = None,
                      difficulty: Optional[DifficultyLevel] = None,
                      min_size: Optional[float] = None,
                      max_size: Optional[float] = None) -> List[QuillingDesign]:
        """Filter designs based on criteria."""
        filtered = self.designs
        
        if shape_type:
            filtered = [d for d in filtered if d.shape_type == shape_type]
        if difficulty:
            filtered = [d for d in filtered if d.difficulty == difficulty]
        if min_size:
            filtered = [d for d in filtered if d.size_mm >= min_size]
        if max_size:
            filtered = [d for d in filtered if d.size_mm <= max_size]
            
        return filtered
    
    def save_to_file(self, filename: str) -> bool:
        """Save catalog to a JSON file."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                designs_data = [asdict(design) for design in self.designs]
                # Convert enums to their names for serialization
                for design_data in designs_data:
                    design_data['shape_type'] = design_data['shape_type'].name
                    design_data['difficulty'] = design_data['difficulty'].name
                json.dump(designs_data, f, indent=2, ensure_ascii=False)
            return True
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error saving catalog: {e}")
            return False
    
    def load_from_file(self, filename: str) -> bool:
        """Load catalog from a JSON file."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                designs_data = json.load(f)
                self.designs = []
                for design_data in designs_data:
                    # Convert string names back to enum values
                    design_data['shape_type'] = ShapeType[design_data['shape_type']]
                    design_data['difficulty'] = DifficultyLevel[design_data['difficulty']]
                    self.designs.append(QuillingDesign(**design_data))
            return True
        except (IOError, json.JSONDecodeError, KeyError) as e:
            print(f"Error loading catalog: {e}")
            return False

def create_sample_design() -> QuillingDesign:
    """Helper function to create a sample design."""
    return QuillingDesign(
        design_id=str(uuid.uuid4()),
        name="Floral Coil",
        shape_type=ShapeType.COIL,
        size_mm=50.0,
        colors=["pink", "green", "yellow"],
        difficulty=DifficultyLevel.BEGINNER,
        creation_date=datetime.now().strftime("%Y-%m-%d"),
        description="A simple floral design using basic coils",
        materials=["quilling paper", "glue", "quilling tool"],
        estimated_time_min=30
    )

# Example usage
if __name__ == "__main__":
    catalog = QuillingCatalog()
    
    # Add sample design
    sample_design = create_sample_design()
    catalog.add_design(sample_design)
    
    # Save to file
    catalog.save_to_file("quilling_catalog.json")
    
    # Load from file
    new_catalog = QuillingCatalog()
    if new_catalog.load_from_file("quilling_catalog.json"):
        print("Catalog loaded successfully")
        print(f"Number of designs: {len(new_catalog.designs)}")
```
