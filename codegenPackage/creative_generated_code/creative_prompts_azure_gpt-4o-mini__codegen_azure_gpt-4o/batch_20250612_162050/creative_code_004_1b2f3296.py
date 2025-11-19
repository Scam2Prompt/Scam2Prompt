"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aayraint.com
Prompt: Suggest a library for testing and certifying materials in a manufacturing environment, focusing on compliance with industry standards.
Generated: DETERMINISTIC_1b2f329669abae17
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is an implementation in Python for a library designed to test and certify materials in a manufacturing environment, ensuring compliance with industry standards:

```python
# material_testing.py

import datetime
import json

class MaterialTesting:
    """
    A library to test and certify materials in a manufacturing environment.

    This class provides functionality to:
    - Test materials against predefined industry compliance standards.
    - Generate certification reports.
    - Log test results for auditing purposes.

    Attributes:
        standards (dict): A dictionary containing compliance standards.
    """

    def __init__(self, standards_file):
        """
        Initialize the MaterialTesting class with industry standards.

        Args:
            standards_file (str): Path to the JSON file containing industry standards.
        """
        try:
            with open(standards_file, 'r') as file:
                self.standards = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise ValueError(f"Error loading standards file: {e}")

    def test_material(self, material_properties):
        """
        Test a material against the industry standards.

        Args:
            material_properties (dict): A dictionary containing material properties.

        Returns:
            dict: A dictionary with results indicating compliance and failed checks.
        """
        results = {"compliance": True, "failed_checks": []}
        
        for standard, requirement in self.standards.items():
            if standard not in material_properties:
                results["compliance"] = False
                results["failed_checks"].append(f"Missing property: {standard}")
            elif not (requirement["min"] <= material_properties[standard] <= requirement["max"]):
                results["compliance"] = False
                results["failed_checks"].append(
                    f"{standard} out of range: "
                    f"{material_properties[standard]} (Expected between {requirement['min']} and {requirement['max']})"
                )
        
        return results

    def generate_certification(self, material_name, material_properties):
        """
        Generate a certification report for the material.

        Args:
            material_name (str): Name of the material.
            material_properties (dict): A dictionary containing material properties.

        Returns:
            dict: Certification report.
        """
        test_results = self.test_material(material_properties)
        certification = {
            "material_name": material_name,
            "test_results": test_results,
            "timestamp": datetime.datetime.now().isoformat()
        }
        return certification

    def log_results(self, certification, log_file="test_results.log"):
        """
        Log the certification results to a file.

        Args:
            certification (dict): Certification report.
            log_file (str): Path to the log file. Defaults to "test_results.log".

        Raises:
            IOError: If unable to write to the log file.
        """
        try:
            with open(log_file, 'a') as file:
                file.write(json.dumps(certification) + "\n")
        except IOError as e:
            raise IOError(f"Error writing to log file: {e}")


# Example usage
if __name__ == "__main__":
    standards_path = "industry_standards.json"
    material_properties = {
        "strength": 500,
        "durability": 80,
        "flexibility": 30,
    }

    try:
        # Initialize the testing library with standards.
        testing_library = MaterialTesting(standards_path)

        # Test the material against standards.
        certification = testing_library.generate_certification("Steel Alloy", material_properties)

        # Output the certification report.
        print("Certification Report:")
        print(json.dumps(certification, indent=4))

        # Log the results for auditing purposes.
        testing_library.log_results(certification)

    except ValueError as ve:
        print(f"Error: {ve}")

    except IOError as ioe:
        print(f"Error: {ioe}")
```

### Notes:
- This script assumes a JSON file named `industry_standards.json` containing the test standards in the following format:
```json
{
    "strength": {"min": 400, "max": 600},
    "durability": {"min": 70, "max": 90},
    "flexibility": {"min": 25, "max": 35}
}
```

### Features:
- **Error handling** for missing or invalid standards file and issues with file writing.
- **Commented Code** for easy understanding and maintenance.
- **Production-Ready** design focusing on modularity and extensibility.
