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
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class ProgramEvaluation:
    """
    A class to blend qualitative and quantitative data for program evaluations.
    """

    def __init__(self, quantitative_data: pd.DataFrame, qualitative_data: pd.DataFrame):
        """
        Initializes the ProgramEvaluation class with quantitative and qualitative data.

        Parameters:
        quantitative_data (pd.DataFrame): DataFrame containing quantitative metrics.
        qualitative_data (pd.DataFrame): DataFrame containing qualitative feedback.
        """
        self.quantitative_data = quantitative_data
        self.qualitative_data = qualitative_data

    def preprocess_data(self):
        """
        Preprocesses the quantitative and qualitative data for analysis.
        This includes handling missing values and ensuring data types are correct.
        """
        # Handle missing values in quantitative data
        self.quantitative_data.fillna(self.quantitative_data.mean(), inplace=True)

        # Convert qualitative data to a consistent format
        self.qualitative_data['feedback'] = self.qualitative_data['feedback'].str.lower().str.strip()

    def analyze_quantitative(self):
        """
        Analyzes the quantitative data and returns summary statistics.
        
        Returns:
        pd.DataFrame: Summary statistics of the quantitative data.
        """
        return self.quantitative_data.describe()

    def analyze_qualitative(self):
        """
        Analyzes the qualitative data and returns frequency counts of feedback themes.
        
        Returns:
        pd.Series: Frequency counts of unique feedback themes.
        """
        return self.qualitative_data['feedback'].value_counts()

    def visualize_data(self):
        """
        Visualizes the quantitative data and qualitative feedback.
        Generates plots for better understanding of the data.
        """
        # Plotting quantitative data
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=self.quantitative_data)
        plt.title('Quantitative Data Distribution')
        plt.ylabel('Values')
        plt.xticks(rotation=45)
        plt.show()

        # Plotting qualitative data
        feedback_counts = self.analyze_qualitative()
        plt.figure(figsize=(12, 6))
        sns.barplot(x=feedback_counts.index, y=feedback_counts.values)
        plt.title('Qualitative Feedback Frequency')
        plt.ylabel('Count')
        plt.xlabel('Feedback Themes')
        plt.xticks(rotation=45)
        plt.show()

    def blend_data(self):
        """
        Blends qualitative and quantitative data into a single report.
        
        Returns:
        dict: A dictionary containing both quantitative and qualitative analysis results.
        """
        quantitative_summary = self.analyze_quantitative()
        qualitative_summary = self.analyze_qualitative()

        blended_report = {
            'quantitative_summary': quantitative_summary,
            'qualitative_summary': qualitative_summary
        }

        return blended_report

# Example usage
if __name__ == "__main__":
    try:
        # Sample quantitative data
        quantitative_data = pd.DataFrame({
            'metric1': np.random.rand(100),
            'metric2': np.random.rand(100) * 100,
            'metric3': np.random.randint(1, 10, size=100)
        })

        # Sample qualitative data
        qualitative_data = pd.DataFrame({
            'feedback': [
                'Great program', 'Needs improvement', 'Excellent service',
                'Could be better', 'Great program', 'Excellent service'
            ]
        })

        # Initialize the ProgramEvaluation class
        evaluation = ProgramEvaluation(quantitative_data, qualitative_data)

        # Preprocess data
        evaluation.preprocess_data()

        # Analyze and visualize data
        print(evaluation.blend_data())
        evaluation.visualize_data()

    except Exception as e:
        print(f"An error occurred: {e}")
```
