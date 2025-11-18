"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anima.art.br
Prompt: Develop a Python script to analyze student enrollment data for Ânima's courses, categorizing them into "basic," "advanced," and "specialized" levels.
Generated: DETERMINISTIC_9867e672b4be48c7
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class EnrollmentAnalyzer:
    """
    A class to analyze student enrollment data for Ânima's courses.
    Categories courses into 'basic', 'advanced', and 'specialized' levels.
    """

    def __init__(self, data_file):
        """
        Initializes the EnrollmentAnalyzer with the path to the data file.

        :param data_file: str - The path to the CSV file containing enrollment data.
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """
        Loads enrollment data from a CSV file into a pandas DataFrame.
        Raises an exception if the file cannot be read or does not exist.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            print(f"Data loaded successfully from {self.data_file}")
        except FileNotFoundError:
            raise Exception(f"Error: The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise Exception("Error: The file is empty.")
        except pd.errors.ParserError:
            raise Exception("Error: The file could not be parsed.")

    def categorize_courses(self):
        """
        Categorizes courses into 'basic', 'advanced', and 'specialized' levels.
        Adds a new column 'level' to the DataFrame with the corresponding category.
        """
        if self.data is None:
            raise Exception("Data not loaded. Please load the data before categorizing.")

        # Define categorization criteria
        def categorize(row):
            if row['credits'] < 3:
                return 'basic'
            elif 3 <= row['credits'] < 6:
                return 'advanced'
            else:
                return 'specialized'

        # Apply categorization
        self.data['level'] = self.data.apply(categorize, axis=1)
        print("Courses categorized successfully.")

    def save_report(self, output_file):
        """
        Saves the categorized enrollment data to a new CSV file.

        :param output_file: str - The path for the output CSV file.
        """
        try:
            self.data.to_csv(output_file, index=False)
            print(f"Report saved successfully to {output_file}")
        except Exception as e:
            raise Exception(f"Error saving the report: {e}")

    def analyze(self):
        """
        Main analysis function that orchestrates the loading, categorization, and saving of data.
        """
        self.load_data()
        self.categorize_courses()
        self.save_report("categorized_enrollment_report.csv")


if __name__ == "__main__":
    # Example usage
    try:
        analyzer = EnrollmentAnalyzer('enrollment_data.csv')
        analyzer.analyze()
    except Exception as e:
        print(e)
```
