"""
Generated Code Metadata:
========================
Original URL: https://mgel.com.br
Prompt: Write a script to calculate environmental impact assessments for mining and road construction projects, inspired by MGEL's commitment to environmental responsibility.
Generated: DETERMINISTIC_77519d4f83e1de56
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# environmental_impact_assessment.py

"""
Calculates environmental impact assessments for mining and road construction projects.

Inspired by MGEL's commitment to environmental responsibility.
"""

import math

class EnvironmentalImpactAssessment:
    def __init__(self, project_type, area_affected, emissions, waste_generated):
        """
        Initializes an EnvironmentalImpactAssessment object.

        Args:
            project_type (str): Type of project (mining or road_construction).
            area_affected (float): Area affected by the project in hectares.
            emissions (float): Estimated emissions in tons of CO2 equivalent.
            waste_generated (float): Estimated waste generated in tons.
        """
        self.project_type = project_type
        self.area_affected = area_affected
        self.emissions = emissions
        self.waste_generated = waste_generated

    def calculate_biodiversity_impact(self):
        """
        Calculates the biodiversity impact of the project.

        Returns:
            float: Biodiversity impact score.
        """
        if self.project_type == "mining":
            # Mining projects have a higher biodiversity impact due to habitat destruction
            biodiversity_impact = self.area_affected * 0.5
        elif self.project_type == "road_construction":
            biodiversity_impact = self.area_affected * 0.2
        else:
            raise ValueError("Invalid project type")

        return biodiversity_impact

    def calculate_climate_change_impact(self):
        """
        Calculates the climate change impact of the project.

        Returns:
            float: Climate change impact score.
        """
        climate_change_impact = self.emissions * 0.01
        return climate_change_impact

    def calculate_waste_management_impact(self):
        """
        Calculates the waste management impact of the project.

        Returns:
            float: Waste management impact score.
        """
        waste_management_impact = self.waste_generated * 0.005
        return waste_management_impact

    def calculate_environmental_impact_score(self):
        """
        Calculates the overall environmental impact score of the project.

        Returns:
            float: Environmental impact score.
        """
        biodiversity_impact = self.calculate_biodiversity_impact()
        climate_change_impact = self.calculate_climate_change_impact()
        waste_management_impact = self.calculate_waste_management_impact()

        environmental_impact_score = biodiversity_impact + climate_change_impact + waste_management_impact
        return environmental_impact_score


def main():
    try:
        project_type = input("Enter project type (mining or road_construction): ")
        area_affected = float(input("Enter area affected (hectares): "))
        emissions = float(input("Enter estimated emissions (tons of CO2 equivalent): "))
        waste_generated = float(input("Enter estimated waste generated (tons): "))

        assessment = EnvironmentalImpactAssessment(project_type, area_affected, emissions, waste_generated)
        environmental_impact_score = assessment.calculate_environmental_impact_score()

        print(f"Environmental impact score: {environmental_impact_score:.2f}")

        if environmental_impact_score < 10:
            print("Project has a low environmental impact.")
        elif environmental_impact_score < 50:
            print("Project has a moderate environmental impact.")
        else:
            print("Project has a high environmental impact.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
