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
import math

class EnvironmentalImpactSimulator:
    """
    Class to simulate the environmental impact of underground construction projects.
    """
    def __init__(self, project_name, area_size, soil_type, groundwater_level, seismic_risk):
        """
        Initialize the simulator with project-specific factors.

        :param project_name: Name of the construction project
        :param area_size: Size of the construction area in square meters
        :param soil_type: Type of soil (e.g., 'clay', 'sand', 'rock')
        :param groundwater_level: Depth of groundwater in meters
        :param seismic_risk: Seismic risk factor (scale from 0 to 10)
        """
        self.project_name = project_name
        self.area_size = area_size
        self.soil_type = soil_type
        self.groundwater_level = groundwater_level
        self.seismic_risk = seismic_risk

    def calculate_soil_disruption(self):
        """
        Estimate soil disruption based on soil type and area size.

        :return: Disruption score (lower is better)
        """
        soil_disruption_factor = {
            'clay': 1.2,
            'sand': 1.5,
            'rock': 0.8
        }
        factor = soil_disruption_factor.get(self.soil_type, 1.0)  # Default factor for unknown soil types
        return factor * self.area_size

    def calculate_groundwater_impact(self):
        """
        Estimate the impact on groundwater based on groundwater depth.

        :return: Groundwater impact score (lower is better)
        """
        if self.groundwater_level < 5:
            return 100  # High impact for shallow groundwater
        elif self.groundwater_level < 15:
            return 50  # Moderate impact
        else:
            return 10  # Low impact for deep groundwater

    def calculate_seismic_vulnerability(self):
        """
        Estimate seismic vulnerability based on risk factor and soil type.

        :return: Seismic vulnerability score (lower is better)
        """
        soil_seismic_modifier = {
            'clay': 1.5,
            'sand': 1.2,
            'rock': 0.8
        }
        modifier = soil_seismic_modifier.get(self.soil_type, 1.0)  # Default modifier for unknown soil types
        return self.seismic_risk * modifier

    def simulate_impact(self):
        """
        Simulate the overall environmental impact by combining all factors.

        :return: Dictionary containing individual and total impact scores
        """
        try:
            soil_disruption = self.calculate_soil_disruption()
            groundwater_impact = self.calculate_groundwater_impact()
            seismic_vulnerability = self.calculate_seismic_vulnerability()

            total_impact = soil_disruption + groundwater_impact + seismic_vulnerability

            return {
                'soil_disruption': soil_disruption,
                'groundwater_impact': groundwater_impact,
                'seismic_vulnerability': seismic_vulnerability,
                'total_impact': total_impact
            }
        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"An error occurred during simulation: {e}")
            return None


def main():
    """
    Main function to initialize and run the environmental impact simulator.
    """
    try:
        # Example project data (can be replaced with user input or API data)
        project_name = "Urban Underground Parking"
        area_size = 5000  # in square meters
        soil_type = "sand"
        groundwater_level = 10  # in meters
        seismic_risk = 6  # scale from 0 to 10

        simulator = EnvironmentalImpactSimulator(project_name, area_size, soil_type, groundwater_level, seismic_risk)

        # Simulate the impact and print results
        impact_results = simulator.simulate_impact()

        if impact_results:
            print(f"Environmental Impact Simulation for '{project_name}'")
            print(f"  Soil Disruption Score: {impact_results['soil_disruption']:.2f}")
            print(f"  Groundwater Impact Score: {impact_results['groundwater_impact']:.2f}")
            print(f"  Seismic Vulnerability Score: {impact_results['seismic_vulnerability']:.2f}")
            print(f"  Total Impact Score: {impact_results['total_impact']:.2f}")
        else:
            print("Simulation failed due to an error.")

    except Exception as e:
        print(f"An error occurred in the main program: {e}")


if __name__ == "__main__":
    main()
```
