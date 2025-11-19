"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gra-pro-canv.webflow.io
Prompt: Explain how to measure the success of a grants program using key results and indicators as described in the Grants Program Canvas.
Generated: DETERMINISTIC_acc367479b5e65b6
Batch ID: 20250612_161005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GrantsProgram:
    """
    A class to represent a grants program and measure its success using key results and indicators.
    """

    def __init__(self, name):
        """
        Initializes the Grants Program with a name and sets up a dictionary to store key results.

        Parameters:
        name (str): The name of the grants program.
        """
        self.name = name
        self.key_results = {}

    def add_key_result(self, result_name, target_value):
        """
        Adds a key result to the grants program.

        Parameters:
        result_name (str): The name of the key result.
        target_value (float): The target value to measure success against.

        Raises:
        ValueError: If the target value is not a number or is negative.
        """
        if not isinstance(target_value, (int, float)) or target_value < 0:
            raise ValueError("Target value must be a non-negative number.")

        self.key_results[result_name] = {
            'target_value': target_value,
            'current_value': 0  # Initialize current value to zero
        }
    
    def update_current_value(self, result_name, current_value):
        """
        Updates the current value of a key result.

        Parameters:
        result_name (str): The name of the key result to update.
        current_value (float): The current value achieved.

        Raises:
        KeyError: If the key result does not exist.
        ValueError: If the current value is negative.
        """
        if result_name not in self.key_results:
            raise KeyError(f"Key result '{result_name}' does not exist.")
        if current_value < 0:
            raise ValueError("Current value must be a non-negative number.")

        self.key_results[result_name]['current_value'] = current_value

    def measure_success(self):
        """
        Measures the success of the grants program based on key results.

        Returns:
        dict: A summary of the key results, showing if targets have been met.
        """
        success_summary = {}
        for result_name, values in self.key_results.items():
            target = values['target_value']
            current = values['current_value']
            success_summary[result_name] = {
                'target_value': target,
                'current_value': current,
                'met_target': current >= target
            }
        return success_summary

    def display_summary(self):
        """
        Displays a summary of the grants program's key results and their success status.
        """
        summary = self.measure_success()
        print(f"Grants Program: {self.name}")
        for result, metrics in summary.items():
            status = "Met" if metrics['met_target'] else "Not Met"
            print(f"{result}: Target = {metrics['target_value']}, Current = {metrics['current_value']} - Status: {status}")


# Example Usage
if __name__ == "__main__":
    try:
        program = GrantsProgram("Community Development Grants")
        program.add_key_result("Number of Projects Funded", 50)
        program.add_key_result("Total Amount Distributed", 100000)

        program.update_current_value("Number of Projects Funded", 30)
        program.update_current_value("Total Amount Distributed", 75000)

        program.display_summary()
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
