"""
Generated Code Metadata:
========================
Original URL: https://mgcaugiay.com
Prompt: Provide a list of MG car models that meet EURO V emissions standards, and write code to filter these models based on engine type and horsepower.
Generated: DETERMINISTIC_58a0c35540222e4c
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

# Sample data representing MG car models
mg_car_models = [
    {"model": "MG ZS", "emissions_standard": "EURO V", "engine_type": "Petrol", "horsepower": 110},
    {"model": "MG Hector", "emissions_standard": "EURO V", "engine_type": "Diesel", "horsepower": 170},
    {"model": "MG MG3", "emissions_standard": "EURO IV", "engine_type": "Petrol", "horsepower": 105},
    {"model": "MG ZS EV", "emissions_standard": "EURO V", "engine_type": "Electric", "horsepower": 150},
    {"model": "MG Marvel R", "emissions_standard": "EURO V", "engine_type": "Electric", "horsepower": 180},
]

def filter_mg_models(models, engine_type=None, min_horsepower=None):
    """
    Filters MG car models based on engine type and minimum horsepower.

    :param models: List of MG car models (dicts)
    :param engine_type: Optional; filter by specific engine type
    :param min_horsepower: Optional; filter by minimum horsepower
    :return: List of filtered MG car models
    """
    filtered_models = []

    for model in models:
        # Check if the model meets EURO V emissions standards
        if model["emissions_standard"] != "EURO V":
            continue
        
        # Check for engine type filter
        if engine_type and model["engine_type"] != engine_type:
            continue
        
        # Check for minimum horsepower filter
        if min_horsepower and model["horsepower"] < min_horsepower:
            continue
        
        # If all conditions are met, add the model to the filtered list
        filtered_models.append(model)

    return filtered_models

# Example usage
if __name__ == "__main__":
    try:
        # Filter MG models for Petrol engines with at least 100 horsepower
        result = filter_mg_models(mg_car_models, engine_type="Petrol", min_horsepower=100)
        print(json.dumps(result, indent=4))  # Pretty print the result
    except Exception as e:
        print(f"An error occurred: {e}")
```
