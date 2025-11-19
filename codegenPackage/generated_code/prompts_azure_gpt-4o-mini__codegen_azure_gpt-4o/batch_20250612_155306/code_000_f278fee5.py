"""
Generated Code Metadata:
========================
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Generate a code snippet to filter auto parts by vehicle type, including options for trucks, cars, motorcycles, and buses, as mentioned on the autopecasbrazz website.
Generated: DETERMINISTIC_f278fee5613d8b26
Batch ID: 20250612_155306
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

# Define a function to filter auto parts by vehicle type
def filter_auto_parts_by_vehicle_type(auto_parts: List[Dict[str, str]], vehicle_type: str) -> List[Dict[str, str]]:
    """
    Filters a list of auto parts based on the specified vehicle type.

    Args:
        auto_parts (List[Dict[str, str]]): A list of dictionaries representing auto parts. 
                                           Each dictionary must contain a 'vehicle_type' key.
        vehicle_type (str): The type of vehicle to filter by. Options: 'truck', 'car', 'motorcycle', 'bus'.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing auto parts for the specified vehicle type.
    """
    # Validate input
    valid_vehicle_types = {'truck', 'car', 'motorcycle', 'bus'}
    if vehicle_type not in valid_vehicle_types:
        raise ValueError(f"Invalid vehicle type: {vehicle_type}. Must be one of {valid_vehicle_types}.")

    # Filter auto parts based on vehicle type
    filtered_parts = [part for part in auto_parts if part.get('vehicle_type') == vehicle_type]

    return filtered_parts


# Example usage
if __name__ == "__main__":
    # Sample data representing auto parts
    auto_parts_data = [
        {"name": "Brake Pad", "vehicle_type": "car"},
        {"name": "Oil Filter", "vehicle_type": "truck"},
        {"name": "Helmet", "vehicle_type": "motorcycle"},
        {"name": "Windshield Wiper", "vehicle_type": "bus"},
        {"name": "Spark Plug", "vehicle_type": "car"},
    ]

    try:
        # Filter auto parts for cars
        car_parts = filter_auto_parts_by_vehicle_type(auto_parts_data, "car")
        print("Auto parts for cars:", car_parts)

        # Filter auto parts for motorcycles
        motorcycle_parts = filter_auto_parts_by_vehicle_type(auto_parts_data, "motorcycle")
        print("Auto parts for motorcycles:", motorcycle_parts)

    except ValueError as e:
        # Handle invalid vehicle type error
        print(f"Error: {e}")
```
