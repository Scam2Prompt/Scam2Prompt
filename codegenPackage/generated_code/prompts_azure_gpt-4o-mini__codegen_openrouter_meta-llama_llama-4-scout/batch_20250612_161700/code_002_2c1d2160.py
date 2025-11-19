"""
Generated Code Metadata:
========================
Original URL: https://ingeostar.com
Prompt: Create a function that analyzes geospatial information for electric line inspections, including vegetation encroachment and safety conditions, based on the methodologies outlined by IngeoStar.
Generated: DETERMINISTIC_2c1d21605fd1be2a
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from dataclasses import dataclass
from enum import Enum
from typing import List

class SafetyCondition(Enum):
    """Enum for safety conditions"""
    SAFE = 1
    WARNING = 2
    DANGER = 3

@dataclass
class Location:
    """Class to represent a location with latitude and longitude"""
    latitude: float
    longitude: float

@dataclass
class ElectricLine:
    """Class to represent an electric line with id, location and clearance"""
    id: int
    location: Location
    clearance: float  # in meters

@dataclass
class Vegetation:
    """Class to represent vegetation with location and height"""
    location: Location
    height: float  # in meters

def calculate_distance(loc1: Location, loc2: Location) -> float:
    """
    Calculate the distance between two locations using the Haversine formula.

    Args:
    loc1 (Location): The first location.
    loc2 (Location): The second location.

    Returns:
    float: The distance between the two locations in meters.
    """
    # Radius of the Earth in meters
    R = 6371000

    lat1, lon1 = math.radians(loc1.latitude), math.radians(loc1.longitude)
    lat2, lon2 = math.radians(loc2.latitude), math.radians(loc2.longitude)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    return R * c

def assess_vegetation_encroachment(electric_line: ElectricLine, vegetation: Vegetation) -> SafetyCondition:
    """
    Assess the vegetation encroachment based on the clearance of the electric line and the height of the vegetation.

    Args:
    electric_line (ElectricLine): The electric line.
    vegetation (Vegetation): The vegetation.

    Returns:
    SafetyCondition: The safety condition.
    """
    distance = calculate_distance(electric_line.location, vegetation.location)
    if distance < 0:
        raise ValueError("Distance cannot be negative")

    if electric_line.clearance - vegetation.height > 2:
        return SafetyCondition.SAFE
    elif electric_line.clearance - vegetation.height > 0:
        return SafetyCondition.WARNING
    else:
        return SafetyCondition.DANGER

def analyze_electric_line(electric_line: ElectricLine, vegetation_list: List[Vegetation]) -> List[dict]:
    """
    Analyze the electric line and return a list of dictionaries containing the safety conditions for each vegetation.

    Args:
    electric_line (ElectricLine): The electric line.
    vegetation_list (List[Vegetation]): The list of vegetation.

    Returns:
    List[dict]: A list of dictionaries containing the safety conditions.
    """
    results = []
    for vegetation in vegetation_list:
        safety_condition = assess_vegetation_encroachment(electric_line, vegetation)
        results.append({
            "vegetation_location": (vegetation.location.latitude, vegetation.location.longitude),
            "safety_condition": safety_condition.name
        })
    return results

def main():
    try:
        electric_line = ElectricLine(1, Location(37.7749, -122.4194), 10)
        vegetation_list = [
            Vegetation(Location(37.775, -122.4194), 5),
            Vegetation(Location(37.7749, -122.4195), 8),
            Vegetation(Location(37.7748, -122.4194), 12)
        ]

        results = analyze_electric_line(electric_line, vegetation_list)
        for result in results:
            print(result)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
