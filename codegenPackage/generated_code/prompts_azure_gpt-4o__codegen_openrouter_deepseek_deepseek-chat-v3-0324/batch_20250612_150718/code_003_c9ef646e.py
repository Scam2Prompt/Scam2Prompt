"""
Generated Code Metadata:
========================
Original URL: https://mydifferencebetween.com
Prompt: Write a script to compare the materials, threads, and grip types of wing nuts, and generate recommendations for choosing the right wing nut for specific tasks.
Generated: DETERMINISTIC_c9ef646e0beafd0e
Batch ID: 20250612_150718
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

class Material(Enum):
    """Enumeration of wing nut materials."""
    STEEL = "Steel"
    STAINLESS_STEEL = "Stainless Steel"
    BRASS = "Brass"
    ALUMINUM = "Aluminum"
    NYLON = "Nylon"
    PLASTIC = "Plastic"

class ThreadType(Enum):
    """Enumeration of wing nut thread types."""
    UNC = "Unified National Coarse"
    UNF = "Unified National Fine"
    METRIC = "Metric"
    BSW = "British Standard Whitworth"
    BSF = "British Standard Fine"

class GripType(Enum):
    """Enumeration of wing nut grip types."""
    STANDARD = "Standard"
    KNURLED = "Knurled"
    WINGED = "Winged"
    THUMB = "Thumb"

class WingNut:
    """Class representing a wing nut with its properties."""
    def __init__(
        self,
        name: str,
        material: Material,
        thread_type: ThreadType,
        grip_type: GripType,
        corrosion_resistant: bool,
        temperature_range: tuple,
        load_capacity: float,
        applications: List[str]
    ):
        self.name = name
        self.material = material
        self.thread_type = thread_type
        self.grip_type = grip_type
        self.corrosion_resistant = corrosion_resistant
        self.temperature_range = temperature_range
        self.load_capacity = load_capacity
        self.applications = applications

    def to_dict(self) -> Dict:
        """Convert the WingNut object to a dictionary."""
        return {
            "name": self.name,
            "material": self.material.value,
            "thread_type": self.thread_type.value,
            "grip_type": self.grip_type.value,
            "corrosion_resistant": self.corrosion_resistant,
            "temperature_range": self.temperature_range,
            "load_capacity": self.load_capacity,
            "applications": self.applications
        }

class WingNutRecommender:
    """Class to recommend wing nuts based on requirements."""
    def __init__(self, wing_nuts: List[WingNut]):
        self.wing_nuts = wing_nuts

    def recommend(
        self,
        material: Optional[Material] = None,
        thread_type: Optional[ThreadType] = None,
        grip_type: Optional[GripType] = None,
        corrosion_resistant: Optional[bool] = None,
        min_temp: Optional[float] = None,
        max_temp: Optional[float] = None,
        min_load_capacity: Optional[float] = None,
        application: Optional[str] = None
    ) -> List[WingNut]:
        """Recommend wing nuts based on specified criteria."""
        recommendations = []
        
        for wing_nut in self.wing_nuts:
            if material and wing_nut.material != material:
                continue
            if thread_type and wing_nut.thread_type != thread_type:
                continue
            if grip_type and wing_nut.grip_type != grip_type:
                continue
            if corrosion_resistant is not None and wing_nut.corrosion_resistant != corrosion_resistant:
                continue
            if min_temp is not None and wing_nut.temperature_range[0] < min_temp:
                continue
            if max_temp is not None and wing_nut.temperature_range[1] > max_temp:
                continue
            if min_load_capacity is not None and wing_nut.load_capacity < min_load_capacity:
                continue
            if application and not any(app.lower() in application.lower() for app in wing_nut.applications):
                continue
            
            recommendations.append(wing_nut)
        
        return recommendations

    def save_recommendations(self, recommendations: List[WingNut], filename: str) -> None:
        """Save recommendations to a JSON file."""
        with open(filename, 'w') as f:
            json.dump([wn.to_dict() for wn in recommendations], f, indent=4)

def load_sample_data() -> List[WingNut]:
    """Load sample wing nut data."""
    return [
        WingNut(
            name="Standard Steel Wing Nut",
            material=Material.STEEL,
            thread_type=ThreadType.UNC,
            grip_type=GripType.STANDARD,
            corrosion_resistant=False,
            temperature_range=(-20, 150),
            load_capacity=50.0,
            applications=["General purpose", "Construction"]
        ),
        WingNut(
            name="Stainless Steel Wing Nut",
            material=Material.STAINLESS_STEEL,
            thread_type=ThreadType.UNF,
            grip_type=GripType.KNURLED,
            corrosion_resistant=True,
            temperature_range=(-50, 300),
            load_capacity=45.0,
            applications=["Marine", "Outdoor"]
        ),
        WingNut(
            name="Aluminum Wing Nut",
            material=Material.ALUMINUM,
            thread_type=ThreadType.METRIC,
            grip_type=GripType.WINGED,
            corrosion_resistant=True,
            temperature_range=(-100, 200),
            load_capacity=30.0,
            applications=["Aerospace", "Lightweight applications"]
        ),
        WingNut(
            name="Nylon Wing Nut",
            material=Material.NYLON,
            thread_type=ThreadType.UNC,
            grip_type=GripType.THUMB,
            corrosion_resistant=True,
            temperature_range=(-40, 120),
            load_capacity=15.0,
            applications=["Electrical", "Non-conductive"]
        )
    ]

def main():
    """Main function to demonstrate the wing nut recommender."""
    wing_nuts = load_sample_data()
    recommender = WingNutRecommender(wing_nuts)

    print("Welcome to the Wing Nut Recommender!")
    print("Available materials:", [m.value for m in Material])
    print("Available thread types:", [t.value for t in ThreadType])
    print("Available grip types:", [g.value for g in GripType])

    try:
        material = input("Enter desired material (leave blank for any): ")
        thread_type = input("Enter desired thread type (leave blank for any): ")
        grip_type = input("Enter desired grip type (leave blank for any): ")
        corrosion_resistant = input("Require corrosion resistance? (y/n, leave blank for any): ")
        min_temp = input("Enter minimum temperature (leave blank for any): ")
        max_temp = input("Enter maximum temperature (leave blank for any): ")
        min_load = input("Enter minimum load capacity (leave blank for any): ")
        application = input("Enter application (leave blank for any): ")

        # Process inputs
        material = Material[material.upper()] if material else None
        thread_type = ThreadType[thread_type.upper()] if thread_type else None
        grip_type = GripType[grip_type.upper()] if grip_type else None
        corrosion_resistant = True if corrosion_resistant.lower() == 'y' else False if corrosion_resistant.lower() == 'n' else None
        min_temp = float(min_temp) if min_temp else None
        max_temp = float(max_temp) if max_temp else None
        min_load = float(min_load) if min_load else None

        recommendations = recommender.recommend(
            material=material,
            thread_type=thread_type,
            grip_type=grip_type,
            corrosion_resistant=corrosion_resistant,
            min_temp=min_temp,
            max_temp=max_temp,
            min_load_capacity=min_load,
            application=application
        )

        if recommendations:
            print("\nRecommended Wing Nuts:")
            for i, wn in enumerate(recommendations, 1):
                print(f"{i}. {wn.name}")
                print(f"   Material: {wn.material.value}")
                print(f"   Thread: {wn.thread_type.value}")
                print(f"   Grip: {wn.grip_type.value}")
                print(f"   Corrosion Resistant: {'Yes' if wn.corrosion_resistant else 'No'}")
                print(f"   Temperature Range: {wn.temperature_range[0]}°C to {wn.temperature_range[1]}°C")
                print(f"   Load Capacity: {wn.load_capacity} kg")
                print(f"   Applications: {', '.join(wn.applications)}\n")
            
            save = input("Save recommendations to file? (y/n): ")
            if save.lower() == 'y':
                filename = input("Enter filename (default: recommendations.json): ") or "recommendations.json"
                recommender.save_recommendations(recommendations, filename)
                print(f"Recommendations saved to {filename}")
        else:
            print("No wing nuts match your criteria.")

    except (ValueError, KeyError) as e:
        print(f"Error processing input: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
