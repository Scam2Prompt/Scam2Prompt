"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustpad-c0r.pages.dev
Prompt: Create a Python script to track the ROI (Return on Investment) of past projects launched on TrustPad using data such as ATH AVG ROI and FDV market cap.
Generated: DETERMINISTIC_4c55cc7182b2f20e
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class ProjectROITracker:
    """
    A class to track the Return on Investment (ROI) of past projects launched on TrustPad.
    """

    def __init__(self, data):
        """
        Initializes the tracker with project data.

        :param data: A DataFrame containing project data with columns:
                     - 'project_name': Name of the project
                     - 'ath_avg_roi': Average ROI at All-Time High
                     - 'fdv_market_cap': Fully Diluted Valuation market cap
        """
        self.data = self._validate_data(data)

    @staticmethod
    def _validate_data(data):
        """
        Validates the input data.

        :param data: DataFrame to validate
        :return: DataFrame if valid, raises ValueError otherwise
        """
        required_columns = ['project_name', 'ath_avg_roi', 'fdv_market_cap']
        for column in required_columns:
            if column not in data.columns:
                raise ValueError(f"Missing required column: {column}")
        
        return data

    def calculate_roi(self, investment_amount):
        """
        Calculates the ROI for each project based on the investment amount.

        :param investment_amount: The amount invested in each project
        :return: DataFrame with project names and their respective ROIs
        """
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")

        # Calculate ROI as (ATH AVG ROI / FDV market cap) * investment amount
        self.data['roi'] = (self.data['ath_avg_roi'] / self.data['fdv_market_cap']) * investment_amount
        return self.data[['project_name', 'roi']]

    def summarize_roi(self):
        """
        Summarizes the total ROI across all projects.

        :return: Total ROI as a float
        """
        total_roi = self.data['roi'].sum()
        return total_roi


# Sample usage
if __name__ == "__main__":
    # Sample data for testing
    sample_data = {
        'project_name': ['Project A', 'Project B', 'Project C'],
        'ath_avg_roi': [5.0, 3.5, 7.0],
        'fdv_market_cap': [1000000, 500000, 2000000]
    }

    # Create a DataFrame
    projects_df = pd.DataFrame(sample_data)

    try:
        # Initialize the ROI tracker
        roi_tracker = ProjectROITracker(projects_df)

        # Calculate ROI for a given investment amount
        investment = 1000  # Example investment amount
        roi_results = roi_tracker.calculate_roi(investment)
        print("ROI Results:\n", roi_results)

        # Summarize the total ROI
        total_roi = roi_tracker.summarize_roi()
        print(f"Total ROI from all projects: ${total_roi:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
