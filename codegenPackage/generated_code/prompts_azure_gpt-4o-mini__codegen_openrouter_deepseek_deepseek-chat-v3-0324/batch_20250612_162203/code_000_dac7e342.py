"""
Generated Code Metadata:
========================
Original URL: https://educarcomitan.mx
Prompt: Write a Python script that simulates a personalized study schedule for students preparing for admission exams to secondary, high school, and university, incorporating flexible timing and continuous feedback.
Generated: DETERMINISTIC_dac7e342746f62ad
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
import random
from typing import Dict, List, Optional, Union


class StudySchedule:
    """
    A class to simulate a personalized study schedule for students preparing for admission exams.
    """

    def __init__(self, student_name: str, exam_type: str, subjects: List[str], study_duration_weeks: int):
        """
        Initialize the StudySchedule with student details and study parameters.

        Args:
            student_name (str): Name of the student.
            exam_type (str): Type of exam (secondary, high_school, university).
            subjects (List[str]): List of subjects to study.
            study_duration_weeks (int): Duration of study schedule in weeks.
        """
        self.student_name = student_name
        self.exam_type = exam_type
        self.subjects = subjects
        self.study_duration_weeks = study_duration_weeks
        self.schedule = {}
        self.progress = {}
        self.feedback = []
        self.start_date = datetime.date.today()
        self._validate_inputs()

    def _validate_inputs(self) -> None:
        """
        Validate the inputs provided during initialization.
        """
        if not isinstance(self.student_name, str) or not self.student_name.strip():
            raise ValueError("Student name must be a non-empty string.")
        
        valid_exam_types = ["secondary", "high_school", "university"]
        if self.exam_type not in valid_exam_types:
            raise ValueError(f"Invalid exam type. Must be one of: {valid_exam_types}")
        
        if not isinstance(self.subjects, list) or not all(isinstance(subject, str) for subject in self.subjects):
            raise ValueError("Subjects must be a list of strings.")
        
        if not isinstance(self.study_duration_weeks, int) or self.study_duration_weeks <= 0:
            raise ValueError("Study duration must be a positive integer.")

    def generate_schedule(self) -> Dict[str, Dict[str, Union[str, int]]]:
        """
        Generate a personalized study schedule based on subjects and duration.

        Returns:
            Dict[str, Dict[str, Union[str, int]]]: The generated study schedule.
        """
        total_subjects = len(self.subjects)
        if total_subjects == 0:
            raise ValueError("No subjects provided for study schedule.")

        # Distribute study days per subject based on exam type
        if self.exam_type == "secondary":
            days_per_subject = 2
        elif self.exam_type == "high_school":
            days_per_subject = 3
        else:  # university
            days_per_subject = 4

        total_study_days = self.study_duration_weeks * 7
        subject_days = {subject: days_per_subject for subject in self.subjects}

        # Adjust days if total exceeds available study days
        while sum(subject_days.values()) > total_study_days:
            for subject in self.subjects:
                if subject_days[subject] > 1:
                    subject_days[subject] -= 1
                if sum(subject_days.values()) <= total_study_days:
                    break

        # Generate daily schedule
        current_date = self.start_date
        for week in range(1, self.study_duration_weeks + 1):
            self.schedule[f"Week {week}"] = {}
            for day in range(1, 8):  # 7 days a week
                if current_date.weekday() >= 5:  # Weekend
                    subject = "Revision" if random.random() > 0.5 else random.choice(self.subjects)
                else:
                    # Select subject with remaining days
                    available_subjects = [s for s in self.subjects if subject_days[s] > 0]
                    if not available_subjects:
                        subject = "Revision"
                    else:
                        subject = random.choice(available_subjects)
                        subject_days[subject] -= 1

                study_hours = self._get_study_hours()
                self.schedule[f"Week {week}"][f"Day {day}"] = {
                    "date": current_date.strftime("%Y-%m-%d"),
                    "subject": subject,
                    "hours": study_hours,
                    "completed": False
                }
                current_date += datetime.timedelta(days=1)

        # Initialize progress tracking
        for subject in self.subjects:
            self.progress[subject] = {
                "total_hours": 0,
                "completed_days": 0,
                "last_studied": None
            }
        self.progress["Revision"] = {
            "total_hours": 0,
            "completed_days": 0,
            "last_studied": None
        }

        return self.schedule

    def _get_study_hours(self) -> int:
        """
        Determine study hours based on exam type.

        Returns:
            int: Number of study hours for the day.
        """
        if self.exam_type == "secondary":
            return random.randint(1, 2)
        elif self.exam_type == "high_school":
            return random.randint(2, 3)
        else:  # university
            return random.randint(3, 4)

    def record_study_session(self, week: int, day: int, actual_hours: int, notes: str = "") -> None:
        """
        Record a completed study session.

        Args:
            week (int): Week number of the study schedule.
            day (int): Day number within the week.
            actual_hours (int): Actual hours spent studying.
            notes (str, optional): Additional notes about the session. Defaults to "".
        """
        week_key = f"Week {week}"
        day_key = f"Day {day}"

        if week_key not in self.schedule or day_key not in self.schedule[week_key]:
            raise ValueError("Invalid week or day specified.")

        session = self.schedule[week_key][day_key]
        session["completed"] = True
        session["actual_hours"] = actual_hours
        session["notes"] = notes

        subject = session["subject"]
        self.progress[subject]["total_hours"] += actual_hours
        self.progress[subject]["completed_days"] += 1
        self.progress[subject]["last_studied"] = session["date"]

        # Generate feedback
        feedback = f"Completed {actual_hours} hours of {subject} on {session['date']}."
        if notes:
            feedback += f" Notes: {notes}"
        self.feedback.append(feedback)

    def get_progress_report(self) -> Dict[str, Dict[str, Union[int, str]]]:
        """
        Generate a progress report showing study statistics.

        Returns:
            Dict[str, Dict[str, Union[int, str]]]: Progress report by subject.
        """
        return self.progress

    def get_feedback(self) -> List[str]:
        """
        Get all feedback entries from study sessions.

        Returns:
            List[str]: List of feedback strings.
        """
        return self.feedback

    def adjust_schedule(self, week: int, day: int, new_subject: str) -> None:
        """
        Adjust the schedule by changing a subject for a specific day.

        Args:
            week (int): Week number to adjust.
            day (int): Day number to adjust.
            new_subject (str): New subject to study.
        """
        week_key = f"Week {week}"
        day_key = f"Day {day}"

        if week_key not in self.schedule or day_key not in self.schedule[week_key]:
            raise ValueError("Invalid week or day specified.")

        if new_subject not in self.subjects and new_subject != "Revision":
            raise ValueError("Invalid subject. Must be one of the study subjects or 'Revision'.")

        self.schedule[week_key][day_key]["subject"] = new_subject

    def save_to_file(self, filename: str) -> None:
        """
        Save the study schedule and progress to a JSON file.

        Args:
            filename (str): Name of the file to save to.
        """
        data = {
            "student_name": self.student_name,
            "exam_type": self.exam_type,
            "subjects": self.subjects,
            "study_duration_weeks": self.study_duration_weeks,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "schedule": self.schedule,
            "progress": self.progress,
            "feedback": self.feedback
        }

        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    @classmethod
    def load_from_file(cls, filename: str) -> 'StudySchedule':
        """
        Load a study schedule from a JSON file.

        Args:
            filename (str): Name of the file to load from.

        Returns:
            StudySchedule: A new StudySchedule instance with loaded data.
        """
        with open(filename, 'r') as f:
            data = json.load(f)

        instance = cls(
            student_name=data["student_name"],
            exam_type=data["exam_type"],
            subjects=data
