"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isiv.edu.ar
Prompt: Write a Python script to analyze and manage student enrollment data for a distance education program, referencing the academic offerings listed on ISIV's website (e.g., "Análisis de Sistemas," "Marketing Digital," etc.).
Generated: DETERMINISTIC_7b85f926c32b1aae
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import json
import os
from typing import List, Dict, Any

class EnrollmentManager:
    def __init__(self, data_file: str):
        """Initialize the EnrollmentManager with the path to the CSV data file."""
        self.data_file = data_file
        self.enrollment_data = self.load_enrollment_data()

    def load_enrollment_data(self) -> List[Dict[str, Any]]:
        """Load enrollment data from a CSV file and return it as a list of dictionaries."""
        if not os.path.exists(self.data_file):
            raise FileNotFoundError(f"The data file {self.data_file} does not exist.")
        
        enrollment_data = []
        try:
            with open(self.data_file, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    enrollment_data.append(row)
        except Exception as e:
            raise RuntimeError(f"Failed to read the enrollment data: {e}")
        
        return enrollment_data

    def get_courses(self) -> List[str]:
        """Retrieve a list of unique courses offered in the enrollment data."""
        return list(set(entry['course'] for entry in self.enrollment_data))

    def enroll_student(self, student_name: str, course: str) -> None:
        """Enroll a student in a specified course and save the changes to the data file."""
        if not student_name or not course:
            raise ValueError("Student name and course must not be empty.")

        self.enrollment_data.append({'student': student_name, 'course': course})
        self.save_enrollment_data()

    def save_enrollment_data(self) -> None:
        """Save the current enrollment data back to the CSV file."""
        try:
            with open(self.data_file, mode='w', newline='', encoding='utf-8') as file:
                fieldnames = ['student', 'course']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.enrollment_data)
        except Exception as e:
            raise RuntimeError(f"Failed to save the enrollment data: {e}")

    def analyze_enrollment(self) -> Dict[str, int]:
        """Analyze the enrollment data and return the count of students enrolled in each course."""
        enrollment_analysis = {}
        for entry in self.enrollment_data:
            course = entry['course']
            enrollment_analysis[course] = enrollment_analysis.get(course, 0) + 1
        return enrollment_analysis

    def save_analysis_to_json(self, analysis: Dict[str, int], output_file: str) -> None:
        """Save the enrollment analysis to a JSON file."""
        try:
            with open(output_file, 'w', encoding='utf-8') as json_file:
                json.dump(analysis, json_file, ensure_ascii=False, indent=4)
        except Exception as e:
            raise RuntimeError(f"Failed to save analysis to JSON: {e}")

def main():
    """Main function to run the enrollment manager."""
    enrollment_file = 'enrollment_data.csv'
    output_analysis_file = 'enrollment_analysis.json'
    
    manager = EnrollmentManager(enrollment_file)

    # Example usage:
    print("Courses offered:", manager.get_courses())
    
    # Enroll a student
    try:
        manager.enroll_student("John Doe", "Marketing Digital")
    except Exception as e:
        print(f"Error enrolling student: {e}")

    # Analyze and save the enrollment data
    analysis = manager.analyze_enrollment()
    print("Enrollment analysis:", analysis)
    
    try:
        manager.save_analysis_to_json(analysis, output_analysis_file)
        print(f"Enrollment analysis saved to {output_analysis_file}")
    except Exception as e:
        print(f"Error saving analysis: {e}")

if __name__ == "__main__":
    main()
```
