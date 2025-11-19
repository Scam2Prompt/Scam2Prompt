"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iaci.org
Prompt: Illustrate how to use a library to generate a scorecard report for evaluating business advocacy efforts, similar to the IACI Scorecard mentioned on their site.
Generated: DETERMINISTIC_e5aa88232788f2ed
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

class Scorecard:
    """
    A class to represent a Scorecard for evaluating business advocacy efforts.

    Attributes
    ----------
    metrics : dict
        A dictionary containing the metrics and their weights for the scorecard.
    results : pd.DataFrame
        A DataFrame to store the results of the scorecard evaluations.

    Methods
    -------
    add_metric(metric_name: str, weight: float):
        Adds a metric to the scorecard with its corresponding weight.
    
    evaluate_efforts(data: pd.DataFrame):
        Evaluates the advocacy efforts based on the metrics and returns a scorecard report.
    """
    
    def __init__(self):
        self.metrics = {}
        self.results = pd.DataFrame()

    def add_metric(self, metric_name: str, weight: float):
        """
        Adds a metric to the scorecard with its corresponding weight.

        Parameters
        ----------
        metric_name : str
            The name of the metric to add.
        weight : float
            The weight of the metric in the total score.
        
        Raises
        ------
        ValueError
            If the weight is not a positive value.
        """
        if weight <= 0:
            raise ValueError("Weight must be a positive value.")
        self.metrics[metric_name] = weight

    def evaluate_efforts(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Evaluates the advocacy efforts based on the metrics and returns a scorecard report.

        Parameters
        ----------
        data : pd.DataFrame
            A DataFrame containing the evaluation data with metrics as columns.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the scorecard report with total scores.
        
        Raises
        ------
        ValueError
            If the DataFrame does not contain required metrics.
        """
        # Validate input data
        missing_metrics = [metric for metric in self.metrics.keys() if metric not in data.columns]
        if missing_metrics:
            raise ValueError(f"Missing metrics in data: {', '.join(missing_metrics)}")

        # Calculate scores
        total_weight = sum(self.metrics.values())
        for metric, weight in self.metrics.items():
            data[f"{metric}_score"] = data[metric] * (weight / total_weight)

        # Add total score column
        data['total_score'] = data[[f"{metric}_score" for metric in self.metrics]].sum(axis=1)

        # Prepare the final report
        self.results = data[['total_score'] + [f"{metric}_score" for metric in self.metrics]]
        return self.results

# Example usage
if __name__ == "__main__":
    # Create sample data
    sample_data = pd.DataFrame({
        'advocacy_effectiveness': [80, 70, 90],
        'community_engagement': [60, 50, 80],
        'policy_influence': [75, 85, 65]
    })

    # Initialize scorecard instance
    scorecard = Scorecard()

    # Add metrics with weights
    scorecard.add_metric('advocacy_effectiveness', 0.4)
    scorecard.add_metric('community_engagement', 0.3)
    scorecard.add_metric('policy_influence', 0.3)

    # Evaluate the efforts
    try:
        report = scorecard.evaluate_efforts(sample_data)
        print("Scorecard Report:")
        print(report)
    except ValueError as e:
        print(f"Error: {e}")
```
