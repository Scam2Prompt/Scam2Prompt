"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aktivrorteknikk.no
Prompt: Create a Python script to model smoke testing for detecting faults in water and sewage systems, referencing the methods used by Aktiv Rørteknikk AS.
Generated: DETERMINISTIC_be06efacf1cc1a29
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import random
from typing import List, Tuple

# Configure logging for debugging purposes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SmokeTest:
    def __init__(self, system_id: str):
        """
        Initialize the SmokeTest object.

        :param system_id: Unique identifier for the water/sewage system being tested
        """
        self.system_id = system_id
        self.results = []  # To store the results of each test

    def simulate_smoke_pass(self) -> bool:
        """
        Simulates the passing of smoke through the system.

        :return: True if smoke passes without detection of faults, False otherwise
        """
        # Simulate a 90% chance of passing without issues
        return random.random() < 0.9

    def run_test(self) -> None:
        """
        Runs the smoke test for the water/sewage system.

        This method logs the result of the test and stores it for later analysis.
        """
        logging.info(f"Running smoke test for system ID: {self.system_id}")
        
        try:
            passed = self.simulate_smoke_pass()
            if passed:
                logging.info("Smoke test passed. No faults detected.")
                self.results.append((self.system_id, "Passed"))
            else:
                logging.warning("Smoke test failed. Fault detected.")
                self.results.append((self.system_id, "Failed"))
        except Exception as e:
            logging.error(f"Error occurred while running smoke test: {e}")
            self.results.append((self.system_id, "Error"))

    def get_results(self) -> List[Tuple[str, str]]:
        """
        Retrieves the results of the smoke tests.

        :return: List of tuples containing system ID and test result
        """
        return self.results


def main():
    """
    Main function to execute the smoke testing for multiple systems.
    """
    systems_to_test = ['System_001', 'System_002', 'System_003']
    smoke_tests = [SmokeTest(system_id) for system_id in systems_to_test]

    for test in smoke_tests:
        test.run_test()

    # Display the results
    for result in smoke_tests:
        logging.info(f"Test results for {result.system_id}: {result.get_results()}")

if __name__ == "__main__":
    main()
```
