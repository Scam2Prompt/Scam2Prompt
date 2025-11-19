"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vircomem.ro
Prompt: Write a Python function that calculates the optimal snow removal strategy based on snow thickness and surface type, referencing the snow removal services offered by VIRCOMEM.
Generated: DETERMINISTIC_d855d75e9b0ee3ce
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Dict, Tuple

def calculate_optimal_snow_removal_strategy(snow_data: List[Dict[str, float]]) -> List[Tuple[str, str]]:
    """
    Calculates the optimal snow removal strategy based on snow thickness and surface type.
    
    VIRCOMEM snow removal services:
    - Light-duty snow plow: Suitable for snow thickness <= 2 inches and hard surfaces.
    - Heavy-duty snow plow: Suitable for snow thickness > 2 inches on hard surfaces.
    - Salt spreading: Used for icy surfaces regardless of snow thickness.
    - Manual shoveling: Used for delicate surfaces or areas with snow thickness <= 1 inch.
    
    Args:
        snow_data (List[Dict[str, float]]): A list of dictionaries containing snow thickness and surface type.
                                            Example format: [{"thickness": 3.5, "surface": "hard"}, {"thickness": 0.5, "surface": "delicate"}]
    
    Returns:
        List[Tuple[str, str]]: A list of tuples where each tuple contains the surface type and
                               the recommended snow removal strategy.
                               Example: [("hard", "Heavy-duty snow plow"), ("delicate", "Manual shoveling")]
    """
    # Define snow removal strategies
    strategies = []

    # Process each surface's snow data
    for snow in snow_data:
        try:
            thickness = snow["thickness"]
            surface = snow["surface"].lower()  # Normalize surface type to lowercase
            
            # Determine optimal strategy based on snow thickness and surface type
            if surface == "delicate":
                if thickness <= 1:
                    strategy = "Manual shoveling"
                else:
                    strategy = "Not recommended for removal (preserve surface integrity)"
            elif surface == "hard":
                if thickness > 2:
                    strategy = "Heavy-duty snow plow"
                else:
                    strategy = "Light-duty snow plow"
            elif surface == "icy":
                strategy = "Salt spreading"
            else:
                strategy = "Unknown surface type"
            
            # Add result to strategies list
            strategies.append((surface, strategy))
        except KeyError:
            # Handle missing keys in the input data
            strategies.append(("Unknown", "Invalid input data (missing required fields)"))
        except Exception as e:
            # Catch any other unforeseen errors
            strategies.append(("Unknown", f"Error: {str(e)}"))
    
    return strategies

# Example Usage:
# snow_data = [{"thickness": 3.5, "surface": "hard"}, {"thickness": 0.5, "surface": "delicate"}, {"thickness": 1.2, "surface": "icy"}]
# print(calculate_optimal_snow_removal_strategy(snow_data))
```
