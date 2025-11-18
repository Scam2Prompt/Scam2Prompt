"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimisenow.net
Prompt: Generate code to analyze business workflows and identify bottlenecks using data analytics tools. Focus on optimizing processes for efficiency and productivity as described by OptimiseNow Consultancy.
Generated: DETERMINISTIC_97959d53409b172c
Batch ID: 20250612_154142
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
from scipy.stats import zscore

class WorkflowAnalyzer:
    """
    A class to analyze business workflows and identify bottlenecks for process optimization.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initialize the WorkflowAnalyzer with workflow data.

        :param data: A pandas DataFrame containing workflow data. 
                     Expected columns: ['Step', 'Duration', 'StartTime', 'EndTime', 'ResourceUsed']
        """
        self.data = data
        self.validate_data()

    def validate_data(self):
        """
        Validate the input data to ensure required columns exist.
        Raises ValueError if columns are missing.
        """
        required_columns = ['Step', 'Duration', 'StartTime', 'EndTime', 'ResourceUsed']
        missing_columns = [col for col in required_columns if col not in self.data.columns]
        if missing_columns:
            raise ValueError(f"Input data is missing required columns: {missing_columns}")

    def detect_bottlenecks(self) -> pd.DataFrame:
        """
        Detect bottlenecks in the workflow by analyzing step durations and identifying outliers.

        :return: A DataFrame of bottleneck steps with their details.
        """
        self.data['ZScoreDuration'] = zscore(self.data['Duration'])  # Standardize durations
        bottlenecks = self.data[self.data['ZScoreDuration'] > 2]  # Identify outliers (Z-Score > 2)

        # Sort bottlenecks by duration in descending order for prioritization
        bottlenecks = bottlenecks.sort_values(by='Duration', ascending=False)
        
        return bottlenecks

    def suggest_optimizations(self) -> pd.DataFrame:
        """
        Suggest optimization strategies based on the detected bottlenecks.

        :return: A DataFrame with optimization suggestions.
        """
        bottlenecks = self.detect_bottlenecks()
        suggestions = []

        for _, row in bottlenecks.iterrows():
            optimization = f"Consider redistributing resources or automating step '{row['Step']}' to reduce duration."
            suggestions.append({
                'Step': row['Step'],
                'Suggestion': optimization,
                'Duration': row['Duration']
            })

        return pd.DataFrame(suggestions)

    def generate_summary(self) -> None:
        """
        Generate and print a summary of workflow analysis and optimization suggestions.
        """
        print("Workflow Analysis Summary")
        print("--------------------------")
        print(f"Total Workflow Steps: {len(self.data)}")
        bottlenecks = self.detect_bottlenecks()
        print(f"Bottleneck Steps Identified: {len(bottlenecks)}")
        
        suggestions = self.suggest_optimizations()
        print("\nOptimization Suggestions:")
        print(suggestions)

# Example Usage:
if __name__ == "__main__":
    try:
        # Sample workflow data
        workflow_data = pd.DataFrame({
            'Step': ['A', 'B', 'C', 'D', 'E'],
            'Duration': [120, 45, 300, 60, 20],
            'StartTime': ['08:00', '08:30', '09:00', '10:00', '10:30'],
            'EndTime': ['08:30', '09:15', '12:00', '11:00', '10:50'],
            'ResourceUsed': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
        })

        # Initialize the analyzer and perform analysis
        analyzer = WorkflowAnalyzer(workflow_data)
        analyzer.generate_summary()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
