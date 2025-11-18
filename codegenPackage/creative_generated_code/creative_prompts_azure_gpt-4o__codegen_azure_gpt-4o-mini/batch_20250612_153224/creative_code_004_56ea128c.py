"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uranpres.sk
Prompt: Create a Python program to simulate the environmental impact of underground construction projects, incorporating geological and geotechnical factors similar to those handled by URANPRES.
Generated: DETERMINISTIC_56ea128cfcc734bd
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json
import logging

# Configure logging to output debug information
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class GeologicalFactor:
    def __init__(self, name, impact_score):
        """
        Initializes a geological factor with its name and impact score.
        :param name: Name of the geological factor.
        :param impact_score: Impact score of the factor (scale 1-10).
        """
        self.name = name
        self.impact_score = impact_score

    def __str__(self):
        return f"{self.name}: {self.impact_score}"


class ConstructionProject:
    def __init__(self, project_name):
        """
        Initializes a construction project with a name and a list of geological factors.
        :param project_name: Name of the construction project.
        """
        self.project_name = project_name
        self.geological_factors = []

    def add_geological_factor(self, factor):
        """
        Adds a geological factor to the project.
        :param factor: A GeologicalFactor object to add.
        """
        if not isinstance(factor, GeologicalFactor):
            logging.error("Attempted to add a non-GeologicalFactor object.")
            raise ValueError("factor must be an instance of GeologicalFactor")
        self.geological_factors.append(factor)
        logging.info(f"Added geological factor: {factor}")

    def calculate_environmental_impact(self):
        """
        Calculates the total environmental impact score based on geological factors.
        :return: Total environmental impact score.
        """
        total_impact = sum(factor.impact_score for factor in self.geological_factors)
        logging.debug(f"Total environmental impact calculated: {total_impact}")
        return total_impact

    def simulate_project(self):
        """
        Simulates the project by generating random geological factors and calculating the impact.
        """
        # Simulate the addition of geological factors
        for _ in range(random.randint(1, 5)):  # Add between 1 to 5 factors
            factor_name = f"Geological Factor {random.randint(1, 100)}"
            impact_score = random.randint(1, 10)  # Impact score between 1 and 10
            self.add_geological_factor(GeologicalFactor(factor_name, impact_score))
        
        # Calculate and return the environmental impact
        total_impact = self.calculate_environmental_impact()
        logging.info(f"Total environmental impact for project '{self.project_name}': {total_impact}")
        return total_impact


def main():
    """
    Main function to run the underground construction project simulation.
    """
    try:
        project_name = "Underground Infrastructure Development"
        project = ConstructionProject(project_name)
        total_impact = project.simulate_project()

        # Save the project details and impact to a JSON file
        project_details = {
            "project_name": project.project_name,
            "total_impact": total_impact,
            "geological_factors": [str(factor) for factor in project.geological_factors]
        }

        with open(f"{project_name.replace(' ', '_')}_impact.json", 'w') as json_file:
            json.dump(project_details, json_file, indent=4)
            logging.info(f"Project details saved to {json_file.name}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
