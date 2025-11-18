"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taiko-t.com
Prompt: Write code to analyze team performance and efficiency in construction projects, focusing on tasks like pole installation and fence construction, using Python and data visualization libraries.
Generated: DETERMINISTIC_6c2569ff308271a4
Batch ID: 20250612_150342
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
import seaborn as sns
import numpy as np

# Set visualization style
sns.set(style="whitegrid")

class TeamPerformanceAnalyzer:
    def __init__(self, data_file):
        """
        Initialize the analyzer with data from a CSV file.

        :param data_file: Path to the CSV file containing project data.
        """
        self.data_file = data_file
        self.data = None
        self.load_data()

    def load_data(self):
        """Load project data from the specified CSV file."""
        try:
            self.data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except Exception as e:
            print(f"An error occurred while loading the data: {e}")
            raise

    def preprocess_data(self):
        """Preprocess the data to ensure it is clean and usable."""
        # Convert dates to datetime objects
        self.data['start_date'] = pd.to_datetime(self.data['start_date'])
        self.data['end_date'] = pd.to_datetime(self.data['end_date'])
        
        # Calculate duration of tasks in days
        self.data['duration'] = (self.data['end_date'] - self.data['start_date']).dt.days
        
        # Handle missing values
        self.data.fillna(0, inplace=True)
        print("Data preprocessing completed.")

    def analyze_performance(self):
        """Analyze team performance and efficiency."""
        performance_summary = self.data.groupby('task_type').agg(
            total_tasks=('task_id', 'count'),
            total_duration=('duration', 'sum'),
            avg_duration=('duration', 'mean')
        ).reset_index()

        print(performance_summary)
        return performance_summary

    def visualize_performance(self, performance_summary):
        """Visualize the team performance using bar plots."""
        plt.figure(figsize=(10, 6))

        # Bar plot for total tasks by task type
        sns.barplot(data=performance_summary, x='task_type', y='total_tasks', palette='viridis')
        plt.title('Total Tasks by Task Type')
        plt.xlabel('Task Type')
        plt.ylabel('Total Tasks')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # Bar plot for average duration by task type
        plt.figure(figsize=(10, 6))
        sns.barplot(data=performance_summary, x='task_type', y='avg_duration', palette='plasma')
        plt.title('Average Duration by Task Type')
        plt.xlabel('Task Type')
        plt.ylabel('Average Duration (Days)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Replace 'construction_project_data.csv' with the path to your CSV file
    analyzer = TeamPerformanceAnalyzer(data_file='construction_project_data.csv')
    analyzer.preprocess_data()
    performance_summary = analyzer.analyze_performance()
    analyzer.visualize_performance(performance_summary)
```
