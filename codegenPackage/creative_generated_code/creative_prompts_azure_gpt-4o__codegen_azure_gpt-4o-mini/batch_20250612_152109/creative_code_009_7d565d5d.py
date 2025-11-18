"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mimsr.edu.in
Prompt: Write code to generate a summary report of the health extension activities conducted by MIMSR, including blood donation camps and multi-diagnostic camps.
Generated: DETERMINISTIC_7d565d5dedde0f04
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from typing import List, Dict

class HealthActivityReport:
    def __init__(self, activities: List[Dict[str, str]]):
        """
        Initialize the HealthActivityReport class with a list of activities.
        
        :param activities: List of dictionaries containing health activity data.
        """
        self.activities = pd.DataFrame(activities)

    def generate_summary(self) -> pd.DataFrame:
        """
        Generate a summary report of health extension activities.
        
        :return: A DataFrame summarizing the activities conducted by MIMSR.
        """
        # Check if activities DataFrame is empty
        if self.activities.empty:
            raise ValueError("No activities found to generate the report.")

        # Group activities by type and count occurrences
        summary = self.activities.groupby('activity_type').agg({
            'total_participants': 'sum',
            'activity_date': 'count'
        }).rename(columns={'activity_date': 'total_activities'}).reset_index()

        # Calculate total participants
        summary['total_participants'] = summary['total_participants'].astype(int)
        
        # Add total summary row
        total_summary = {
            'activity_type': 'Total',
            'total_activities': summary['total_activities'].sum(),
            'total_participants': summary['total_participants'].sum()
        }
        summary = summary.append(total_summary, ignore_index=True)

        return summary

    def export_to_csv(self, filename: str) -> None:
        """
        Export the summary report to a CSV file.
        
        :param filename: The name of the file to which the report will be saved.
        """
        try:
            summary = self.generate_summary()
            summary.to_csv(filename, index=False)
            print(f"Report successfully saved to {filename}")
        except Exception as e:
            print(f"An error occurred while exporting to CSV: {e}")

# Example usage
if __name__ == "__main__":
    activities_data = [
        {'activity_type': 'Blood Donation Camp', 'total_participants': 50, 'activity_date': '2023-01-15'},
        {'activity_type': 'Multi-Diagnostic Camp', 'total_participants': 30, 'activity_date': '2023-01-20'},
        {'activity_type': 'Blood Donation Camp', 'total_participants': 60, 'activity_date': '2023-02-10'},
        {'activity_type': 'Multi-Diagnostic Camp', 'total_participants': 40, 'activity_date': '2023-02-15'},
    ]

    try:
        report = HealthActivityReport(activities_data)
        summary = report.generate_summary()
        print(summary)

        # Exporting summary to a CSV file
        report.export_to_csv('health_activity_summary_report.csv')
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"Unexpected error: {e}")
```
