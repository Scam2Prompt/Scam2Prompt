"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://khaptadtours.com
Prompt: Write a script to generate a packing list for high-altitude treks like the Manaslu Circuit Trek, referencing the challenges described on Khaptad Tours.
Generated: DETERMINISTIC_78f67ff4bbb3cd2c
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class PackingListGenerator:
    """A class to generate a packing list for high-altitude treks."""

    def __init__(self):
        # Define essential packing categories and items
        self.packing_list: Dict[str, List[str]] = {
            "Clothing": [
                "Base layers (thermal tops and bottoms)",
                "Insulating layer (fleece or down jacket)",
                "Waterproof and windproof jacket",
                "Trekking pants",
                "Warm hat and gloves",
                "Socks (wool or synthetic)",
                "Gaiters",
                "Sun hat",
                "Trekking boots (water-resistant)"
            ],
            "Sleeping Gear": [
                "Sleeping bag (rated for low temperatures)",
                "Sleeping pad",
                "Travel pillow"
            ],
            "Personal Items": [
                "Sunscreen",
                "Lip balm with SPF",
                "Toiletries (toothbrush, toothpaste, etc.)",
                "Medications",
                "First aid kit"
            ],
            "Food and Hydration": [
                "Water bottles or hydration system",
                "Water purification tablets or filter",
                "Energy bars and snacks"
            ],
            "Navigation and Safety": [
                "Map and compass (or GPS device)",
                "Headlamp with extra batteries",
                "Multi-tool or knife"
            ],
            "Miscellaneous": [
                "Trekking poles",
                "Dry bags for clothing",
                "Power bank",
                "Camera and extra batteries"
            ]
        }

    def generate_packing_list(self) -> str:
        """Generates a packing list in a formatted string."""
        packing_list_str = "Packing List for High-Altitude Treks:\n"
        for category, items in self.packing_list.items():
            packing_list_str += f"\n{category}:\n"
            packing_list_str += "\n".join(f"- {item}" for item in items)
            packing_list_str += "\n"
        return packing_list_str

    def save_to_file(self, filename: str) -> None:
        """Saves the packing list to a JSON file.

        Args:
            filename (str): The name of the file to save the packing list to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.packing_list, file, indent=4)
            print(f"Packing list saved to {filename}.")
        except IOError as e:
            print(f"Error saving packing list to {filename}: {e}")

def main():
    """Main function to run the packing list generator."""
    generator = PackingListGenerator()
    
    # Generate the packing list
    packing_list = generator.generate_packing_list()
    print(packing_list)

    # Save packing list to file
    generator.save_to_file("packing_list.json")

if __name__ == "__main__":
    main()
```
