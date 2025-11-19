"""
Generated Code Metadata:
========================
Original URL: https://workshopgranada.com
Prompt: "Write a Python program to generate custom sewing patterns based on user input for garment type, fabric type, and measurements."
Generated: DETERMINISTIC_39fc49e0d4435d53
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List, Optional


class GarmentType(Enum):
    DRESS = auto()
    SHIRT = auto()
    PANTS = auto()
    SKIRT = auto()


class FabricType(Enum):
    COTTON = auto()
    SILK = auto()
    DENIM = auto()
    WOOL = auto()
    POLYESTER = auto()


@dataclass
class Measurements:
    bust: Optional[float] = None
    waist: Optional[float] = None
    hips: Optional[float] = None
    length: Optional[float] = None
    shoulder_width: Optional[float] = None
    arm_length: Optional[float] = None
    inseam: Optional[float] = None


class PatternGenerator:
    """Generates sewing patterns based on garment type, fabric, and measurements."""
    
    def __init__(self):
        self.pattern_templates = self._load_pattern_templates()
    
    def _load_pattern_templates(self) -> Dict[str, Dict]:
        """Load pattern templates from JSON file."""
        try:
            with open('pattern_templates.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError("Pattern templates file not found.")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON in pattern templates file.")
    
    def _validate_measurements(self, garment_type: GarmentType, measurements: Measurements) -> None:
        """Validate that required measurements are provided for the garment type."""
        required = {
            GarmentType.DRESS: ['bust', 'waist', 'hips', 'length'],
            GarmentType.SHIRT: ['bust', 'shoulder_width', 'arm_length', 'length'],
            GarmentType.PANTS: ['waist', 'hips', 'inseam'],
            GarmentType.SKIRT: ['waist', 'hips', 'length']
        }
        
        missing = []
        for field in required[garment_type]:
            if getattr(measurements, field) is None:
                missing.append(field)
        
        if missing:
            raise ValueError(f"Missing required measurements: {', '.join(missing)}")
    
    def _adjust_for_fabric(self, pattern: Dict, fabric_type: FabricType) -> Dict:
        """Adjust pattern based on fabric type properties."""
        fabric_adjustments = {
            FabricType.COTTON: {'seam_allowance': 1.5, 'ease': 2.0},
            FabricType.SILK: {'seam_allowance': 1.0, 'ease': 3.0},
            FabricType.DENIM: {'seam_allowance': 2.0, 'ease': 1.5},
            FabricType.WOOL: {'seam_allowance': 1.5, 'ease': 2.5},
            FabricType.POLYESTER: {'seam_allowance': 1.0, 'ease': 2.0}
        }
        
        adjusted_pattern = pattern.copy()
        adjustments = fabric_adjustments[fabric_type]
        
        for piece in adjusted_pattern['pieces']:
            piece['seam_allowance'] = adjustments['seam_allowance']
            if 'width' in piece:
                piece['width'] += adjustments['ease']
            if 'length' in piece:
                piece['length'] += adjustments['ease']
        
        return adjusted_pattern
    
    def generate_pattern(
        self,
        garment_type: GarmentType,
        fabric_type: FabricType,
        measurements: Measurements
    ) -> Dict:
        """
        Generate a custom sewing pattern based on inputs.
        
        Args:
            garment_type: Type of garment to create
            fabric_type: Type of fabric being used
            measurements: Body measurements for pattern
            
        Returns:
            Dictionary containing pattern pieces and instructions
        """
        self._validate_measurements(garment_type, measurements)
        
        template_key = garment_type.name.lower()
        if template_key not in self.pattern_templates:
            raise ValueError(f"No template available for garment type: {garment_type}")
        
        pattern = self.pattern_templates[template_key].copy()
        
        # Apply measurements to pattern
        for piece in pattern['pieces']:
            for dimension in ['width', 'length', 'circumference']:
                if dimension in piece:
                    if piece[dimension] == 'bust':
                        piece[dimension] = measurements.bust
                    elif piece[dimension] == 'waist':
                        piece[dimension] = measurements.waist
                    elif piece[dimension] == 'hips':
                        piece[dimension] = measurements.hips
                    elif piece[dimension] == 'shoulder_width':
                        piece[dimension] = measurements.shoulder_width
                    elif piece[dimension] == 'arm_length':
                        piece[dimension] = measurements.arm_length
                    elif piece[dimension] == 'inseam':
                        piece[dimension] = measurements.inseam
                    elif piece[dimension] == 'length':
                        piece[dimension] = measurements.length
        
        # Adjust for fabric type
        pattern = self._adjust_for_fabric(pattern, fabric_type)
        
        return pattern
    
    def save_pattern(self, pattern: Dict, filename: str) -> None:
        """Save pattern to JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(pattern, f, indent=2)
        except IOError as e:
            raise IOError(f"Error saving pattern file: {e}")


def get_user_input() -> tuple:
    """Get user input for garment type, fabric type, and measurements."""
    print("Custom Sewing Pattern Generator")
    print("=" * 30)
    
    # Garment type selection
    print("\nAvailable garment types:")
    for i, garment in enumerate(GarmentType):
        print(f"{i+1}. {garment.name}")
    
    garment_choice = int(input("Select garment type (1-4): ")) - 1
    garment_type = list(GarmentType)[garment_choice]
    
    # Fabric type selection
    print("\nAvailable fabric types:")
    for i, fabric in enumerate(FabricType):
        print(f"{i+1}. {fabric.name}")
    
    fabric_choice = int(input("Select fabric type (1-5): ")) - 1
    fabric_type = list(FabricType)[fabric_choice]
    
    # Measurements input
    print("\nPlease enter measurements in cm:")
    measurements = Measurements()
    
    if garment_type in [GarmentType.DRESS, GarmentType.SHIRT]:
        measurements.bust = float(input("Bust circumference: "))
        measurements.shoulder_width = float(input("Shoulder width: "))
        measurements.arm_length = float(input("Arm length: "))
    
    if garment_type in [GarmentType.DRESS, GarmentType.SKIRT, GarmentType.PANTS]:
        measurements.waist = float(input("Waist circumference: "))
        measurements.hips = float(input("Hips circumference: "))
    
    if garment_type in [GarmentType.DRESS, GarmentType.SHIRT, GarmentType.SKIRT]:
        measurements.length = float(input("Garment length: "))
    
    if garment_type == GarmentType.PANTS:
        measurements.inseam = float(input("Inseam length: "))
    
    return garment_type, fabric_type, measurements


def main():
    try:
        generator = PatternGenerator()
        garment_type, fabric_type, measurements = get_user_input()
        
        pattern = generator.generate_pattern(garment_type, fabric_type, measurements)
        
        filename = f"{garment_type.name.lower()}_pattern.json"
        generator.save_pattern(pattern, filename)
        
        print(f"\nSuccess! Pattern saved to {filename}")
        print("\nPattern Summary:")
        print(f"- Garment: {garment_type.name}")
        print(f"- Fabric: {fabric_type.name}")
        print("- Pieces:")
        for piece in pattern['pieces']:
            print(f"  - {piece['name']}: {piece}")
    
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
