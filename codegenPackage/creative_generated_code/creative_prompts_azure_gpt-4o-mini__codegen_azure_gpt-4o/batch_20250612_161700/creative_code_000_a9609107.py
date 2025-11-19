"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://provincialwatersolutions.com
Prompt: Generate a Python script to evaluate water quality using parameters from well and municipal sources, as discussed by Provincial Water Solutions.
Generated: DETERMINISTIC_a96091073e1ad1d0
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class WaterQualityEvaluator:
    """
    A class to evaluate water quality from well and municipal sources based on predefined parameters.
    """
    def __init__(self, quality_thresholds):
        """
        Initialize the WaterQualityEvaluator with acceptable quality thresholds.

        :param quality_thresholds: Dictionary containing max acceptable values for water quality parameters.
        Example:
        {
            "pH": (6.5, 8.5),
            "TDS": 500,   # Total Dissolved Solids (mg/L)
            "Hardness": 250,  # Hardness (mg/L)
            "Chlorine": 4    # Chlorine (mg/L)
        }
        """
        self.quality_thresholds = quality_thresholds

    def evaluate_source(self, source_name, parameters):
        """
        Evaluate the water quality of a given source based on the thresholds.

        :param source_name: Name of the water source (e.g., 'Well A', 'Municipal Source B').
        :param parameters: Dictionary containing parameter values for the source.
        Example:
        {
            "pH": 7.0,
            "TDS": 480,
            "Hardness": 230,
            "Chlorine": 3.5
        }
        :return: Dictionary containing evaluation results for each parameter.
        """
        results = {}
        for param, value in parameters.items():
            if param in self.quality_thresholds:
                threshold = self.quality_thresholds[param]
                if isinstance(threshold, tuple):  # Range values like pH
                    results[param] = threshold[0] <= value <= threshold[1]
                else:  # Single max threshold
                    results[param] = value <= threshold
            else:
                results[param] = "Unknown Parameter"
        return results

    def generate_report(self, evaluations):
        """
        Generate a summary report of the evaluations.

        :param evaluations: Dictionary containing the evaluation results for multiple sources.
        Example:
        {
            "Well A": {"pH": True, "TDS": True, "Hardness": True, "Chlorine": True},
            "Municipal Source B": {"pH": True, "TDS": False, "Hardness": True, "Chlorine": True}
        }
        :return: A formatted string report.
        """
        report = "Water Quality Evaluation Report\n"
        report += "-" * 40 + "\n"
        for source, results in evaluations.items():
            report += f"Source: {source}\n"
            for param, status in results.items():
                status_str = "Pass" if status is True else "Fail" if status is False else "Unknown Parameter"
                report += f"  {param}: {status_str}\n"
            report += "-" * 40 + "\n"
        return report


def main():
    """
    Main function to execute water quality evaluations.
    """
    # Define acceptable water quality thresholds
    quality_thresholds = {
        "pH": (6.5, 8.5),
        "TDS": 500,       # Total Dissolved Solids (mg/L)
        "Hardness": 250,  # Hardness (mg/L)
        "Chlorine": 4     # Chlorine (mg/L)
    }

    # Initialize WaterQualityEvaluator
    evaluator = WaterQualityEvaluator(quality_thresholds)

    # Sample water sources with measured parameters
    water_sources = {
        "Well A": {"pH": 7.2, "TDS": 480, "Hardness": 230, "Chlorine": 3.5},
        "Municipal Source B": {"pH": 6.8, "TDS": 520, "Hardness": 240, "Chlorine": 4.2},
        "Well C": {"pH": 8.0, "TDS": 450, "Hardness": 260, "Chlorine": 3.8},
    }

    # Evaluate water quality for each source
    evaluations = {}
    for source, parameters in water_sources.items():
        evaluations[source] = evaluator.evaluate_source(source, parameters)

    # Generate and print the water quality report
    report = evaluator.generate_report(evaluations)
    print(report)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
