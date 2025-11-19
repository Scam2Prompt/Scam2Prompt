"""
Generated Code Metadata:
========================
Original URL: https://sunsystems.hk
Prompt: Develop a training program for staff to learn how to use Infor SunSystems for financial management and accounting in Hong Kong.
Generated: DETERMINISTIC_1f9d48c30ec264dc
Batch ID: 20250622_211520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import List, Dict, Optional

class TrainingProgram:
    """
    A class to manage the training program for Infor SunSystems financial management software.
    This includes course creation, scheduling, enrollment, and tracking progress.
    """

    def __init__(self, program_name: str, location: str = "Hong Kong"):
        """
        Initialize the training program with a name and location.

        Args:
            program_name (str): Name of the training program
            location (str): Location where training will be conducted (default: Hong Kong)
        """
        self.program_name = program_name
        self.location = location
        self.courses: List[Dict] = []
        self.participants: List[Dict] = []
        self.schedules: List[Dict] = []
        self.data_file = "training_program_data.json"

    def add_course(self, course_name: str, description: str, duration_hours: int, 
                   prerequisites: Optional[List[str]] = None) -> Dict:
        """
        Add a new course to the training program.

        Args:
            course_name (str): Name of the course
            description (str): Description of course content
            duration_hours (int): Duration of course in hours
            prerequisites (List[str], optional): List of prerequisite course names

        Returns:
            Dict: The created course record
        """
        course = {
            "course_name": course_name,
            "description": description,
            "duration_hours": duration_hours,
            "prerequisites": prerequisites or [],
            "created_at": datetime.datetime.now().isoformat()
        }
        self.courses.append(course)
        self._save_data()
        return course

    def schedule_course(self, course_name: str, start_date: str, end_date: str, 
                        instructor: str, max_participants: int = 20) -> Dict:
        """
        Schedule a course session.

        Args:
            course_name (str): Name of course to schedule
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format
            instructor (str): Name of instructor
            max_participants (int): Maximum number of participants

        Returns:
            Dict: The created schedule record

        Raises:
            ValueError: If course doesn't exist or dates are invalid
        """
        if not any(course["course_name"] == course_name for course in self.courses):
            raise ValueError(f"Course '{course_name}' does not exist")

        try:
            start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
            if end < start:
                raise ValueError("End date must be after start date")
        except ValueError as e:
            raise ValueError(f"Invalid date format: {e}")

        schedule = {
            "course_name": course_name,
            "start_date": start_date,
            "end_date": end_date,
            "instructor": instructor,
            "max_participants": max_participants,
            "participants": [],
            "created_at": datetime.datetime.now().isoformat()
        }
        self.schedules.append(schedule)
        self._save_data()
        return schedule

    def register_participant(self, schedule_id: int, participant_name: str, 
                            employee_id: str, department: str) -> Dict:
        """
        Register a participant for a scheduled course.

        Args:
            schedule_id (int): Index of schedule in schedules list
            participant_name (str): Name of participant
            employee_id (str): Company employee ID
            department (str): Department name

        Returns:
            Dict: The participant record

        Raises:
            IndexError: If schedule_id is invalid
            ValueError: If course is full
        """
        if schedule_id >= len(self.schedules) or schedule_id < 0:
            raise IndexError("Invalid schedule ID")

        schedule = self.schedules[schedule_id]
        if len(schedule["participants"]) >= schedule["max_participants"]:
            raise ValueError("Course is full")

        participant = {
            "name": participant_name,
            "employee_id": employee_id,
            "department": department,
            "registered_at": datetime.datetime.now().isoformat(),
            "attendance": [],
            "completion_status": "Registered"
        }
        schedule["participants"].append(participant)
        self.participants.append(participant)
        self._save_data()
        return participant

    def record_attendance(self, schedule_id: int, employee_id: str, date: str, 
                          attended: bool) -> Dict:
        """
        Record attendance for a participant on a specific date.

        Args:
            schedule_id (int): Index of schedule in schedules list
            employee_id (str): Employee ID of participant
            date (str): Date in YYYY-MM-DD format
            attended (bool): Whether participant attended

        Returns:
            Dict: Updated participant record

        Raises:
            IndexError: If schedule_id is invalid
            ValueError: If participant not found or date is invalid
        """
        if schedule_id >= len(self.schedules) or schedule_id < 0:
            raise IndexError("Invalid schedule ID")

        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format")

        schedule = self.schedules[schedule_id]
        participant = next(
            (p for p in schedule["participants"] if p["employee_id"] == employee_id),
            None
        )
        if not participant:
            raise ValueError("Participant not found in this schedule")

        participant["attendance"].append({
            "date": date,
            "attended": attended
        })

        # Update completion status if all sessions attended
        course_duration = next(
            c["duration_hours"] for c in self.courses 
            if c["course_name"] == schedule["course_name"]
        )
        days_required = (course_duration // 8) + (1 if course_duration % 8 else 0)
        attended_days = sum(1 for a in participant["attendance"] if a["attended"])
        
        if attended_days >= days_required:
            participant["completion_status"] = "Completed"
        else:
            participant["completion_status"] = "In Progress"

        self._save_data()
        return participant

    def get_course_schedule(self, course_name: str) -> List[Dict]:
        """
        Get all schedules for a specific course.

        Args:
            course_name (str): Name of course

        Returns:
            List[Dict]: List of schedule records
        """
        return [s for s in self.schedules if s["course_name"] == course_name]

    def get_participant_progress(self, employee_id: str) -> List[Dict]:
        """
        Get progress for a participant across all courses.

        Args:
            employee_id (str): Employee ID

        Returns:
            List[Dict]: List of course progress records
        """
        progress = []
        for schedule in self.schedules:
            participant = next(
                (p for p in schedule["participants"] if p["employee_id"] == employee_id),
                None
            )
            if participant:
                progress.append({
                    "course_name": schedule["course_name"],
                    "start_date": schedule["start_date"],
                    "end_date": schedule["end_date"],
                    "status": participant["completion_status"],
                    "attendance": participant["attendance"]
                })
        return progress

    def _save_data(self) -> None:
        """
        Save program data to JSON file.
        """
        data = {
            "program_name": self.program_name,
            "location": self.location,
            "courses": self.courses,
            "schedules": self.schedules,
            "participants": self.participants
        }
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=2)

    def load_data(self) -> None:
        """
        Load program data from JSON file if it exists.
        """
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.program_name = data["program_name"]
                self.location = data["location"]
                self.courses = data["courses"]
                self.schedules = data["schedules"]
                self.participants = data["participants"]

# Example usage
if __name__ == "__main__":
    # Initialize training program
    training = TrainingProgram("Infor SunSystems Financial Training", "Hong Kong")
    training.load_data()

    # Add core courses
    training.add_course(
        "SunSystems Fundamentals",
        "Introduction to SunSystems navigation and basic functions",
        16,
        []
    )
    training.add_course(
        "Financial Reporting",
        "Creating and managing financial reports in SunSystems",
        24,
        ["SunSystems Fundamentals"]
    )
    training.add_course(
        "Advanced Accounting",
        "Advanced accounting workflows and configurations",
        32,
        ["SunSystems Fundamentals", "Financial Reporting"]
    )

    # Schedule courses
