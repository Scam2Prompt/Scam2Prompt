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
from typing import List, Dict, Optional
from enum import Enum

class OilQuality(Enum):
    """Enum representing the quality rating of cooking oils."""
    PREMIUM = "Premium"
    STANDARD = "Standard"
    BASIC = "Basic"

class CookingOil:
    """Class representing a cooking oil with its attributes."""
    
    def __init__(
        self,
        name: str,
        taste: str,
        aroma: str,
        quality: OilQuality,
        origin: str,
        smoke_point_c: Optional[int] = None
    ):
        """
        Initialize a CookingOil instance.
        
        Args:
            name: Name of the oil.
            taste: Description of the taste profile.
            aroma: Description of the aroma.
            quality: Quality rating (Premium, Standard, Basic).
            origin: Country or region of origin.
            smoke_point_c: Smoke point in Celsius (optional).
        """
        self.name = name
        self.taste = taste
        self.aroma = aroma
        self.quality = quality
        self.origin = origin
        self.smoke_point_c = smoke_point_c

    def to_dict(self) -> Dict:
        """Convert the CookingOil instance to a dictionary."""
        return {
            "name": self.name,
            "taste": self.taste,
            "aroma": self.aroma,
            "quality": self.quality.value,
            "origin": self.origin,
            "smoke_point_c": self.smoke_point_c
        }

class OilCollection:
    """Class to manage a collection of cooking oils."""
    
    def __init__(self):
        """Initialize an empty OilCollection."""
        self.oils: List[CookingOil] = []

    def add_oil(self, oil: CookingOil) -> None:
        """Add a CookingOil to the collection.
        
        Args:
            oil: CookingOil instance to add.
        """
        self.oils.append(oil)

    def remove_oil(self, oil_name: str) -> bool:
        """Remove a CookingOil by name.
        
        Args:
            oil_name: Name of the oil to remove.
            
        Returns:
            bool: True if oil was found and removed, False otherwise.
        """
        for i, oil in enumerate(self.oils):
            if oil.name.lower() == oil_name.lower():
                self.oils.pop(i)
                return True
        return False

    def get_oils_by_quality(self, quality: OilQuality) -> List[CookingOil]:
        """Get all oils of a specific quality.
        
        Args:
            quality: Quality rating to filter by.
            
        Returns:
            List of CookingOil instances matching the quality.
        """
        return [oil for oil in self.oils if oil.quality == quality]

    def save_to_file(self, filename: str) -> None:
        """Save the oil collection to a JSON file.
        
        Args:
            filename: Name of the file to save to.
            
        Raises:
            IOError: If file writing fails.
        """
        try:
            with open(filename, 'w') as f:
                json.dump([oil.to_dict() for oil in self.oils], f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save collection to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load an oil collection from a JSON file.
        
        Args:
            filename: Name of the file to load from.
            
        Raises:
            IOError: If file reading fails.
            ValueError: If file content is invalid.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.oils = [
                    CookingOil(
                        name=item["name"],
                        taste=item["taste"],
                        aroma=item["aroma"],
                        quality=OilQuality(item["quality"]),
                        origin=item["origin"],
                        smoke_point_c=item.get("smoke_point_c")
                    ) for item in data
                ]
        except IOError as e:
            raise IOError(f"Failed to load collection from file: {e}")
        except (json.JSONDecodeError, KeyError) as e:
            raise ValueError(f"Invalid file content: {e}")

def main():
    """Example usage of the OilCollection class."""
    collection = OilCollection()
    
    # Add some example oils
    collection.add_oil(CookingOil(
        name="Extra Virgin Olive Oil",
        taste="Fruity and slightly bitter",
        aroma="Fresh and grassy",
        quality=OilQuality.PREMIUM,
        origin="Italy",
        smoke_point_c=190
    ))
    
    collection.add_oil(CookingOil(
        name="Avocado Oil",
        taste="Buttery and mild",
        aroma="Neutral",
        quality=OilQuality.PREMIUM,
        origin="Mexico",
        smoke_point_c=270
    ))
    
    collection.add_oil(CookingOil(
        name="Canola Oil",
        taste="Neutral",
        aroma="Mild",
        quality=OilQuality.STANDARD,
        origin="Canada",
        smoke_point_c=204
    ))
    
    # Save to file
    try:
        collection.save_to_file("cooking_oils.json")
        print("Collection saved successfully.")
    except IOError as e:
        print(f"Error saving collection: {e}")
    
    # Load from file
    new_collection = OilCollection()
    try:
        new_collection.load_from_file("cooking_oils.json")
        print("Collection loaded successfully.")
        
        # Print premium oils
        print("\nPremium oils:")
        for oil in new_collection.get_oils_by_quality(OilQuality.PREMIUM):
            print(f"- {oil.name} from {oil.origin}")
            
    except (IOError, ValueError) as e:
        print(f"Error loading collection: {e}")

if __name__ == "__main__":
    main()
```
