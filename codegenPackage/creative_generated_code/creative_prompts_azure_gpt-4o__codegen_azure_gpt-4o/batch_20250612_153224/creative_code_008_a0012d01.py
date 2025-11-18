"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emareels.se
Prompt: Create a Python script to filter Emanuelson Reels models by price range and line class, including options like "Trout 2 Wide" and "Sea-Trout."
Generated: DETERMINISTIC_a0012d01cc787e66
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def filter_models_by_price_and_line_class(models, min_price, max_price, line_class):
    """
    Filter Emanuelson Reels models by price range and line class.

    Parameters:
        models (list): List of reel models (dicts) with 'name', 'price', and 'line_class'.
        min_price (float): Minimum price of the reel.
        max_price (float): Maximum price of the reel.
        line_class (str): Desired line class, e.g., "Trout 2 Wide", "Sea-Trout".

    Returns:
        list: Filtered list of models matching the criteria.
    """
    try:
        # Validate inputs
        if not isinstance(models, list):
            raise ValueError("The 'models' parameter must be a list.")
        if not isinstance(min_price, (int, float)) or not isinstance(max_price, (int, float)):
            raise ValueError("The 'min_price' and 'max_price' must be numbers.")
        if not isinstance(line_class, str):
            raise ValueError("The 'line_class' must be a string.")

        # Filter the models
        filtered_models = [
            model for model in models
            if min_price <= model.get('price', 0) <= max_price and model.get('line_class') == line_class
        ]

        return filtered_models
    except Exception as e:
        print(f"Error while filtering models: {e}")
        return []

# Example usage:
if __name__ == "__main__":
    # Sample data representing Emanuelson Reels models
    reel_models = [
        {"name": "Trout 2 Wide", "price": 150.0, "line_class": "Trout 2 Wide"},
        {"name": "Sea-Trout", "price": 200.0, "line_class": "Sea-Trout"},
        {"name": "Ultra-Light", "price": 100.0, "line_class": "Trout 1 Narrow"},
        {"name": "Heavy-Duty", "price": 300.0, "line_class": "Sea-Trout"},
    ]

    # Filter by price range and line class
    min_price = 100.0
    max_price = 250.0
    desired_line_class = "Sea-Trout"

    # Get filtered results
    filtered_reels = filter_models_by_price_and_line_class(reel_models, min_price, max_price, desired_line_class)

    # Print results
    print("Filtered Emanuelson Reels models:")
    print(json.dumps(filtered_reels, indent=4))
```
