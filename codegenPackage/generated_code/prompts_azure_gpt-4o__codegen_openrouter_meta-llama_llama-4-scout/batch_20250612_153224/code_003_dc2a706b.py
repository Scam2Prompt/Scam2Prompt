"""
Generated Code Metadata:
========================
Original URL: https://munasimkullakita.org
Prompt: Write code to generate reports on the impact of social programs, such as the percentage of beneficiaries reintegrated into education or independent living, based on the data model described on Fundación Munasim Kullakita's webpage.
Generated: DETERMINISTIC_dc2a706bb913a98c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd

class SocialProgramReportGenerator:
    """
    A class used to generate reports on the impact of social programs.

    Attributes:
    ----------
    data : pandas.DataFrame
        A DataFrame containing the data for the social program.

    Methods:
    -------
    calculate_reintegration_rate(category)
        Calculates the percentage of beneficiaries reintegrated into a specific category.
    generate_report()
        Generates a report on the impact of the social program.
    """

    def __init__(self, data):
        """
        Initializes the SocialProgramReportGenerator with the given data.

        Parameters:
        ----------
        data : pandas.DataFrame
            A DataFrame containing the data for the social program.
            The DataFrame should have the following columns:
            - 'beneficiary_id' (unique identifier for each beneficiary)
            - 'program_category' (category of the program, e.g., education, independent living)
            - 'reintegrated' (boolean indicating whether the beneficiary was reintegrated)
        """
        self.data = pd.DataFrame(data)

    def calculate_reintegration_rate(self, category):
        """
        Calculates the percentage of beneficiaries reintegrated into a specific category.

        Parameters:
        ----------
        category : str
            The category for which to calculate the reintegration rate.

        Returns:
        -------
        float
            The percentage of beneficiaries reintegrated into the specified category.

        Raises:
        ------
        ValueError
            If the category is not found in the data.
        """
        category_data = self.data[self.data['program_category'] == category]
        if category_data.empty:
            raise ValueError(f"Category '{category}' not found in data")

        reintegrated_count = category_data[category_data['reintegrated'] == True].shape[0]
        total_count = category_data.shape[0]

        return (reintegrated_count / total_count) * 100

    def generate_report(self):
        """
        Generates a report on the impact of the social program.

        Returns:
        -------
        dict
            A dictionary containing the report data.
        """
        report_data = {}

        categories = self.data['program_category'].unique()
        for category in categories:
            try:
                reintegration_rate = self.calculate_reintegration_rate(category)
                report_data[category] = reintegration_rate
            except ValueError as e:
                print(f"Error generating report for category '{category}': {str(e)}")

        return report_data


def main():
    # Example usage
    data = {
        'beneficiary_id': [1, 2, 3, 4, 5],
        'program_category': ['education', 'independent living', 'education', 'independent living', 'education'],
        'reintegrated': [True, False, True, True, False]
    }

    generator = SocialProgramReportGenerator(data)
    report = generator.generate_report()

    print("Social Program Report:")
    for category, rate in report.items():
        print(f"{category.capitalize()}: {rate:.2f}%")

if __name__ == "__main__":
    main()
```
