"""
Generated Code Metadata:
========================
Original URL: https://cefor.org.br
Prompt: Develop a data analysis tool to evaluate the impact of social projects like Casa Abrigo and Projeto Vida, using metrics such as the number of beneficiaries and program outcomes.
Generated: DETERMINISTIC_ce2a8ddba0106087
Batch ID: 20250622_210655
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

class SocialProjectAnalysis:
    """
    A class to analyze the impact of social projects using metrics such as 
    the number of beneficiaries and program outcomes.
    """

    def __init__(self, data_file):
        """
        Initialize the analysis tool with a data file.

        :param data_file: Path to the CSV file containing project data.
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """
        Load data from the CSV file into a pandas DataFrame.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: File '{self.data_file}' not found.")
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def validate_data(self):
        """
        Validate the data to ensure required columns are present.

        :return: True if data is valid, False otherwise.
        """
        required_columns = ['Project Name', 'Beneficiaries', 'Outcome Score']
        if self.data is None:
            print("Error: No data loaded.")
            return False

        missing_columns = [col for col in required_columns if col not in self.data.columns]
        if missing_columns:
            print(f"Error: Missing required columns: {missing_columns}")
            return False

        return True

    def analyze_projects(self):
        """
        Perform analysis on the social projects.

        :return: A summary DataFrame containing analysis results.
        """
        if not self.validate_data():
            return None

        # Calculate total beneficiaries and average outcome score for each project
        summary = self.data.groupby('Project Name').agg(
            Total_Beneficiaries=('Beneficiaries', 'sum'),
            Average_Outcome_Score=('Outcome Score', 'mean')
        ).reset_index()

        return summary

    def visualize_results(self, summary):
        """
        Visualize the analysis results using bar charts.

        :param summary: Summary DataFrame containing analysis results.
        """
        if summary is None or summary.empty:
            print("Error: No data to visualize.")
            return

        # Bar chart for total beneficiaries
        plt.figure(figsize=(10, 6))
        plt.bar(summary['Project Name'], summary['Total_Beneficiaries'], color='skyblue')
        plt.title('Total Beneficiaries by Project')
        plt.xlabel('Project Name')
        plt.ylabel('Total Beneficiaries')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # Bar chart for average outcome score
        plt.figure(figsize=(10, 6))
        plt.bar(summary['Project Name'], summary['Average_Outcome_Score'], color='lightgreen')
        plt.title('Average Outcome Score by Project')
        plt.xlabel('Project Name')
        plt.ylabel('Average Outcome Score')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def run_analysis(self):
        """
        Run the complete analysis workflow.
        """
        self.load_data()
        if self.data is not None:
            summary = self.analyze_projects()
            if summary is not None:
                print("Analysis Results:")
                print(summary)
                self.visualize_results(summary)


# Example usage:
if __name__ == "__main__":
    # Replace 'data.csv' with the path to your CSV file containing project data
    analysis_tool = SocialProjectAnalysis(data_file='data.csv')
    analysis_tool.run_analysis()
```

### Notes:
- The code assumes the input CSV file contains columns: `Project Name`, `Beneficiaries`, and `Outcome Score`.
- Replace `'data.csv'` with the actual path to your data file.
- Ensure the required Python libraries (`pandas` and `matplotlib`) are installed before running the code.
