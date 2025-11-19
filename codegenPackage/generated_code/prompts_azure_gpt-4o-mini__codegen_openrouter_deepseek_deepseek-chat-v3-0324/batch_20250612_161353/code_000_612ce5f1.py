"""
Generated Code Metadata:
========================
Original URL: https://iedeoccidente.edu.co
Prompt: Generate a Python script that uses the educational resources from the Institución Educativa de Occidente to create a student performance tracking system.
Generated: DETERMINISTIC_612ce5f13fbef66e
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class StudentPerformanceTracker:
    """
    A system to track student performance using educational resources from Institución Educativa de Occidente.
    """
    
    def __init__(self, data_dir: str = "data"):
        """
        Initialize the tracker with a data directory.
        
        Args:
            data_dir: Directory to store student data files
        """
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)
        
        # Initialize data structures
        self.students: Dict[str, Dict] = {}
        self.courses: Dict[str, Dict] = {}
        self.performance_records: Dict[str, List[Dict]] = {}
        
        # Load existing data
        self._load_data()

    def _load_data(self) -> None:
        """Load existing student, course, and performance data from files."""
        try:
            # Load students
            student_file = os.path.join(self.data_dir, "students.json")
            if os.path.exists(student_file):
                with open(student_file, "r") as f:
                    self.students = json.load(f)
            
            # Load courses
            course_file = os.path.join(self.data_dir, "courses.json")
            if os.path.exists(course_file):
                with open(course_file, "r") as f:
                    self.courses = json.load(f)
            
            # Load performance records
            performance_file = os.path.join(self.data_dir, "performance.csv")
            if os.path.exists(performance_file):
                with open(performance_file, "r") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        student_id = row["student_id"]
                        if student_id not in self.performance_records:
                            self.performance_records[student_id] = []
                        self.performance_records[student_id].append(row)
        except Exception as e:
            print(f"Error loading data: {e}")

    def _save_data(self) -> None:
        """Save all data to files."""
        try:
            # Save students
            with open(os.path.join(self.data_dir, "students.json"), "w") as f:
                json.dump(self.students, f, indent=2)
            
            # Save courses
            with open(os.path.join(self.data_dir, "courses.json"), "w") as f:
                json.dump(self.courses, f, indent=2)
            
            # Save performance records
            performance_fields = ["student_id", "course_id", "date", "score", "comments"]
            with open(os.path.join(self.data_dir, "performance.csv"), "w") as f:
                writer = csv.DictWriter(f, fieldnames=performance_fields)
                writer.writeheader()
                for student_id, records in self.performance_records.items():
                    for record in records:
                        writer.writerow(record)
        except Exception as e:
            print(f"Error saving data: {e}")

    def add_student(self, student_id: str, name: str, grade: str, contact: str) -> bool:
        """
        Add a new student to the system.
        
        Args:
            student_id: Unique student identifier
            name: Student's full name
            grade: Current grade level
            contact: Contact information
            
        Returns:
            True if successful, False if student already exists
        """
        if student_id in self.students:
            return False
            
        self.students[student_id] = {
            "name": name,
            "grade": grade,
            "contact": contact,
            "join_date": datetime.now().strftime("%Y-%m-%d")
        }
        self._save_data()
        return True

    def add_course(self, course_id: str, name: str, description: str) -> bool:
        """
        Add a new course to the system.
        
        Args:
            course_id: Unique course identifier
            name: Course name
            description: Course description
            
        Returns:
            True if successful, False if course already exists
        """
        if course_id in self.courses:
            return False
            
        self.courses[course_id] = {
            "name": name,
            "description": description
        }
        self._save_data()
        return True

    def record_performance(self, student_id: str, course_id: str, score: float, comments: str = "") -> bool:
        """
        Record a student's performance in a course.
        
        Args:
            student_id: Student identifier
            course_id: Course identifier
            score: Performance score (0-100)
            comments: Optional comments
            
        Returns:
            True if successful, False if student or course doesn't exist
        """
        if student_id not in self.students or course_id not in self.courses:
            return False
            
        if student_id not in self.performance_records:
            self.performance_records[student_id] = []
            
        record = {
            "student_id": student_id,
            "course_id": course_id,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "score": score,
            "comments": comments
        }
        
        self.performance_records[student_id].append(record)
        self._save_data()
        return True

    def get_student_performance(self, student_id: str) -> Optional[List[Dict]]:
        """
        Get all performance records for a student.
        
        Args:
            student_id: Student identifier
            
        Returns:
            List of performance records or None if student doesn't exist
        """
        if student_id not in self.students:
            return None
        return self.performance_records.get(student_id, [])

    def get_course_performance(self, course_id: str) -> Optional[List[Dict]]:
        """
        Get all performance records for a course.
        
        Args:
            course_id: Course identifier
            
        Returns:
            List of performance records or None if course doesn't exist
        """
        if course_id not in self.courses:
            return None
            
        records = []
        for student_records in self.performance_records.values():
            for record in student_records:
                if record["course_id"] == course_id:
                    records.append(record)
        return records

    def get_student_average(self, student_id: str) -> Optional[float]:
        """
        Calculate average performance score for a student.
        
        Args:
            student_id: Student identifier
            
        Returns:
            Average score or None if student doesn't exist or has no records
        """
        if student_id not in self.students:
            return None
            
        records = self.performance_records.get(student_id, [])
        if not records:
            return None
            
        total = sum(float(record["score"]) for record in records)
        return total / len(records)

    def get_course_average(self, course_id: str) -> Optional[float]:
        """
        Calculate average performance score for a course.
        
        Args:
            course_id: Course identifier
            
        Returns:
            Average score or None if course doesn't exist or has no records
        """
        if course_id not in self.courses:
            return None
            
        records = self.get_course_performance(course_id)
        if not records:
            return None
            
        total = sum(float(record["score"]) for record in records)
        return total / len(records)

    def generate_report(self, student_id: str) -> Optional[str]:
        """
        Generate a performance report for a student.
        
        Args:
            student_id: Student identifier
            
        Returns:
            Formatted report string or None if student doesn't exist
        """
        if student_id not in self.students:
            return None
            
        student = self.students[student_id]
        records = self.performance_records.get(student_id, [])
        
        report = [
            f"Student Performance Report",
            f"Name: {student['name']}",
            f"Grade: {student['grade']}",
            f"Contact: {student['contact']}",
            f"Join Date: {student['join_date']}",
            "\nPerformance Records:"
        ]
        
        for record in records:
            course = self.courses[record["course_id"]]
            report.append(
                f"- {course['name']} ({record['date']}): "
                f"Score: {record['score']}, Comments: {record['comments']}"
            )
        
        avg_score = self.get_student_average(student_id)
        if avg_score is not None:
            report.append(f"\nOverall Average Score: {avg_score:.2f}")
        
        return "\n".join(report)


# Example usage
if __name__ == "__main__":
    tracker = StudentPerformanceTracker()
    
    # Add sample data
    tracker.add_student("S001", "Juan Perez", "10th Grade", "juan@example.com")
    tracker.add_course("MATH101", "Mathematics", "Basic algebra and geometry")
    
    # Record performance
    tracker.record_performance("S001", "MATH101", 85, "Good progress")
    tracker.record_performance("S001", "MATH101", 92, "Excellent work")
    
    #
