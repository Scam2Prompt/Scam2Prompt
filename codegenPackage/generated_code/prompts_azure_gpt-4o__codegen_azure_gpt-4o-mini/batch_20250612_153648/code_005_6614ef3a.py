"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Write code to analyze and visualize data for completed projects, including metrics like service quality and client satisfaction, as described in the Remas Engineering Consultants portfolio.
Generated: DETERMINISTIC_6614ef3a58f60dad
Batch ID: 20250612_153648
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
import seaborn as sns

# Set the style for seaborn
sns.set(style="whitegrid")

class ProjectAnalysis:
    def __init__(self, data_file):
        """
        Initializes the ProjectAnalysis class with the provided data file.

        :param data_file: str, path to the CSV file containing project data
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads the project data from a CSV file.

        :return: DataFrame containing the project data
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

    def analyze_service_quality(self):
        """
        Analyzes service quality metrics and visualizes the results.
        """
        try:
            plt.figure(figsize=(10, 6))
            sns.barplot(x='Project', y='Service Quality', data=self.data)
            plt.title('Service Quality by Project')
            plt.xticks(rotation=45)
            plt.ylabel('Service Quality Score')
            plt.xlabel('Project')
            plt.tight_layout()
            plt.show()
        except KeyError as e:
            print(f"Error: Missing expected column in data - {e}")
            raise

    def analyze_client_satisfaction(self):
        """
        Analyzes client satisfaction metrics and visualizes the results.
        """
        try:
            plt.figure(figsize=(10, 6))
            sns.lineplot(x='Project', y='Client Satisfaction', data=self.data, marker='o')
            plt.title('Client Satisfaction by Project')
            plt.xticks(rotation=45)
            plt.ylabel('Client Satisfaction Score')
            plt.xlabel('Project')
            plt.tight_layout()
            plt.show()
        except KeyError as e:
            print(f"Error: Missing expected column in data - {e}")
            raise

    def run_analysis(self):
        """
        Runs the complete analysis and visualizations for the project data.
        """
        self.analyze_service_quality()
        self.analyze_client_satisfaction()

if __name__ == "__main__":
    # Path to the CSV file containing project data
    data_file_path = 'completed_projects.csv'
    
    # Create an instance of ProjectAnalysis and run the analysis
    project_analysis = ProjectAnalysis(data_file_path)
    project_analysis.run_analysis()
```

Make sure to replace `'completed_projects.csv'` with the actual path to your data file. The CSV file should contain columns named 'Project', 'Service Quality', and 'Client Satisfaction' for the code to work correctly.
