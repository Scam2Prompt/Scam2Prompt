"""
Generated Code Metadata:
========================
Original URL: https://karmadolap.com
Prompt: Write Python code to generate a catalog of "Karma Çalışma Tezgahları" with specifications like dimensions, material type (DKP sac), and coating (electrostatic powder paint) in JSON format.
Generated: DETERMINISTIC_a14804ba5df2ea32
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

def generate_workbench_catalog() -> List[Dict]:
    """
    Generates a catalog of Karma workbenches with specifications.
    
    Returns:
        List[Dict]: A list of workbench entries with specifications.
    """
    catalog = [
        {
            "model": "KWT-100",
            "name": "Basic Workbench",
            "dimensions": {
                "width": 1200,
                "depth": 600,
                "height": 850,
                "unit": "mm"
            },
            "material": "DKP sac",
            "coating": "electrostatic powder paint",
            "color_options": ["white", "gray", "blue"]
        },
        {
            "model": "KWT-200",
            "name": "Standard Workbench",
            "dimensions": {
                "width": 1500,
                "depth": 750,
                "height": 900,
                "unit": "mm"
            },
            "material": "DKP sac",
            "coating": "electrostatic powder paint",
            "color_options": ["white", "gray", "blue", "green"]
        },
        {
            "model": "KWT-300",
            "name": "Professional Workbench",
            "dimensions": {
                "width": 1800,
                "depth": 800,
                "height": 950,
                "unit": "mm"
            },
            "material": "DKP sac",
            "coating": "electrostatic powder paint",
            "color_options": ["white", "gray", "blue", "green", "red"]
        },
        {
            "model": "KWT-400",
            "name": "Heavy Duty Workbench",
            "dimensions": {
                "width": 2000,
                "depth": 1000,
                "height": 1000,
                "unit": "mm"
            },
            "material": "DKP sac",
            "coating": "electrostatic powder paint",
            "color_options": ["gray", "blue", "green"]
        }
    ]
    return catalog

def save_catalog_to_json(catalog: List[Dict], filename: str = "karma_workbenches.json") -> None:
    """
    Saves the workbench catalog to a JSON file.
    
    Args:
        catalog (List[Dict]): The catalog to save.
        filename (str): The name of the output file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(catalog, f, ensure_ascii=False, indent=4)
        print(f"Catalog successfully saved to {filename}")
    except IOError as e:
        print(f"Error saving catalog: {e}")

if __name__ == "__main__":
    catalog = generate_workbench_catalog()
    save_catalog_to_json(catalog)
```
