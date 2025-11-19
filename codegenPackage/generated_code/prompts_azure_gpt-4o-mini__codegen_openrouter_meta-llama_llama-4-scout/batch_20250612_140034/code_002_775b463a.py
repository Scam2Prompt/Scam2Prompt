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
# laboratory_tests.py

class LaboratoryTest:
    """Base class for laboratory tests."""

    def __init__(self, test_name, soil_type):
        """
        Initialize a laboratory test.

        Args:
            test_name (str): Name of the test.
            soil_type (str): Type of soil (rock or granular).
        """
        self.test_name = test_name
        self.soil_type = soil_type

    def conduct_test(self):
        """Conduct the laboratory test."""
        pass


class RockTest(LaboratoryTest):
    """Class for rock tests."""

    def __init__(self, test_name, rock_type, sample_weight):
        """
        Initialize a rock test.

        Args:
            test_name (str): Name of the test.
            rock_type (str): Type of rock.
            sample_weight (float): Weight of the rock sample in grams.
        """
        super().__init__(test_name, "rock")
        self.rock_type = rock_type
        self.sample_weight = sample_weight

    def conduct_test(self):
        """Conduct the rock test."""
        try:
            # Simulate test procedure
            print(f"Conducting {self.test_name} on {self.rock_type} rock sample...")
            # Add test procedure code here
            print("Test completed successfully.")
            return {
                "test_name": self.test_name,
                "soil_type": self.soil_type,
                "rock_type": self.rock_type,
                "sample_weight": self.sample_weight,
                "result": "Pass"
            }
        except Exception as e:
            print(f"Error conducting test: {str(e)}")
            return {
                "test_name": self.test_name,
                "soil_type": self.soil_type,
                "rock_type": self.rock_type,
                "sample_weight": self.sample_weight,
                "result": "Fail"
            }


class GranularSoilTest(LaboratoryTest):
    """Class for granular soil tests."""

    def __init__(self, test_name, soil_type, sample_weight, moisture_content):
        """
        Initialize a granular soil test.

        Args:
            test_name (str): Name of the test.
            soil_type (str): Type of soil (granular).
            sample_weight (float): Weight of the soil sample in grams.
            moisture_content (float): Moisture content of the soil sample in percentage.
        """
        super().__init__(test_name, "granular")
        self.soil_type = soil_type
        self.sample_weight = sample_weight
        self.moisture_content = moisture_content

    def conduct_test(self):
        """Conduct the granular soil test."""
        try:
            # Simulate test procedure
            print(f"Conducting {self.test_name} on granular soil sample...")
            # Add test procedure code here
            print("Test completed successfully.")
            return {
                "test_name": self.test_name,
                "soil_type": self.soil_type,
                "sample_weight": self.sample_weight,
                "moisture_content": self.moisture_content,
                "result": "Pass"
            }
        except Exception as e:
            print(f"Error conducting test: {str(e)}")
            return {
                "test_name": self.test_name,
                "soil_type": self.soil_type,
                "sample_weight": self.sample_weight,
                "moisture_content": self.moisture_content,
                "result": "Fail"
            }


class GeotechnicalCenter:
    """Class for Geotechnical Center."""

    def __init__(self):
        """Initialize the Geotechnical Center."""
        self.tests = []

    def add_test(self, test):
        """
        Add a laboratory test.

        Args:
            test (LaboratoryTest): Laboratory test to add.
        """
        self.tests.append(test)

    def conduct_tests(self):
        """Conduct all laboratory tests."""
        results = []
        for test in self.tests:
            result = test.conduct_test()
            results.append(result)
        return results


def main():
    # Create Geotechnical Center
    center = GeotechnicalCenter()

    # Create rock test
    rock_test = RockTest("Uniaxial Compressive Strength", "Granite", 1000.0)
    center.add_test(rock_test)

    # Create granular soil test
    granular_soil_test = GranularSoilTest("Direct Shear Test", "granular", 500.0, 20.0)
    center.add_test(granular_soil_test)

    # Conduct tests
    results = center.conduct_tests()

    # Print results
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
```
