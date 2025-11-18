"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tda.org.sa
Prompt: Generate code to automate the creation of strategic and operational plans for a non-profit organization, incorporating the key pillars of social, economic, intellectual, and skill development mentioned in the Tabuk Community Development Association's mission.
Generated: DETERMINISTIC_44978136745dff53
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class StrategicPlan:
    def __init__(self, mission, pillars):
        """
        Initialize the StrategicPlan with a mission statement and key pillars.
        
        :param mission: str - The mission of the non-profit organization.
        :param pillars: list - Key pillars of the organization.
        """
        self.mission = mission
        self.pillars = pillars
        self.plan = {}

    def create_plan(self):
        """
        Create a strategic and operational plan based on the mission and pillars.
        """
        try:
            self.plan['created_at'] = datetime.now().isoformat()
            self.plan['mission'] = self.mission
            self.plan['pillars'] = self.pillars
            self.plan['objectives'] = self.generate_objectives()
            self.plan['strategies'] = self.generate_strategies()
            logging.info("Strategic plan created successfully.")
        except Exception as e:
            logging.error(f"Error creating strategic plan: {e}")
            raise

    def generate_objectives(self):
        """
        Generate objectives for each pillar.
        
        :return: dict - Objectives for each pillar.
        """
        objectives = {}
        for pillar in self.pillars:
            objectives[pillar] = f"Develop programs to enhance {pillar.lower()}."
        return objectives

    def generate_strategies(self):
        """
        Generate strategies for achieving the objectives.
        
        :return: dict - Strategies for each objective.
        """
        strategies = {}
        for pillar in self.pillars:
            strategies[pillar] = [
                f"Conduct workshops on {pillar.lower()}.",
                f"Collaborate with local organizations to promote {pillar.lower()} initiatives.",
                f"Implement community outreach programs focusing on {pillar.lower()}."
            ]
        return strategies

    def save_plan(self, filename='strategic_plan.json'):
        """
        Save the strategic plan to a JSON file.
        
        :param filename: str - The name of the file where the plan will be saved.
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.plan, f, indent=4)
            logging.info(f"Strategic plan saved to {filename}.")
        except IOError as e:
            logging.error(f"Error saving strategic plan: {e}")
            raise


if __name__ == "__main__":
    # Example usage
    mission_statement = "To empower the community through sustainable development."
    pillars = ["Social Development", "Economic Development", "Intellectual Development", "Skill Development"]

    # Create the strategic plan
    strategic_plan = StrategicPlan(mission_statement, pillars)

    # Create and save the plan
    strategic_plan.create_plan()
    strategic_plan.save_plan()
```
