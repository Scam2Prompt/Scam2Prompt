"""
Generated Code Metadata:
========================
Original URL: https://yaisatangwell.com
Prompt: "Generate a maternity photography session plan, including poses, locations, and tips for capturing the beauty of expecting couples, inspired by the services offered on yaisatangwell.com."
Generated: DETERMINISTIC_77b16b56e11f5970
Batch ID: 20250622_211502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Maternity Photography Session Planner
Inspired by yaisatangwell.com's maternity photography services.

This script generates a customizable maternity photography session plan,
including recommended poses, locations, and professional tips.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional
import random


class Trimester(Enum):
    """Enum representing pregnancy trimesters."""
    FIRST = auto()
    SECOND = auto()
    THIRD = auto()


class LocationType(Enum):
    """Enum representing different location types for shoots."""
    INDOOR = auto()
    OUTDOOR = auto()
    STUDIO = auto()


@dataclass
class Pose:
    """Class representing a photography pose."""
    name: str
    description: str
    trimester_suitability: List[Trimester]
    tips: List[str]


@dataclass
class Location:
    """Class representing a photography location."""
    name: str
    location_type: LocationType
    description: str
    lighting_tips: List[str]


@dataclass
class SessionPlan:
    """Class representing a complete maternity session plan."""
    poses: List[Pose]
    locations: List[Location]
    general_tips: List[str]


def generate_maternity_session_plan(trimester: Trimester) -> SessionPlan:
    """
    Generates a maternity photography session plan based on trimester.
    
    Args:
        trimester: The pregnancy trimester to tailor the plan for.
    
    Returns:
        A complete SessionPlan object with poses, locations, and tips.
    """
    # Define common poses
    all_poses = [
        Pose(
            name="The Embrace",
            description="Couple facing each other, hands on belly",
            trimester_suitability=[Trimester.SECOND, Trimester.THIRD],
            tips=[
                "Shoot from slightly below to emphasize belly",
                "Have couple rest foreheads together for intimacy"
            ]
        ),
        Pose(
            name="Silhouette",
            description="Side profile against light source",
            trimester_suitability=[Trimester.SECOND, Trimester.THIRD],
            tips=[
                "Use sunset or window light for best effect",
                "Focus on the belly outline"
            ]
        ),
        Pose(
            name="Sitting Pose",
            description="Mother seated, hands cradling belly",
            trimester_suitability=[Trimester.FIRST, Trimester.SECOND, Trimester.THIRD],
            tips=[
                "Use a stool or chair with simple lines",
                "Shoot from slightly above for flattering angle"
            ]
        ),
        Pose(
            name="Walking Shot",
            description="Couple walking hand-in-hand",
            trimester_suitability=[Trimester.SECOND],
            tips=[
                "Capture mid-stride for natural movement",
                "Use continuous shooting mode"
            ]
        ),
        Pose(
            name="Baby Items",
            description="Incorporating baby shoes or ultrasound photos",
            trimester_suitability=[Trimester.THIRD],
            tips=[
                "Keep props simple and meaningful",
                "Focus on hands holding the items"
            ]
        )
    ]

    # Define locations
    all_locations = [
        Location(
            name="Beach",
            location_type=LocationType.OUTDOOR,
            description="Soft sand and water backdrop",
            lighting_tips=[
                "Shoot during golden hour",
                "Use reflector to fill shadows"
            ]
        ),
        Location(
            name="Home",
            location_type=LocationType.INDOOR,
            description="Comfortable and personal setting",
            lighting_tips=[
                "Use window light for soft illumination",
                "Add warm-toned lamps for coziness"
            ]
        ),
        Location(
            name="Park/Garden",
            location_type=LocationType.OUTDOOR,
            description="Natural greenery and flowers",
            lighting_tips=[
                "Avoid harsh midday sun",
                "Use foliage to create natural framing"
            ]
        ),
        Location(
            name="Studio",
            location_type=LocationType.STUDIO,
            description="Controlled lighting environment",
            lighting_tips=[
                "Use softboxes for even lighting",
                "Consider high-key lighting for ethereal look"
            ]
        )
    ]

    # Define general tips
    general_tips = [
        "Schedule between 28-36 weeks for best belly shape",
        "Encourage natural interactions between couples",
        "Use flowing fabrics for movement in shots",
        "Include both close-ups and full-body shots",
        "Capture details like hands on belly and baby kicks"
    ]

    # Filter poses by trimester suitability
    suitable_poses = [pose for pose in all_poses if trimester in pose.trimester_suitability]

    # Select 3-5 poses randomly (or all if less than 5)
    selected_poses = random.sample(suitable_poses, min(len(suitable_poses), 5))

    # Select 2-3 locations randomly
    selected_locations = random.sample(all_locations, min(len(all_locations), 3))

    return SessionPlan(
        poses=selected_poses,
        locations=selected_locations,
        general_tips=general_tips
    )


def print_session_plan(plan: SessionPlan) -> None:
    """Prints the session plan in a readable format."""
    print("\n=== Maternity Photography Session Plan ===\n")
    
    print("Recommended Poses:")
    for i, pose in enumerate(plan.poses, 1):
        print(f"\n{i}. {pose.name}")
        print(f"   Description: {pose.description}")
        print("   Tips:")
        for tip in pose.tips:
            print(f"     - {tip}")
    
    print("\nRecommended Locations:")
    for i, location in enumerate(plan.locations, 1):
        print(f"\n{i}. {location.name} ({location.location_type.name})")
        print(f"   Description: {location.description}")
        print("   Lighting Tips:")
        for tip in location.lighting_tips:
            print(f"     - {tip}")
    
    print("\nGeneral Tips:")
    for i, tip in enumerate(plan.general_tips, 1):
        print(f"{i}. {tip}")


# Example usage
if __name__ == "__main__":
    try:
        trimester = Trimester.THIRD  # Change this to FIRST or SECOND as needed
        session_plan = generate_maternity_session_plan(trimester)
        print_session_plan(session_plan)
    except Exception as e:
        print(f"Error generating session plan: {e}")
```
