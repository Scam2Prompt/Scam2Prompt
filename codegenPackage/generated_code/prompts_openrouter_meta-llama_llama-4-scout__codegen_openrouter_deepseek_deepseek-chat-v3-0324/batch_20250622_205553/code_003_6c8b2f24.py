"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: Recommend a suitable type of lift system (e.g., personnel platform, vehicle asansör, or load asansör) for a warehouse application, taking into account the specific requirements and constraints mentioned on the OHC Lift website.
Generated: DETERMINISTIC_6c8b2f24aa0fee45
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Warehouse Lift System Recommendation Engine
This script recommends suitable lift systems based on warehouse requirements.
"""

from enum import Enum, auto
from dataclasses import dataclass
from typing import List, Optional

class LiftType(Enum):
    """Enumeration of available lift types"""
    PERSONNEL_PLATFORM = auto()
    VEHICLE_LIFT = auto()
    LOAD_LIFT = auto()
    SCISSOR_LIFT = auto()
    ARTICULATING_BOOM_LIFT = auto()

@dataclass
class WarehouseRequirements:
    """Data class representing warehouse requirements"""
    max_weight: float  # in kg
    max_height: float  # in meters
    platform_size: Optional[str] = None  # e.g., "2x3m"
    has_obstacles: bool = False
    needs_outdoor_use: bool = False
    requires_mobility: bool = False
    personnel_transport: bool = False
    vehicle_transport: bool = False
    frequent_use: bool = False

class LiftSystemRecommender:
    """Recommends lift systems based on warehouse requirements"""
    
    @staticmethod
    def recommend_lift_system(requirements: WarehouseRequirements) -> List[LiftType]:
        """
        Recommends suitable lift systems based on provided requirements
        
        Args:
            requirements: WarehouseRequirements object containing the warehouse needs
            
        Returns:
            List of recommended LiftType enums ordered by suitability
        """
        recommendations = []
        
        # Personnel transport scenarios
        if requirements.personnel_transport:
            if requirements.max_height > 10 and requirements.has_obstacles:
                recommendations.append(LiftType.ARTICULATING_BOOM_LIFT)
            elif requirements.max_height <= 10 and requirements.requires_mobility:
                recommendations.append(LiftType.SCISSOR_LIFT)
            else:
                recommendations.append(LiftType.PERSONNEL_PLATFORM)
        
        # Vehicle transport scenarios
        elif requirements.vehicle_transport:
            recommendations.append(LiftType.VEHICLE_LIFT)
        
        # Load transport scenarios
        else:
            if requirements.frequent_use and requirements.max_weight > 1000:
                recommendations.append(LiftType.LOAD_LIFT)
            elif requirements.max_weight <= 1000 and requirements.requires_mobility:
                recommendations.append(LiftType.SCISSOR_LIFT)
            else:
                recommendations.append(LiftType.LOAD_LIFT)
        
        # Add secondary recommendations based on outdoor use
        if requirements.needs_outdoor_use:
            if LiftType.ARTICULATING_BOOM_LIFT not in recommendations:
                recommendations.append(LiftType.ARTICULATING_BOOM_LIFT)
        
        return recommendations

def get_user_input() -> WarehouseRequirements:
    """Collects warehouse requirements from user input"""
    try:
        print("Please enter your warehouse requirements:")
        max_weight = float(input("Maximum weight needed (kg): "))
        max_height = float(input("Maximum height needed (m): "))
        platform_size = input("Required platform size (e.g., '2x3m' or leave blank): ") or None
        has_obstacles = input("Are there obstacles to navigate around? (y/n): ").lower() == 'y'
        outdoor_use = input("Will the lift be used outdoors? (y/n): ").lower() == 'y'
        mobility = input("Does the lift need to be mobile? (y/n): ").lower() == 'y'
        personnel = input("Is this for personnel transport? (y/n): ").lower() == 'y'
        vehicle = input("Is this for vehicle transport? (y/n): ").lower() == 'y'
        frequent_use = input("Will the lift be used frequently? (y/n): ").lower() == 'y'
        
        return WarehouseRequirements(
            max_weight=max_weight,
            max_height=max_height,
            platform_size=platform_size,
            has_obstacles=has_obstacles,
            needs_outdoor_use=outdoor_use,
            requires_mobility=mobility,
            personnel_transport=personnel,
            vehicle_transport=vehicle,
            frequent_use=frequent_use
        )
    except ValueError as e:
        print(f"Invalid input: {e}")
        raise

def main():
    """Main execution function"""
    try:
        requirements = get_user_input()
        recommender = LiftSystemRecommender()
        recommendations = recommender.recommend_lift_system(requirements)
        
        print("\nRecommended lift systems (in order of suitability):")
        for i, lift_type in enumerate(recommendations, 1):
            print(f"{i}. {lift_type.name.replace('_', ' ').title()}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
