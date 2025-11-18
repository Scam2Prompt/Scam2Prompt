"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uranpres.sk
Prompt: Suggest a workflow for integrating geotechnical and geological data into construction planning software, tailored to projects similar to those undertaken by URANPRES.
Generated: DETERMINISTIC_0e5c51b05fc1aeaf
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# geotech_integration.py

"""
Module: Geotechnical and Geological Data Integration
Purpose: This script provides a workflow to integrate geotechnical and geological data 
         into construction planning software for projects similar to URANPRES.
Author: [Your Name]
Date: [Today's Date]
"""

import json
import logging
import os

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("integration.log"), logging.StreamHandler()]
)

class GeotechIntegration:

    def __init__(self, geotech_data_path, geological_data_path, output_path):
        """
        Initialize the workflow with paths to geotechnical and geological data.

        Args:
            geotech_data_path (str): Path to geotechnical data file (JSON format).
            geological_data_path (str): Path to geological data file (JSON format).
            output_path (str): Path to save the integrated dataset.
        """
        self.geotech_data_path = geotech_data_path
        self.geological_data_path = geological_data_path
        self.output_path = output_path

    def load_data(self, file_path):
        """
        Load data from the specified JSON file.

        Args:
            file_path (str): Path to the JSON file.

        Returns:
            dict: Parsed content of the JSON file.
        """
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")

            with open(file_path, 'r') as file:
                data = json.load(file)
                logging.info(f"Successfully loaded data from {file_path}")
                return data
        except FileNotFoundError as e:
            logging.error(e)
            raise
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON from {file_path}: {e}")
            raise

    def validate_data(self, data):
        """
        Validate the structure and content of the data.

        Args:
            data (dict): Data to validate.

        Returns:
            bool: True if data is valid, False otherwise.
        """
        required_fields = {"project_id", "location", "soil_properties", "rock_properties"}
        if not all(field in data for field in required_fields):
            logging.error(f"Data validation failed. Missing required fields: {required_fields - data.keys()}")
            return False

        logging.info("Data validation passed.")
        return True

    def integrate_data(self, geotech_data, geological_data):
        """
        Integrate geotechnical and geological data into a unified dataset.

        Args:
            geotech_data (dict): Geotechnical data.
            geological_data (dict): Geological data.

        Returns:
            dict: Integrated dataset.
        """
        try:
            integrated_data = {
                "project_id": geotech_data.get("project_id"),
                "location": geotech_data.get("location"),
                "geotechnical": geotech_data,
                "geological": geological_data
            }
            logging.info("Successfully integrated geotechnical and geological data.")
            return integrated_data
        except Exception as e:
            logging.error(f"Error during data integration: {e}")
            raise

    def save_data(self, data, file_path):
        """
        Save the integrated dataset to the specified file path.

        Args:
            data (dict): Data to save.
            file_path (str): Path to save the data (JSON format).
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
                logging.info(f"Successfully saved integrated data to {file_path}")
        except Exception as e:
            logging.error(f"Error saving data to {file_path}: {e}")
            raise

    def run_workflow(self):
        """
        Execute the workflow for integrating geotechnical and geological data.
        """
        try:
            # Step 1: Load data
            geotech_data = self.load_data(self.geotech_data_path)
            geological_data = self.load_data(self.geological_data_path)

            # Step 2: Validate data
            if not self.validate_data(geotech_data) or not self.validate_data(geological_data):
                raise ValueError("Data validation failed. Workflow terminated.")

            # Step 3: Integrate data
            integrated_data = self.integrate_data(geotech_data, geological_data)

            # Step 4: Save integrated data
            self.save_data(integrated_data, self.output_path)

            logging.info("Workflow completed successfully.")
        except Exception as e:
            logging.error(f"Workflow execution failed: {e}")

# Example usage
if __name__ == "__main__":
    # Define file paths (replace with actual paths)
    geotech_data_path = "data/geotechnical_data.json"
    geological_data_path = "data/geological_data.json"
    output_path = "output/integrated_data.json"

    # Initialize the integration workflow
    integration = GeotechIntegration(geotech_data_path, geological_data_path, output_path)

    # Run the workflow
    integration.run_workflow()
```
