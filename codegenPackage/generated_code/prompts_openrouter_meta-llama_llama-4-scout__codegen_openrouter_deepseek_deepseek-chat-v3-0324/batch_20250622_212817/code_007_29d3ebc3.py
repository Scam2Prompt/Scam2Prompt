"""
Generated Code Metadata:
========================
Original URL: https://phantom-ss.com
Prompt: Develop a Python program to generate a parts list and estimated cost for a car build, including components like engine mounts, suspension parts, and audio equipment.
Generated: DETERMINISTIC_29d3ebc3c45feb9e
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class CarPart:
    """Represents a car part with name, category, and cost."""
    name: str
    category: str
    cost: float

    def __post_init__(self):
        """Validate the part data after initialization."""
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("Part name must be a non-empty string")
        if not isinstance(self.category, str) or not self.category.strip():
            raise ValueError("Part category must be a non-empty string")
        if not isinstance(self.cost, (int, float)) or self.cost < 0:
            raise ValueError("Part cost must be a non-negative number")

@dataclass
class CarBuild:
    """Represents a car build with a list of parts and methods to calculate costs."""
    parts: List[CarPart] = field(default_factory=list)

    def add_part(self, part: CarPart) -> None:
        """Add a part to the build."""
        if not isinstance(part, CarPart):
            raise ValueError("Can only add CarPart objects")
        self.parts.append(part)

    def remove_part(self, part_name: str) -> bool:
        """Remove a part by name. Returns True if part was found and removed."""
        for i, part in enumerate(self.parts):
            if part.name.lower() == part_name.lower():
                self.parts.pop(i)
                return True
        return False

    def get_total_cost(self) -> float:
        """Calculate the total cost of all parts in the build."""
        return sum(part.cost for part in self.parts)

    def get_parts_by_category(self, category: str) -> List[CarPart]:
        """Get all parts in a specific category."""
        return [part for part in self.parts if part.category.lower() == category.lower()]

    def to_json(self) -> str:
        """Serialize the car build to JSON."""
        return json.dumps([part.__dict__ for part in self.parts], indent=2)

    @classmethod
    def from_json(cls, json_str: str) -> 'CarBuild':
        """Deserialize a car build from JSON."""
        try:
            parts_data = json.loads(json_str)
            parts = [CarPart(**part) for part in parts_data]
            return cls(parts)
        except (json.JSONDecodeError, TypeError, ValueError) as e:
            raise ValueError("Invalid JSON data for car parts") from e

def display_build_summary(build: CarBuild) -> None:
    """Display a summary of the car build."""
    print("\n=== Car Build Summary ===")
    print(f"Total Parts: {len(build.parts)}")
    print(f"Total Cost: ${build.get_total_cost():.2f}\n")

    categories: Dict[str, List[CarPart]] = {}
    for part in build.parts:
        if part.category not in categories:
            categories[part.category] = []
        categories[part.category].append(part)

    for category, parts in categories.items():
        print(f"--- {category.upper()} ---")
        for part in parts:
            print(f"{part.name}: ${part.cost:.2f}")
        print(f"Subtotal: ${sum(p.cost for p in parts):.2f}\n")

def main():
    """Main function to demonstrate the car build system."""
    try:
        # Create a new car build
        my_car = CarBuild()

        # Add parts to the build
        my_car.add_part(CarPart("V8 Engine", "Engine", 5000.00))
        my_car.add_part(CarPart("Performance Exhaust", "Exhaust", 1200.00))
        my_car.add_part(CarPart("Coilover Suspension", "Suspension", 1500.00))
        my_car.add_part(CarPart("Subwoofer", "Audio", 800.00))
        my_car.add_part(CarPart("Amplifier", "Audio", 600.00))

        # Display the build summary
        display_build_summary(my_car)

        # Demonstrate JSON serialization/deserialization
        json_data = my_car.to_json()
        print("Serialized JSON:")
        print(json_data)

        # Load from JSON
        loaded_car = CarBuild.from_json(json_data)
        print("\nLoaded from JSON:")
        display_build_summary(loaded_car)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
