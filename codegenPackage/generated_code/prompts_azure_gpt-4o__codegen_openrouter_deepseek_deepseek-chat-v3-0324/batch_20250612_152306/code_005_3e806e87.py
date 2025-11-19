"""
Generated Code Metadata:
========================
Original URL: https://rspbharat.com
Prompt: Create a program to manage course durations and schedules for vocational training programs like "Cloud Computing and Storage Basics" and "Diploma in Industrial Safety" listed on the RSP Bharat website.
Generated: DETERMINISTIC_3e806e87c87d63a8
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Union

class CourseSchedule:
    """Represents a schedule for a single course session."""
    
    def __init__(self, start_date: str, end_date: str, days_of_week: List[str], 
                 start_time: str, end_time: str, max_capacity: int):
        """
        Initialize a course schedule.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            days_of_week: List of days (e.g., ["Mon", "Wed", "Fri"])
            start_time: Start time in HH:MM format
            end_time: End time in HH:MM format
            max_capacity: Maximum number of students
        """
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        self.days_of_week = days_of_week
        self.start_time = start_time
        self.end_time = end_time
        self.max_capacity = max_capacity
        self.current_enrollment = 0
        
    def to_dict(self) -> Dict:
        """Convert schedule to dictionary for serialization."""
        return {
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "days_of_week": self.days_of_week,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "max_capacity": self.max_capacity,
            "current_enrollment": self.current_enrollment
        }
        
    def is_full(self) -> bool:
        """Check if the schedule has reached maximum capacity."""
        return self.current_enrollment >= self.max_capacity
        
    def enroll_student(self) -> bool:
        """Enroll a student if there's capacity."""
        if not self.is_full():
            self.current_enrollment += 1
            return True
        return False

class Course:
    """Represents a vocational training course."""
    
    def __init__(self, course_id: str, name: str, description: str, duration_weeks: int):
        """
        Initialize a course.
        
        Args:
            course_id: Unique identifier for the course
            name: Course name
            description: Course description
            duration_weeks: Duration in weeks
        """
        self.course_id = course_id
        self.name = name
        self.description = description
        self.duration_weeks = duration_weeks
        self.schedules: List[CourseSchedule] = []
        
    def add_schedule(self, schedule: CourseSchedule) -> None:
        """Add a schedule to the course."""
        self.schedules.append(schedule)
        
    def get_available_schedules(self) -> List[CourseSchedule]:
        """Get all schedules with available capacity."""
        return [s for s in self.schedules if not s.is_full()]
        
    def to_dict(self) -> Dict:
        """Convert course to dictionary for serialization."""
        return {
            "course_id": self.course_id,
            "name": self.name,
            "description": self.description,
            "duration_weeks": self.duration_weeks,
            "schedules": [s.to_dict() for s in self.schedules]
        }

class CourseManager:
    """Manages multiple vocational training courses."""
    
    def __init__(self):
        """Initialize the course manager."""
        self.courses: Dict[str, Course] = {}
        
    def add_course(self, course: Course) -> None:
        """Add a course to the manager."""
        if course.course_id in self.courses:
            raise ValueError(f"Course with ID {course.course_id} already exists")
        self.courses[course.course_id] = course
        
    def get_course(self, course_id: str) -> Optional[Course]:
        """Get a course by ID."""
        return self.courses.get(course_id)
        
    def remove_course(self, course_id: str) -> bool:
        """Remove a course by ID."""
        if course_id in self.courses:
            del self.courses[course_id]
            return True
        return False
        
    def enroll_student(self, course_id: str, schedule_index: int) -> bool:
        """
        Enroll a student in a course schedule.
        
        Args:
            course_id: ID of the course
            schedule_index: Index of the schedule in the course's schedules list
            
        Returns:
            bool: True if enrollment was successful, False otherwise
        """
        course = self.get_course(course_id)
        if not course:
            return False
            
        try:
            schedule = course.schedules[schedule_index]
            return schedule.enroll_student()
        except IndexError:
            return False
            
    def save_to_file(self, filename: str) -> bool:
        """Save all courses to a JSON file."""
        try:
            with open(filename, 'w') as f:
                data = {
                    "courses": [course.to_dict() for course in self.courses.values()]
                }
                json.dump(data, f, indent=2)
            return True
        except (IOError, json.JSONDecodeError):
            return False
            
    def load_from_file(self, filename: str) -> bool:
        """Load courses from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.courses = {}
                
                for course_data in data.get("courses", []):
                    course = Course(
                        course_id=course_data["course_id"],
                        name=course_data["name"],
                        description=course_data["description"],
                        duration_weeks=course_data["duration_weeks"]
                    )
                    
                    for schedule_data in course_data.get("schedules", []):
                        schedule = CourseSchedule(
                            start_date=schedule_data["start_date"],
                            end_date=schedule_data["end_date"],
                            days_of_week=schedule_data["days_of_week"],
                            start_time=schedule_data["start_time"],
                            end_time=schedule_data["end_time"],
                            max_capacity=schedule_data["max_capacity"]
                        )
                        schedule.current_enrollment = schedule_data["current_enrollment"]
                        course.add_schedule(schedule)
                    
                    self.add_course(course)
            return True
        except (IOError, json.JSONDecodeError, KeyError):
            return False

# Example usage
if __name__ == "__main__":
    manager = CourseManager()
    
    # Create sample courses
    cloud_course = Course(
        course_id="CC101",
        name="Cloud Computing and Storage Basics",
        description="Fundamentals of cloud computing and storage technologies",
        duration_weeks=12
    )
    
    safety_course = Course(
        course_id="DIS202",
        name="Diploma in Industrial Safety",
        description="Comprehensive training in industrial safety practices",
        duration_weeks=24
    )
    
    # Add schedules
    cloud_course.add_schedule(CourseSchedule(
        start_date="2023-10-01",
        end_date="2023-12-24",
        days_of_week=["Mon", "Wed", "Fri"],
        start_time="09:00",
        end_time="12:00",
        max_capacity=20
    ))
    
    safety_course.add_schedule(CourseSchedule(
        start_date="2023-10-02",
        end_date="2024-03-25",
        days_of_week=["Tue", "Thu"],
        start_time="14:00",
        end_time="17:00",
        max_capacity=15
    ))
    
    # Add courses to manager
    manager.add_course(cloud_course)
    manager.add_course(safety_course)
    
    # Save to file
    manager.save_to_file("courses.json")
    
    # Load from file
    new_manager = CourseManager()
    new_manager.load_from_file("courses.json")
    
    # Enroll a student
    success = new_manager.enroll_student("CC101", 0)
    print(f"Enrollment successful: {success}")
```
