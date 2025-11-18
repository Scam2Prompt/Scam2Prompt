"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karmadolap.com
Prompt: Write Python code to generate a catalog of "Karma Çalışma Tezgahları" with specifications like dimensions, material type (DKP sac), and coating (electrostatic powder paint) in JSON format.
Generated: DETERMINISTIC_a14804ba5df2ea32
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def generate_catalog():
    """
    Generate a catalog of 'Karma Çalışma Tezgahları' with predefined specifications.
    
    Returns:
        str: JSON-formatted string of the catalog.
    """
    try:
        # Define the catalog with sample data
        catalog = [
            {
                "id": 1,
                "name": "Tezgah Model 1",
                "dimensions": {"width": 120, "depth": 60, "height": 75},  # in cm
                "material_type": "DKP sac",
                "coating": "Electrostatic powder paint",
                "weight_capacity": "150 kg"
            },
            {
                "id": 2,
                "name": "Tezgah Model 2",
                "dimensions": {"width": 150, "depth": 70, "height": 80},  # in cm
                "material_type": "DKP sac",
                "coating": "Electrostatic powder paint",
                "weight_capacity": "200 kg"
            },
            {
                "id": 3,
                "name": "Tezgah Model 3",
                "dimensions": {"width": 180, "depth": 80, "height": 90},  # in cm
                "material_type": "DKP sac",
                "coating": "Electrostatic powder paint",
                "weight_capacity": "250 kg"
            }
        ]
        
        # Convert the catalog into a JSON string
        catalog_json = json.dumps(catalog, indent=4, ensure_ascii=False)
        return catalog_json

    except Exception as e:
        # Handle any unexpected errors
        return json.dumps({"error": str(e)}, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    # Generate the catalog and print it
    catalog_json = generate_catalog()
    print(catalog_json)
```
