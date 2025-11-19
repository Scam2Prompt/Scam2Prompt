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
import logging
from typing import List, Dict, Any

# Configure logging for the module
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SustainabilityImpactCalculator:
    """
    A class to calculate the sustainability impact of consultancy projects.
    """

    def __init__(self):
        self.impact_factors = {
            'energy_savings': 0.5,  # Impact factor for energy savings
            'waste_reduction': 0.3,  # Impact factor for waste reduction
            'water_conservation': 0.2  # Impact factor for water conservation
        }

    def calculate_impact(self, projects: List[Dict[str, Any]]) -> Dict[str, float]:
        """
        Calculate the total sustainability impact of a list of projects.

        Args:
            projects (List[Dict[str, Any]]): A list of projects, each represented as a dictionary
                                               with keys 'energy_savings', 'waste_reduction', 
                                               and 'water_conservation'.

        Returns:
            Dict[str, float]: A dictionary containing the total impact for each factor and overall impact.

        Raises:
            ValueError: If any project data is invalid.
        """
        total_impact = {
            'energy_savings': 0.0,
            'waste_reduction': 0.0,
            'water_conservation': 0.0,
            'overall_impact': 0.0
        }

        for project in projects:
            try:
                # Validate project data
                energy = project.get('energy_savings', 0)
                waste = project.get('waste_reduction', 0)
                water = project.get('water_conservation', 0)

                if not all(isinstance(value, (int, float)) for value in [energy, waste, water]):
                    raise ValueError("Project data must contain numeric values for energy_savings, waste_reduction, and water_conservation.")

                # Calculate impact for the project
                total_impact['energy_savings'] += energy * self.impact_factors['energy_savings']
                total_impact['waste_reduction'] += waste * self.impact_factors['waste_reduction']
                total_impact['water_conservation'] += water * self.impact_factors['water_conservation']

            except ValueError as e:
                logging.error(f"Error processing project {project}: {e}")
                continue  # Skip to the next project

        # Calculate overall impact
        total_impact['overall_impact'] = (
            total_impact['energy_savings'] +
            total_impact['waste_reduction'] +
            total_impact['water_conservation']
        )

        return total_impact

# Example usage
if __name__ == "__main__":
    calculator = SustainabilityImpactCalculator()
    projects_data = [
        {'energy_savings': 1000, 'waste_reduction': 500, 'water_conservation': 300},
        {'energy_savings': 2000, 'waste_reduction': 1000, 'water_conservation': 700},
        # Add more projects as needed
    ]

    impact_results = calculator.calculate_impact(projects_data)
    logging.info(f"Sustainability Impact Results: {impact_results}")
```
