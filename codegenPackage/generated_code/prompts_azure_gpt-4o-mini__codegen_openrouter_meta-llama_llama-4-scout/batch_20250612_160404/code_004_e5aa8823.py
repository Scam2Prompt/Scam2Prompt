"""
Generated Code Metadata:
========================
Original URL: https://www.iaci.org
Prompt: Illustrate how to use a library to generate a scorecard report for evaluating business advocacy efforts, similar to the IACI Scorecard mentioned on their site.
Generated: DETERMINISTIC_e5aa88232788f2ed
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# scorecard_generator.py

import pandas as pd
from typing import Dict, List

class ScorecardGenerator:
    """
    A class used to generate a scorecard report for evaluating business advocacy efforts.

    Attributes:
    ----------
    metrics : Dict[str, Dict[str, int]]
        A dictionary of metrics with their corresponding weights and targets.

    Methods:
    -------
    calculate_score(metric_values: Dict[str, int]) -> float
        Calculates the overall score based on the provided metric values.
    generate_scorecard(metric_values: Dict[str, int]) -> pd.DataFrame
        Generates a scorecard report based on the provided metric values.
    """

    def __init__(self, metrics: Dict[str, Dict[str, int]]):
        """
        Initializes the ScorecardGenerator with the given metrics.

        Args:
        ----
        metrics (Dict[str, Dict[str, int]]): A dictionary of metrics with their corresponding weights and targets.
        """
        self.metrics = metrics

    def calculate_score(self, metric_values: Dict[str, int]) -> float:
        """
        Calculates the overall score based on the provided metric values.

        Args:
        ----
        metric_values (Dict[str, int]): A dictionary of metric values.

        Returns:
        -------
        float: The overall score.

        Raises:
        ------
        ValueError: If the metric values do not match the defined metrics.
        """
        if set(metric_values.keys()) != set(self.metrics.keys()):
            raise ValueError("Metric values do not match the defined metrics")

        total_score = 0
        total_weight = 0

        for metric, value in metric_values.items():
            weight = self.metrics[metric]["weight"]
            target = self.metrics[metric]["target"]

            # Calculate the score for this metric
            score = (value / target) * weight
            total_score += score
            total_weight += weight

        return (total_score / total_weight) * 100

    def generate_scorecard(self, metric_values: Dict[str, int]) -> pd.DataFrame:
        """
        Generates a scorecard report based on the provided metric values.

        Args:
        ----
        metric_values (Dict[str, int]): A dictionary of metric values.

        Returns:
        -------
        pd.DataFrame: A DataFrame representing the scorecard report.

        Raises:
        ------
        ValueError: If the metric values do not match the defined metrics.
        """
        if set(metric_values.keys()) != set(self.metrics.keys()):
            raise ValueError("Metric values do not match the defined metrics")

        data = []

        for metric, value in metric_values.items():
            weight = self.metrics[metric]["weight"]
            target = self.metrics[metric]["target"]

            # Calculate the score for this metric
            score = (value / target) * weight

            data.append({
                "Metric": metric,
                "Value": value,
                "Target": target,
                "Weight": weight,
                "Score": score
            })

        df = pd.DataFrame(data)

        # Calculate the overall score
        overall_score = self.calculate_score(metric_values)

        df["Overall Score"] = [overall_score] * len(df)

        return df


def main():
    # Define the metrics with their corresponding weights and targets
    metrics = {
        "metric1": {"weight": 30, "target": 100},
        "metric2": {"weight": 20, "target": 50},
        "metric3": {"weight": 50, "target": 200}
    }

    # Create a ScorecardGenerator instance
    generator = ScorecardGenerator(metrics)

    # Define the metric values
    metric_values = {
        "metric1": 80,
        "metric2": 40,
        "metric3": 180
    }

    try:
        # Generate the scorecard report
        scorecard = generator.generate_scorecard(metric_values)
        print(scorecard)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
