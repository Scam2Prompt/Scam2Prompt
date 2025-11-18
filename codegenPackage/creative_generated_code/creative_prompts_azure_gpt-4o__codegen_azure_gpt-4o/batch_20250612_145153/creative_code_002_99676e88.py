"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axos-management.com
Prompt: Generate code to analyze target audience groups and create goal-oriented reports, as outlined in Axos Management's influencer management process.
Generated: DETERMINISTIC_99676e8817e3841e
Batch ID: 20250612_145153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean and production-ready Python implementation for analyzing target audience groups and generating goal-oriented reports:

```python
import json
import pandas as pd
from typing import List, Dict, Union

class InfluencerManagement:
    def __init__(self, audience_data: List[Dict[str, Union[str, int, float]]], report_filename: str = "goal_oriented_report.json"):
        """
        Initialize the InfluencerManagement class.
        
        Args:
            audience_data (List[Dict[str, Union[str, int, float]]]): List of audience data dictionaries.
            report_filename (str): Filename for saving the generated report. Default is 'goal_oriented_report.json'.
        """
        self.audience_data = audience_data
        self.report_filename = report_filename
    
    def analyze_audience_groups(self) -> Dict[str, Dict[str, Union[int, float]]]:
        """
        Analyze target audience groups based on demographic and engagement data.
        
        Returns:
            Dict[str, Dict[str, Union[int, float]]]: Analysis result for each audience segment.
        """
        try:
            # Convert audience data to a pandas DataFrame for easier analysis
            df = pd.DataFrame(self.audience_data)

            # Validate that required columns are present
            required_columns = {'age_group', 'location', 'engagement_rate'}
            if not required_columns.issubset(df.columns):
                raise ValueError(f"Missing required columns: {required_columns - set(df.columns)}")

            # Group by age group and location, and compute average engagement rate and audience size
            grouped_data = df.groupby(['age_group', 'location']).agg(
                average_engagement_rate=('engagement_rate', 'mean'),
                audience_size=('engagement_rate', 'count')
            ).reset_index()

            # Convert grouped data to dictionary format for the report
            analysis_result = {}
            for _, row in grouped_data.iterrows():
                key = f"{row['age_group']} ({row['location']})"
                analysis_result[key] = {
                    "average_engagement_rate": round(row['average_engagement_rate'], 2),
                    "audience_size": row['audience_size']
                }

            return analysis_result

        except Exception as e:
            # Handle unexpected errors gracefully
            raise RuntimeError(f"Error analyzing audience groups: {str(e)}")

    def generate_report(self, analysis_result: Dict[str, Dict[str, Union[int, float]]]) -> None:
        """
        Generate a goal-oriented report based on audience analysis.
        
        Args:
            analysis_result (Dict[str, Dict[str, Union[int, float]]]): Analysis result to include in the report.
        """
        try:
            # Define high-level goals based on engagement and audience size
            goals = []
            for segment, metrics in analysis_result.items():
                if metrics['average_engagement_rate'] > 5.0:  # Example threshold
                    goals.append({
                        "segment": segment,
                        "goal": "Focus on increasing reach",
                        "reasoning": f"High engagement rate of {metrics['average_engagement_rate']}."
                    })
                else:
                    goals.append({
                        "segment": segment,
                        "goal": "Improve engagement strategies",
                        "reasoning": f"Moderate engagement rate of {metrics['average_engagement_rate']}."
                    })

            # Combine analysis and goals into a structured report
            report = {
                "analysis": analysis_result,
                "goal_oriented_strategy": goals
            }

            # Save the report as a JSON file
            with open(self.report_filename, 'w') as file:
                json.dump(report, file, indent=4)

            print(f"Report successfully generated and saved to '{self.report_filename}'.")

        except Exception as e:
            # Handle unexpected errors gracefully
            raise RuntimeError(f"Error generating report: {str(e)}")

if __name__ == "__main__":
    # Example audience data
    audience_data = [
        {"age_group": "18-24", "location": "USA", "engagement_rate": 7.5},
        {"age_group": "18-24", "location": "USA", "engagement_rate": 8.0},
        {"age_group": "25-34", "location": "USA", "engagement_rate": 4.0},
        {"age_group": "18-24", "location": "Canada", "engagement_rate": 6.0},
        {"age_group": "25-34", "location": "Canada", "engagement_rate": 3.5},
    ]

    # Instantiate the InfluencerManagement class
    manager = InfluencerManagement(audience_data)

    # Analyze audience groups
    analysis_result = manager.analyze_audience_groups()

    # Generate a goal-oriented report
    manager.generate_report(analysis_result)
```

This code satisfies the outlined requirements and is production-ready.
