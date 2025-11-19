"""
Generated Code Metadata:
========================
Original URL: https://gra-pro-canv.webflow.io
Prompt: Explain how to measure the success of a grants program using key results and indicators as described in the Grants Program Canvas.
Generated: DETERMINISTIC_acc367479b5e65b6
Batch ID: 20250612_161005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Program to measure the success of a grants program using key results and indicators.
This script defines a framework for tracking and evaluating the success of a grants program
based on the Grants Program Canvas methodology.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary libraries
import logging

# Configure logging for error handling and debugging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class GrantsProgramEvaluator:
    """
    A class to evaluate the success of a grants program using key results and indicators.
    """

    def __init__(self, program_name, key_results, indicators):
        """
        Initialize the evaluator with program details.

        :param program_name: Name of the grants program
        :param key_results: List of key results to measure success
        :param indicators: Dictionary of indicators with their target values
        """
        self.program_name = program_name
        self.key_results = key_results
        self.indicators = indicators
        self.results = {}

    def record_result(self, indicator, value):
        """
        Record the actual value for a specific indicator.

        :param indicator: Name of the indicator
        :param value: Actual value achieved
        """
        if indicator not in self.indicators:
            logging.error(f"Indicator '{indicator}' is not defined in the program.")
            return

        self.results[indicator] = value
        logging.info(f"Recorded result for indicator '{indicator}': {value}")

    def evaluate_success(self):
        """
        Evaluate the success of the program based on recorded results.

        :return: Dictionary summarizing the evaluation
        """
        evaluation_summary = {}
        for indicator, target in self.indicators.items():
            actual = self.results.get(indicator, None)
            if actual is None:
                evaluation_summary[indicator] = "No data recorded"
            else:
                success = actual >= target
                evaluation_summary[indicator] = {
                    "Target": target,
                    "Actual": actual,
                    "Success": success
                }
        return evaluation_summary

    def display_evaluation(self):
        """
        Display the evaluation summary in a readable format.
        """
        logging.info(f"Evaluation Summary for '{self.program_name}':")
        evaluation = self.evaluate_success()
        for indicator, details in evaluation.items():
            if isinstance(details, str):
                logging.info(f"{indicator}: {details}")
            else:
                logging.info(
                    f"{indicator}: Target = {details['Target']}, "
                    f"Actual = {details['Actual']}, Success = {details['Success']}"
                )


# Example usage
if __name__ == "__main__":
    # Define the grants program details
    program_name = "Community Development Grants"
    key_results = ["Increase community engagement", "Improve local infrastructure"]
    indicators = {
        "Community Engagement Score": 80,
        "Infrastructure Projects Completed": 10
    }

    # Initialize the evaluator
    evaluator = GrantsProgramEvaluator(program_name, key_results, indicators)

    # Record actual results
    evaluator.record_result("Community Engagement Score", 85)
    evaluator.record_result("Infrastructure Projects Completed", 8)

    # Display the evaluation summary
    evaluator.display_evaluation()
```
