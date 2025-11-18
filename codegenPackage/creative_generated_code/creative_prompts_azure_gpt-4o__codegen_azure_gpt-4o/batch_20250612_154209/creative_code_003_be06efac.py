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
import random
import logging

# Configure logging for detailed output
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SmokeTest:
    """
    Class to model the smoke testing process for detecting faults in water and sewage systems.
    """

    def __init__(self, system_name):
        """
        Initializes the SmokeTest instance.
        
        Args:
            system_name (str): Name of the system being tested (e.g., 'Water System', 'Sewage System').
        """
        self.system_name = system_name
        self.test_results = []

    def simulate_smoke_test(self):
        """
        Simulates the smoke testing process. Uses random values to model faults.

        Returns:
            dict: A dictionary containing test results with fault detection.
        """
        logging.info(f"Starting smoke test for {self.system_name}.")

        # Simulating pipes in the system
        pipes = ['Pipe_1', 'Pipe_2', 'Pipe_3', 'Pipe_4', 'Pipe_5']

        # Randomly simulate faults in the pipes
        for pipe in pipes:
            fault_detected = random.choice([True, False])  # Randomly decide if there's a fault
            result = {
                "pipe": pipe,
                "fault_detected": fault_detected
            }
            self.test_results.append(result)
            logging.info(f"Tested {pipe}: {'Fault detected' if fault_detected else 'No fault detected'}.")

        return self.test_results

    def generate_report(self):
        """
        Generates a detailed report based on the test results.

        Returns:
            str: A formatted string containing the test report.
        """
        logging.info("Generating test report...")
        report = f"Smoke Test Report for {self.system_name}\n\n"
        report += "Pipe               | Fault Detected\n"
        report += "-----------------------------------\n"

        for result in self.test_results:
            status = "YES" if result['fault_detected'] else "NO"
            report += f"{result['pipe']:<18} | {status}\n"

        return report


def main():
    """
    Main function to execute the smoke testing process.
    """
    try:
        # Create an instance of SmokeTest
        water_system_test = SmokeTest("Water System")

        # Run the test
        test_results = water_system_test.simulate_smoke_test()

        # Generate and print the report
        report = water_system_test.generate_report()
        print(report)

    except Exception as e:
        # Catch any unexpected errors
        logging.error(f"An error occurred during smoke testing: {e}")


if __name__ == "__main__":
    main()
```
