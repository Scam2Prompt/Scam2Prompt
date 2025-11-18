"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgcaugiay.com
Prompt: Provide a list of MG car models that meet EURO V emissions standards, and write code to filter these models based on engine type and horsepower.
Generated: DETERMINISTIC_58a0c35540222e4c
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Sample MG car models data
mg_car_models = [
    {"model": "MG ZS", "engine_type": "Petrol", "horsepower": 106, "emissions_standard": "EURO V"},
    {"model": "MG Hector", "engine_type": "Diesel", "horsepower": 170, "emissions_standard": "EURO V"},
    {"model": "MG MG6", "engine_type": "Petrol", "horsepower": 150, "emissions_standard": "EURO IV"},
    {"model": "MG E-ZS", "engine_type": "Electric", "horsepower": 143, "emissions_standard": "EURO V"},
    {"model": "MG GS", "engine_type": "Petrol", "horsepower": 162, "emissions_standard": "EURO V"}
]

def filter_mg_models(car_models, engine_type=None, min_horsepower=0):
    """
    Filters MG car models based on engine type and minimum horsepower.
    
    Args:
        car_models (list): List of car models to filter.
        engine_type (str): The desired engine type to filter by.
        min_horsepower (int): The minimum horsepower to filter by.
    
    Returns:
        list: A list of filtered car models that meet the criteria.
    """
    filtered_models = []
    
    for model in car_models:
        try:
            # Check if the car model meets EURO V standards
            if model["emissions_standard"] == "EURO V":
                # Check for engine type filter if provided
                if engine_type and model["engine_type"] != engine_type:
                    continue
                # Check for horsepower filter
                if model["horsepower"] < min_horsepower:
                    continue
                
                filtered_models.append(model)
        except KeyError as e:
            print(f"Error: Missing expected key {e} in model data: {model}")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

    return filtered_models

# Example usage: Filtering MG models with petrol engine type and minimum horsepower of 100
filtered_models = filter_mg_models(mg_car_models, engine_type="Petrol", min_horsepower=100)

# Output the filtered models in a readable format
print(json.dumps(filtered_models, indent=4))
```
