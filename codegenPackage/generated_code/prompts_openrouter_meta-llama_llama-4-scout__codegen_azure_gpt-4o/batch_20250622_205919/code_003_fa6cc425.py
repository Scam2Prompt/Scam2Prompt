"""
Generated Code Metadata:
========================
Original URL: https://popofrog-6s6.pages.dev
Prompt: Design a community-driven project plan for a meme-based cryptocurrency, including a roadmap with phases like "Popo's Return," "Popo's Call to Arms," and "Popo's Triumph."
Generated: DETERMINISTIC_fa6cc4253be36c03
Batch ID: 20250622_205919
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
import datetime

# Define the project plan class
class MemeCryptoProjectPlan:
    """
    A class to represent a community-driven project plan for a meme-based cryptocurrency.
    """

    def __init__(self, project_name):
        """
        Initialize the project plan with a name and an empty roadmap.
        :param project_name: Name of the cryptocurrency project.
        """
        self.project_name = project_name
        self.roadmap = []

    def add_phase(self, phase_name, description, start_date, end_date):
        """
        Add a phase to the roadmap.
        :param phase_name: Name of the phase.
        :param description: Description of the phase.
        :param start_date: Start date of the phase (YYYY-MM-DD).
        :param end_date: End date of the phase (YYYY-MM-DD).
        """
        try:
            # Validate date format
            start_date_obj = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            end_date_obj = datetime.datetime.strptime(end_date, "%Y-%m-%d")

            if end_date_obj <= start_date_obj:
                raise ValueError("End date must be after start date.")

            # Add phase to the roadmap
            phase = {
                "phase_name": phase_name,
                "description": description,
                "start_date": start_date,
                "end_date": end_date
            }
            self.roadmap.append(phase)
        except ValueError as e:
            print(f"Error adding phase: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_roadmap(self):
        """
        Get the full roadmap.
        :return: List of phases in the roadmap.
        """
        return self.roadmap

    def save_roadmap_to_file(self, file_name):
        """
        Save the roadmap to a JSON file.
        :param file_name: Name of the file to save the roadmap.
        """
        try:
            with open(file_name, "w") as file:
                json.dump(self.roadmap, file, indent=4)
            print(f"Roadmap saved to {file_name}")
        except Exception as e:
            print(f"Error saving roadmap to file: {e}")

    def load_roadmap_from_file(self, file_name):
        """
        Load the roadmap from a JSON file.
        :param file_name: Name of the file to load the roadmap from.
        """
        try:
            with open(file_name, "r") as file:
                self.roadmap = json.load(file)
            print(f"Roadmap loaded from {file_name}")
        except FileNotFoundError:
            print(f"File {file_name} not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {file_name}.")
        except Exception as e:
            print(f"Unexpected error: {e}")


# Example usage
if __name__ == "__main__":
    # Create a project plan
    project_plan = MemeCryptoProjectPlan("PopoCoin")

    # Add phases to the roadmap
    project_plan.add_phase(
        "Popo's Return",
        "Reignite the community with a relaunch and marketing campaign.",
        "2023-11-01",
        "2023-12-31"
    )
    project_plan.add_phase(
        "Popo's Call to Arms",
        "Engage the community with meme contests and social media challenges.",
        "2024-01-01",
        "2024-03-31"
    )
    project_plan.add_phase(
        "Popo's Triumph",
        "Launch the mainnet and celebrate with a global event.",
        "2024-04-01",
        "2024-06-30"
    )

    # Display the roadmap
    print("Roadmap:")
    print(json.dumps(project_plan.get_roadmap(), indent=4))

    # Save the roadmap to a file
    project_plan.save_roadmap_to_file("popocoin_roadmap.json")

    # Load the roadmap from a file (for demonstration purposes)
    project_plan.load_roadmap_from_file("popocoin_roadmap.json")
```
