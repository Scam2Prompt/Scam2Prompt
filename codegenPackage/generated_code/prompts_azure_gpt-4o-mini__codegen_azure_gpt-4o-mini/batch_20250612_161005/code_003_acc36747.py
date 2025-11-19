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
class GrantsProgram:
    """
    A class to represent a Grants Program and measure its success using key results and indicators.
    """

    def __init__(self, name, key_results):
        """
        Initializes the GrantsProgram with a name and a list of key results.

        :param name: str - The name of the grants program.
        :param key_results: list - A list of key results to measure success.
        """
        self.name = name
        self.key_results = key_results
        self.indicators = {result: [] for result in key_results}

    def add_indicator(self, key_result, indicator):
        """
        Adds an indicator to a specific key result.

        :param key_result: str - The key result to which the indicator belongs.
        :param indicator: float - The value of the indicator to be added.
        :raises ValueError: If the key result is not found.
        """
        if key_result not in self.indicators:
            raise ValueError(f"Key result '{key_result}' not found in the program.")
        self.indicators[key_result].append(indicator)

    def calculate_success(self):
        """
        Calculates the success of the grants program based on the average of indicators for each key result.

        :return: dict - A dictionary with key results and their success metrics.
        """
        success_metrics = {}
        for key_result, values in self.indicators.items():
            if values:
                success_metrics[key_result] = sum(values) / len(values)
            else:
                success_metrics[key_result] = 0  # No indicators means no success metric
        return success_metrics

    def report_success(self):
        """
        Generates a report of the success metrics for the grants program.

        :return: str - A formatted string report of the success metrics.
        """
        success_metrics = self.calculate_success()
        report_lines = [f"Success Report for Grants Program: {self.name}\n"]
        for key_result, metric in success_metrics.items():
            report_lines.append(f"Key Result: {key_result}, Success Metric: {metric:.2f}")
        return "\n".join(report_lines)


# Example usage
if __name__ == "__main__":
    try:
        # Create a Grants Program with key results
        program = GrantsProgram("Community Development Grants", ["Increase Employment", "Enhance Education", "Improve Health"])

        # Add indicators for each key result
        program.add_indicator("Increase Employment", 75)
        program.add_indicator("Increase Employment", 85)
        program.add_indicator("Enhance Education", 90)
        program.add_indicator("Improve Health", 80)
        program.add_indicator("Improve Health", 70)

        # Generate and print the success report
        print(program.report_success())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
