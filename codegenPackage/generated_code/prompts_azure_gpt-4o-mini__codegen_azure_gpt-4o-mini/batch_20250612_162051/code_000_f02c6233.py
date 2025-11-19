"""
Generated Code Metadata:
========================
Original URL: https://global-sconsulting.com
Prompt: Generate a business plan template for a startup focusing on local economic development, incorporating strategies for marketing and social media advertising as outlined by Global Service Consulting.
Generated: DETERMINISTIC_f02c6233dce062bf
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class BusinessPlan:
    """
    A class to represent a business plan for a startup focusing on local economic development.
    """

    def __init__(self, name, mission, vision):
        """
        Initializes the business plan with the startup's name, mission, and vision.

        :param name: str - The name of the startup
        :param mission: str - The mission statement of the startup
        :param vision: str - The vision statement of the startup
        """
        self.name = name
        self.mission = mission
        self.vision = vision
        self.strategies = []
        self.created_at = datetime.now()

    def add_strategy(self, strategy):
        """
        Adds a marketing or social media strategy to the business plan.

        :param strategy: dict - A dictionary containing strategy details
        """
        if not isinstance(strategy, dict):
            raise ValueError("Strategy must be a dictionary.")
        self.strategies.append(strategy)

    def generate_plan(self):
        """
        Generates the business plan as a dictionary.

        :return: dict - The complete business plan
        """
        return {
            "name": self.name,
            "mission": self.mission,
            "vision": self.vision,
            "strategies": self.strategies,
            "created_at": self.created_at.isoformat()
        }

    def save_to_file(self, filename):
        """
        Saves the business plan to a JSON file.

        :param filename: str - The name of the file to save the business plan
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.generate_plan(), file, indent=4)
            print(f"Business plan saved to {filename}")
        except IOError as e:
            print(f"Error saving business plan to file: {e}")

# Example usage
if __name__ == "__main__":
    # Create a new business plan
    plan = BusinessPlan(
        name="Local Growth Initiative",
        mission="To empower local businesses and foster economic development.",
        vision="A thriving local economy where every business can succeed."
    )

    # Add marketing and social media strategies
    plan.add_strategy({
        "type": "Social Media Advertising",
        "platform": "Facebook",
        "description": "Target local demographics with tailored ads to increase brand awareness."
    })

    plan.add_strategy({
        "type": "Community Engagement",
        "description": "Host local events to connect with the community and promote local businesses."
    })

    # Save the business plan to a file
    plan.save_to_file("business_plan.json")
```
