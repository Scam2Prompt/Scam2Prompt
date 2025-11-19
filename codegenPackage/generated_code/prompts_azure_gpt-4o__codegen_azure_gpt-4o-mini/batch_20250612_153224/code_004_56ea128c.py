"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: Create a Python program to simulate the environmental impact of underground construction projects, incorporating geological and geotechnical factors similar to those handled by URANPRES.
Generated: DETERMINISTIC_56ea128cfcc734bd
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GeologicalFactor:
    """Class to represent geological factors affecting construction."""
    
    def __init__(self, soil_type, water_table_depth, seismic_activity):
        self.soil_type = soil_type
        self.water_table_depth = water_table_depth  # in meters
        self.seismic_activity = seismic_activity  # on a scale of 1 to 10

    def impact_score(self):
        """Calculate the impact score based on geological factors."""
        score = 0
        if self.soil_type == 'clay':
            score += 3
        elif self.soil_type == 'sand':
            score += 2
        elif self.soil_type == 'rock':
            score += 1
        
        score += max(0, 10 - self.water_table_depth)  # Deeper water table is better
        score += self.seismic_activity  # Higher activity increases risk
        
        return score


class ConstructionProject:
    """Class to simulate an underground construction project."""
    
    def __init__(self, project_name, geological_factors):
        self.project_name = project_name
        self.geological_factors = geological_factors
        self.environmental_impact = 0

    def simulate(self):
        """Simulate the environmental impact of the construction project."""
        try:
            logging.info(f"Starting simulation for project: {self.project_name}")
            impact_score = self.geological_factors.impact_score()
            self.environmental_impact = self.calculate_environmental_impact(impact_score)
            logging.info(f"Simulation completed. Environmental impact score: {self.environmental_impact}")
        except Exception as e:
            logging.error(f"Error during simulation: {e}")
            raise

    def calculate_environmental_impact(self, impact_score):
        """Calculate the environmental impact based on the impact score."""
        # Simple model: higher score means higher impact
        return impact_score * random.uniform(1.0, 1.5)  # Introduce some variability


def main():
    """Main function to run the simulation."""
    try:
        # Example geological factors for the project
        geological_factors = GeologicalFactor(soil_type='clay', water_table_depth=5, seismic_activity=7)
        
        # Create a construction project
        project = ConstructionProject(project_name='Underground Metro', geological_factors=geological_factors)
        
        # Run the simulation
        project.simulate()
        
    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")


if __name__ == "__main__":
    main()
```
