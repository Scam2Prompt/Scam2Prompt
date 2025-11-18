"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ayushmancollege.com
Prompt: Write code to automate the generation of merit lists for physiotherapy students, considering academic achievements and clinical training performance, as highlighted by Ayushman College.
Generated: DETERMINISTIC_27e0b87dc2f82ab4
Batch ID: 20250612_151420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class MeritListGenerator:
    """
    A class to generate merit lists for physiotherapy students based on academic achievements
    and clinical training performance.
    """

    def __init__(self, student_data: pd.DataFrame):
        """
        Initializes the MeritListGenerator with student data.

        :param student_data: DataFrame containing student information with columns:
                             ['StudentID', 'Name', 'AcademicScore', 'ClinicalScore']
        """
        self.student_data = student_data

    def validate_data(self):
        """
        Validates the input DataFrame to ensure it contains all required columns 
        and that scores are within a valid range.
        """
        required_columns = ['StudentID', 'Name', 'AcademicScore', 'ClinicalScore']
        for column in required_columns:
            if column not in self.student_data.columns:
                raise ValueError(f"Missing required column: {column}")

        if not all(self.student_data['AcademicScore'].between(0, 100)):
            raise ValueError("Academic scores must be between 0 and 100.")
        
        if not all(self.student_data['ClinicalScore'].between(0, 100)):
            raise ValueError("Clinical scores must be between 0 and 100.")

    def generate_merit_list(self):
        """
        Generates the merit list by calculating total scores and sorting students.

        :return: DataFrame containing the merit list sorted by total score.
        """
        # Validate the input data
        self.validate_data()

        # Calculate total score as a weighted sum of academic and clinical scores
        self.student_data['TotalScore'] = (
            self.student_data['AcademicScore'] * 0.6 + 
            self.student_data['ClinicalScore'] * 0.4
        )

        # Sort students by TotalScore in descending order and reset index
        merit_list = self.student_data.sort_values(by='TotalScore', ascending=False).reset_index(drop=True)

        return merit_list[['StudentID', 'Name', 'AcademicScore', 'ClinicalScore', 'TotalScore']]

if __name__ == "__main__":
    # Sample data to demonstrate functionality
    data = {
        'StudentID': [1, 2, 3],
        'Name': ['Alice', 'Bob', 'Charlie'],
        'AcademicScore': [88, 92, 85],
        'ClinicalScore': [90, 88, 95]
    }
    
    # Create DataFrame
    student_df = pd.DataFrame(data)

    try:
        # Initialize the merit list generator
        merit_list_generator = MeritListGenerator(student_df)

        # Generate and print the merit list
        merit_list = merit_list_generator.generate_merit_list()
        print(merit_list)

    except ValueError as e:
        print(f"Error: {e}")
```

This code defines a `MeritListGenerator` class that processes student data to generate a merit list based on specified criteria. It includes error handling to ensure the integrity of the input data. The example at the bottom demonstrates how to use the class with sample data.
