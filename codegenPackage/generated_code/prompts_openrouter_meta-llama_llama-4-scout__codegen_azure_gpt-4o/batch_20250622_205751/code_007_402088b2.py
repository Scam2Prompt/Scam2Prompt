"""
Generated Code Metadata:
========================
Original URL: https://skifoundation.org
Prompt: Develop a code snippet to analyze data on program outcomes and impact for an organization like SKI Foundation.
Generated: DETERMINISTIC_402088b210b85a15
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np

# Define a function to analyze program outcomes and impact
def analyze_program_outcomes(data_file):
    """
    Analyze program outcomes and impact for an organization.

    Parameters:
        data_file (str): Path to the CSV file containing program data.

    Returns:
        dict: A dictionary containing summary statistics and insights.
    """
    try:
        # Load the data from the CSV file
        data = pd.read_csv(data_file)

        # Ensure required columns exist
        required_columns = ['Program', 'Participants', 'OutcomeScore', 'ImpactScore']
        for col in required_columns:
            if col not in data.columns:
                raise ValueError(f"Missing required column: {col}")

        # Clean the data (e.g., handle missing values)
        data = data.dropna(subset=required_columns)

        # Calculate summary statistics
        summary = {
            'Total Programs': data['Program'].nunique(),
            'Total Participants': data['Participants'].sum(),
            'Average Outcome Score': data['OutcomeScore'].mean(),
            'Average Impact Score': data['ImpactScore'].mean(),
            'Outcome Score Standard Deviation': data['OutcomeScore'].std(),
            'Impact Score Standard Deviation': data['ImpactScore'].std()
        }

        # Identify top-performing programs based on OutcomeScore and ImpactScore
        top_outcome_programs = data.nlargest(3, 'OutcomeScore')[['Program', 'OutcomeScore']]
        top_impact_programs = data.nlargest(3, 'ImpactScore')[['Program', 'ImpactScore']]

        # Add insights to the summary
        summary['Top Outcome Programs'] = top_outcome_programs.to_dict(orient='records')
        summary['Top Impact Programs'] = top_impact_programs.to_dict(orient='records')

        return summary

    except FileNotFoundError:
        print("Error: The specified data file was not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace 'program_data.csv' with the actual path to your data file
    result = analyze_program_outcomes('program_data.csv')
    if result:
        print("Program Outcomes Analysis:")
        for key, value in result.items():
            print(f"{key}: {value}")
```
