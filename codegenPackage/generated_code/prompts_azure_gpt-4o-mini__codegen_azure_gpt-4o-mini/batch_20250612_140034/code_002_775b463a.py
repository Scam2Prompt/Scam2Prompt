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
import pandas as pd
import numpy as np

class GeotechnicalTest:
    """
    A class to represent a geotechnical test for rock and granular soils.
    """

    def __init__(self, sample_id, sample_type, test_type):
        """
        Initializes the GeotechnicalTest instance.

        Parameters:
        sample_id (str): Unique identifier for the sample.
        sample_type (str): Type of the sample (rock or granular soil).
        test_type (str): Type of test to be conducted.
        """
        self.sample_id = sample_id
        self.sample_type = sample_type
        self.test_type = test_type
        self.results = None

    def conduct_test(self):
        """
        Conducts the specified geotechnical test and stores the results.
        Raises ValueError if the test type is not supported.
        """
        try:
            if self.test_type == "Atterberg Limits":
                self.results = self._atterberg_limits_test()
            elif self.test_type == "Compaction Test":
                self.results = self._compaction_test()
            elif self.test_type == "Unconfined Compression Test":
                self.results = self._unconfined_compression_test()
            else:
                raise ValueError(f"Test type '{self.test_type}' is not supported.")
        except Exception as e:
            print(f"Error conducting test: {e}")

    def _atterberg_limits_test(self):
        """
        Simulates the Atterberg Limits test and returns the results.

        Returns:
        dict: Results of the Atterberg Limits test.
        """
        # Simulated results for demonstration purposes
        results = {
            "Liquid Limit": np.random.uniform(20, 50),
            "Plastic Limit": np.random.uniform(10, 30),
            "Plasticity Index": np.random.uniform(5, 20)
        }
        return results

    def _compaction_test(self):
        """
        Simulates the Compaction test and returns the results.

        Returns:
        dict: Results of the Compaction test.
        """
        # Simulated results for demonstration purposes
        results = {
            "Maximum Dry Density": np.random.uniform(1.5, 2.0),
            "Optimum Moisture Content": np.random.uniform(10, 20)
        }
        return results

    def _unconfined_compression_test(self):
        """
        Simulates the Unconfined Compression test and returns the results.

        Returns:
        dict: Results of the Unconfined Compression test.
        """
        # Simulated results for demonstration purposes
        results = {
            "Unconfined Compressive Strength": np.random.uniform(100, 300)
        }
        return results

    def get_results(self):
        """
        Returns the results of the conducted test.

        Returns:
        dict: Results of the test or None if the test has not been conducted.
        """
        return self.results

# Example usage
if __name__ == "__main__":
    # Create a geotechnical test instance
    test = GeotechnicalTest(sample_id="S001", sample_type="granular soil", test_type="Atterberg Limits")
    
    # Conduct the test
    test.conduct_test()
    
    # Retrieve and print the results
    results = test.get_results()
    if results:
        print(f"Test Results for Sample ID {test.sample_id}: {results}")
    else:
        print("No results available. Test may not have been conducted.")
```
