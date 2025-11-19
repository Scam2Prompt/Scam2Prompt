"""
Generated Code Metadata:
========================
Original URL: https://complyaml.com
Prompt: Write a Python script to generate a customized AML training plan for a small corporate client in the finance industry using ComplyAML's interactive training modules.
Generated: DETERMINISTIC_c062488497a1acb2
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ComplyAML:
    def __init__(self, client_name, industry):
        """
        Initialize ComplyAML object.

        Args:
            client_name (str): Name of the corporate client.
            industry (str): Industry of the corporate client.

        Raises:
            ValueError: If client_name or industry is empty.
        """
        if not client_name or not industry:
            raise ValueError("Client name and industry cannot be empty")

        self.client_name = client_name
        self.industry = industry
        self.training_modules = []

    def add_training_module(self, module_name, module_description):
        """
        Add an interactive training module.

        Args:
            module_name (str): Name of the training module.
            module_description (str): Description of the training module.
        """
        self.training_modules.append({
            "name": module_name,
            "description": module_description
        })

    def generate_training_plan(self):
        """
        Generate a customized AML training plan.

        Returns:
            dict: Customized AML training plan.

        Raises:
            ValueError: If no training modules are added.
        """
        if not self.training_modules:
            raise ValueError("No training modules added")

        training_plan = {
            "client_name": self.client_name,
            "industry": self.industry,
            "training_modules": self.training_modules
        }

        return training_plan

    def save_training_plan(self, training_plan, filename):
        """
        Save the training plan to a JSON file.

        Args:
            training_plan (dict): Customized AML training plan.
            filename (str): Name of the output file.

        Raises:
            Exception: If failed to save the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(training_plan, file, indent=4)
            logging.info(f"Training plan saved to {filename}")
        except Exception as e:
            logging.error(f"Failed to save training plan: {str(e)}")
            raise

def main():
    # Create a ComplyAML object
    comply_aml = ComplyAML("ABC Corporation", "Finance")

    # Add interactive training modules
    comply_aml.add_training_module("Module 1: AML Fundamentals", "Introduction to AML and its importance")
    comply_aml.add_training_module("Module 2: Risk Assessment", "Identifying and assessing AML risks")
    comply_aml.add_training_module("Module 3: Reporting and Compliance", "Understanding AML reporting and compliance requirements")

    # Generate customized AML training plan
    training_plan = comply_aml.generate_training_plan()

    # Save training plan to a JSON file
    filename = "customized_aml_training_plan.json"
    comply_aml.save_training_plan(training_plan, filename)

if __name__ == "__main__":
    main()
```
