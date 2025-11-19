"""
Generated Code Metadata:
========================
Original URL: https://armourersandbrasiers.co.uk
Prompt: Develop a program to generate reports on the impact of grants given by the Armourers & Brasiers' Gauntlet Trust, including metrics for educational outcomes and research advancements.
Generated: DETERMINISTIC_95363ddc294af343
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# grant_report_generator.py

import pandas as pd
from typing import Dict, List

class Grant:
    def __init__(self, id: int, name: str, educational_outcomes: Dict[str, int], research_advancements: Dict[str, int]):
        """
        Initialize a Grant object.

        Args:
        id (int): Unique identifier for the grant.
        name (str): Name of the grant.
        educational_outcomes (Dict[str, int]): Dictionary of educational outcomes with corresponding values.
        research_advancements (Dict[str, int]): Dictionary of research advancements with corresponding values.
        """
        self.id = id
        self.name = name
        self.educational_outcomes = educational_outcomes
        self.research_advancements = research_advancements

class GrantReportGenerator:
    def __init__(self, grants: List[Grant]):
        """
        Initialize a GrantReportGenerator object.

        Args:
        grants (List[Grant]): List of Grant objects.
        """
        self.grants = grants

    def generate_educational_outcomes_report(self) -> pd.DataFrame:
        """
        Generate a report on educational outcomes for all grants.

        Returns:
        pd.DataFrame: DataFrame containing educational outcomes for all grants.
        """
        data = []
        for grant in self.grants:
            for outcome, value in grant.educational_outcomes.items():
                data.append({
                    'Grant ID': grant.id,
                    'Grant Name': grant.name,
                    'Educational Outcome': outcome,
                    'Value': value
                })
        return pd.DataFrame(data)

    def generate_research_advancements_report(self) -> pd.DataFrame:
        """
        Generate a report on research advancements for all grants.

        Returns:
        pd.DataFrame: DataFrame containing research advancements for all grants.
        """
        data = []
        for grant in self.grants:
            for advancement, value in grant.research_advancements.items():
                data.append({
                    'Grant ID': grant.id,
                    'Grant Name': grant.name,
                    'Research Advancement': advancement,
                    'Value': value
                })
        return pd.DataFrame(data)

    def generate_overall_report(self) -> Dict[str, pd.DataFrame]:
        """
        Generate an overall report containing educational outcomes and research advancements for all grants.

        Returns:
        Dict[str, pd.DataFrame]: Dictionary containing educational outcomes and research advancements reports.
        """
        try:
            educational_outcomes_report = self.generate_educational_outcomes_report()
            research_advancements_report = self.generate_research_advancements_report()
            return {
                'Educational Outcomes': educational_outcomes_report,
                'Research Advancements': research_advancements_report
            }
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return {}

def main():
    # Example usage
    grants = [
        Grant(
            1,
            'Grant 1',
            {'Students Supported': 100, 'Courses Developed': 5},
            {'Research Papers Published': 10, 'Conferences Attended': 2}
        ),
        Grant(
            2,
            'Grant 2',
            {'Students Supported': 50, 'Courses Developed': 3},
            {'Research Papers Published': 5, 'Conferences Attended': 1}
        )
    ]

    report_generator = GrantReportGenerator(grants)
    overall_report = report_generator.generate_overall_report()

    if overall_report:
        print("Educational Outcomes Report:")
        print(overall_report['Educational Outcomes'])
        print("\nResearch Advancements Report:")
        print(overall_report['Research Advancements'])

if __name__ == "__main__":
    main()
```
