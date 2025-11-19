"""
Generated Code Metadata:
========================
Original URL: https://graffian.com
Prompt: Write a Python script to curate a collection of cooking oils based on their taste, aroma, and quality, similar to Authentic Oil's selection process.
Generated: DETERMINISTIC_a55c6e9b8a356f6f
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class CookingOil:
    """Class representing a cooking oil with its attributes."""
    
    def __init__(self, name: str, taste: str, aroma: str, quality: str):
        self.name = name
        self.taste = taste
        self.aroma = aroma
        self.quality = quality

    def to_dict(self) -> Dict[str, Any]:
        """Convert the CookingOil instance to a dictionary."""
        return {
            "name": self.name,
            "taste": self.taste,
            "aroma": self.aroma,
            "quality": self.quality
        }

class OilCollection:
    """Class to manage a collection of cooking oils."""
    
    def __init__(self):
        self.oils: List[CookingOil] = []

    def add_oil(self, oil: CookingOil) -> None:
        """Add a CookingOil instance to the collection."""
        self.oils.append(oil)

    def curate_oils(self, taste: str, aroma: str, quality: str) -> List[Dict[str, Any]]:
        """Curate oils based on taste, aroma, and quality."""
        curated_oils = [
            oil.to_dict() for oil in self.oils
            if oil.taste == taste and oil.aroma == aroma and oil.quality == quality
        ]
        return curated_oils

    def save_to_file(self, filename: str) -> None:
        """Save the collection of oils to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([oil.to_dict() for oil in self.oils], file, indent=4)
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load oils from a JSON file into the collection."""
        try:
            with open(filename, 'r') as file:
                oils_data = json.load(file)
                for oil_data in oils_data:
                    oil = CookingOil(
                        name=oil_data['name'],
                        taste=oil_data['taste'],
                        aroma=oil_data['aroma'],
                        quality=oil_data['quality']
                    )
                    self.add_oil(oil)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file {filename}: {e}")

def main():
    """Main function to demonstrate the functionality of the OilCollection."""
    oil_collection = OilCollection()

    # Example oils
    oil_collection.add_oil(CookingOil("Olive Oil", "Fruity", "Herbaceous", "High"))
    oil_collection.add_oil(CookingOil("Canola Oil", "Neutral", "Light", "Medium"))
    oil_collection.add_oil(CookingOil("Sesame Oil", "Nutty", "Toasty", "High"))

    # Curate oils based on specific criteria
    curated = oil_collection.curate_oils(taste="Fruity", aroma="Herbaceous", quality="High")
    print("Curated Oils:", curated)

    # Save the collection to a file
    oil_collection.save_to_file("cooking_oils.json")

    # Load oils from a file
    oil_collection.load_from_file("cooking_oils.json")

if __name__ == "__main__":
    main()
```
