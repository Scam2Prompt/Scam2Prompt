"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: Generate a Python script to analyze student performance data for a coaching academy like Potencia Academy, focusing on JEE and NEET preparation.
Generated: DETERMINISTIC_ed55983f9662d950
Batch ID: 20250612_155654
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

class StudentPerformanceAnalyzer:
    """
    A class to analyze student performance data for JEE and NEET preparation.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with the provided data file.

        :param data_file: str, path to the CSV file containing student performance data
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads the student performance data from a CSV file.

        :return: DataFrame containing the student performance data
        """
        try:
            data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
            return data
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except pd.errors.ParserError:
            print("Error: The file could not be parsed.")
            raise

    def summarize_performance(self):
        """
        Summarizes the performance of students by calculating mean and median scores.

        :return: DataFrame with summary statistics
        """
        try:
            summary = self.data[['StudentID', 'Score']].groupby('StudentID').agg(['mean', 'median'])
            summary.columns = ['Mean Score', 'Median Score']
            print("Performance summary calculated.")
            return summary
        except KeyError as e:
            print(f"Error: Missing expected column in data - {e}")
            raise

    def visualize_performance(self):
        """
        Visualizes the performance of students using a histogram.

        :return: None
        """
        try:
            plt.figure(figsize=(10, 6))
            plt.hist(self.data['Score'], bins=20, color='blue', alpha=0.7)
            plt.title('Distribution of Student Scores')
            plt.xlabel('Scores')
            plt.ylabel('Number of Students')
            plt.grid(axis='y', alpha=0.75)
            plt.axvline(self.data['Score'].mean(), color='red', linestyle='dashed', linewidth=1, label='Mean Score')
            plt.axvline(self.data['Score'].median(), color='green', linestyle='dashed', linewidth=1, label='Median Score')
            plt.legend()
            plt.show()
            print("Performance visualization displayed.")
        except KeyError as e:
            print(f"Error: Missing expected column in data - {e}")
            raise

    def save_summary(self, summary, output_file):
        """
        Saves the performance summary to a CSV file.

        :param summary: DataFrame, the summary statistics to save
        :param output_file: str, path to the output CSV file
        """
        try:
            summary.to_csv(output_file)
            print(f"Summary saved to {output_file}.")
        except Exception as e:
            print(f"Error saving summary: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    try:
        analyzer = StudentPerformanceAnalyzer('student_performance.csv')
        summary = analyzer.summarize_performance()
        analyzer.visualize_performance()
        analyzer.save_summary(summary, 'performance_summary.csv')
    except Exception as e:
        print(f"An error occurred: {e}")
```
