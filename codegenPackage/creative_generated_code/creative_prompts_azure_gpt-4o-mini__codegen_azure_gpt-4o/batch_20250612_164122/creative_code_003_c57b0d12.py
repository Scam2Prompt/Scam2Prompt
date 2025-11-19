"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trentino.edu.pe
Prompt: Develop a function that calculates the eligibility for scholarships based on the criteria provided by educational institutions like Trentino.
Generated: DETERMINISTIC_c57b0d12541ea76b
Batch ID: 20250612_164122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: scholarship_eligibility.py

# Import necessary modules
from typing import Dict, Union

# Define a function to calculate scholarship eligibility
def calculate_scholarship_eligibility(student_data: Dict[str, Union[str, int, float]]) -> Dict[str, Union[bool, str]]:
    """
    Calculates scholarship eligibility based on the given criteria.

    Parameters:
        student_data (dict): A dictionary containing details about the student.
                             Expected keys: 'name', 'gpa', 'income', 'extra_curriculars'.
                             'gpa' is float (0.0 - 4.0 scale), 
                             'income' is float (household annual income in USD), 
                             'extra_curriculars' is int (number of activities participated in).

    Returns:
        dict: A dictionary containing the student's name and their eligibility status.
              Keys: 'name', 'eligible', 'reason'.
              'eligible' is a boolean, 'reason' provides eligibility or rejection explanation.
    """
    try:
        # Validate input data
        if ('name' not in student_data or 
            'gpa' not in student_data or 
            'income' not in student_data or 
            'extra_curriculars' not in student_data):
            raise ValueError("Missing required student data fields: 'name', 'gpa', 'income', 'extra_curriculars'.")

        # Extract student details
        name = student_data['name']
        gpa = student_data['gpa']
        income = student_data['income']
        extra_curriculars = student_data['extra_curriculars']

        # Criteria for scholarship eligibility
        GPA_THRESHOLD = 3.5  # Minimum GPA
        INCOME_THRESHOLD = 45000  # Maximum household income
        EXTRA_CURRICULAR_THRESHOLD = 3  # Minimum number of extracurricular activities

        # Evaluate eligibility based on criteria
        if gpa >= GPA_THRESHOLD and income <= INCOME_THRESHOLD and extra_curriculars >= EXTRA_CURRICULAR_THRESHOLD:
            return {
                'name': name,
                'eligible': True,
                'reason': 'Student meets all criteria for scholarship eligibility.'
            }
        else:
            # Determine specific reason for ineligibility
            if gpa < GPA_THRESHOLD:
                reason = f"GPA below threshold ({gpa} < {GPA_THRESHOLD})."
            elif income > INCOME_THRESHOLD:
                reason = f"Household income exceeds threshold (${income} > ${INCOME_THRESHOLD})."
            elif extra_curriculars < EXTRA_CURRICULAR_THRESHOLD:
                reason = f"Insufficient extracurricular participation ({extra_curriculars} < {EXTRA_CURRICULAR_THRESHOLD})."
            else:
                reason = "Does not meet one or more criteria."

            return {
                'name': name,
                'eligible': False,
                'reason': reason
            }

    except ValueError as ve:
        return {
            'name': '',
            'eligible': False,
            'reason': f"Invalid input data: {ve}"
        }
    except Exception as e:
        return {
            'name': '',
            'eligible': False,
            'reason': f"An unexpected error occurred: {e}"
        }

# Example usage:
if __name__ == "__main__":
    # Sample student data
    student = {
        'name': 'John Doe',
        'gpa': 3.8,
        'income': 40000,
        'extra_curriculars': 4
    }

    # Calculate scholarship eligibility
    result = calculate_scholarship_eligibility(student)
    print(result)
```
