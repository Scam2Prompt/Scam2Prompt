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
from enum import Enum
from typing import List, Dict, Optional

class VehicleType(Enum):
    """Enum representing different vehicle types."""
    CAR = "car"
    TRUCK = "truck"
    MOTORCYCLE = "motorcycle"
    BUS = "bus"

class AutoPart:
    """Class representing an auto part with vehicle type compatibility."""
    def __init__(self, part_id: str, name: str, price: float, compatible_vehicles: List[VehicleType]):
        self.part_id = part_id
        self.name = name
        self.price = price
        self.compatible_vehicles = compatible_vehicles

    def __repr__(self):
        return f"AutoPart(id={self.part_id}, name={self.name}, price={self.price}, compatible_with={self.compatible_vehicles})"

class AutoPartsFilter:
    """Class for filtering auto parts by vehicle type."""
    def __init__(self, parts: List[AutoPart]):
        self.parts = parts

    def filter_by_vehicle_type(self, vehicle_type: VehicleType) -> List[AutoPart]:
        """
        Filters auto parts by the specified vehicle type.
        
        Args:
            vehicle_type: VehicleType enum value to filter by
            
        Returns:
            List of AutoPart objects compatible with the specified vehicle type
        """
        if not isinstance(vehicle_type, VehicleType):
            raise ValueError("Invalid vehicle type. Must be a VehicleType enum value.")
            
        return [part for part in self.parts if vehicle_type in part.compatible_vehicles]

    def get_available_vehicle_types(self) -> Dict[str, List[AutoPart]]:
        """
        Returns a dictionary mapping each vehicle type to its compatible parts.
        
        Returns:
            Dictionary with VehicleType values as keys and lists of compatible parts as values
        """
        result = {vt.value: [] for vt in VehicleType}
        for part in self.parts:
            for vt in part.compatible_vehicles:
                result[vt.value].append(part)
        return result

# Example usage
if __name__ == "__main__":
    # Sample auto parts data
    parts = [
        AutoPart("p1", "Brake Pads", 45.99, [VehicleType.CAR, VehicleType.TRUCK]),
        AutoPart("p2", "Headlight", 32.50, [VehicleType.CAR, VehicleType.BUS]),
        AutoPart("p3", "Tire", 89.99, [VehicleType.CAR, VehicleType.TRUCK, VehicleType.BUS]),
        AutoPart("p4", "Exhaust Pipe", 120.00, [VehicleType.MOTORCYCLE]),
        AutoPart("p5", "Mirror", 25.75, [VehicleType.CAR, VehicleType.MOTORCYCLE, VehicleType.BUS])
    ]
    
    filter = AutoPartsFilter(parts)
    
    # Filter by vehicle type
    car_parts = filter.filter_by_vehicle_type(VehicleType.CAR)
    print("Car parts:", car_parts)
    
    # Get all available vehicle types and their parts
    available_types = filter.get_available_vehicle_types()
    print("\nAvailable vehicle types and parts:")
    for vt, parts_list in available_types.items():
        print(f"{vt}: {len(parts_list)} parts available")
```
