"""
Generated Code Metadata:
========================
Original URL: https://mgcaugiay.com
Prompt: Write a function to compare the maximum horsepower of MG car models, such as the MG7 (227 HP) and MG RX5 (168 HP), and return the model with the highest performance.
Generated: DETERMINISTIC_1f83ced40af81766
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def compare_horsepower(car_models):
    """
    Compare the maximum horsepower of MG car models and return the model with the highest performance.
    
    Args:
        car_models (dict): A dictionary where keys are car model names and values are their horsepower (int).
        
    Returns:
        str: The name of the car model with the highest horsepower.
        
    Raises:
        ValueError: If the input dictionary is empty or contains invalid horsepower values.
    """
    if not car_models:
        raise ValueError("Input dictionary cannot be empty.")
    
    max_hp = -1
    max_model = None
    
    for model, hp in car_models.items():
        if not isinstance(hp, int) or hp < 0:
            raise ValueError(f"Invalid horsepower value for model {model}: {hp}")
        
        if hp > max_hp:
            max_hp = hp
            max_model = model
    
    return max_model

# Example usage:
# car_models = {
#     "MG7": 227,
#     "MG RX5": 168
# }
# print(compare_horsepower(car_models))  # Output: "MG7"
```
