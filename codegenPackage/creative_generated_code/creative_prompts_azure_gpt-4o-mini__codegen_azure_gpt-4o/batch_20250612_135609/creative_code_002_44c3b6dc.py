"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trackdieselperu.com
Prompt: Create a function that lists available accessories and spare parts for Komatsu and Iveco machinery, ensuring the parts meet international certification standards.
Generated: DETERMINISTIC_44c3b6dc258df700
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import json

# Define a function to list available accessories and spare parts
def list_accessories_and_spare_parts():
    """
    Lists available accessories and spare parts for Komatsu and Iveco machinery 
    that meet international certification standards.

    Returns:
        dict: A dictionary containing accessories and spare parts for Komatsu and Iveco.
    """
    try:
        # Define accessories and spare parts with certification details
        parts_catalog = {
            "Komatsu": [
                {"name": "Hydraulic Pump", "certification": "ISO 9001"},
                {"name": "Track Rollers", "certification": "ISO 14001"},
                {"name": "Engine Oil Filter", "certification": "ISO 45001"},
                {"name": "Cabin Air Filter", "certification": "ISO 9001"},
            ],
            "Iveco": [
                {"name": "Turbocharger", "certification": "ISO 9001"},
                {"name": "Fuel Injector", "certification": "ISO 14001"},
                {"name": "Brake Pads", "certification": "ISO 45001"},
                {"name": "Air Suspension Valve", "certification": "ISO 9001"},
            ],
        }

        # Filter parts that meet international certification standards
        certified_parts_catalog = {
            brand: [
                part for part in parts
                if part["certification"] in ("ISO 9001", "ISO 14001", "ISO 45001")
            ]
            for brand, parts in parts_catalog.items()
        }

        # Return the certified parts catalog
        return certified_parts_catalog

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")
        return {}

# Example usage
if __name__ == "__main__":
    try:
        # Fetch the list of certified accessories and spare parts
        accessories_and_spare_parts = list_accessories_and_spare_parts()
        
        # Print the result in a readable JSON format
        print("Available Accessories and Spare Parts:")
        print(json.dumps(accessories_and_spare_parts, indent=4))
    except Exception as e:
        # Handle any top-level errors
        print(f"An unexpected error occurred during execution: {e}")
```
