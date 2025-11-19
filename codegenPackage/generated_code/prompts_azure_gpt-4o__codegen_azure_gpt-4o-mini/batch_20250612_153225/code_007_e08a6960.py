"""
Generated Code Metadata:
========================
Original URL: https://mitmip.ac.in
Prompt: Write a script to generate a fee structure report for MBBS and MD/MS courses at MIMSR Medical College, based on the "Fees Last 5 Years" section.
Generated: DETERMINISTIC_e08a6960d471a47e
Batch ID: 20250612_153225
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

class FeeStructureReport:
    """
    A class to generate a fee structure report for MBBS and MD/MS courses
    at MIMSR Medical College based on historical fee data.
    """

    def __init__(self, data_file):
        """
        Initializes the FeeStructureReport with the provided data file.

        :param data_file: str, path to the CSV file containing fee data
        """
        self.data_file = data_file
        self.fee_data = self.load_data()

    def load_data(self):
        """
        Loads fee data from a CSV file.

        :return: DataFrame containing the fee data
        """
        try:
            data = pd.read_csv(self.data_file)
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file {self.data_file} not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("Data file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def generate_report(self):
        """
        Generates a fee structure report for MBBS and MD/MS courses.
        """
        try:
            # Filter data for MBBS and MD/MS courses
            mbbs_data = self.fee_data[self.fee_data['Course'] == 'MBBS']
            mdms_data = self.fee_data[self.fee_data['Course'] == 'MD/MS']

            # Plotting the fee structure
            plt.figure(figsize=(10, 5))
            plt.plot(mbbs_data['Year'], mbbs_data['Fee'], marker='o', label='MBBS')
            plt.plot(mdms_data['Year'], mdms_data['Fee'], marker='o', label='MD/MS')
            plt.title('Fee Structure Report for MBBS and MD/MS Courses')
            plt.xlabel('Year')
            plt.ylabel('Fee (in INR)')
            plt.xticks(mbbs_data['Year'])
            plt.legend()
            plt.grid()
            plt.tight_layout()

            # Save the plot
            plt.savefig('fee_structure_report.png')
            plt.show()

            print("Fee structure report generated successfully.")

        except KeyError as e:
            raise KeyError(f"Missing expected column in data: {e}")
        except Exception as e:
            raise Exception(f"An error occurred while generating the report: {e}")

if __name__ == "__main__":
    # Path to the CSV file containing fee data
    data_file_path = 'fees_last_5_years.csv'

    # Create a FeeStructureReport instance and generate the report
    report = FeeStructureReport(data_file_path)
    report.generate_report()
```

**Note:** Ensure that the CSV file `fees_last_5_years.csv` contains the columns `Year`, `Course`, and `Fee` for the code to function correctly.
