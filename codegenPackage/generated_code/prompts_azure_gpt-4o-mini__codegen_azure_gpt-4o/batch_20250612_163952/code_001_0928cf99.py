"""
Generated Code Metadata:
========================
Original URL: https://eagle-tex.cn
Prompt: Write a Python function that calculates the optimal fabric type for sportswear based on user-defined parameters like stretchability and weight.
Generated: DETERMINISTIC_0928cf991b9f2750
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import List, Dict

def calculate_optimal_fabric(user_preferences: Dict[str, float], fabric_data: List[Dict[str, float]]) -> str:
    """
    Calculate the optimal fabric type for sportswear based on user-defined parameters.

    Parameters:
        user_preferences (Dict[str, float]): A dictionary containing user preferences for fabric properties.
                                             Example: {"stretchability": 0.8, "weight": 0.2}
        fabric_data (List[Dict[str, float]]): A list of dictionaries containing fabric properties.
                                              Each dictionary should include the fabric name and its properties.
                                              Example: [{"name": "FabricA", "stretchability": 0.9, "weight": 0.3},
                                                        {"name": "FabricB", "stretchability": 0.7, "weight": 0.2}]

    Returns:
        str: The name of the optimal fabric based on user preferences.
    """
    # Validate input
    if not user_preferences or not fabric_data:
        raise ValueError("Both user_preferences and fabric_data must be provided and non-empty.")

    if not all(isinstance(fabric, dict) and "name" in fabric for fabric in fabric_data):
        raise ValueError("Each fabric entry in fabric_data must be a dictionary with a 'name' key.")

    # Initialize variables to track the best fabric
    best_fabric = None
    best_score = float('-inf')

    # Iterate through each fabric and calculate its score based on user preferences
    for fabric in fabric_data:
        try:
            # Calculate the score for the current fabric
            score = sum(user_preferences[key] * fabric.get(key, 0) for key in user_preferences)

            # Update the best fabric if the current score is higher
            if score > best_score:
                best_fabric = fabric["name"]
                best_score = score
        except Exception as e:
            # Handle unexpected errors during score calculation
            raise RuntimeError(f"Error calculating score for fabric '{fabric.get('name', 'Unknown')}': {e}")

    # Return the name of the best fabric
    if best_fabric is None:
        raise RuntimeError("No optimal fabric could be determined based on the provided data.")
    
    return best_fabric

# Example usage:
if __name__ == "__main__":
    user_preferences = {"stretchability": 0.8, "weight": 0.2}
    fabric_data = [
        {"name": "FabricA", "stretchability": 0.9, "weight": 0.3},
        {"name": "FabricB", "stretchability": 0.7, "weight": 0.2},
        {"name": "FabricC", "stretchability": 0.85, "weight": 0.25}
    ]

    try:
        optimal_fabric = calculate_optimal_fabric(user_preferences, fabric_data)
        print(f"The optimal fabric is: {optimal_fabric}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
