"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://institutopangoa.edu.pe
Prompt: Write a script to analyze student performance data for technical programs such as "Mecatrónica Automotriz," using the educational focus described on the Instituto Pangoa site.
Generated: DETERMINISTIC_27c44ed47cdc7231
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt

class StudentPerformanceAnalyzer:
    """A class to analyze student performance data for technical programs."""

    def __init__(self, data_file):
        """Initialize the analyzer with a data file.
        
        Args:
            data_file (str): The path to the CSV file containing student performance data.
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """Load student performance data from the CSV file."""
        try:
            self.data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
        except pd.errors.ParserError:
            print("Error: The file could not be parsed.")

    def clean_data(self):
        """Clean the loaded data by removing null values and duplicates."""
        if self.data is not None:
            initial_shape = self.data.shape
            self.data.dropna(inplace=True)  # Remove rows with null values
            self.data.drop_duplicates(inplace=True)  # Remove duplicate rows
            print(f"Data cleaned. Shape changed from {initial_shape} to {self.data.shape}.")
        else:
            print("Error: Data not loaded. Please load data first.")

    def analyze_performance(self):
        """Analyze performance data and generate statistics."""
        if self.data is not None:
            performance_stats = self.data.describe()  # Get descriptive statistics
            print("Performance Statistics:")
            print(performance_stats)
            return performance_stats
        else:
            print("Error: Data not loaded. Please load data first.")

    def visualize_performance(self):
        """Visualize student performance data using a bar chart."""
        if self.data is not None:
            try:
                self.data['AverageScore'] = self.data[['ExamScore', 'ProjectScore']].mean(axis=1)
                plt.figure(figsize=(10, 6))
                plt.bar(self.data['StudentID'], self.data['AverageScore'], color='skyblue')
                plt.title('Student Average Scores')
                plt.xlabel('Student ID')
                plt.ylabel('Average Score')
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()
            except KeyError as e:
                print(f"Error: Missing column in data - {e}")
        else:
            print("Error: Data not loaded. Please load data first.")

def main():
    """Main function to run the performance analysis."""
    analyzer = StudentPerformanceAnalyzer('student_performance.csv')  # Change to your file path
    analyzer.load_data()
    analyzer.clean_data()
    analyzer.analyze_performance()
    analyzer.visualize_performance()

if __name__ == "__main__":
    main()
```

This Python script assumes you have a CSV file named `student_performance.csv` with columns such as `StudentID`, `ExamScore`, and `ProjectScore`. Adjust the column names in the code if your file structure is different. Make sure to install the required libraries if not already installed (e.g., `pandas`, `matplotlib`).
