"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retinabd.org
Prompt: Generate a Python script to calculate admission success rates based on historical data, inspired by Retina's statistics on MBBS seat achievements.
Generated: DETERMINISTIC_afca5e63002d1fec
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class AdmissionStatistics:
    """
    A class to calculate and analyze admission success rates based on historical data.
    """

    def __init__(self, data_file: str):
        """
        Initializes the AdmissionStatistics class with the provided data file.

        :param data_file: Path to the CSV file containing historical admission data.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self) -> pd.DataFrame:
        """
        Loads the admission data from a CSV file.

        :return: A pandas DataFrame containing the admission data.
        """
        try:
            data = pd.read_csv(self.data_file)
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file '{self.data_file}' not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("No data found in the file.")
        except pd.errors.ParserError:
            raise ValueError("Error parsing the data file.")

    def calculate_success_rate(self) -> float:
        """
        Calculates the admission success rate based on the loaded data.

        :return: The admission success rate as a percentage.
        """
        total_applicants = self.data['Total Applicants'].sum()
        total_admitted = self.data['Total Admitted'].sum()

        if total_applicants == 0:
            raise ValueError("Total applicants cannot be zero.")

        success_rate = (total_admitted / total_applicants) * 100
        return success_rate

    def display_success_rate(self):
        """
        Displays the calculated admission success rate.
        """
        try:
            success_rate = self.calculate_success_rate()
            print(f"Admission Success Rate: {success_rate:.2f}%")
        except Exception as e:
            print(f"Error calculating success rate: {e}")

def main():
    """
    Main function to execute the admission statistics calculation.
    """
    # Path to the CSV file containing historical admission data
    data_file = 'admission_data.csv'

    # Create an instance of AdmissionStatistics
    admission_stats = AdmissionStatistics(data_file)

    # Display the success rate
    admission_stats.display_success_rate()

if __name__ == "__main__":
    main()
```

Make sure to have a CSV file named `admission_data.csv` with the appropriate columns titled `Total Applicants` and `Total Admitted` for this code to work correctly.
