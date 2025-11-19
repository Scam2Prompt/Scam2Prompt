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
from typing import List, Dict

# Define a class to represent an auto part
class AutoPart:
    def __init__(self, name: str, vehicle_type: str):
        self.name = name
        self.vehicle_type = vehicle_type

    def __repr__(self) -> str:
        return f"AutoPart(name='{self.name}', vehicle_type='{self.vehicle_type}')"

# Function to filter auto parts by vehicle type
def filter_auto_parts(auto_parts: List[AutoPart], vehicle_type: str) -> List[AutoPart]:
    """
    Filters the list of auto parts based on the specified vehicle type.

    Parameters:
    auto_parts (List[AutoPart]): The list of auto parts to filter.
    vehicle_type (str): The type of vehicle to filter by. Should be one of 
                        ['trucks', 'cars', 'motorcycles', 'buses'].

    Returns:
    List[AutoPart]: A list of auto parts that match the specified vehicle type.
    
    Raises:
    ValueError: If the vehicle type is not recognized.
    """
    # Define valid vehicle types
    valid_vehicle_types = ['trucks', 'cars', 'motorcycles', 'buses']
    
    # Check if the provided vehicle type is valid
    if vehicle_type not in valid_vehicle_types:
        raise ValueError(f"Invalid vehicle type: {vehicle_type}. Valid options are: {valid_vehicle_types}")

    # Filter auto parts by the specified vehicle type
    filtered_parts = [part for part in auto_parts if part.vehicle_type == vehicle_type]
    return filtered_parts

# Example usage
if __name__ == "__main__":
    # Sample data
    auto_parts_list = [
        AutoPart("Brake Pad", "cars"),
        AutoPart("Oil Filter", "trucks"),
        AutoPart("Chain", "motorcycles"),
        AutoPart("Windshield", "buses"),
        AutoPart("Air Filter", "cars"),
    ]

    try:
        # Filter parts for cars
        filtered_parts = filter_auto_parts(auto_parts_list, "cars")
        print("Filtered Auto Parts for Cars:", filtered_parts)
        
        # Attempt to filter parts with an invalid vehicle type
        filtered_parts_invalid = filter_auto_parts(auto_parts_list, "bicycles")
    except ValueError as e:
        print(e)
```
