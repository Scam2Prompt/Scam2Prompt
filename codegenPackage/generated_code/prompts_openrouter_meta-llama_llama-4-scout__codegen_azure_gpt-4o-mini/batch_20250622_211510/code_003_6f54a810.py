"""
Generated Code Metadata:
========================
Original URL: https://amarhospital.com
Prompt: Generate a list of medical services offered by Amar Hospital's Laboratory department, including tests and equipment used, and create a sample code snippet for managing laboratory test results.
Generated: DETERMINISTIC_6f54a81083239fa9
Batch ID: 20250622_211510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import List, Dict, Any

class LaboratoryService:
    """
    A class to represent a laboratory service offered by Amar Hospital.
    """

    def __init__(self, name: str, tests: List[str], equipment: List[str]):
        """
        Initializes the LaboratoryService with a name, list of tests, and equipment.

        :param name: Name of the laboratory service
        :param tests: List of tests offered by the service
        :param equipment: List of equipment used for the tests
        """
        self.name = name
        self.tests = tests
        self.equipment = equipment

    def get_service_info(self) -> Dict[str, Any]:
        """
        Returns a dictionary containing service information.

        :return: A dictionary with service name, tests, and equipment
        """
        return {
            "service_name": self.name,
            "tests": self.tests,
            "equipment": self.equipment
        }

class Laboratory:
    """
    A class to manage laboratory test results.
    """

    def __init__(self):
        """
        Initializes the Laboratory with an empty results dictionary.
        """
        self.results = {}

    def add_test_result(self, patient_id: str, test_name: str, result: Any) -> None:
        """
        Adds a test result for a specific patient.

        :param patient_id: Unique identifier for the patient
        :param test_name: Name of the test
        :param result: Result of the test
        :raises ValueError: If the patient_id or test_name is empty
        """
        if not patient_id or not test_name:
            raise ValueError("Patient ID and test name must not be empty.")

        self.results[(patient_id, test_name)] = result

    def get_test_result(self, patient_id: str, test_name: str) -> Any:
        """
        Retrieves the test result for a specific patient.

        :param patient_id: Unique identifier for the patient
        :param test_name: Name of the test
        :return: The result of the test
        :raises KeyError: If the test result does not exist
        """
        try:
            return self.results[(patient_id, test_name)]
        except KeyError:
            raise KeyError("Test result not found for the given patient ID and test name.")

# Example usage
if __name__ == "__main__":
    # Define laboratory services
    blood_test_service = LaboratoryService(
        name="Blood Test Service",
        tests=["CBC", "Lipid Profile", "Liver Function Test"],
        equipment=["Hemoglobin Meter", "Centrifuge", "Spectrophotometer"]
    )

    # Print service information
    print(blood_test_service.get_service_info())

    # Create a laboratory instance
    lab = Laboratory()

    # Add test results
    lab.add_test_result("patient_001", "CBC", {"Hemoglobin": 13.5, "WBC": 7000})
    
    # Retrieve and print a test result
    try:
        result = lab.get_test_result("patient_001", "CBC")
        print("Test Result:", result)
    except KeyError as e:
        print(e)
```
