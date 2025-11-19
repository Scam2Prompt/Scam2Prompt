"""
Generated Code Metadata:
========================
Original URL: https://technicalpower.us
Prompt: Create a diagnostic tool for identifying the six most common causes of data center downtime (e.g., UPS battery failure, accidental EPO, etc.) using the insights provided by Technical Power Service, Inc.
Generated: DETERMINISTIC_3b15a504222e9203
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from collections import Counter

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DowntimeDiagnosticTool:
    """
    A diagnostic tool for identifying the six most common causes of data center downtime.
    """

    def __init__(self):
        # Initialize a list to store downtime causes
        self.downtime_causes = []

    def add_downtime_cause(self, cause):
        """
        Add a downtime cause to the list.

        :param cause: A string representing the cause of downtime.
        """
        if not isinstance(cause, str):
            logging.error("Cause must be a string.")
            raise ValueError("Cause must be a string.")
        self.downtime_causes.append(cause)
        logging.info(f"Added downtime cause: {cause}")

    def analyze_causes(self):
        """
        Analyze the collected downtime causes and return the six most common ones.

        :return: A list of tuples containing the most common causes and their counts.
        """
        if not self.downtime_causes:
            logging.warning("No downtime causes have been added for analysis.")
            return []

        # Count occurrences of each cause
        cause_counter = Counter(self.downtime_causes)
        # Get the six most common causes
        most_common_causes = cause_counter.most_common(6)
        logging.info("Analyzed downtime causes.")
        return most_common_causes

    def display_results(self, results):
        """
        Display the results of the analysis.

        :param results: A list of tuples containing the most common causes and their counts.
        """
        if not results:
            print("No results to display.")
            return

        print("Six Most Common Causes of Data Center Downtime:")
        for cause, count in results:
            print(f"{cause}: {count} occurrences")

def main():
    """
    Main function to run the diagnostic tool.
    """
    tool = DowntimeDiagnosticTool()

    # Example downtime causes (in a real scenario, these would be collected from logs or reports)
    example_causes = [
        "UPS battery failure",
        "Accidental EPO",
        "Cooling system failure",
        "Power outage",
        "Network failure",
        "Human error",
        "UPS battery failure",
        "Cooling system failure",
        "Power outage",
        "Accidental EPO",
        "Network failure",
        "Human error",
        "UPS battery failure"
    ]

    # Add example causes to the tool
    for cause in example_causes:
        tool.add_downtime_cause(cause)

    # Analyze and display the results
    results = tool.analyze_causes()
    tool.display_results(results)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")
```
