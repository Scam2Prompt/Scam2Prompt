"""
Generated Code Metadata:
========================
Original URL: https://www.igeog.uerj.br
Prompt: Write a Python script to analyze the selection process for professor positions at the Instituto de Geografia, Universidade do Estado do Rio de Janeiro (UERJ), including calculating the number of applicants and interviewees for each position.
Generated: DETERMINISTIC_9fcbf0cb94a38c9b
Batch ID: 20250622_211713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class ProfessorSelectionAnalyzer:
    """
    A class to analyze the selection process for professor positions.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with the provided data file.

        :param data_file: Path to the CSV file containing selection data.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads the selection data from a CSV file.

        :return: DataFrame containing the selection data.
        """
        try:
            data = pd.read_csv(self.data_file)
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The file is empty.")
        except pd.errors.ParserError:
            raise ValueError("Error parsing the file. Please check the format.")

    def analyze_selection(self):
        """
        Analyzes the selection process and calculates the number of applicants
        and interviewees for each position.

        :return: DataFrame with the analysis results.
        """
        try:
            # Grouping the data by position and counting applicants and interviewees
            analysis = self.data.groupby('Position').agg(
                total_applicants=('Applicant', 'count'),
                total_interviewees=('Interviewee', 'count')
            ).reset_index()

            return analysis
        except KeyError as e:
            raise KeyError(f"Missing expected column in data: {e}")

    def save_analysis(self, output_file):
        """
        Saves the analysis results to a CSV file.

        :param output_file: Path to the output CSV file.
        """
        analysis = self.analyze_selection()
        try:
            analysis.to_csv(output_file, index=False)
            print(f"Analysis saved to {output_file}")
        except Exception as e:
            raise RuntimeError(f"Failed to save analysis: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        analyzer = ProfessorSelectionAnalyzer('selection_data.csv')
        analyzer.save_analysis('analysis_results.csv')
    except Exception as e:
        print(f"An error occurred: {e}")
```

Make sure to replace `'selection_data.csv'` with the actual path to your data file containing the selection process information. The expected columns in the CSV file are `Position`, `Applicant`, and `Interviewee`.
