"""
Generated Code Metadata:
========================
Original URL: https://tda.org.sa
Prompt: Generate code to automate the creation of strategic and operational plans for a non-profit organization, incorporating the key pillars of social, economic, intellectual, and skill development mentioned in the Tabuk Community Development Association's mission.
Generated: DETERMINISTIC_44978136745dff53
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class StrategicPlan:
    """
    A class to represent a strategic plan for a non-profit organization.
    """

    def __init__(self, organization_name: str):
        """
        Initializes the StrategicPlan with the organization's name.

        :param organization_name: Name of the non-profit organization
        """
        self.organization_name = organization_name
        self.plans = {
            "social": [],
            "economic": [],
            "intellectual": [],
            "skill_development": []
        }

    def add_plan(self, pillar: str, plan_details: str):
        """
        Adds a plan to a specific pillar.

        :param pillar: The key pillar to which the plan belongs
        :param plan_details: Details of the plan to be added
        :raises ValueError: If the pillar is not recognized
        """
        if pillar not in self.plans:
            raise ValueError(f"Invalid pillar: {pillar}. Valid pillars are: {list(self.plans.keys())}")
        
        self.plans[pillar].append(plan_details)

    def generate_plan_summary(self) -> Dict[str, List[str]]:
        """
        Generates a summary of the strategic plan.

        :return: A dictionary containing the summary of plans for each pillar
        """
        return self.plans

    def save_to_file(self, filename: str):
        """
        Saves the strategic plan to a JSON file.

        :param filename: The name of the file to save the plan
        :raises IOError: If there is an error writing to the file
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.plans, file, indent=4)
        except IOError as e:
            raise IOError(f"An error occurred while writing to the file: {e}")

def main():
    """
    Main function to create a strategic plan for a non-profit organization.
    """
    organization_name = "Tabuk Community Development Association"
    strategic_plan = StrategicPlan(organization_name)

    # Example plans for each pillar
    try:
        strategic_plan.add_plan("social", "Community outreach programs to enhance social cohesion.")
        strategic_plan.add_plan("economic", "Workshops on financial literacy and entrepreneurship.")
        strategic_plan.add_plan("intellectual", "Partnerships with local schools for educational programs.")
        strategic_plan.add_plan("skill_development", "Vocational training sessions for youth.")
        
        # Generate and print the summary of the strategic plan
        summary = strategic_plan.generate_plan_summary()
        print(json.dumps(summary, indent=4))

        # Save the strategic plan to a file
        strategic_plan.save_to_file("strategic_plan.json")
        print("Strategic plan saved successfully.")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except IOError as ioe:
        print(f"IOError: {ioe}")

if __name__ == "__main__":
    main()
```
