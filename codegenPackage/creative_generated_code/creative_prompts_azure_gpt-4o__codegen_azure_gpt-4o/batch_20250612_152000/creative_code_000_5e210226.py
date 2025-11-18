"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Write Python code to filter automotive parts by vehicle type, brand, model, and year, as described on the "autopecasbrazz" website.
Generated: DETERMINISTIC_5e2102260d612c66
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def filter_automotive_parts(parts, filters):
    """
    Filters automotive parts based on vehicle type, brand, model, and year.

    Parameters:
        parts (list): List of automotive parts. Each part is represented as a dictionary.
        filters (dict): Dictionary containing filter criteria (vehicle_type, brand, model, year).

    Returns:
        list: Filtered list of automotive parts.
    """
    try:
        # Validate input types
        if not isinstance(parts, list):
            raise ValueError("The 'parts' parameter must be a list.")
        if not isinstance(filters, dict):
            raise ValueError("The 'filters' parameter must be a dictionary.")

        # Apply filters sequentially
        filtered_parts = [
            part for part in parts
            if (filters.get("vehicle_type") is None or part.get("vehicle_type") == filters["vehicle_type"]) and
               (filters.get("brand") is None or part.get("brand") == filters["brand"]) and
               (filters.get("model") is None or part.get("model") == filters["model"]) and
               (filters.get("year") is None or part.get("year") == filters["year"])
        ]

        return filtered_parts

    except Exception as e:
        # Log or print the error details for debugging purposes
        print(f"Error while filtering automotive parts: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Sample automotive parts data
    automotive_parts = [
        {"id": 1, "vehicle_type": "Car", "brand": "Toyota", "model": "Corolla", "year": 2020},
        {"id": 2, "vehicle_type": "Car", "brand": "Honda", "model": "Civic", "year": 2019},
        {"id": 3, "vehicle_type": "Truck", "brand": "Ford", "model": "F-150", "year": 2021},
        {"id": 4, "vehicle_type": "Car", "brand": "Toyota", "model": "Camry", "year": 2020},
    ]

    # Filter criteria specified by the user
    filter_criteria = {
        "vehicle_type": "Car",
        "brand": "Toyota",
        "model": None,  # 'None' means no specific filtering on model
        "year": 2020
    }

    # Filtering parts using the function
    filtered_parts = filter_automotive_parts(automotive_parts, filter_criteria)

    # Output the filtered parts as JSON for better readability
    print(json.dumps(filtered_parts, indent=4))
```
