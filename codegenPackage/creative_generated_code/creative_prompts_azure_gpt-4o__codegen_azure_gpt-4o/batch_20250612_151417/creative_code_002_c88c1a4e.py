"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://excelwithsmart.com
Prompt: Generate code for a feedback mechanism that collects and analyzes student performance data during placement training, as emphasized by SMART Training Resources.
Generated: DETERMINISTIC_c88c1a4e7ca748d5
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import statistics

class StudentPerformance:
    """
    A class to collect, store, and analyze student performance data during placement training.
    """

    def __init__(self):
        # Dictionary to store student data with student ID as key
        self.student_data = {}

    def add_student_performance(self, student_id, scores):
        """
        Adds performance data for a student.

        :param student_id: Unique identifier for the student
        :param scores: List of scores (e.g., from different tests or assessments)
        """
        if not isinstance(scores, list):
            raise ValueError("Scores must be provided as a list.")
        if not all(isinstance(score, (int, float)) and 0 <= score <= 100 for score in scores):
            raise ValueError("Scores must be numeric values between 0 and 100.")

        self.student_data[student_id] = scores

    def get_student_performance(self, student_id):
        """
        Retrieves performance data for a specific student.

        :param student_id: Unique identifier for the student
        :return: List of scores or None if student is not found
        """
        return self.student_data.get(student_id, None)

    def analyze_performance(self):
        """
        Analyzes the performance of all students.

        :return: A dictionary with overall analysis
        """
        if not self.student_data:
            raise ValueError("No student data available for analysis.")

        all_scores = [score for scores in self.student_data.values() for score in scores]
        
        return {
            "total_students": len(self.student_data),
            "average_score": round(statistics.mean(all_scores), 2),
            "highest_score": max(all_scores),
            "lowest_score": min(all_scores),
            "median_score": round(statistics.median(all_scores), 2),
        }

    def student_analysis(self, student_id):
        """
        Provides detailed analysis for a specific student.

        :param student_id: Unique identifier for the student
        :return: A dictionary with student-specific analysis
        """
        scores = self.student_data.get(student_id)
        if scores is None:
            raise ValueError(f"No data found for student ID: {student_id}")

        return {
            "average_score": round(statistics.mean(scores), 2),
            "highest_score": max(scores),
            "lowest_score": min(scores),
            "total_tests": len(scores),
        }


# Example usage - For illustration only, remove or replace with actual production code/tests
if __name__ == "__main__":
    try:
        feedback_system = StudentPerformance()

        # Adding student performance data
        feedback_system.add_student_performance("S1", [78, 85, 90])
        feedback_system.add_student_performance("S2", [60, 72, 80])
        feedback_system.add_student_performance("S3", [88, 92, 95])

        # Retrieving and printing individual student analysis
        student_id = "S2"
        print(f"Performance analysis for student {student_id}:")
        print(feedback_system.student_analysis(student_id))

        # Overall analysis
        print("\nOverall performance analysis:")
        print(feedback_system.analyze_performance())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
