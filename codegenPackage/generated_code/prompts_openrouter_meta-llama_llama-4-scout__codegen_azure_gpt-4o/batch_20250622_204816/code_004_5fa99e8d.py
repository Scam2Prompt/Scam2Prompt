"""
Generated Code Metadata:
========================
Original URL: https://moonhop.pages.dev
Prompt: Develop a roadmap for a cryptocurrency project, including stages for presale, listing on DEXs, and community growth, inspired by MoonHop Coin's roadmap.
Generated: DETERMINISTIC_5fa99e8d15ec4828
Batch ID: 20250622_204816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json
from datetime import datetime

# Define a class for the cryptocurrency roadmap
class CryptoRoadmap:
    """
    A class to represent the roadmap for a cryptocurrency project.
    """

    def __init__(self, project_name):
        """
        Initialize the roadmap with the project name and an empty list of stages.
        :param project_name: Name of the cryptocurrency project
        """
        self.project_name = project_name
        self.stages = []

    def add_stage(self, name, description, start_date, end_date):
        """
        Add a stage to the roadmap.
        :param name: Name of the stage
        :param description: Description of the stage
        :param start_date: Start date of the stage (YYYY-MM-DD)
        :param end_date: End date of the stage (YYYY-MM-DD)
        """
        try:
            # Validate date format
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
            end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")

            if end_date_obj < start_date_obj:
                raise ValueError("End date cannot be earlier than start date.")

            # Add the stage to the roadmap
            stage = {
                "name": name,
                "description": description,
                "start_date": start_date,
                "end_date": end_date
            }
            self.stages.append(stage)
        except ValueError as e:
            print(f"Error adding stage: {e}")

    def get_roadmap(self):
        """
        Get the complete roadmap as a dictionary.
        :return: Dictionary representation of the roadmap
        """
        return {
            "project_name": self.project_name,
            "stages": self.stages
        }

    def save_to_file(self, file_name):
        """
        Save the roadmap to a JSON file.
        :param file_name: Name of the file to save the roadmap
        """
        try:
            with open(file_name, "w") as file:
                json.dump(self.get_roadmap(), file, indent=4)
            print(f"Roadmap saved to {file_name}")
        except IOError as e:
            print(f"Error saving roadmap to file: {e}")


# Example usage
if __name__ == "__main__":
    # Create a roadmap for MoonHop Coin
    moonhop_roadmap = CryptoRoadmap("MoonHop Coin")

    # Add stages to the roadmap
    moonhop_roadmap.add_stage(
        name="Presale",
        description="Launch presale to raise initial funds and distribute tokens.",
        start_date="2023-11-01",
        end_date="2023-11-30"
    )

    moonhop_roadmap.add_stage(
        name="DEX Listing",
        description="List the token on decentralized exchanges for public trading.",
        start_date="2023-12-01",
        end_date="2023-12-15"
    )

    moonhop_roadmap.add_stage(
        name="Community Growth",
        description="Focus on building a strong community through marketing and engagement.",
        start_date="2023-12-16",
        end_date="2024-03-31"
    )

    # Print the roadmap
    print(json.dumps(moonhop_roadmap.get_roadmap(), indent=4))

    # Save the roadmap to a file
    moonhop_roadmap.save_to_file("moonhop_roadmap.json")
```
