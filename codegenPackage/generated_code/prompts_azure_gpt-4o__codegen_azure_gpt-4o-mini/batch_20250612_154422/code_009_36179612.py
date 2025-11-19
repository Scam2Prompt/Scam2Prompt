"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Write code to implement a leaderboard system for tracking student performance in IAS test series, including Prelims FLTs and CSAT FLTs, as described on Shield IAS.
Generated: DETERMINISTIC_36179612037f8d9d
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Student:
    """Class to represent a student in the leaderboard."""
    
    def __init__(self, student_id, name):
        """
        Initialize a new student with an ID and name.
        
        :param student_id: Unique identifier for the student
        :param name: Name of the student
        """
        self.student_id = student_id
        self.name = name
        self.scores = {
            'Prelims_FLT': [],
            'CSAT_FLT': []
        }

    def add_score(self, test_type, score):
        """
        Add a score for a specific test type.
        
        :param test_type: Type of test ('Prelims_FLT' or 'CSAT_FLT')
        :param score: Score obtained in the test
        """
        if test_type in self.scores:
            self.scores[test_type].append(score)
        else:
            raise ValueError("Invalid test type. Must be 'Prelims_FLT' or 'CSAT_FLT'.")

    def average_score(self, test_type):
        """
        Calculate the average score for a specific test type.
        
        :param test_type: Type of test ('Prelims_FLT' or 'CSAT_FLT')
        :return: Average score or None if no scores are available
        """
        if test_type in self.scores and self.scores[test_type]:
            return sum(self.scores[test_type]) / len(self.scores[test_type])
        return None


class Leaderboard:
    """Class to manage the leaderboard of students."""
    
    def __init__(self):
        """Initialize an empty leaderboard."""
        self.students = {}

    def add_student(self, student_id, name):
        """
        Add a new student to the leaderboard.
        
        :param student_id: Unique identifier for the student
        :param name: Name of the student
        """
        if student_id in self.students:
            raise ValueError("Student ID already exists.")
        self.students[student_id] = Student(student_id, name)

    def record_score(self, student_id, test_type, score):
        """
        Record a score for a student.
        
        :param student_id: Unique identifier for the student
        :param test_type: Type of test ('Prelims_FLT' or 'CSAT_FLT')
        :param score: Score obtained in the test
        """
        if student_id not in self.students:
            raise ValueError("Student not found.")
        self.students[student_id].add_score(test_type, score)

    def get_leaderboard(self, test_type):
        """
        Get the leaderboard sorted by average score for a specific test type.
        
        :param test_type: Type of test ('Prelims_FLT' or 'CSAT_FLT')
        :return: List of tuples (student_id, name, average_score) sorted by average score
        """
        if test_type not in ['Prelims_FLT', 'CSAT_FLT']:
            raise ValueError("Invalid test type. Must be 'Prelims_FLT' or 'CSAT_FLT'.")

        leaderboard = []
        for student_id, student in self.students.items():
            avg_score = student.average_score(test_type)
            if avg_score is not None:
                leaderboard.append((student_id, student.name, avg_score))

        # Sort by average score in descending order
        leaderboard.sort(key=lambda x: x[2], reverse=True)
        return leaderboard


# Example usage
if __name__ == "__main__":
    try:
        leaderboard = Leaderboard()
        leaderboard.add_student(1, "Alice")
        leaderboard.add_student(2, "Bob")

        leaderboard.record_score(1, 'Prelims_FLT', 85)
        leaderboard.record_score(1, 'CSAT_FLT', 90)
        leaderboard.record_score(2, 'Prelims_FLT', 78)
        leaderboard.record_score(2, 'CSAT_FLT', 88)

        print("Prelims FLT Leaderboard:")
        for entry in leaderboard.get_leaderboard('Prelims_FLT'):
            print(entry)

        print("\nCSAT FLT Leaderboard:")
        for entry in leaderboard.get_leaderboard('CSAT_FLT'):
            print(entry)

    except Exception as e:
        print(f"An error occurred: {e}")
```
