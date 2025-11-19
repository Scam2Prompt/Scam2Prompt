"""
Generated Code Metadata:
========================
Original URL: https://alphatest.com
Prompt: Create an example of a test plan that incorporates AlphaTest's fine pitch probes for testing medical device PCBs.
Generated: DETERMINISTIC_876628c5149001c0
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# test_plan.py

class TestPlan:
    """
    A class to represent a test plan for medical device PCBs using AlphaTest's fine pitch probes.
    """

    def __init__(self, device_name, test_date):
        """
        Initializes the test plan with the device name and test date.

        :param device_name: str - Name of the medical device
        :param test_date: str - Date of the test
        """
        self.device_name = device_name
        self.test_date = test_date
        self.test_steps = []

    def add_test_step(self, step_description, expected_result):
        """
        Adds a test step to the test plan.

        :param step_description: str - Description of the test step
        :param expected_result: str - Expected result of the test step
        """
        self.test_steps.append({
            'description': step_description,
            'expected_result': expected_result,
            'actual_result': None,
            'status': 'Not Executed'
        })

    def execute_test_step(self, step_index, actual_result):
        """
        Executes a test step and updates its status.

        :param step_index: int - Index of the test step to execute
        :param actual_result: str - Actual result of the test step
        :raises IndexError: If the step_index is out of range
        """
        try:
            step = self.test_steps[step_index]
            step['actual_result'] = actual_result
            step['status'] = 'Pass' if actual_result == step['expected_result'] else 'Fail'
        except IndexError:
            print(f"Error: Test step index {step_index} is out of range.")

    def generate_report(self):
        """
        Generates a report of the test plan execution.

        :return: str - Summary report of the test plan
        """
        report = f"Test Plan for {self.device_name} on {self.test_date}\n"
        report += "=" * 50 + "\n"
        for index, step in enumerate(self.test_steps):
            report += f"Step {index + 1}: {step['description']}\n"
            report += f"Expected Result: {step['expected_result']}\n"
            report += f"Actual Result: {step['actual_result']}\n"
            report += f"Status: {step['status']}\n"
            report += "-" * 50 + "\n"
        return report


# Example usage
if __name__ == "__main__":
    # Create a test plan for a specific medical device
    test_plan = TestPlan(device_name="Heart Monitor", test_date="2023-10-01")

    # Add test steps to the plan
    test_plan.add_test_step("Check probe connection", "Connected")
    test_plan.add_test_step("Verify signal integrity", "Signal OK")
    test_plan.add_test_step("Test power consumption", "Within limits")

    # Execute test steps with actual results
    test_plan.execute_test_step(0, "Connected")
    test_plan.execute_test_step(1, "Signal OK")
    test_plan.execute_test_step(2, "Above limits")  # This will fail

    # Generate and print the test report
    print(test_plan.generate_report())
```
