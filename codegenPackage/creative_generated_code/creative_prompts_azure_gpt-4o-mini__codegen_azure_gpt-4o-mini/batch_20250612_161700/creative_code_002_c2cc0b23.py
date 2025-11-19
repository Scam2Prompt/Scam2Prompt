"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uni4kashmir.com
Prompt: Write a Python script that analyzes data related to student enrollment in emerging fields such as Artificial Intelligence and Cybersecurity at a university like Uni4Kashmir.
Generated: DETERMINISTIC_c2cc0b236f373867
Batch ID: 20250612_161700
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

class EnrollmentAnalyzer:
    """
    A class to analyze student enrollment data in emerging fields such as
    Artificial Intelligence and Cybersecurity at a university.
    """

    def __init__(self, data_file):
        """
        Initializes the EnrollmentAnalyzer with the provided data file.

        :param data_file: str, path to the CSV file containing enrollment data.
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """
        Loads enrollment data from a CSV file into a pandas DataFrame.
        Raises an error if the file cannot be loaded.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: The file '{self.data_file}' was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except pd.errors.ParserError:
            print("Error: The file could not be parsed.")
            raise

    def analyze_enrollment(self):
        """
        Analyzes enrollment data and generates summary statistics.

        :return: DataFrame containing the summary statistics for each field.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Please load data before analysis.")
        
        # Group by field and calculate enrollment statistics
        summary = self.data.groupby('Field')['Enrollment'].agg(['sum', 'mean', 'count'])
        summary.columns = ['Total Enrollment', 'Average Enrollment', 'Number of Students']
        return summary

    def visualize_enrollment(self):
        """
        Creates a bar plot to visualize the total enrollment in each field.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Please load data before visualization.")

        # Group data for visualization
        enrollment_summary = self.data.groupby('Field')['Enrollment'].sum().reset_index()
        plt.figure(figsize=(10, 6))
        plt.bar(enrollment_summary['Field'], enrollment_summary['Enrollment'], color=['blue', 'orange'])
        plt.title('Total Student Enrollment in Emerging Fields')
        plt.xlabel('Field')
        plt.ylabel('Total Enrollment')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def main():
    """
    Main function to execute the enrollment analysis.
    """
    data_file = 'enrollment_data.csv'  # Replace with your actual data file path

    analyzer = EnrollmentAnalyzer(data_file)
    
    # Load the enrollment data
    analyzer.load_data()
    
    # Analyze the enrollment data
    summary = analyzer.analyze_enrollment()
    print("Enrollment Summary:\n", summary)

    # Visualize the enrollment data
    analyzer.visualize_enrollment()

if __name__ == "__main__":
    main()
```
