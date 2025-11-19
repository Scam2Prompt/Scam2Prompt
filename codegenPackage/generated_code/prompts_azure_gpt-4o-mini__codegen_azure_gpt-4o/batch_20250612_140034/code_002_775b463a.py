"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: Generate code for conducting laboratory tests on rock and granular soils based on the testing services offered by the Geotechnical Center.
Generated: DETERMINISTIC_775b463a0e65dffe
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class GeotechnicalLab:
    """
    A class to manage laboratory tests for rock and granular soils.
    """

    def __init__(self):
        """
        Initialize the GeotechnicalLab with available tests.
        """
        self.available_tests = {
            "rock": ["Uniaxial Compression Test", "Point Load Test", "Triaxial Test"],
            "granular_soil": ["Sieve Analysis", "Proctor Compaction Test", "Direct Shear Test"]
        }

    def list_tests(self):
        """
        List all available tests for rock and granular soils.

        Returns:
            dict: A dictionary of available tests categorized by material type.
        """
        return self.available_tests

    def conduct_test(self, material_type, test_name, sample_data):
        """
        Conduct a specified test on the given material type.

        Args:
            material_type (str): The type of material ("rock" or "granular_soil").
            test_name (str): The name of the test to conduct.
            sample_data (dict): The sample data required for the test.

        Returns:
            dict: A dictionary containing the test results.

        Raises:
            ValueError: If the material type or test name is invalid.
        """
        # Validate material type
        if material_type not in self.available_tests:
            raise ValueError(f"Invalid material type: {material_type}. Must be 'rock' or 'granular_soil'.")

        # Validate test name
        if test_name not in self.available_tests[material_type]:
            raise ValueError(f"Invalid test name: {test_name}. Available tests for {material_type}: {self.available_tests[material_type]}")

        # Simulate test results (in a real-world scenario, this would involve complex calculations or lab equipment)
        test_results = {
            "material_type": material_type,
            "test_name": test_name,
            "sample_data": sample_data,
            "results": f"Simulated results for {test_name} on {material_type}."
        }

        return test_results

    def save_results(self, results, file_path):
        """
        Save test results to a JSON file.

        Args:
            results (dict): The test results to save.
            file_path (str): The file path where results should be saved.

        Raises:
            IOError: If there is an issue saving the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(results, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving results to file: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize the lab
    lab = GeotechnicalLab()

    # List available tests
    print("Available Tests:")
    print(json.dumps(lab.list_tests(), indent=4))

    # Conduct a test
    try:
        sample_data = {"sample_id": "12345", "weight": 50, "dimensions": {"length": 10, "width": 5, "height": 2}}
        results = lab.conduct_test("rock", "Uniaxial Compression Test", sample_data)
        print("\nTest Results:")
        print(json.dumps(results, indent=4))

        # Save results to a file
        lab.save_results(results, "test_results.json")
        print("\nResults saved to 'test_results.json'.")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except IOError as ioe:
        print(f"IOError: {ioe}")
```
