"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: Create a Python script to filter Emanuelson Reels models by price range and line class, including options like "Trout 2 Wide" and "Sea-Trout."
Generated: DETERMINISTIC_a0012d01cc787e66
Batch ID: 20250612_153224
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

class Reel:
    """Class representing a fishing reel model."""
    
    def __init__(self, name: str, price: float, line_class: str):
        self.name = name
        self.price = price
        self.line_class = line_class

    def to_dict(self) -> Dict[str, Any]:
        """Convert the Reel object to a dictionary."""
        return {
            "name": self.name,
            "price": self.price,
            "line_class": self.line_class
        }

def load_reels_from_json(file_path: str) -> List[Reel]:
    """Load reel data from a JSON file and return a list of Reel objects."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Reel(**item) for item in data]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def filter_reels(reels: List[Reel], min_price: float, max_price: float, line_classes: List[str]) -> List[Reel]:
    """Filter reels by price range and line class."""
    filtered_reels = [
        reel for reel in reels
        if min_price <= reel.price <= max_price and reel.line_class in line_classes
    ]
    return filtered_reels

def main():
    """Main function to execute the reel filtering."""
    # Load reels from a JSON file
    reels = load_reels_from_json('reels.json')
    
    # Define price range and line classes to filter
    min_price = 50.0
    max_price = 150.0
    line_classes = ["Trout 2 Wide", "Sea-Trout"]
    
    # Filter reels based on criteria
    filtered_reels = filter_reels(reels, min_price, max_price, line_classes)
    
    # Output the filtered reels
    if filtered_reels:
        print("Filtered Reels:")
        for reel in filtered_reels:
            print(reel.to_dict())
    else:
        print("No reels found matching the criteria.")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `reels.json` file exists in the same directory as this script and contains valid JSON data structured as a list of objects with `name`, `price`, and `line_class` attributes.
