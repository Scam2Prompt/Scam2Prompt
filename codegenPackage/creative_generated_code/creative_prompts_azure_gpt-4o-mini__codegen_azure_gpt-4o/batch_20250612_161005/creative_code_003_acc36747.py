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
# grants_program_success.py

"""
This script provides a framework to measure the success of a grants program
using key results and indicators based on the Grants Program Canvas.

The program defines functions to track metrics, calculate key performance indicators (KPIs),
and generate a summary report. It uses a dictionary to store indicators and their values.
"""

import json

class GrantsProgram:
    def __init__(self, program_name):
        """
        Initialize the grants program with a name and an empty dictionary for indicators.
        :param program_name: Name of the grants program.
        """
        self.program_name = program_name
        self.indicators = {}

    def add_indicator(self, indicator_name, target_value):
        """
        Add a key result indicator to track.
        :param indicator_name: Name of the indicator (e.g., "Number of projects funded").
        :param target_value: Target value for this indicator.
        """
        if indicator_name in self.indicators:
            raise ValueError(f"Indicator '{indicator_name}' already exists.")
        self.indicators[indicator_name] = {"target": target_value, "actual": 0}

    def update_actual_value(self, indicator_name, actual_value):
        """
        Update the actual value for a specific indicator.
        :param indicator_name: Name of the indicator to update.
        :param actual_value: Actual value achieved for the indicator.
        """
        if indicator_name not in self.indicators:
            raise ValueError(f"Indicator '{indicator_name}' does not exist.")
        self.indicators[indicator_name]["actual"] = actual_value

    def calculate_success_rate(self, indicator_name):
        """
        Calculate the success rate for a given indicator.
        :param indicator_name: Name of the indicator to calculate the success rate for.
        :return: Success rate as a percentage.
        """
        if indicator_name not in self.indicators:
            raise ValueError(f"Indicator '{indicator_name}' does not exist.")
        indicator = self.indicators[indicator_name]
        if indicator["target"] == 0:
            raise ValueError("Target value cannot be zero.")
        success_rate = (indicator["actual"] / indicator["target"]) * 100
        return round(success_rate, 2)

    def generate_report(self):
        """
        Generate a summary report for the grants program.
        :return: Report as a JSON object.
        """
        report = {
            "Program Name": self.program_name,
            "Indicators": [],
        }
        for name, data in self.indicators.items():
            success_rate = self.calculate_success_rate(name)
            report["Indicators"].append({
                "Indicator Name": name,
                "Target Value": data["target"],
                "Actual Value": data["actual"],
                "Success Rate (%)": success_rate,
            })
        return json.dumps(report, indent=4)

# Example usage:
if __name__ == "__main__":
    try:
        # Instantiate the grants program
        grants_program = GrantsProgram("Community Development Grants")

        # Add indicators
        grants_program.add_indicator("Number of projects funded", 50)
        grants_program.add_indicator("Total funds distributed ($)", 100000)

        # Update actual values
        grants_program.update_actual_value("Number of projects funded", 42)
        grants_program.update_actual_value("Total funds distributed ($)", 85000)

        # Generate and print the report
        report = grants_program.generate_report()
        print("Grants Program Success Report:")
        print(report)

    except Exception as e:
        # Handle errors gracefully
        print(f"Error: {e}")
```
