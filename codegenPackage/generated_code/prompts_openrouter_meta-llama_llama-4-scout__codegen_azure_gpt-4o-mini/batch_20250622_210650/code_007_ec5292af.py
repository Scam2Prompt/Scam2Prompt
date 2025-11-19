"""
Generated Code Metadata:
========================
Original URL: https://deepti.ac.in
Prompt: Develop a Python script to analyze student performance in CBSE exams, specifically for classes X and XII.
Generated: DETERMINISTIC_ec5292af8e12bbc9
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt

class StudentPerformanceAnalyzer:
    """
    A class to analyze student performance in CBSE exams for classes X and XII.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with the provided data file.

        :param data_file: str - Path to the CSV file containing student performance data.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads the student performance data from a CSV file.

        :return: DataFrame - A pandas DataFrame containing the student data.
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

    def analyze_performance(self):
        """
        Analyzes the performance of students and generates summary statistics.
        """
        try:
            # Grouping by class and calculating mean scores
            summary = self.data.groupby('Class')['Score'].agg(['mean', 'median', 'std', 'count'])
            print("Performance analysis completed.")
            return summary
        except KeyError as e:
            print(f"Error: Missing expected column in data - {e}")
            raise

    def plot_performance(self):
        """
        Plots the performance of students in a bar chart.
        """
        try:
            summary = self.analyze_performance()
            summary['mean'].plot(kind='bar', yerr=summary['std'], capsize=4)
            plt.title('Average Student Performance in CBSE Exams')
            plt.xlabel('Class')
            plt.ylabel('Average Score')
            plt.xticks(rotation=0)
            plt.grid(axis='y')
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error while plotting performance: {e}")
            raise

if __name__ == "__main__":
    # Path to the CSV file containing student performance data
    data_file_path = 'student_performance.csv'
    
    # Create an instance of the analyzer
    analyzer = StudentPerformanceAnalyzer(data_file_path)
    
    # Perform analysis and plot results
    try:
        performance_summary = analyzer.analyze_performance()
        print(performance_summary)
        analyzer.plot_performance()
    except Exception as e:
        print(f"An error occurred during analysis: {e}")
```

Make sure to have a CSV file named `student_performance.csv` with at least the columns `Class` and `Score` for the script to run successfully.
