"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dexodoor.com
Prompt: Create a function to compare the strength and durability of UPVC door systems with traditional wooden doors, incorporating the anti-fungi and anti-termite properties mentioned on the Dexodoor webpage.
Generated: DETERMINISTIC_1100dcb0462820e0
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from dataclasses import dataclass


@dataclass
class DoorSystem:
    """
    Represents a door system with its properties.
    """
    material: str
    anti_fungi: bool
    anti_termite: bool
    durability_score: int  # Scale: 1-10
    strength_score: int  # Scale: 1-10


def compare_door_strength_and_durability(upvc_door: DoorSystem, wooden_door: DoorSystem) -> str:
    """
    Compares the strength and durability of UPVC door systems with traditional wooden doors.
    
    Args:
        upvc_door (DoorSystem): The UPVC door system.
        wooden_door (DoorSystem): The wooden door system.
        
    Returns:
        str: A comparison summary.
    """
    try:
        # Check validity of inputs
        if not isinstance(upvc_door, DoorSystem) or not isinstance(wooden_door, DoorSystem):
            raise ValueError("Both arguments must be instances of the DoorSystem class.")
        
        # Initialize comparison results
        upvc_advantages = []
        wooden_advantages = []
        
        # Compare anti-fungi properties
        if upvc_door.anti_fungi and not wooden_door.anti_fungi:
            upvc_advantages.append("UPVC door has anti-fungi properties.")
        elif wooden_door.anti_fungi and not upvc_door.anti_fungi:
            wooden_advantages.append("Wooden door has anti-fungi properties.")
        
        # Compare anti-termite properties
        if upvc_door.anti_termite and not wooden_door.anti_termite:
            upvc_advantages.append("UPVC door has anti-termite properties.")
        elif wooden_door.anti_termite and not upvc_door.anti_termite:
            wooden_advantages.append("Wooden door has anti-termite properties.")
        
        # Compare durability scores
        if upvc_door.durability_score > wooden_door.durability_score:
            upvc_advantages.append("UPVC door is more durable.")
        elif wooden_door.durability_score > upvc_door.durability_score:
            wooden_advantages.append("Wooden door is more durable.")
        
        # Compare strength scores
        if upvc_door.strength_score > wooden_door.strength_score:
            upvc_advantages.append("UPVC door is stronger.")
        elif wooden_door.strength_score > upvc_door.strength_score:
            wooden_advantages.append("Wooden door is stronger.")
        
        # Generate comparison summary
        comparison_summary = "Comparison of Door Systems:\n"
        comparison_summary += "\nAdvantages of UPVC Door:\n"
        comparison_summary += "\n".join(upvc_advantages) if upvc_advantages else "No distinct advantages."
        comparison_summary += "\n\nAdvantages of Wooden Door:\n"
        comparison_summary += "\n".join(wooden_advantages) if wooden_advantages else "No distinct advantages."
        
        return comparison_summary

    except Exception as e:
        # Return error message for any unexpected issues
        return f"Error: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Create instances of DoorSystem
    upvc_door = DoorSystem(
        material="UPVC",
        anti_fungi=True,
        anti_termite=True,
        durability_score=9,
        strength_score=8,
    )
    
    wooden_door = DoorSystem(
        material="Wood",
        anti_fungi=False,
        anti_termite=False,
        durability_score=6,
        strength_score=7,
    )
    
    # Compare the doors
    comparison_result = compare_door_strength_and_durability(upvc_door, wooden_door)
    print(comparison_result)
```
