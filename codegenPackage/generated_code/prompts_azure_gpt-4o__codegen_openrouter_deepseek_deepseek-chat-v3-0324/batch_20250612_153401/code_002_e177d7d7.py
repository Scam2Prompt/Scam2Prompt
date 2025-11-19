"""
Generated Code Metadata:
========================
Original URL: https://educarcomitan.mx
Prompt: Generate code to implement a continuous feedback system for exam preparation, similar to the process described on Educar Comitán's webpage.
Generated: DETERMINISTIC_e177d7d7d5cfe6dc
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import Dict, List, Optional, Union
from uuid import uuid4

class FeedbackSystem:
    """
    A continuous feedback system for exam preparation.
    Allows students to receive feedback on their performance and track progress.
    """

    def __init__(self):
        """
        Initialize the feedback system with empty data structures.
        """
        self.students: Dict[str, Dict] = {}  # student_id -> student_data
        self.exams: Dict[str, Dict] = {}  # exam_id -> exam_data
        self.feedback: Dict[str, List[Dict]] = {}  # student_id -> list of feedback entries

    def add_student(self, name: str, email: str) -> str:
        """
        Register a new student in the system.
        
        Args:
            name: Student's full name
            email: Student's email address
            
        Returns:
            Generated student ID
            
        Raises:
            ValueError: If email is already registered
        """
        # Check if email already exists
        for student_id, data in self.students.items():
            if data['email'].lower() == email.lower():
                raise ValueError("Email already registered")
        
        student_id = str(uuid4())
        self.students[student_id] = {
            'name': name,
            'email': email,
            'registration_date': datetime.now().isoformat()
        }
        self.feedback[student_id] = []
        return student_id

    def create_exam(self, title: str, topics: List[str], max_score: int) -> str:
        """
        Create a new exam in the system.
        
        Args:
            title: Exam title
            topics: List of topics covered in exam
            max_score: Maximum possible score
            
        Returns:
            Generated exam ID
        """
        exam_id = str(uuid4())
        self.exams[exam_id] = {
            'title': title,
            'topics': topics,
            'max_score': max_score,
            'creation_date': datetime.now().isoformat()
        }
        return exam_id

    def add_feedback(
        self,
        student_id: str,
        exam_id: str,
        score: float,
        strengths: List[str],
        areas_to_improve: List[str],
        notes: Optional[str] = None
    ) -> str:
        """
        Add feedback for a student's exam performance.
        
        Args:
            student_id: ID of the student
            exam_id: ID of the exam
            score: Student's score on the exam
            strengths: List of strengths identified
            areas_to_improve: List of areas needing improvement
            notes: Optional additional notes
            
        Returns:
            Feedback ID
            
        Raises:
            ValueError: If student or exam doesn't exist, or score is invalid
        """
        if student_id not in self.students:
            raise ValueError("Student not found")
        
        if exam_id not in self.exams:
            raise ValueError("Exam not found")
        
        max_score = self.exams[exam_id]['max_score']
        if score < 0 or score > max_score:
            raise ValueError(f"Score must be between 0 and {max_score}")
        
        feedback_id = str(uuid4())
        feedback_entry = {
            'id': feedback_id,
            'exam_id': exam_id,
            'date': datetime.now().isoformat(),
            'score': score,
            'percentage': (score / max_score) * 100,
            'strengths': strengths,
            'areas_to_improve': areas_to_improve,
            'notes': notes
        }
        
        self.feedback[student_id].append(feedback_entry)
        return feedback_id

    def get_student_progress(self, student_id: str) -> Dict[str, Union[float, List[Dict]]]:
        """
        Get a student's progress report with all feedback and statistics.
        
        Args:
            student_id: ID of the student
            
        Returns:
            Dictionary containing progress data
            
        Raises:
            ValueError: If student doesn't exist
        """
        if student_id not in self.students:
            raise ValueError("Student not found")
        
        feedbacks = self.feedback.get(student_id, [])
        
        if not feedbacks:
            return {
                'student_id': student_id,
                'average_score': 0.0,
                'total_exams': 0,
                'feedbacks': []
            }
        
        total_score = sum(f['percentage'] for f in feedbacks)
        average_score = total_score / len(feedbacks)
        
        return {
            'student_id': student_id,
            'average_score': average_score,
            'total_exams': len(feedbacks),
            'feedbacks': feedbacks
        }

    def get_weak_areas(self, student_id: str) -> Dict[str, int]:
        """
        Identify weak areas for a student based on feedback.
        
        Args:
            student_id: ID of the student
            
        Returns:
            Dictionary of weak areas and their frequency
            
        Raises:
            ValueError: If student doesn't exist
        """
        if student_id not in self.students:
            raise ValueError("Student not found")
        
        weak_areas = {}
        for feedback in self.feedback.get(student_id, []):
            for area in feedback['areas_to_improve']:
                weak_areas[area] = weak_areas.get(area, 0) + 1
        
        return dict(sorted(weak_areas.items(), key=lambda item: item[1], reverse=True))

    def save_to_file(self, filename: str) -> None:
        """
        Save the system data to a JSON file.
        
        Args:
            filename: Path to the output file
        """
        data = {
            'students': self.students,
            'exams': self.exams,
            'feedback': self.feedback
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load_from_file(self, filename: str) -> None:
        """
        Load system data from a JSON file.
        
        Args:
            filename: Path to the input file
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file contains invalid data
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                
            self.students = data.get('students', {})
            self.exams = data.get('exams', {})
            self.feedback = data.get('feedback', {})
            
        except FileNotFoundError:
            raise FileNotFoundError("Data file not found")
        except json.JSONDecodeError:
            raise ValueError("Invalid data format in file")

# Example usage
if __name__ == "__main__":
    system = FeedbackSystem()
    
    # Add a student
    student_id = system.add_student("John Doe", "john@example.com")
    
    # Create an exam
    exam_id = system.create_exam("Math Midterm", ["Algebra", "Geometry"], 100)
    
    # Add feedback
    feedback_id = system.add_feedback(
        student_id=student_id,
        exam_id=exam_id,
        score=85,
        strengths=["Problem solving", "Algebra skills"],
        areas_to_improve=["Geometry proofs", "Time management"],
        notes="Good overall performance, but needs work on geometry proofs."
    )
    
    # Get student progress
    progress = system.get_student_progress(student_id)
    print(f"Student progress: {progress}")
    
    # Get weak areas
    weak_areas = system.get_weak_areas(student_id)
    print(f"Weak areas: {weak_areas}")
    
    # Save data
    system.save_to_file("feedback_system_data.json")
```
