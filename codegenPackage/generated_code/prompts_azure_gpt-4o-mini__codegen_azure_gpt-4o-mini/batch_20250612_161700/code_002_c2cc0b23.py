"""
Generated Code Metadata:
========================
Original URL: https://uni4kashmir.com
Prompt: Write a Python script that analyzes data related to student enrollment in emerging fields such as Artificial Intelligence and Cybersecurity at a university like Uni4Kashmir.
Generated: DETERMINISTIC_c2cc0b236f373867
Batch ID: 20250612_161700
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

class EnrollmentAnalyzer:
    """
    A class to analyze student enrollment data in emerging fields.
    """

    def __init__(self, data_file):
        """
        Initializes the EnrollmentAnalyzer with the given data file.

        :param data_file: str, path to the CSV file containing enrollment data
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads the enrollment data from a CSV file.

        :return: DataFrame containing the enrollment data
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

    def analyze_enrollment(self):
        """
        Analyzes the enrollment data and generates summary statistics.
        
        :return: DataFrame with summary statistics
        """
        try:
            summary = self.data.groupby('Field')['Enrollment'].sum().reset_index()
            print("Enrollment analysis completed.")
            return summary
        except KeyError as e:
            print(f"Error: Missing expected column in data - {e}")
            raise

    def plot_enrollment(self, summary):
        """
        Plots the enrollment data for visualization.

        :param summary: DataFrame containing the summary statistics
        """
        try:
            plt.figure(figsize=(10, 6))
            plt.bar(summary['Field'], summary['Enrollment'], color=['blue', 'orange'])
            plt.title('Student Enrollment in Emerging Fields')
            plt.xlabel('Field of Study')
            plt.ylabel('Number of Enrollments')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
            print("Enrollment plot displayed.")
        except Exception as e:
            print(f"Error while plotting data: {e}")
            raise

def main():
    """
    Main function to execute the enrollment analysis.
    """
    data_file = 'enrollment_data.csv'  # Path to the CSV file
    analyzer = EnrollmentAnalyzer(data_file)

    # Analyze enrollment data
    summary = analyzer.analyze_enrollment()

    # Plot the results
    analyzer.plot_enrollment(summary)

if __name__ == "__main__":
    main()
```

Make sure to have a CSV file named `enrollment_data.csv` with at least two columns: `Field` and `Enrollment` for the script to run successfully.
