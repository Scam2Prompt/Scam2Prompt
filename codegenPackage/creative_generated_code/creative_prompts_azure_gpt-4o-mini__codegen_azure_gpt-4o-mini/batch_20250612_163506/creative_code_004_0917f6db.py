"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aktivrorteknikk.no
Prompt: What are the best practices for smoke testing in plumbing systems, and how can I implement them in a code-based solution, as suggested by Aktiv Rørteknikk AS?
Generated: DETERMINISTIC_0917f6dbaea1f1c6
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import time
import random

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SmokeTestResult:
    """Class to hold the results of a smoke test."""
    def __init__(self, test_name, status, details):
        self.test_name = test_name
        self.status = status
        self.details = details

    def __str__(self):
        return f"Test: {self.test_name}, Status: {self.status}, Details: {self.details}"

class PlumbingSmokeTester:
    """Class to perform smoke testing on plumbing systems."""
    def __init__(self, system_name):
        self.system_name = system_name

    def perform_smoke_test(self):
        """Perform smoke test and return the result."""
        logging.info(f"Starting smoke test for {self.system_name}...")
        try:
            # Simulate test execution with a random outcome
            result = random.choice([True, False])
            if result:
                details = "No leaks detected."
                status = "PASS"
            else:
                details = "Leaking detected at connection point."
                status = "FAIL"
            
            logging.info(f"Smoke test completed for {self.system_name}.")
            return SmokeTestResult(self.system_name, status, details)
        except Exception as e:
            logging.error(f"Error during smoke test for {self.system_name}: {e}")
            return SmokeTestResult(self.system_name, "ERROR", str(e))

def main():
    """Main function to execute smoke testing."""
    systems_to_test = ["System A", "System B", "System C"]

    results = []
    for system in systems_to_test:
        tester = PlumbingSmokeTester(system)
        result = tester.perform_smoke_test()
        results.append(result)

        logging.info(str(result))

    # Summary of results
    logging.info("Smoke Test Summary:")
    for result in results:
        logging.info(str(result))

if __name__ == "__main__":
    main()
```
