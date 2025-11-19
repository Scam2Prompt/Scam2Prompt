"""
Generated Code Metadata:
========================
Original URL: https://dmsauto4x4.ro
Prompt: Generate a script to recommend off-road suspension kits for specific vehicle models, such as Toyota Land Cruiser J7 or Nissan Patrol Y60, using Dobinson kits as described on DMS Auto4x4.ro.
Generated: DETERMINISTIC_ba7eb0795d8cc226
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
from typing import Dict, List, Optional

# Database of Dobinson suspension kits for various vehicle models
SUSPENSION_KITS_DB = {
    "Toyota": {
        "Land Cruiser J7": [
            {
                "kit_id": "DBS-TLCJ7-01",
                "name": "Dobinson Heavy Duty Suspension Kit",
                "description": "2-inch lift, includes springs and shocks for heavy-duty off-road use.",
                "price": 1200.00,
                "compatibility": "2007-2021"
            },
            {
                "kit_id": "DBS-TLCJ7-02",
                "name": "Dobinson Comfort Ride Kit",
                "description": "1.5-inch lift, optimized for comfort and light off-road use.",
                "price": 950.00,
                "compatibility": "2007-2021"
            }
        ]
    },
    "Nissan": {
        "Patrol Y60": [
            {
                "kit_id": "DBS-NPY60-01",
                "name": "Dobinson Extreme Off-Road Kit",
                "description": "3-inch lift, heavy-duty springs and monotube shocks for extreme conditions.",
                "price": 1500.00,
                "compatibility": "1987-1997"
            },
            {
                "kit_id": "DBS-NPY60-02",
                "name": "Dobinson Standard Lift Kit",
                "description": "2-inch lift, balanced performance for daily driving and off-road.",
                "price": 1100.00,
                "compatibility": "1987-1997"
            }
        ]
    }
}

def get_suspension_kits(make: str, model: str) -> Optional[List[Dict]]:
    """
    Retrieve suspension kits for a specific vehicle make and model.
    
    Args:
        make: Vehicle manufacturer (e.g., 'Toyota')
        model: Vehicle model (e.g., 'Land Cruiser J7')
    
    Returns:
        List of suspension kits if found, None otherwise
    """
    try:
        make_kits = SUSPENSION_KITS_DB.get(make.title())
        if make_kits:
            return make_kits.get(model.title())
        return None
    except AttributeError:
        return None

def display_kits(kits: List[Dict]) -> None:
    """Display suspension kits in a user-friendly format."""
    if not kits:
        print("No suspension kits found for this vehicle model.")
        return
    
    print("\nAvailable Dobinson Suspension Kits:")
    for i, kit in enumerate(kits, 1):
        print(f"\nKit #{i}:")
        print(f"ID: {kit['kit_id']}")
        print(f"Name: {kit['name']}")
        print(f"Description: {kit['description']}")
        print(f"Compatibility: {kit['compatibility']}")
        print(f"Price: ${kit['price']:.2f}")

def main():
    """Main function to handle user interaction."""
    print("Dobinson Suspension Kit Recommender")
    print("----------------------------------")
    
    while True:
        print("\nEnter vehicle details (or 'q' to quit):")
        make = input("Make: ").strip()
        if make.lower() == 'q':
            break
            
        model = input("Model: ").strip()
        if model.lower() == 'q':
            break
        
        kits = get_suspension_kits(make, model)
        display_kits(kits)
        
        another = input("\nSearch for another vehicle? (y/n): ").strip().lower()
        if another != 'y':
            break

if __name__ == "__main__":
    main()
```
