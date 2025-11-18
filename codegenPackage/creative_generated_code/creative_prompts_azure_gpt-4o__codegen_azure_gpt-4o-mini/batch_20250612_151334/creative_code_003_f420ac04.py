"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecpowerlightingltd.com
Prompt: Create a script to calculate energy efficiency for street lighting projects, incorporating the innovative approach described by E.C. Power & Lighting Ltd.
Generated: DETERMINISTIC_f420ac04818cbb4a
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging to capture errors and info for debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class StreetLightingEfficiencyCalculator:
    """
    A class to calculate energy efficiency for street lighting projects.
    """

    def __init__(self, project_data):
        """
        Initializes the calculator with project data.

        Args:
            project_data (dict): A dictionary containing the project data.
        """
        self.project_data = project_data

    def calculate_energy_efficiency(self):
        """
        Calculates the energy efficiency for the street lighting project.

        Returns:
            dict: A dictionary containing efficiency metrics.
        """
        try:
            total_power_consumed = self.calculate_total_power_consumed()
            total_lumens_produced = self.calculate_total_lumens_produced()

            if total_power_consumed == 0:
                logging.warning("Total power consumed is 0, cannot calculate efficiency.")
                return {"efficiency": 0}

            efficiency = total_lumens_produced / total_power_consumed
            logging.info(f"Calculated efficiency: {efficiency}")

            return {
                "total_power_consumed": total_power_consumed,
                "total_lumens_produced": total_lumens_produced,
                "efficiency": efficiency
            }
        except Exception as e:
            logging.error(f"Error calculating energy efficiency: {e}")
            return {"error": str(e)}

    def calculate_total_power_consumed(self):
        """
        Calculates the total power consumed by the lighting system.

        Returns:
            float: Total power consumed in watts.
        """
        return sum(light['power'] for light in self.project_data.get('lights', []))

    def calculate_total_lumens_produced(self):
        """
        Calculates the total lumens produced by the lighting system.

        Returns:
            float: Total lumens produced.
        """
        return sum(light['lumens'] for light in self.project_data.get('lights', []))

def load_project_data(file_path):
    """
    Loads project data from a JSON file.

    Args:
        file_path (str): Path to the JSON file containing project data.

    Returns:
        dict: Project data.
    """
    try:
        with open(file_path, 'r') as file:
            project_data = json.load(file)
            logging.info("Project data loaded successfully.")
            return project_data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON: {e}")
        raise

if __name__ == '__main__':
    # Example usage
    try:
        project_data = load_project_data('project_data.json')
        calculator = StreetLightingEfficiencyCalculator(project_data)
        efficiency_metrics = calculator.calculate_energy_efficiency()

        print("Energy Efficiency Metrics:")
        print(json.dumps(efficiency_metrics, indent=4))
    except Exception as e:
        logging.error(f"Failed to calculate energy efficiency: {e}")
```

**Note:** This code assumes that the `project_data.json` file contains a list of lights with keys `power` and `lumens` for each light. Ensure the structure of the JSON file meets this requirement for the script to function correctly.
