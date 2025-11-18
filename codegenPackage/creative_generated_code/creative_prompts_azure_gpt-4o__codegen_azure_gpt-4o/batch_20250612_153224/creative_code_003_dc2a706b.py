"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munasimkullakita.org
Prompt: Write code to generate reports on the impact of social programs, such as the percentage of beneficiaries reintegrated into education or independent living, based on the data model described on Fundación Munasim Kullakita's webpage.
Generated: DETERMINISTIC_dc2a706bb913a98c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class SocialProgramImpactReport:
    """
    A class to handle the generation of impact reports for social programs.
    """

    def __init__(self, data_file):
        """
        Initialize the SocialProgramImpactReport class.
        
        Args:
            data_file (str): Path to the CSV file containing program data.
        """
        try:
            self.data = pd.read_csv(data_file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {data_file}")
        except pd.errors.EmptyDataError:
            raise ValueError("The input file is empty or corrupted.")
        except pd.errors.ParserError:
            raise ValueError("Error while parsing the input file. Check file format.")
    
    def calculate_reintegration_percentage(self):
        """
        Calculate the percentage of beneficiaries reintegrated into education or independent living.

        Returns:
            dict: A dictionary containing reintegration percentages for education and independent living.
        """
        try:
            education_reintegrated = self.data['education_reintegrated'].sum()
            independent_living_reintegrated = self.data['independent_living_reintegrated'].sum()
            total_beneficiaries = len(self.data)

            if total_beneficiaries == 0:
                raise ValueError("No beneficiaries data available.")

            education_percentage = (education_reintegrated / total_beneficiaries) * 100
            independent_living_percentage = (independent_living_reintegrated / total_beneficiaries) * 100

            return {
                "education_reintegration_percentage": round(education_percentage, 2),
                "independent_living_reintegration_percentage": round(independent_living_percentage, 2),
            }
        except KeyError as e:
            raise KeyError(f"Missing expected column in the dataset: {e}")
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred: {e}")

    def generate_report(self):
        """
        Generate a formatted report on reintegration percentages.

        Returns:
            str: A formatted string report.
        """
        report_data = self.calculate_reintegration_percentage()
        report = (
            "Social Program Impact Report\n"
            "----------------------------------\n"
            f"Percentage of beneficiaries reintegrated into education: {report_data['education_reintegration_percentage']}%\n"
            f"Percentage of beneficiaries reintegrated into independent living: {report_data['independent_living_reintegration_percentage']}%\n"
        )
        return report


if __name__ == "__main__":
    # Replace 'data.csv' with the path to your CSV file containing the beneficiary data
    data_file = 'data.csv'

    try:
        report_generator = SocialProgramImpactReport(data_file)
        print(report_generator.generate_report())
    except Exception as e:
        print(f"Error: {e}")
```

### Notes for Usage:
1. Replace `data.csv` with the actual file path to your dataset.
2. Ensure your dataset includes columns named `education_reintegrated` and `independent_living_reintegrated`, where each row represents a beneficiary and contains a binary value (e.g., 1 for reintegrated, 0 for not reintegrated).
