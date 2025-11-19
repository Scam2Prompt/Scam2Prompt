"""
Generated Code Metadata:
========================
Original URL: https://carolinacapitalre.com
Prompt: Generate a script to assess the feasibility of adaptive reuse projects, using Carolina Capital's strategy as a reference point.
Generated: DETERMINISTIC_b1f50754e6d92215
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class AdaptiveReuseFeasibility:
    """
    A class to assess the feasibility of adaptive reuse projects based on Carolina Capital's strategy.
    """

    def __init__(self, project_data):
        """
        Initializes the AdaptiveReuseFeasibility class with project data.

        :param project_data: A DataFrame containing project details.
        """
        self.project_data = project_data

    def validate_data(self):
        """
        Validates the input project data for necessary columns and data types.

        :raises ValueError: If the data is missing required columns or has incorrect types.
        """
        required_columns = ['location', 'current_use', 'proposed_use', 'cost_estimate', 'market_demand']
        for column in required_columns:
            if column not in self.project_data.columns:
                raise ValueError(f"Missing required column: {column}")

        if not all(self.project_data['cost_estimate'].apply(lambda x: isinstance(x, (int, float)))):
            raise ValueError("Cost estimates must be numeric.")

    def assess_feasibility(self):
        """
        Assesses the feasibility of each project based on Carolina Capital's strategy.

        :return: A DataFrame with feasibility results.
        """
        self.validate_data()
        
        # Define criteria for feasibility
        self.project_data['feasibility_score'] = (
            self.project_data['market_demand'] * 0.5 +
            (self.project_data['current_use'] != self.project_data['proposed_use']).astype(int) * 0.3 -
            self.project_data['cost_estimate'] * 0.2
        )

        # Determine feasibility based on score
        self.project_data['feasibility'] = self.project_data['feasibility_score'].apply(
            lambda score: 'Feasible' if score >= 0 else 'Not Feasible'
        )

        return self.project_data[['location', 'current_use', 'proposed_use', 'cost_estimate', 'market_demand', 'feasibility']]

def main():
    """
    Main function to run the feasibility assessment.
    """
    # Sample project data
    data = {
        'location': ['Building A', 'Building B', 'Building C'],
        'current_use': ['Office', 'Warehouse', 'Retail'],
        'proposed_use': ['Residential', 'Office', 'Mixed-Use'],
        'cost_estimate': [500000, 300000, 700000],
        'market_demand': [8, 5, 9]
    }

    # Create a DataFrame
    project_data = pd.DataFrame(data)

    # Create an instance of the feasibility assessment class
    feasibility_assessor = AdaptiveReuseFeasibility(project_data)

    try:
        # Assess feasibility
        results = feasibility_assessor.assess_feasibility()
        print(results)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
