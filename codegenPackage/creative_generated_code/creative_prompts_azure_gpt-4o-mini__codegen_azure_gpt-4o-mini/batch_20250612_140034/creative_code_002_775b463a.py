"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foundation.ru
Prompt: Generate code for conducting laboratory tests on rock and granular soils based on the testing services offered by the Geotechnical Center.
Generated: DETERMINISTIC_775b463a0e65dffe
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LaboratoryTest:
    """
    A class to represent a laboratory test for geotechnical analysis 
    on rock and granular soils.
    """

    def __init__(self, test_name: str, sample_id: str):
        """
        Initialize the LaboratoryTest with a name and sample identifier.

        :param test_name: The name of the test to be conducted.
        :param sample_id: The unique identifier for the soil or rock sample.
        """
        self.test_name = test_name
        self.sample_id = sample_id

    def conduct_test(self) -> Dict[str, Any]:
        """
        Conducts the laboratory test based on the test name.

        :return: A dictionary containing test results.
        """
        logging.info(f"Conducting test: {self.test_name} on sample: {self.sample_id}")
        
        # Simulate test logic based on test_name
        try:
            if self.test_name == "Atterberg Limits":
                return self.atterberg_limits_test()
            elif self.test_name == "Compaction Test":
                return self.compaction_test()
            elif self.test_name == "Shear Strength Test":
                return self.shear_strength_test()
            else:
                raise ValueError("Unsupported test type.")
        except Exception as e:
            logging.error(f"Error conducting test {self.test_name} on sample {self.sample_id}: {str(e)}")
            return {"error": str(e)}

    def atterberg_limits_test(self) -> Dict[str, Any]:
        """
        Simulates the Atterberg Limits test.

        :return: A dictionary with test results.
        """
        # Placeholder for test results
        results = {
            'liquid_limit': 25.0,  # example value
            'plastic_limit': 15.0,  # example value
            'plasticity_index': 10.0 # calculated value
        }
        logging.info(f"Atterberg Limits Test Results: {results}")
        return results

    def compaction_test(self) -> Dict[str, Any]:
        """
        Simulates the Compaction test.

        :return: A dictionary with test results.
        """
        # Placeholder for test results
        results = {
            'max_density': 1.85,  # example value in g/cm^3
            'optimum_moisture_content': 12.5  # example value in %
        }
        logging.info(f"Compaction Test Results: {results}")
        return results

    def shear_strength_test(self) -> Dict[str, Any]:
        """
        Simulates the Shear Strength test.

        :return: A dictionary with test results.
        """
        # Placeholder for test results
        results = {
            'cohesion': 30.0,  # example value in kPa
            'friction_angle': 25.0  # example value in degrees
        }
        logging.info(f"Shear Strength Test Results: {results}")
        return results


def main():
    """
    Main function to execute the laboratory tests.
    """
    # Sample tests for demonstration purposes
    tests: List[LaboratoryTest] = [
        LaboratoryTest("Atterberg Limits", "Sample001"),
        LaboratoryTest("Compaction Test", "Sample002"),
        LaboratoryTest("Shear Strength Test", "Sample003"),
        LaboratoryTest("Unknown Test", "Sample004")  # This will trigger an error
    ]

    # Conduct each test and print results
    for test in tests:
        results = test.conduct_test()
        logging.info(f"Results for {test.test_name} on {test.sample_id}: {results}")


if __name__ == "__main__":
    main()
```
