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
# geotechnical_testing.py
# This script provides functionality to conduct laboratory tests on rock and granular soils
# based on testing services offered by the Geotechnical Center.

import os


class GeotechnicalLab:
    """
    A class to represent laboratory tests conducted for geotechnical analysis.
    """

    def __init__(self):
        """
        Initialize the GeotechnicalLab class with a list of available tests.
        """
        self.tests_available = {
            "rock": [
                "Uniaxial Compressive Strength Test",
                "Point Load Test",
                "Slake Durability Test",
            ],
            "granular_soil": [
                "Particle Size Distribution",
                "Proctor Compaction Test",
                "Direct Shear Test",
            ],
        }

    def list_tests(self, material_type):
        """
        List the available tests for a given material type.

        :param material_type: str, either "rock" or "granular_soil"
        :return: list of test names
        """
        if material_type not in self.tests_available:
            raise ValueError("Invalid material type. Choose 'rock' or 'granular_soil'.")
        return self.tests_available[material_type]

    def conduct_test(self, material_type, test_name):
        """
        Conduct a specific test for the given material type.

        :param material_type: str, "rock" or "granular_soil"
        :param test_name: str, name of the test to be conducted
        :return: str, simulated results of the test
        """
        if material_type not in self.tests_available:
            raise ValueError("Invalid material type. Choose 'rock' or 'granular_soil'.")
        if test_name not in self.tests_available[material_type]:
            raise ValueError(f"Invalid test name. Use list_tests('{material_type}') to see available tests.")

        # Simulate test results (In a real-world scenario, this would involve complex calculations and instrumentation)
        results = f"Successfully conducted '{test_name}' for {material_type}. Results simulated."
        return results

    def save_results(self, test_name, results, output_dir="test_results"):
        """
        Save test results to a file.

        :param test_name: str, name of the test conducted
        :param results: str, results of the test
        :param output_dir: str, directory to save the results
        :return: None
        """
        try:
            # Create output directory if it does not exist
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            # Save results to a file
            file_path = os.path.join(output_dir, f"{test_name.replace(' ', '_')}_results.txt")
            with open(file_path, "w") as file:
                file.write(results)
            print(f"Results saved to {file_path}")

        except Exception as e:
            print(f"Error saving results: {e}")


# Example usage (uncomment to test functionality):
if __name__ == "__main__":
    lab = GeotechnicalLab()

    try:
        # Example: List available tests for rock
        print("Available tests for rock:")
        print(lab.list_tests("rock"))

        # Example: Conduct a test for granular soil
        test_result = lab.conduct_test("granular_soil", "Particle Size Distribution")
        print(test_result)

        # Example: Save the test results
        lab.save_results("Particle Size Distribution", test_result)

    except Exception as error:
        print(f"An error occurred: {error}")
```
