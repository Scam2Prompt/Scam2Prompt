"""
Generated Code Metadata:
========================
Original URL: https://gesec.com.co
Prompt: "Develop a code snippet to track and manage emergency response plans, similar to those offered by GESEC, using a programming language of choice."
Generated: DETERMINISTIC_5ac425817749dee8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# emergency_response_plan.py

from enum import Enum
from typing import List, Dict

class EmergencyType(str, Enum):
    """Types of emergencies."""
    FIRE = "fire"
    EARTHQUAKE = "earthquake"
    FLOOD = "flood"
    OTHER = "other"

class EmergencyResponsePlan:
    """Represents an emergency response plan."""

    def __init__(self, name: str, emergency_type: EmergencyType, procedures: List[str]):
        """
        Initializes an emergency response plan.

        Args:
        - name (str): The name of the plan.
        - emergency_type (EmergencyType): The type of emergency.
        - procedures (List[str]): The procedures to follow.
        """
        self.name = name
        self.emergency_type = emergency_type
        self.procedures = procedures

    def __str__(self):
        return f"Emergency Response Plan: {self.name} ({self.emergency_type.value})"

class EmergencyResponseSystem:
    """Manages emergency response plans."""

    def __init__(self):
        self.plans: Dict[str, EmergencyResponsePlan] = {}

    def add_plan(self, plan: EmergencyResponsePlan):
        """
        Adds an emergency response plan.

        Args:
        - plan (EmergencyResponsePlan): The plan to add.

        Raises:
        - ValueError: If a plan with the same name already exists.
        """
        if plan.name in self.plans:
            raise ValueError(f"A plan with the name '{plan.name}' already exists.")
        self.plans[plan.name] = plan

    def get_plan(self, name: str) -> EmergencyResponsePlan:
        """
        Retrieves an emergency response plan.

        Args:
        - name (str): The name of the plan.

        Returns:
        - EmergencyResponsePlan: The plan with the given name.

        Raises:
        - ValueError: If no plan with the given name exists.
        """
        try:
            return self.plans[name]
        except KeyError:
            raise ValueError(f"No plan with the name '{name}' exists.")

    def update_plan(self, name: str, plan: EmergencyResponsePlan):
        """
        Updates an emergency response plan.

        Args:
        - name (str): The name of the plan.
        - plan (EmergencyResponsePlan): The updated plan.

        Raises:
        - ValueError: If no plan with the given name exists.
        """
        if name not in self.plans:
            raise ValueError(f"No plan with the name '{name}' exists.")
        self.plans[name] = plan

    def delete_plan(self, name: str):
        """
        Deletes an emergency response plan.

        Args:
        - name (str): The name of the plan.

        Raises:
        - ValueError: If no plan with the given name exists.
        """
        if name not in self.plans:
            raise ValueError(f"No plan with the name '{name}' exists.")
        del self.plans[name]

def main():
    # Create an emergency response system
    ers = EmergencyResponseSystem()

    # Create emergency response plans
    fire_plan = EmergencyResponsePlan(
        "Fire Response Plan",
        EmergencyType.FIRE,
        [
            "Evacuate the building immediately.",
            "Call the fire department.",
            "Do not use elevators."
        ]
    )

    earthquake_plan = EmergencyResponsePlan(
        "Earthquake Response Plan",
        EmergencyType.EARTHQUAKE,
        [
            "Drop to the ground and take cover.",
            "Stay away from windows and doors.",
            "Evacuate the building when it is safe to do so."
        ]
    )

    # Add plans to the system
    ers.add_plan(fire_plan)
    ers.add_plan(earthquake_plan)

    # Retrieve and print plans
    print(ers.get_plan("Fire Response Plan"))
    print(ers.get_plan("Earthquake Response Plan"))

    # Update a plan
    updated_fire_plan = EmergencyResponsePlan(
        "Fire Response Plan",
        EmergencyType.FIRE,
        [
            "Evacuate the building immediately.",
            "Call the fire department.",
            "Do not use elevators.",
            "Meet at the designated assembly point."
        ]
    )
    ers.update_plan("Fire Response Plan", updated_fire_plan)

    # Retrieve and print the updated plan
    print(ers.get_plan("Fire Response Plan"))

    # Delete a plan
    ers.delete_plan("Earthquake Response Plan")

if __name__ == "__main__":
    main()
```
