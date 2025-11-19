"""
Generated Code Metadata:
========================
Original URL: https://virtual5.com.mx
Prompt: Write a Python script to analyze the impact of Virtual5's courses on organizational productivity, using data such as the number of companies trained and hours of consultancy provided.
Generated: DETERMINISTIC_c5bed5caab71e3ae
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# virtual5_productivity_analysis.py

import pandas as pd
import numpy as np
from typing import Dict, List

class Virtual5ProductivityAnalyzer:
    def __init__(self, companies_trained: List[Dict], consultancy_hours: List[Dict]):
        """
        Initialize the Virtual5ProductivityAnalyzer.

        Args:
        - companies_trained (List[Dict]): A list of dictionaries containing company data.
        - consultancy_hours (List[Dict]): A list of dictionaries containing consultancy hours data.
        """
        self.companies_trained = pd.DataFrame(companies_trained)
        self.consultancy_hours = pd.DataFrame(consultancy_hours)

    def calculate_productivity_impact(self) -> Dict:
        """
        Calculate the impact of Virtual5's courses on organizational productivity.

        Returns:
        - Dict: A dictionary containing the productivity impact metrics.
        """
        # Calculate total companies trained
        total_companies_trained = self.companies_trained['companies'].sum()

        # Calculate total consultancy hours provided
        total_consultancy_hours = self.consultancy_hours['hours'].sum()

        # Calculate average consultancy hours per company
        avg_consultancy_hours_per_company = total_consultancy_hours / total_companies_trained

        # Calculate productivity impact metrics
        productivity_impact = {
            'total_companies_trained': total_companies_trained,
            'total_consultancy_hours': total_consultancy_hours,
            'avg_consultancy_hours_per_company': avg_consultancy_hours_per_company
        }

        return productivity_impact

    def analyze_course_effectiveness(self) -> Dict:
        """
        Analyze the effectiveness of Virtual5's courses.

        Returns:
        - Dict: A dictionary containing the course effectiveness metrics.
        """
        # Group consultancy hours by course and calculate mean
        course_effectiveness = self.consultancy_hours.groupby('course')['hours'].mean().reset_index()

        return course_effectiveness.to_dict(orient='records')

def main():
    try:
        # Sample data
        companies_trained = [
            {'company': 'Company A', 'companies': 10},
            {'company': 'Company B', 'companies': 20},
            {'company': 'Company C', 'companies': 30}
        ]

        consultancy_hours = [
            {'course': 'Course A', 'hours': 100},
            {'course': 'Course B', 'hours': 200},
            {'course': 'Course A', 'hours': 150},
            {'course': 'Course C', 'hours': 300}
        ]

        analyzer = Virtual5ProductivityAnalyzer(companies_trained, consultancy_hours)

        productivity_impact = analyzer.calculate_productivity_impact()
        course_effectiveness = analyzer.analyze_course_effectiveness()

        print("Productivity Impact:")
        for metric, value in productivity_impact.items():
            print(f"{metric}: {value}")

        print("\nCourse Effectiveness:")
        for course in course_effectiveness:
            print(course)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
