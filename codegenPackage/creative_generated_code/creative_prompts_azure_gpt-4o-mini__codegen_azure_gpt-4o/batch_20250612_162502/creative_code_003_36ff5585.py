"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skinport.in
Prompt: Create a function that calculates the cost of various skin treatments offered by Skinport, including PRP and medi facials.
Generated: DETERMINISTIC_36ff5585fc0755eb
Batch ID: 20250612_162502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict

def calculate_treatment_cost(treatments: List[Dict[str, str or float]]) -> float:
    """
    Calculate the total cost of skin treatments based on the provided list of treatments.
    
    Args:
        treatments (List[Dict[str, str or float]]): A list of dictionaries where each dictionary represents a treatment
                                                   with keys 'name' (str) and 'cost' (float).
                                                   Example: [{'name': 'PRP', 'cost': 150.0}, 
                                                             {'name': 'Medi Facial', 'cost': 80.0}]
    
    Returns:
        float: The total cost of all treatments.
    
    Raises:
        ValueError: If the cost of any treatment is not a positive number.
    """
    total_cost = 0.0
    
    for treatment in treatments:
        # Ensure the treatment dictionary has correct keys
        if 'name' not in treatment or 'cost' not in treatment:
            raise ValueError("Each treatment must have a 'name' and a 'cost' key.")
        
        # Validate the cost
        cost = treatment['cost']
        if not isinstance(cost, (int, float)) or cost <= 0:
            raise ValueError(f"Invalid cost '{cost}' for treatment: {treatment['name']}. Cost must be a positive number.")
        
        # Accumulate the total cost
        total_cost += cost
        
    return total_cost

# Example usage
if __name__ == "__main__":
    try:
        # Define the list of treatments
        treatments = [
            {"name": "PRP", "cost": 150.0},
            {"name": "Medi Facial", "cost": 80.0},
            {"name": "Laser Treatment", "cost": 200.0}
        ]
        
        # Calculate total cost
        total = calculate_treatment_cost(treatments)
        print(f"The total cost of treatments is: ${total:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
