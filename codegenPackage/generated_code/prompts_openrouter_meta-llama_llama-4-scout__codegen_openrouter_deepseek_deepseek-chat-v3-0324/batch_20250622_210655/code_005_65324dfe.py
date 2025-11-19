"""
Generated Code Metadata:
========================
Original URL: https://evinblue.com
Prompt: Provide a list of recommended DEF products for specific vehicle models (e.g., MG, Jeep, Mahindra, Hyundai, Ford & Eicher) and their corresponding engine types.
Generated: DETERMINISTIC_65324dfea8492adb
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List, Tuple

# Database of DEF products mapped to vehicle models and engine types
DEF_PRODUCTS_DB = {
    "MG": {
        "Hector": ["Diesel 2.0L", "Diesel 1.5L"],
        "Gloster": ["Diesel 2.0L"],
    },
    "Jeep": {
        "Compass": ["Diesel 2.0L"],
        "Meridian": ["Diesel 1.5L"],
    },
    "Mahindra": {
        "Scorpio": ["Diesel 2.2L", "Diesel 1.6L"],
        "XUV700": ["Diesel 2.2L"],
    },
    "Hyundai": {
        "Creta": ["Diesel 1.5L"],
        "Tucson": ["Diesel 2.0L"],
    },
    "Ford": {
        "Endeavour": ["Diesel 3.2L", "Diesel 2.2L"],
        "EcoSport": ["Diesel 1.5L"],
    },
    "Eicher": {
        "Pro 2049": ["Diesel 3.0L"],
        "Pro 2095": ["Diesel 5.0L"],
    }
}

# DEF product recommendations
DEF_PRODUCTS = [
    "AdBlue Premium",
    "BlueDEF",
    "Diesel Exhaust Fluid Standard",
    "EcoDEF",
    "PURAGEN DEF"
]

def get_def_recommendations(vehicle_make: str, vehicle_model: str) -> Tuple[List[str], List[str]]:
    """
    Get recommended DEF products and compatible engine types for a vehicle.
    
    Args:
        vehicle_make: Manufacturer name (e.g., "MG", "Jeep")
        vehicle_model: Vehicle model name (e.g., "Hector", "Compass")
    
    Returns:
        Tuple containing:
        - List of recommended DEF products
        - List of compatible engine types
    
    Raises:
        ValueError: If vehicle make or model is not found in database
    """
    try:
        models = DEF_PRODUCTS_DB[vehicle_make]
    except KeyError:
        raise ValueError(f"Vehicle make '{vehicle_make}' not found in database")
    
    try:
        engine_types = models[vehicle_model]
    except KeyError:
        raise ValueError(f"Model '{vehicle_model}' not found for make '{vehicle_make}'")
    
    return DEF_PRODUCTS, engine_types

def list_available_makes() -> List[str]:
    """Return list of available vehicle makes in the database."""
    return list(DEF_PRODUCTS_DB.keys())

def list_available_models(make: str) -> List[str]:
    """
    Return list of available models for a given make.
    
    Args:
        make: Vehicle manufacturer name
        
    Returns:
        List of available models
        
    Raises:
        ValueError: If make is not found in database
    """
    try:
        return list(DEF_PRODUCTS_DB[make].keys())
    except KeyError:
        raise ValueError(f"Vehicle make '{make}' not found in database")

# Example usage
if __name__ == "__main__":
    try:
        makes = list_available_makes()
        print("Available makes:", makes)
        
        models = list_available_models("MG")
        print("Available MG models:", models)
        
        products, engines = get_def_recommendations("MG", "Hector")
        print("Recommended DEF products:", products)
        print("Compatible engines:", engines)
    except ValueError as e:
        print(f"Error: {e}")
```
