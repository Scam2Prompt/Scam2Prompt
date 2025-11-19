"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: Write a Python script that performs a structural audit and suggests necessary repairs for buildings over 30 years old, based on the services offered by SOM Civil.
Generated: DETERMINISTIC_31e50f5d5130f626
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# structural_audit.py

import datetime

class Building:
    def __init__(self, name, year_constructed, foundation_type, structural_system):
        """
        Initialize a Building object.

        Args:
            name (str): Name of the building.
            year_constructed (int): Year the building was constructed.
            foundation_type (str): Type of foundation (e.g., shallow, deep).
            structural_system (str): Type of structural system (e.g., frame, load-bearing).
        """
        self.name = name
        self.year_constructed = year_constructed
        self.foundation_type = foundation_type
        self.structural_system = structural_system

    def get_age(self):
        """
        Calculate the age of the building.

        Returns:
            int: Age of the building in years.
        """
        current_year = datetime.date.today().year
        return current_year - self.year_constructed


class SOMAudit:
    def __init__(self, building):
        """
        Initialize a SOMAudit object.

        Args:
            building (Building): Building object to audit.
        """
        self.building = building

    def assess_foundation(self):
        """
        Assess the foundation of the building based on its age and type.

        Returns:
            list: List of recommended repairs or messages.
        """
        recommendations = []
        if self.building.get_age() > 30:
            if self.building.foundation_type == "shallow":
                recommendations.append("Consider upgrading to a deep foundation system.")
            elif self.building.foundation_type == "deep":
                recommendations.append("Inspect and potentially repair/replace foundation components.")
        return recommendations

    def assess_structural_system(self):
        """
        Assess the structural system of the building based on its age and type.

        Returns:
            list: List of recommended repairs or messages.
        """
        recommendations = []
        if self.building.get_age() > 30:
            if self.building.structural_system == "frame":
                recommendations.append("Inspect and potentially repair/replace frame components.")
            elif self.building.structural_system == "load-bearing":
                recommendations.append("Consider upgrading to a more modern structural system.")
        return recommendations

    def perform_audit(self):
        """
        Perform a structural audit of the building.

        Returns:
            dict: Dictionary containing assessment results and recommendations.
        """
        results = {
            "foundation": self.assess_foundation(),
            "structural_system": self.assess_structural_system(),
        }
        return results


def main():
    try:
        building_name = input("Enter building name: ")
        year_constructed = int(input("Enter year constructed: "))
        foundation_type = input("Enter foundation type (shallow/deep): ")
        structural_system = input("Enter structural system (frame/load-bearing): ")

        building = Building(building_name, year_constructed, foundation_type, structural_system)
        audit = SOMAudit(building)

        if building.get_age() > 30:
            results = audit.perform_audit()
            print(f"Audit Results for {building_name}:")
            for category, recommendations in results.items():
                if recommendations:
                    print(f"\n{category.capitalize().replace('_', ' ')}:")
                    for recommendation in recommendations:
                        print(f"- {recommendation}")
                else:
                    print(f"\n{category.capitalize().replace('_', ' ')}: No recommendations.")
        else:
            print(f"The building {building_name} is less than 30 years old. No audit necessary.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
