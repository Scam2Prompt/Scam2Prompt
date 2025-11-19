"""
Generated Code Metadata:
========================
Original URL: https://bulldogito.pages.dev
Prompt: Create a roadmap for a cryptocurrency project like Bulldogito Coin that includes phases for token development, marketing, and global expansion of real-world assets.
Generated: DETERMINISTIC_bdac7f162a2638a3
Batch ID: 20250622_211533
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CryptoProjectRoadmap:
    """
    A class to represent the roadmap for a cryptocurrency project.
    """

    def __init__(self, project_name):
        """
        Initializes the roadmap with the project name and an empty list of phases.

        :param project_name: Name of the cryptocurrency project
        """
        self.project_name = project_name
        self.phases = []

    def add_phase(self, phase_name, description, start_date, end_date):
        """
        Adds a new phase to the roadmap.

        :param phase_name: Name of the phase
        :param description: Description of the phase
        :param start_date: Start date of the phase (YYYY-MM-DD)
        :param end_date: End date of the phase (YYYY-MM-DD)
        """
        try:
            phase = {
                'phase_name': phase_name,
                'description': description,
                'start_date': start_date,
                'end_date': end_date
            }
            self.phases.append(phase)
        except Exception as e:
            print(f"Error adding phase: {e}")

    def display_roadmap(self):
        """
        Displays the complete roadmap with all phases.
        """
        print(f"Roadmap for {self.project_name}:")
        for phase in self.phases:
            print(f"Phase: {phase['phase_name']}")
            print(f"  Description: {phase['description']}")
            print(f"  Start Date: {phase['start_date']}")
            print(f"  End Date: {phase['end_date']}")
            print("-" * 40)

    def save_roadmap(self, filename):
        """
        Saves the roadmap to a file in JSON format.

        :param filename: Name of the file to save the roadmap
        """
        import json
        try:
            with open(filename, 'w') as file:
                json.dump(self.phases, file, indent=4)
            print(f"Roadmap saved to {filename}")
        except IOError as e:
            print(f"Error saving roadmap: {e}")

# Example usage
if __name__ == "__main__":
    # Create a new cryptocurrency project roadmap
    project = CryptoProjectRoadmap("Bulldogito Coin")

    # Add phases to the roadmap
    project.add_phase(
        phase_name="Token Development",
        description="Develop the token smart contract and conduct audits.",
        start_date="2023-01-01",
        end_date="2023-03-31"
    )
    project.add_phase(
        phase_name="Marketing Campaign",
        description="Launch marketing campaigns to build community and awareness.",
        start_date="2023-04-01",
        end_date="2023-06-30"
    )
    project.add_phase(
        phase_name="Global Expansion",
        description="Expand the use of the token in real-world assets and partnerships.",
        start_date="2023-07-01",
        end_date="2023-12-31"
    )

    # Display the roadmap
    project.display_roadmap()

    # Save the roadmap to a file
    project.save_roadmap("bulldogito_coin_roadmap.json")
```
