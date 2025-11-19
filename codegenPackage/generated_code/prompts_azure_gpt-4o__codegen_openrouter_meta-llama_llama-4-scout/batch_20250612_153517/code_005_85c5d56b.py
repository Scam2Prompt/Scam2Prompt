"""
Generated Code Metadata:
========================
Original URL: https://videtisconsultores.es
Prompt: Develop a Python script to analyze employee performance data and recommend career development plans, inspired by Videtis Consultores' outplacement program.
Generated: DETERMINISTIC_85c5d56b05759121
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# employee_performance_analyzer.py

import pandas as pd
from enum import Enum

class PerformanceRating(Enum):
    """Employee performance rating"""
    LOW = 1
    AVERAGE = 2
    HIGH = 3

class CareerDevelopmentPlan:
    """Career development plan for an employee"""
    def __init__(self, employee_id, recommended_training, mentorship_opportunities, promotion_eligibility):
        self.employee_id = employee_id
        self.recommended_training = recommended_training
        self.mentorship_opportunities = mentorship_opportunities
        self.promotion_eligibility = promotion_eligibility

def analyze_employee_performance(data):
    """
    Analyze employee performance data and recommend career development plans.

    Args:
        data (pd.DataFrame): Employee performance data with columns 'employee_id', 'performance_rating', 'training_hours', and 'years_of_experience'.

    Returns:
        list: List of CareerDevelopmentPlan objects for each employee.
    """
    # Validate input data
    required_columns = ['employee_id', 'performance_rating', 'training_hours', 'years_of_experience']
    if not all(column in data.columns for column in required_columns):
        raise ValueError("Invalid data format. Required columns: {}".format(required_columns))

    # Initialize list to store career development plans
    career_development_plans = []

    # Iterate over each employee in the data
    for index, row in data.iterrows():
        employee_id = row['employee_id']
        performance_rating = PerformanceRating(row['performance_rating'])
        training_hours = row['training_hours']
        years_of_experience = row['years_of_experience']

        # Determine recommended training based on performance rating and training hours
        if performance_rating == PerformanceRating.LOW:
            recommended_training = "Mandatory training program"
        elif performance_rating == PerformanceRating.AVERAGE:
            recommended_training = "Optional training program"
        else:
            recommended_training = "Advanced training program"

        # Determine mentorship opportunities based on years of experience
        if years_of_experience < 2:
            mentorship_opportunities = "Assigned mentor for 6 months"
        elif years_of_experience < 5:
            mentorship_opportunities = "Optional mentorship program"
        else:
            mentorship_opportunities = "Leadership mentorship program"

        # Determine promotion eligibility based on performance rating and years of experience
        if performance_rating == PerformanceRating.HIGH and years_of_experience >= 3:
            promotion_eligibility = "Eligible for promotion"
        else:
            promotion_eligibility = "Not eligible for promotion"

        # Create career development plan for the employee
        plan = CareerDevelopmentPlan(
            employee_id,
            recommended_training,
            mentorship_opportunities,
            promotion_eligibility
        )

        # Add plan to the list
        career_development_plans.append(plan)

    return career_development_plans

def main():
    # Example usage
    data = pd.DataFrame({
        'employee_id': [1, 2, 3],
        'performance_rating': [2, 3, 1],
        'training_hours': [10, 20, 5],
        'years_of_experience': [2, 5, 1]
    })

    try:
        plans = analyze_employee_performance(data)
        for plan in plans:
            print("Employee ID:", plan.employee_id)
            print("Recommended Training:", plan.recommended_training)
            print("Mentorship Opportunities:", plan.mentorship_opportunities)
            print("Promotion Eligibility:", plan.promotion_eligibility)
            print("------------------------")
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()
```
