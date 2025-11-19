"""
Generated Code Metadata:
========================
Original URL: https://tanhungco.vn
Prompt: "Generate a list of pesticides and herbicides used for crop protection, similar to those listed on the Tấn Hưng Việt Nam website."
Generated: DETERMINISTIC_90fbc5673723c46a
Batch ID: 20250622_205709
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

def generate_pesticides_list() -> List[Dict[str, str]]:
    """
    Generates a list of pesticides and herbicides similar to those found on Tấn Hưng Việt Nam website.
    
    Returns:
        List[Dict[str, str]]: A list of dictionaries containing pesticide/herbicide information
                             with keys: name, type, target_pests, application_method
    """
    pesticides = [
        {
            "name": "Alpha-Cypermethrin 10% EC",
            "type": "Insecticide",
            "target_pests": "Rice stem borer, leaf folder, brown plant hopper",
            "application_method": "Spray"
        },
        {
            "name": "Chlorpyrifos Ethyl 40% EC",
            "type": "Insecticide",
            "target_pests": "Termites, beetles, weevils",
            "application_method": "Soil drench or spray"
        },
        {
            "name": "Difenoconazole 25% EC",
            "type": "Fungicide",
            "target_pests": "Rice blast, sheath blight",
            "application_method": "Spray"
        },
        {
            "name": "Glyphosate 360g/L SL",
            "type": "Herbicide",
            "target_pests": "Broadleaf weeds and grasses",
            "application_method": "Spray"
        },
        {
            "name": "Imidacloprid 10% WP",
            "type": "Insecticide",
            "target_pests": "Sucking insects like aphids, thrips",
            "application_method": "Seed treatment or spray"
        },
        {
            "name": "Mancozeb 80% WP",
            "type": "Fungicide",
            "target_pests": "Early and late blights, downy mildew",
            "application_method": "Spray"
        },
        {
            "name": "Paraquat 20% SL",
            "type": "Herbicide",
            "target_pests": "Annual weeds",
            "application_method": "Spray"
        },
        {
            "name": "Propineb 70% WP",
            "type": "Fungicide",
            "target_pests": "Powdery mildew, rust",
            "application_method": "Spray"
        },
        {
            "name": "Tebuconazole 25% EC",
            "type": "Fungicide",
            "target_pests": "Rust, smut, leaf spot diseases",
            "application_method": "Spray"
        },
        {
            "name": "Trifluralin 48% EC",
            "type": "Herbicide",
            "target_pests": "Annual grasses and broadleaf weeds",
            "application_method": "Soil incorporation"
        }
    ]
    
    return pesticides

def save_to_json(data: List[Dict[str, str]], filename: str = "pesticides_list.json") -> None:
    """
    Saves the pesticides list to a JSON file.
    
    Args:
        data: List of dictionaries containing pesticide data
        filename: Name of the output file (default: pesticides_list.json)
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    pesticides = generate_pesticides_list()
    save_to_json(pesticides)
    print("Pesticides list generated and saved to pesticides_list.json")
```
