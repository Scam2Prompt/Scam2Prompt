"""
Generated Code Metadata:
========================
Original URL: https://dmsauto4x4.ro
Prompt: Write Python code to create a configurator for off-road tires and rims, referencing brands like BF Goodrich, Atturo, and ITP as listed on DMS Auto4x4's website.
Generated: DETERMINISTIC_7784469db7c07844
Batch ID: 20250612_152739
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
from typing import List, Dict, Optional

@dataclass
class Tire:
    brand: str
    model: str
    size: str
    price: float
    terrain_type: str  # e.g., mud, all-terrain, rock
    warranty_months: int

@dataclass
class Rim:
    brand: str
    model: str
    size: str
    price: float
    material: str  # e.g., steel, alloy
    bolt_pattern: str

class TireRimConfigurator:
    def __init__(self):
        self.tires: List[Tire] = []
        self.rims: List[Rim] = []
        self.load_inventory()

    def load_inventory(self) -> None:
        """Load tire and rim inventory from JSON file."""
        try:
            with open('inventory.json', 'r') as f:
                data = json.load(f)
                self.tires = [Tire(**tire) for tire in data.get('tires', [])]
                self.rims = [Rim(**rim) for rim in data.get('rims', [])]
        except FileNotFoundError:
            print("Inventory file not found. Starting with empty inventory.")
        except json.JSONDecodeError:
            print("Error decoding inventory file. Starting with empty inventory.")
        except Exception as e:
            print(f"Unexpected error loading inventory: {e}")

    def save_inventory(self) -> None:
        """Save current inventory to JSON file."""
        try:
            with open('inventory.json', 'w') as f:
                json.dump({
                    'tires': [t.__dict__ for t in self.tires],
                    'rims': [r.__dict__ for r in self.rims]
                }, f, indent=4)
        except Exception as e:
            print(f"Error saving inventory: {e}")

    def add_tire(self, tire: Tire) -> None:
        """Add a new tire to inventory."""
        self.tires.append(tire)
        self.save_inventory()

    def add_rim(self, rim: Rim) -> None:
        """Add a new rim to inventory."""
        self.rims.append(rim)
        self.save_inventory()

    def get_tires_by_brand(self, brand: str) -> List[Tire]:
        """Get all tires from a specific brand."""
        return [t for t in self.tires if t.brand.lower() == brand.lower()]

    def get_rims_by_brand(self, brand: str) -> List[Rim]:
        """Get all rims from a specific brand."""
        return [r for r in self.rims if r.brand.lower() == brand.lower()]

    def get_compatible_rims(self, tire_size: str) -> List[Rim]:
        """Get rims compatible with a given tire size."""
        return [r for r in self.rims if r.size == tire_size]

    def create_configuration(self, tire_brand: str, tire_model: str, rim_brand: str, rim_model: str) -> Optional[Dict]:
        """Create a tire and rim configuration."""
        selected_tire = next(
            (t for t in self.tires 
             if t.brand.lower() == tire_brand.lower() 
             and t.model.lower() == tire_model.lower()), 
            None
        )
        
        selected_rim = next(
            (r for r in self.rims 
             if r.brand.lower() == rim_brand.lower() 
             and r.model.lower() == rim_model.lower()), 
            None
        )

        if not selected_tire or not selected_rim:
            return None

        if selected_tire.size != selected_rim.size:
            return None

        return {
            'tire': selected_tire,
            'rim': selected_rim,
            'total_price': selected_tire.price + selected_rim.price
        }

def initialize_sample_data(configurator: TireRimConfigurator) -> None:
    """Initialize sample data for demonstration."""
    sample_tires = [
        Tire("BF Goodrich", "Mud-Terrain T/A KM3", "33x12.50R17", 350.99, "mud", 60),
        Tire("Atturo", "Trail Blade X/T", "35x12.50R20", 289.99, "all-terrain", 48),
        Tire("ITP", "Mud Lite XL", "28x10R14", 189.99, "mud", 36)
    ]

    sample_rims = [
        Rim("ITP", "SS212", "17x9", 199.99, "steel", "6x139.7"),
        Rim("Atturo", "AT-117", "20x10", 249.99, "alloy", "8x170"),
        Rim("BF Goodrich", "D-Window", "14x7", 149.99, "steel", "4x100")
    ]

    for tire in sample_tires:
        configurator.add_tire(tire)
    
    for rim in sample_rims:
        configurator.add_rim(rim)

def main():
    configurator = TireRimConfigurator()
    
    # Uncomment to initialize with sample data
    # initialize_sample_data(configurator)

    # Example usage
    bf_tires = configurator.get_tires_by_brand("BF Goodrich")
    print("BF Goodrich Tires:")
    for tire in bf_tires:
        print(f"- {tire.model} ({tire.size}): ${tire.price}")

    configuration = configurator.create_configuration(
        "BF Goodrich", "Mud-Terrain T/A KM3",
        "ITP", "SS212"
    )
    
    if configuration:
        print("\nConfiguration Created:")
        print(f"Tire: {configuration['tire'].brand} {configuration['tire'].model}")
        print(f"Rim: {configuration['rim'].brand} {configuration['rim'].model}")
        print(f"Total Price: ${configuration['total_price']:.2f}")
    else:
        print("\nCould not create configuration (invalid selection or incompatible sizes)")

if __name__ == "__main__":
    main()
```
