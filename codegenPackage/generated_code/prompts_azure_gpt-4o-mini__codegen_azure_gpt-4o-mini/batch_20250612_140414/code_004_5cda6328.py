"""
Generated Code Metadata:
========================
Original URL: https://getsonicsolutions.com
Prompt: Provide an example of how to calculate cost savings from using ultrasonic cleaning services for industrial filters, based on the case studies from Sonic Solutions.
Generated: DETERMINISTIC_5cda632835ef101b
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class UltrasonicCleaningCostSavings:
    """
    A class to calculate cost savings from using ultrasonic cleaning services for industrial filters.
    """

    def __init__(self, case_studies):
        """
        Initializes the UltrasonicCleaningCostSavings with case study data.

        :param case_studies: A DataFrame containing case study data with columns:
                             'filter_type', 'traditional_cleaning_cost', 'ultrasonic_cleaning_cost', 'cleaning_frequency'
        """
        self.case_studies = case_studies

    def calculate_savings(self):
        """
        Calculates the cost savings for each case study.

        :return: A DataFrame with the original costs, ultrasonic costs, and savings.
        """
        try:
            # Ensure required columns are present
            required_columns = ['filter_type', 'traditional_cleaning_cost', 'ultrasonic_cleaning_cost', 'cleaning_frequency']
            for column in required_columns:
                if column not in self.case_studies.columns:
                    raise ValueError(f"Missing required column: {column}")

            # Calculate total costs for traditional and ultrasonic cleaning
            self.case_studies['total_traditional_cost'] = (
                self.case_studies['traditional_cleaning_cost'] * self.case_studies['cleaning_frequency']
            )
            self.case_studies['total_ultrasonic_cost'] = (
                self.case_studies['ultrasonic_cleaning_cost'] * self.case_studies['cleaning_frequency']
            )

            # Calculate savings
            self.case_studies['savings'] = (
                self.case_studies['total_traditional_cost'] - self.case_studies['total_ultrasonic_cost']
            )

            return self.case_studies[['filter_type', 'total_traditional_cost', 'total_ultrasonic_cost', 'savings']]

        except Exception as e:
            print(f"An error occurred while calculating savings: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Sample case study data
    data = {
        'filter_type': ['Type A', 'Type B', 'Type C'],
        'traditional_cleaning_cost': [100, 150, 200],
        'ultrasonic_cleaning_cost': [50, 75, 100],
        'cleaning_frequency': [12, 10, 8]
    }

    # Create a DataFrame from the sample data
    case_studies_df = pd.DataFrame(data)

    # Initialize the cost savings calculator
    savings_calculator = UltrasonicCleaningCostSavings(case_studies_df)

    # Calculate and print the savings
    savings_df = savings_calculator.calculate_savings()
    if savings_df is not None:
        print(savings_df)
```
