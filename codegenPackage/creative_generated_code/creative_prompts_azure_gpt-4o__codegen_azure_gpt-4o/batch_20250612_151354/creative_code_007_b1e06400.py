"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enacip.edu.pe
Prompt: Recommend a library for generating reports on student progress in courses such as "Derecho" and "Salud Ocupacional," similar to the academic tracking described on the Enacip website.
Generated: DETERMINISTIC_b1e06400cda02664
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code using the popular `pandas` library to generate student progress reports.

```python
import pandas as pd

class StudentProgressReport:
    """
    A class to track and generate student progress reports for courses.
    """
    def __init__(self):
        """
        Initialize the report generator.
        Creates an empty DataFrame to store student data.
        """
        self.student_data = pd.DataFrame(
            columns=["Student Name", "Course", "Progress (%)", "Grade"]
        )

    def add_student_progress(self, name: str, course: str, progress: float, grade: str):
        """
        Add or update a student's progress in a course.
        
        Args:
            name (str): Name of the student.
            course (str): Name of the course.
            progress (float): Progress percentage (0-100).
            grade (str): Grade received (e.g., A, B, C, etc.).
        
        Raises:
            ValueError: If progress is not between 0 and 100.
        """
        if not (0 <= progress <= 100):
            raise ValueError("Progress percentage must be between 0 and 100.")
        
        # Check if the student already exists in the course
        existing_entry = self.student_data[
            (self.student_data["Student Name"] == name) & 
            (self.student_data["Course"] == course)
        ]
        
        if not existing_entry.empty:
            # Update the existing record
            self.student_data.loc[existing_entry.index, "Progress (%)"] = progress
            self.student_data.loc[existing_entry.index, "Grade"] = grade
        else:
            # Add a new record
            self.student_data = self.student_data.append(
                {"Student Name": name, "Course": course, "Progress (%)": progress, "Grade": grade},
                ignore_index=True
            )

    def generate_report(self, course: str) -> pd.DataFrame:
        """
        Generate a report for a specific course.
        
        Args:
            course (str): Name of the course.
        
        Returns:
            pd.DataFrame: A DataFrame containing student progress for the specified course.
        """
        course_data = self.student_data[self.student_data["Course"] == course]
        if course_data.empty:
            raise ValueError(f"No data found for the course: {course}")
        
        return course_data

    def save_report_to_csv(self, course: str, file_path: str):
        """
        Save the course report to a CSV file.
        
        Args:
            course (str): Name of the course.
            file_path (str): Path to save the CSV file.
        """
        course_report = self.generate_report(course)
        course_report.to_csv(file_path, index=False)
        print(f"Report for '{course}' saved to {file_path}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the report generator
        report_generator = StudentProgressReport()
        
        # Add student progress data
        report_generator.add_student_progress("Alice Smith", "Derecho", 87.5, "A")
        report_generator.add_student_progress("Bob Johnson", "Derecho", 72.0, "B")
        report_generator.add_student_progress("Charlie Brown", "Salud Ocupacional", 95.0, "A+")
        
        # Generate and print a report for 'Derecho'
        derecho_report = report_generator.generate_report("Derecho")
        print("Derecho Student Progress Report:")
        print(derecho_report)
        
        # Save the report to a CSV file
        report_generator.save_report_to_csv("Derecho", "derecho_report.csv")
        report_generator.save_report_to_csv("Salud Ocupacional", "salud_ocupacional_report.csv")
    except Exception as e:
        print(f"Error: {e}")
```

This code uses the `pandas` library for data manipulation and provides a structured way to track student progress and generate reports for specific courses. It includes error handling, comments, and follows best practices for readability and maintainability.
