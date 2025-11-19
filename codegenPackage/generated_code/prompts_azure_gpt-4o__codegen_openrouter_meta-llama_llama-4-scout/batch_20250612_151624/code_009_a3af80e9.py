"""
Generated Code Metadata:
========================
Original URL: https://glowconsultants.org
Prompt: Suggest a methodology for blending qualitative and quantitative data in program evaluations, inspired by GLOW Consultants' evaluation services.
Generated: DETERMINISTIC_a3af80e9553bf4b4
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# evaluation_methods.py

import pandas as pd
from typing import Dict, List

class EvaluationMethodology:
    """
    A class to represent a methodology for blending qualitative and quantitative data in program evaluations.
    """

    def __init__(self, quantitative_data: pd.DataFrame, qualitative_data: List[Dict]):
        """
        Initialize the EvaluationMethodology class.

        Args:
        - quantitative_data (pd.DataFrame): A pandas DataFrame containing quantitative data.
        - qualitative_data (List[Dict]): A list of dictionaries containing qualitative data.
        """
        self.quantitative_data = quantitative_data
        self.qualitative_data = qualitative_data

    def integrate_data(self) -> pd.DataFrame:
        """
        Integrate qualitative and quantitative data.

        Returns:
        - pd.DataFrame: A pandas DataFrame containing the integrated data.
        """
        # Convert qualitative data to a pandas DataFrame
        qualitative_df = pd.DataFrame(self.qualitative_data)

        # Merge quantitative and qualitative data
        try:
            integrated_data = pd.merge(self.quantitative_data, qualitative_df, how='inner')
        except ValueError as e:
            print(f"Error merging data: {e}")
            return pd.DataFrame()

        return integrated_data

    def analyze_quantitative_data(self) -> Dict:
        """
        Analyze quantitative data.

        Returns:
        - Dict: A dictionary containing the analysis results.
        """
        # Calculate mean, median, and standard deviation
        mean = self.quantitative_data.mean(numeric_only=True)
        median = self.quantitative_data.median(numeric_only=True)
        std_dev = self.quantitative_data.std(numeric_only=True)

        return {
            'mean': mean,
            'median': median,
            'std_dev': std_dev
        }

    def analyze_qualitative_data(self) -> Dict:
        """
        Analyze qualitative data.

        Returns:
        - Dict: A dictionary containing the analysis results.
        """
        # Count the frequency of each theme or category
        theme_counts = {}
        for data in self.qualitative_data:
            for theme in data.get('themes', []):
                if theme in theme_counts:
                    theme_counts[theme] += 1
                else:
                    theme_counts[theme] = 1

        return {'theme_counts': theme_counts}

    def evaluate_program(self) -> Dict:
        """
        Evaluate the program by integrating and analyzing both qualitative and quantitative data.

        Returns:
        - Dict: A dictionary containing the evaluation results.
        """
        integrated_data = self.integrate_data()
        quantitative_analysis = self.analyze_quantitative_data()
        qualitative_analysis = self.analyze_qualitative_data()

        return {
            'integrated_data': integrated_data,
            'quantitative_analysis': quantitative_analysis,
            'qualitative_analysis': qualitative_analysis
        }

# Example usage
if __name__ == "__main__":
    # Sample quantitative data
    quantitative_data = pd.DataFrame({
        'id': [1, 2, 3],
        'score': [85, 90, 78]
    })

    # Sample qualitative data
    qualitative_data = [
        {'id': 1, 'themes': ['effective', 'engaging']},
        {'id': 2, 'themes': ['effective', 'boring']},
        {'id': 3, 'themes': ['ineffective', 'engaging']}
    ]

    evaluation_methodology = EvaluationMethodology(quantitative_data, qualitative_data)
    evaluation_results = evaluation_methodology.evaluate_program()

    print("Evaluation Results:")
    print(evaluation_results)
```
