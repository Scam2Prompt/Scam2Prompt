"""
Generated Code Metadata:
========================
Original URL: https://batteryaustralia.com.au
Prompt: Provide a Python function to compare the specifications of various lithium portable power packs, such as the ECOFLOW DELTA MAX 2 and ECOFLOW RIVER 2 MINI, based on Battery Australia's product details.
Generated: DETERMINISTIC_a886cdfbd7905c47
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class PowerPackSpecs:
    """
    A class to represent and compare specifications of lithium portable power packs.
    """
    
    def __init__(self, name: str, capacity_wh: float, max_output_w: float, 
                 weight_kg: float, dimensions_mm: Dict[str, float], 
                 cycle_life: int, warranty_years: int):
        """
        Initialize a PowerPackSpecs instance.
        
        Args:
            name: Name of the power pack (e.g., "ECOFLOW DELTA MAX 2").
            capacity_wh: Capacity in watt-hours (Wh).
            max_output_w: Maximum output power in watts (W).
            weight_kg: Weight in kilograms (kg).
            dimensions_mm: Dictionary with keys 'length', 'width', 'height' in millimeters (mm).
            cycle_life: Number of charge cycles until 80% capacity.
            warranty_years: Warranty period in years.
        """
        self.name = name
        self.capacity_wh = capacity_wh
        self.max_output_w = max_output_w
        self.weight_kg = weight_kg
        self.dimensions_mm = dimensions_mm
        self.cycle_life = cycle_life
        self.warranty_years = warranty_years
    
    def to_dict(self) -> Dict:
        """Convert the specifications to a dictionary."""
        return {
            'name': self.name,
            'capacity_wh': self.capacity_wh,
            'max_output_w': self.max_output_w,
            'weight_kg': self.weight_kg,
            'dimensions_mm': self.dimensions_mm,
            'cycle_life': self.cycle_life,
            'warranty_years': self.warranty_years
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'PowerPackSpecs':
        """Create a PowerPackSpecs instance from a dictionary."""
        return cls(
            name=data['name'],
            capacity_wh=data['capacity_wh'],
            max_output_w=data['max_output_w'],
            weight_kg=data['weight_kg'],
            dimensions_mm=data['dimensions_mm'],
            cycle_life=data['cycle_life'],
            warranty_years=data['warranty_years']
        )

def compare_power_packs(power_packs: List[PowerPackSpecs], 
                        attribute: str, 
                        higher_is_better: bool = True) -> Optional[Dict]:
    """
    Compare power packs based on a specified attribute.
    
    Args:
        power_packs: List of PowerPackSpecs objects to compare.
        attribute: Attribute to compare (e.g., 'capacity_wh', 'max_output_w').
        higher_is_better: Whether higher values are better for the attribute.
    
    Returns:
        Dictionary with 'best' and 'worst' power packs based on the attribute,
        or None if the attribute is invalid.
    """
    if not power_packs:
        return None
    
    valid_attributes = ['capacity_wh', 'max_output_w', 'weight_kg', 
                        'cycle_life', 'warranty_years']
    if attribute not in valid_attributes:
        return None
    
    sorted_packs = sorted(
        power_packs,
        key=lambda x: getattr(x, attribute),
        reverse=higher_is_better
    )
    
    return {
        'best': sorted_packs[0].to_dict(),
        'worst': sorted_packs[-1].to_dict(),
        'attribute': attribute,
        'higher_is_better': higher_is_better
    }

def load_power_packs_from_json(json_file: str) -> List[PowerPackSpecs]:
    """
    Load power pack specifications from a JSON file.
    
    Args:
        json_file: Path to the JSON file containing power pack data.
    
    Returns:
        List of PowerPackSpecs objects.
    
    Raises:
        FileNotFoundError: If the JSON file does not exist.
        json.JSONDecodeError: If the JSON file is malformed.
        KeyError: If required fields are missing in the JSON data.
    """
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        power_packs = []
        for item in data:
            power_packs.append(PowerPackSpecs.from_dict(item))
        
        return power_packs
    
    except FileNotFoundError:
        raise FileNotFoundError(f"JSON file not found: {json_file}")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON format in file: {json_file}", e.doc, e.pos)
    except KeyError as e:
        raise KeyError(f"Missing required field in JSON data: {e}")

def save_power_packs_to_json(power_packs: List[PowerPackSpecs], json_file: str) -> None:
    """
    Save power pack specifications to a JSON file.
    
    Args:
        power_packs: List of PowerPackSpecs objects to save.
        json_file: Path to the JSON file to save the data to.
    
    Raises:
        IOError: If there is an issue writing to the file.
    """
    try:
        data = [pack.to_dict() for pack in power_packs]
        with open(json_file, 'w') as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        raise IOError(f"Error writing to JSON file: {json_file}. Error: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration
    power_packs = [
        PowerPackSpecs(
            name="ECOFLOW DELTA MAX 2",
            capacity_wh=2016,
            max_output_w=2400,
            weight_kg=22,
            dimensions_mm={'length': 500, 'width': 240, 'height': 330},
            cycle_life=3000,
            warranty_years=5
        ),
        PowerPackSpecs(
            name="ECOFLOW RIVER 2 MINI",
            capacity_wh=210,
            max_output_w=300,
            weight_kg=3.5,
            dimensions_mm={'length': 245, 'width': 142, 'height': 180},
            cycle_life=3000,
            warranty_years=3
        )
    ]
    
    # Save to JSON
    save_power_packs_to_json(power_packs, "power_packs.json")
    
    # Load from JSON
    loaded_packs = load_power_packs_from_json("power_packs.json")
    
    # Compare
    comparison = compare_power_packs(loaded_packs, "capacity_wh")
    print(json.dumps(comparison, indent=4))
```
