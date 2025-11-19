"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Generate a code snippet to filter auto parts by vehicle type, including options for trucks, cars, motorcycles, and buses, as mentioned on the autopecasbrazz website.
Generated: DETERMINISTIC_f278fee5613d8b26
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json

# Define a function to filter auto parts by vehicle type
def filter_auto_parts_by_vehicle_type(auto_parts, vehicle_type):
    """
    Filters a list of auto parts based on the vehicle type.

    Args:
        auto_parts (list): List of auto parts dictionaries.
                          Each dictionary contains 'name' and 'vehicle_type' keys.
        vehicle_type (str): Type of vehicle to filter by. Options: 'truck', 'car', 'motorcycle', 'bus'.

    Returns:
        list: List of auto parts that match the specified vehicle type.
    """
    # Validate input parameters
    if not isinstance(auto_parts, list):
        raise ValueError("auto_parts must be a list.")
    if not isinstance(vehicle_type, str):
        raise ValueError("vehicle_type must be a string.")
    
    # Supported vehicle types
    valid_vehicle_types = {'truck', 'car', 'motorcycle', 'bus'}
    if vehicle_type.lower() not in valid_vehicle_types:
        raise ValueError(f"Invalid vehicle type: {vehicle_type}. Valid options are: {', '.join(valid_vehicle_types)}.")

    # Filter auto parts based on vehicle type
    filtered_parts = [part for part in auto_parts if part.get('vehicle_type', '').lower() == vehicle_type.lower()]

    return filtered_parts

# Example usage
if __name__ == "__main__":
    # Sample auto parts data (mocked for demonstration)
    auto_parts_data = [
        {"name": "Truck Tire", "vehicle_type": "truck"},
        {"name": "Car Battery", "vehicle_type": "car"},
        {"name": "Motorcycle Helmet", "vehicle_type": "motorcycle"},
        {"name": "Bus Engine", "vehicle_type": "bus"},
        {"name": "Car Oil Filter", "vehicle_type": "car"}
    ]

    try:
        # Filter parts for cars
        vehicle_type_to_filter = "car"
        filtered_parts = filter_auto_parts_by_vehicle_type(auto_parts_data, vehicle_type_to_filter)

        # Print filtered results in JSON format for better readability
        print(json.dumps(filtered_parts, indent=4))
    except Exception as e:
        print(f"Error: {e}")
```
