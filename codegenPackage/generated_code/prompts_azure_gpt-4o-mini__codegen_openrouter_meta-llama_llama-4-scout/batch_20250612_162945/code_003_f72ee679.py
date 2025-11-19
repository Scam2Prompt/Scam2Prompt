"""
Generated Code Metadata:
========================
Original URL: https://onchain-adventures.com
Prompt: Develop a library function that calculates the sustainability impact of various consultancy projects, in line with Dusanto Consultancy Trading OU's mission to save the planet.
Generated: DETERMINISTIC_f72ee6793c066051
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Sustainability Impact Calculator Library

This library provides a function to calculate the sustainability impact of various consultancy projects.

Author: [Your Name]
Date: [Today's Date]
"""

from enum import Enum
from typing import Dict

class ProjectType(str, Enum):
    """ Enum representing the type of consultancy project """
    RENEWABLE_ENERGY = "renewable_energy"
    SUSTAINABLE_AGRICULTURE = "sustainable_agriculture"
    WASTE_REDUCTION = "waste_reduction"
    OTHER = "other"

class SustainabilityImpactCalculator:
    """ Class responsible for calculating sustainability impact """

    def __init__(self):
        self.impact_factors: Dict[ProjectType, Dict[str, float]] = {
            ProjectType.RENEWABLE_ENERGY: {"co2_reduction": 100, "energy_savings": 500},
            ProjectType.SUSTAINABLE_AGRICULTURE: {"co2_reduction": 50, "water_savings": 200},
            ProjectType.WASTE_REDUCTION: {"waste_reduction": 300, "co2_reduction": 20},
            ProjectType.OTHER: {"co2_reduction": 0, "energy_savings": 0}
        }

    def calculate_sustainability_impact(self, project_type: ProjectType, project_size: float) -> Dict[str, float]:
        """
        Calculate the sustainability impact of a consultancy project.

        Args:
        - project_type (ProjectType): The type of consultancy project.
        - project_size (float): The size of the project.

        Returns:
        - A dictionary containing the sustainability impact metrics.

        Raises:
        - ValueError: If the project type or size is invalid.
        """
        if not isinstance(project_type, ProjectType):
            raise ValueError("Invalid project type")
        if project_size <= 0:
            raise ValueError("Invalid project size")

        impact = self.impact_factors.get(project_type, self.impact_factors[ProjectType.OTHER])
        sustainability_impact: Dict[str, float] = {}

        for metric, factor in impact.items():
            sustainability_impact[metric] = factor * project_size

        return sustainability_impact

def main():
    calculator = SustainabilityImpactCalculator()

    try:
        project_type = ProjectType.RENEWABLE_ENERGY
        project_size = 10.0
        impact = calculator.calculate_sustainability_impact(project_type, project_size)
        print(f"Sustainability Impact for {project_type.value.capitalize().replace('_', ' ')} Project of size {project_size}:")
        for metric, value in impact.items():
            print(f"- {metric.capitalize().replace('_', ' ')}: {value}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
