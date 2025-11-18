"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foundation.ru
Prompt: Create a script for performing geotechnical expertise and detailed instrument-based inspections of construction sites, as outlined by the Научно-образовательный центр «Геотехника».
Generated: DETERMINISTIC_7cd98937b8c2752a
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import json
import logging
import os
import sys
from datetime import datetime
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("geotechnical_inspection.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

class GeotechnicalInspection:
    """
    A class to handle geotechnical expertise and detailed instrument-based
    inspections of construction sites as per Научно-образовательный центр «Геотехника».
    """

    def __init__(self, config_file: str):
        """
        Initializes the geotechnical inspection class with a configuration file.
        :param config_file: Path to the JSON configuration file.
        """
        self.config = self.load_config(config_file)

    def load_config(self, path: str) -> Dict:
        """
        Loads configuration parameters from a JSON file.
        :param path: Path to the configuration file.
        :return: Dictionary containing configuration parameters.
        """
        try:
            logging.info("Loading configuration from %s", path)
            with open(path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            logging.error("Configuration file not found at %s", path)
            sys.exit("Configuration file missing.")
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from configuration file %s", path)
            sys.exit("Invalid configuration file format.")

    def perform_inspection(self, site_data: List[Dict]) -> None:
        """
        Perform geotechnical inspections on the provided site data.
        :param site_data: List of dictionaries containing site data.
        """
        for site in site_data:
            try:
                logging.info("Inspecting site: %s", site["site_name"])
                # Simulate data collection from instruments
                soil_analysis = self.analyze_soil(site["measurement_data"])
                stability_report = self.check_stability(site["measurement_data"])

                # Save results
                self.save_results(site["site_name"], soil_analysis, stability_report)
                logging.info("Inspection completed for site: %s", site["site_name"])

            except KeyError as e:
                logging.error("Missing key in site data: %s", str(e))
            except Exception as e:
                logging.error("Unexpected error during inspection: %s", str(e))

    def analyze_soil(self, measurements: Dict) -> Dict:
        """
        Simulates analysis of soil based on measurement data.
        :param measurements: Dictionary of measurement data.
        :return: Dictionary with analysis results.
        """
        # Example of soil analysis logic (simplified for illustration purposes)
        soil_type = "Clay" if measurements.get("soil_density", 0) > 2.0 else "Sand"
        water_content = measurements.get("water_content", 0)
        return {
            "soil_type": soil_type,
            "water_content": water_content,
            "recommendations": "Monitor water levels regularly."
        }

    def check_stability(self, measurements: Dict) -> Dict:
        """
        Simulates stability checking based on measurement data.
        :param measurements: Dictionary of measurement data.
        :return: Dictionary with stability results and safety recommendations.
        """
        stress = measurements.get("stress", 0)
        strain = measurements.get("strain", 0)
        if stress / strain > 1.5:
            stability = "Stable"
            recommendations = "No immediate action needed."
        else:
            stability = "Unstable"
            recommendations = "Reinforce structure and monitor closely."
        return {
            "stability": stability,
            "recommendations": recommendations
        }

    def save_results(self, site_name: str, soil_analysis: Dict, stability_report: Dict) -> None:
        """
        Saves inspection results to a CSV file.
        :param site_name: Name of the construction site.
        :param soil_analysis: Soil analysis results.
        :param stability_report: Stability report results.
        """
        output_file = f"{site_name}_inspection_results.csv"
        try:
            logging.info("Saving results to %s", output_file)
            headers = ["Site Name", "Soil Type", "Water Content", "Soil Recommendations",
                       "Stability", "Stability Recommendations"]
            data = [
                site_name,
                soil_analysis["soil_type"],
                soil_analysis["water_content"],
                soil_analysis["recommendations"],
                stability_report["stability"],
                stability_report["recommendations"]
            ]
            write_header = not os.path.exists(output_file)  # Add header only if file doesn't exist

            with open(output_file, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                if write_header:
                    writer.writerow(headers)
                writer.writerow(data)

        except IOError as e:
            logging.error("Error writing to file %s: %s", output_file, str(e))

# Example usage
if __name__ == "__main__":
    # Load configuration and site data
    inspection = GeotechnicalInspection(config_file="config.json")
    site_data = [
        {
            "site_name": "Site A",
            "measurement_data": {
                "soil_density": 2.5,
                "water_content": 0.15,
                "stress": 3.0,
                "strain": 2.0
            }
        },
        {
            "site_name": "Site B",
            "measurement_data": {
                "soil_density": 1.8,
                "water_content": 0.10,
                "stress": 1.2,
                "strain": 1.5
            }
        }
    ]
    # Perform inspections
    inspection.perform_inspection(site_data)
```
