"""
Generated Code Metadata:
========================
Original URL: https://debridgeadvisory.com
Prompt: Write a script to analyze student enrollment data for sales training programs, categorizing them by industry (e.g., real estate, automobile, financial products, insurance) as offered by Debridge Advisory.
Generated: DETERMINISTIC_5ccfe19355fab0c7
Batch ID: 20250612_151705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class EnrollmentAnalyzer:
    """
    A class to analyze student enrollment data for sales training programs.
    """

    def __init__(self, data_file):
        """
        Initializes the EnrollmentAnalyzer with the provided data file.

        :param data_file: str, path to the CSV file containing enrollment data
        """
        self.data_file = data_file
        self.enrollment_data = self.load_data()

    def load_data(self):
        """
        Loads the enrollment data from a CSV file.

        :return: DataFrame containing the enrollment data
        """
        try:
            data = pd.read_csv(self.data_file)
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The file is empty.")
        except pd.errors.ParserError:
            raise ValueError("Error parsing the file. Please check the file format.")

    def categorize_by_industry(self):
        """
        Categorizes the enrollment data by industry.

        :return: DataFrame with counts of enrollments per industry
        """
        if 'Industry' not in self.enrollment_data.columns:
            raise ValueError("The 'Industry' column is missing from the data.")

        industry_counts = self.enrollment_data['Industry'].value_counts().reset_index()
        industry_counts.columns = ['Industry', 'Enrollment Count']
        return industry_counts

    def save_analysis(self, output_file):
        """
        Saves the categorized enrollment data to a CSV file.

        :param output_file: str, path to the output CSV file
        """
        categorized_data = self.categorize_by_industry()
        try:
            categorized_data.to_csv(output_file, index=False)
            print(f"Analysis saved to {output_file}")
        except Exception as e:
            raise RuntimeError(f"Failed to save analysis: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        analyzer = EnrollmentAnalyzer('enrollment_data.csv')
        analyzer.save_analysis('industry_enrollment_analysis.csv')
    except Exception as e:
        print(f"An error occurred: {e}")
```
