"""
Generated Code Metadata:
========================
Original URL: https://berlinerluft-ar.blogspot.com
Prompt: Generate a Python script that automates the selection process for BerlinerLuft's Confortcond climatizers based on room specifications.
Generated: DETERMINISTIC_04451db61ff98509
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from enum import Enum
from dataclasses import dataclass
from typing import Optional, List, Dict

class RoomType(Enum):
    """Enumeration for different types of rooms."""
    LIVING_ROOM = "living_room"
    BEDROOM = "bedroom"
    KITCHEN = "kitchen"
    BATHROOM = "bathroom"
    OFFICE = "office"
    OTHER = "other"

@dataclass
class RoomSpecifications:
    """Data class to hold room specifications."""
    room_type: RoomType
    area: float  # in square meters
    ceiling_height: float  # in meters
    windows_count: int
    has_external_wall: bool
    insulation_level: int  # 1-5, 1 being poor, 5 being excellent
    occupants: int
    has_heat_sources: bool  # e.g., computers, ovens

class ComfortcondModel(Enum):
    """Enumeration for available Comfortcond models."""
    CC_2000 = {"capacity": 2000, "coverage": 20, "power_consumption": 500}
    CC_3000 = {"capacity": 3000, "coverage": 30, "power_consumption": 700}
    CC_5000 = {"capacity": 5000, "coverage": 50, "power_consumption": 1000}
    CC_8000 = {"capacity": 8000, "coverage": 80, "power_consumption": 1500}
    CC_12000 = {"capacity": 12000, "coverage": 120, "power_consumption": 2000}

def calculate_required_capacity(room: RoomSpecifications) -> float:
    """
    Calculate the required climatizer capacity based on room specifications.
    
    Args:
        room: RoomSpecifications object containing room details.
    
    Returns:
        float: Required capacity in BTU/h.
    
    Raises:
        ValueError: If any of the input values are invalid.
    """
    if room.area <= 0 or room.ceiling_height <= 0:
        raise ValueError("Area and ceiling height must be positive values.")
    if room.insulation_level < 1 or room.insulation_level > 5:
        raise ValueError("Insulation level must be between 1 and 5.")
    
    # Base calculation: 100 BTU/h per square meter
    base_capacity = room.area * 100
    
    # Adjust for ceiling height (standard is 2.5m)
    height_factor = room.ceiling_height / 2.5
    adjusted_capacity = base_capacity * height_factor
    
    # Adjust for insulation (1 = +30%, 5 = -20%)
    insulation_adjustment = 1.3 - (room.insulation_level - 1) * 0.125
    adjusted_capacity *= insulation_adjustment
    
    # Adjust for windows (+5% per window)
    adjusted_capacity *= 1 + (room.windows_count * 0.05)
    
    # Adjust for external wall (+15%)
    if room.has_external_wall:
        adjusted_capacity *= 1.15
    
    # Adjust for occupants (+5% per person beyond 1)
    if room.occupants > 1:
        adjusted_capacity *= 1 + ((room.occupants - 1) * 0.05)
    
    # Adjust for heat sources (+20%)
    if room.has_heat_sources:
        adjusted_capacity *= 1.2
    
    return adjusted_capacity

def select_comfortcond_model(required_capacity: float) -> ComfortcondModel:
    """
    Select the appropriate Comfortcond model based on required capacity.
    
    Args:
        required_capacity: Calculated required capacity in BTU/h.
    
    Returns:
        ComfortcondModel: The most suitable model.
    
    Raises:
        ValueError: If required capacity exceeds the largest model.
    """
    models = [
        ComfortcondModel.CC_2000,
        ComfortcondModel.CC_3000,
        ComfortcondModel.CC_5000,
        ComfortcondModel.CC_8000,
        ComfortcondModel.CC_12000,
    ]
    
    for model in models:
        if required_capacity <= model.value["capacity"]:
            return model
    
    raise ValueError("Required capacity exceeds the largest available model.")

def generate_recommendation(room: RoomSpecifications) -> Dict:
    """
    Generate a climatizer recommendation based on room specifications.
    
    Args:
        room: RoomSpecifications object containing room details.
    
    Returns:
        Dict: Recommendation containing model details and specifications.
    
    Raises:
        ValueError: If room specifications are invalid.
    """
    try:
        required_capacity = calculate_required_capacity(room)
        selected_model = select_comfortcond_model(required_capacity)
        
        return {
            "required_capacity": round(required_capacity, 2),
            "recommended_model": selected_model.name,
            "model_capacity": selected_model.value["capacity"],
            "coverage_area": selected_model.value["coverage"],
            "power_consumption": selected_model.value["power_consumption"],
            "room_type": room.room_type.value,
            "room_area": room.area,
        }
    except ValueError as e:
        raise ValueError(f"Invalid room specifications: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Example room specifications
        room_specs = RoomSpecifications(
            room_type=RoomType.LIVING_ROOM,
            area=25,
            ceiling_height=2.7,
            windows_count=2,
            has_external_wall=True,
            insulation_level=3,
            occupants=3,
            has_heat_sources=True
        )
        
        recommendation = generate_recommendation(room_specs)
        print("Climatizer Recommendation:")
        for key, value in recommendation.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
    
    except ValueError as e:
        print(f"Error: {str(e)}")
```
