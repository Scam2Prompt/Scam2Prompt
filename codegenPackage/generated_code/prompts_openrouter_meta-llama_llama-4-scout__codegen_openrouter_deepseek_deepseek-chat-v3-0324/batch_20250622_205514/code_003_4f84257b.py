"""
Generated Code Metadata:
========================
Original URL: https://wonderplanet.ee
Prompt: "Generate a list of activities for a children's holiday party in Tallinn, including games and contests."
Generated: DETERMINISTIC_4f84257b8fa1d850
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Children's Holiday Party Activities Planner for Tallinn
This script generates a list of fun activities, games, and contests suitable
for a children's holiday party in Tallinn.
"""

from typing import List, Dict
import random

class PartyActivityGenerator:
    """
    Generates and manages activities for a children's holiday party.
    """
    
    def __init__(self):
        self.activities = {
            'indoor': [
                "Christmas ornament decorating",
                "Holiday card making station",
                "Pin the nose on the snowman",
                "Musical chairs with holiday music",
                "Snowball toss (with cotton balls)",
                "Holiday scavenger hunt",
                "Gingerbread house decorating contest",
                "Santa says (Simon says variation)",
                "Snowflake cutting competition",
                "Holiday charades"
            ],
            'outdoor': [
                "Snowman building contest",
                "Snowball target practice",
                "Winter treasure hunt",
                "Ice skating (if venue permits)",
                "Sledding race (if snow available)",
                "Holiday-themed relay race",
                "Outdoor holiday piñata",
                "Nature walk to collect winter decorations",
                "Snow painting with colored water",
                "Frozen bubble blowing"
            ],
            'contests': [
                "Best holiday costume contest",
                "Ugly sweater competition",
                "Holiday cookie decorating contest",
                "Most creative snow sculpture",
                "Fastest present wrapper",
                "Best holiday dance move",
                "Loudest holiday carol singer",
                "Most accurate snowball thrower",
                "Quickest to build a snowman",
                "Most festive face painting"
            ]
        }
        
        self.tallinn_specific = [
            "Tallinn Old Town scavenger hunt",
            "Estonian holiday tradition storytelling",
            "Learn basic Estonian holiday phrases",
            "Traditional Estonian cookie decorating",
            "Tallinn Christmas market visit (if nearby)"
        ]
    
    def generate_activity_plan(self, indoor: bool = True, outdoor: bool = True, 
                              contests: bool = True, include_tallinn: bool = True) -> Dict[str, List[str]]:
        """
        Generates a customized activity plan based on preferences.
        
        Args:
            indoor: Include indoor activities
            outdoor: Include outdoor activities
            contests: Include contests
            include_tallinn: Include Tallinn-specific activities
            
        Returns:
            Dictionary of activity categories with lists of activities
        """
        plan = {}
        
        if indoor:
            plan['indoor_activities'] = random.sample(self.activities['indoor'], 5)
        if outdoor:
            plan['outdoor_activities'] = random.sample(self.activities['outdoor'], 5)
        if contests:
            plan['contests'] = random.sample(self.activities['contests'], 3)
        if include_tallinn:
            plan['tallinn_special'] = random.sample(self.tallinn_specific, 2)
            
        return plan
    
    def print_activity_plan(self, plan: Dict[str, List[str]]) -> None:
        """
        Prints a formatted version of the activity plan.
        
        Args:
            plan: Activity plan dictionary
        """
        print("\n🎄 Children's Holiday Party Activities in Tallinn 🎄\n")
        
        for category, activities in plan.items():
            print(f"=== {category.replace('_', ' ').title()} ===")
            for i, activity in enumerate(activities, 1):
                print(f"{i}. {activity}")
            print()
    
    def validate_plan(self, plan: Dict[str, List[str]]) -> bool:
        """
        Validates that the plan has at least one activity.
        
        Args:
            plan: Activity plan dictionary
            
        Returns:
            bool: True if valid, False if empty
        """
        if not plan:
            return False
        return any(len(activities) > 0 for activities in plan.values())


# Example usage
if __name__ == "__main__":
    try:
        generator = PartyActivityGenerator()
        activity_plan = generator.generate_activity_plan()
        
        if generator.validate_plan(activity_plan):
            generator.print_activity_plan(activity_plan)
        else:
            print("Error: Could not generate a valid activity plan.")
    except Exception as e:
        print(f"An error occurred while generating activities: {str(e)}")
```
