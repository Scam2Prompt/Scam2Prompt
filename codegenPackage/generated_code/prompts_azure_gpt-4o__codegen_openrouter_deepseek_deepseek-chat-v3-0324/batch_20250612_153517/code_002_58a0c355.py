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
# Import necessary libraries
from typing import List, Dict, Optional

# Define a data structure to hold MG car models information
class MGCarModel:
    def __init__(self, model_name: str, engine_type: str, horsepower: int, euro_standard: str):
        self.model_name = model_name
        self.engine_type = engine_type
        self.horsepower = horsepower
        self.euro_standard = euro_standard

    def __repr__(self):
        return f"MG {self.model_name} ({self.engine_type}, {self.horsepower}HP, {self.euro_standard})"

# Sample database of MG car models (would typically come from a database in production)
def get_mg_car_models() -> List[MGCarModel]:
    return [
        MGCarModel("MG3", "Petrol", 106, "EURO V"),
        MGCarModel("ZS", "Petrol", 105, "EURO V"),
        MGCarModel("ZS", "Electric", 143, "EURO V"),
        MGCarModel("HS", "Petrol", 162, "EURO V"),
        MGCarModel("HS", "Hybrid", 258, "EURO V"),
        MGCarModel("5", "Diesel", 148, "EURO IV"),  # Not EURO V
        MGCarModel("TF", "Petrol", 135, "EURO V"),
    ]

# Function to filter MG car models by EURO standard, engine type, and horsepower range
def filter_mg_models(
    euro_standard: str = "EURO V",
    engine_type: Optional[str] = None,
    min_horsepower: Optional[int] = None,
    max_horsepower: Optional[int] = None
) -> List[MGCarModel]:
    """
    Filters MG car models based on specified criteria.
    
    Args:
        euro_standard: Emission standard to filter by (default: EURO V)
        engine_type: Specific engine type to filter (e.g., "Petrol", "Electric")
        min_horsepower: Minimum horsepower threshold
        max_horsepower: Maximum horsepower threshold
    
    Returns:
        List of MGCarModel objects that match the criteria
    """
    all_models = get_mg_car_models()
    filtered_models = []
    
    for model in all_models:
        # Check EURO standard first
        if model.euro_standard != euro_standard:
            continue
            
        # Check engine type if specified
        if engine_type is not None and model.engine_type != engine_type:
            continue
            
        # Check horsepower range if specified
        if min_horsepower is not None and model.horsepower < min_horsepower:
            continue
        if max_horsepower is not None and model.horsepower > max_horsepower:
            continue
            
        filtered_models.append(model)
    
    return filtered_models

# Example usage
if __name__ == "__main__":
    print("All EURO V MG models:")
    euro_v_models = filter_mg_models()
    for model in euro_v_models:
        print(model)
    
    print("\nEURO V Petrol models with at least 100HP:")
    petrol_models = filter_mg_models(engine_type="Petrol", min_horsepower=100)
    for model in petrol_models:
        print(model)
    
    print("\nEURO V models with 100-150HP:")
    mid_range_models = filter_mg_models(min_horsepower=100, max_horsepower=150)
    for model in mid_range_models:
        print(model)
```
