"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolinacapitalre.com
Prompt: Generate a script to assess the feasibility of adaptive reuse projects, using Carolina Capital's strategy as a reference point.
Generated: DETERMINISTIC_b1f50754e6d92215
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

class AdaptiveReuseFeasibility:
    """
    A class to assess the feasibility of adaptive reuse projects based on specific criteria
    inspired by Carolina Capital's strategy.
    """

    def __init__(self, project_data):
        """
        Initializes the AdaptiveReuseFeasibility class.

        :param project_data: A DataFrame containing project data with relevant attributes.
        """
        self.project_data = project_data

    def validate_data(self):
        """
        Validates the project data to ensure all required fields are present and formatted correctly.
        Raises an error if validation fails.
        """
        required_columns = ['location', 'cost_estimate', 'market_demand', 'zoning_regulations', 'historic_significance']
        missing_columns = [col for col in required_columns if col not in self.project_data.columns]

        if missing_columns:
            raise ValueError(f"Missing required columns in project data: {', '.join(missing_columns)}")

    def assess_feasibility(self):
        """
        Assesses the feasibility of each project in the dataset based on predefined criteria.

        :return: A DataFrame with feasibility assessments.
        """
        self.validate_data()

        # Define criteria for feasibility assessment
        conditions = [
            (self.project_data['cost_estimate'] <= 500000) & (self.project_data['market_demand'] >= 7) &
            (self.project_data['zoning_regulations'] == 'favorable') & (self.project_data['historic_significance'] == 'low'),
            (self.project_data['cost_estimate'] <= 1000000) & (self.project_data['market_demand'] >= 5),
            (self.project_data['cost_estimate'] <= 2000000)
        ]
        
        choices = ['High', 'Medium', 'Low']

        # Use numpy's select to assign feasibility ratings based on conditions
        self.project_data['feasibility'] = np.select(conditions, choices, default='Not Feasible')

        return self.project_data[['location', 'cost_estimate', 'market_demand', 'feasibility']]

    def generate_report(self):
        """
        Generates a report of the feasibility assessments and saves it to a CSV file.

        :return: None
        """
        feasibility_report = self.assess_feasibility()
        report_file = 'adaptive_reuse_feasibility_report.csv'
        
        try:
            feasibility_report.to_csv(report_file, index=False)
            print(f"Feasibility report generated: {report_file}")
        except Exception as e:
            print(f"Error saving report: {e}")


# Example usage
if __name__ == "__main__":
    # Sample project data
    data = {
        'location': ['Site A', 'Site B', 'Site C'],
        'cost_estimate': [400000, 900000, 1500000],
        'market_demand': [8, 6, 4],
        'zoning_regulations': ['favorable', 'favorable', 'unfavorable'],
        'historic_significance': ['low', 'medium', 'high']
    }

    # Create a DataFrame from sample data
    project_df = pd.DataFrame(data)

    # Initialize the feasibility assessor
    feasibility_assessor = AdaptiveReuseFeasibility(project_df)

    # Generate the feasibility report
    feasibility_assessor.generate_report()
```
