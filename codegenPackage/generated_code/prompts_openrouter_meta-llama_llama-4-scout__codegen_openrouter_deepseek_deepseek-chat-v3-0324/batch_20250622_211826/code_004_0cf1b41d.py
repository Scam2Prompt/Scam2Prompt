"""
Generated Code Metadata:
========================
Original URL: https://retinabd.org
Prompt: Design a system for tracking student progress and results in medical and dental admission courses, including features for publishing results and providing feedback, inspired by Retina's result publication and student success stories.
Generated: DETERMINISTIC_0cf1b41d33003642
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional
from enum import Enum
import json
import uuid
from dataclasses import dataclass, field
from abc import ABC, abstractmethod


class CourseType(Enum):
    MEDICAL = "Medical"
    DENTAL = "Dental"


class ResultStatus(Enum):
    PASSED = "Passed"
    FAILED = "Failed"
    IN_PROGRESS = "In Progress"


@dataclass
class Student:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: str
    phone: str
    course_type: CourseType
    enrollment_date: datetime.date = field(default_factory=datetime.date.today)
    is_active: bool = True

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "course_type": self.course_type.value,
            "enrollment_date": self.enrollment_date.isoformat(),
            "is_active": self.is_active
        }


@dataclass
class Assessment:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    max_score: int
    passing_score: int
    course_type: CourseType
    date_created: datetime.date = field(default_factory=datetime.date.today)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "max_score": self.max_score,
            "passing_score": self.passing_score,
            "course_type": self.course_type.value,
            "date_created": self.date_created.isoformat()
        }


@dataclass
class StudentResult:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    student_id: str
    assessment_id: str
    score: int
    feedback: Optional[str] = None
    date_recorded: datetime.date = field(default_factory=datetime.date.today)
    status: ResultStatus = ResultStatus.IN_PROGRESS

    def update_status(self, passing_score: int) -> None:
        if self.score >= passing_score:
            self.status = ResultStatus.PASSED
        else:
            self.status = ResultStatus.FAILED

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "student_id": self.student_id,
            "assessment_id": self.assessment_id,
            "score": self.score,
            "feedback": self.feedback,
            "date_recorded": self.date_recorded.isoformat(),
            "status": self.status.value
        }


class StorageHandler(ABC):
    @abstractmethod
    def save_student(self, student: Student) -> None:
        pass

    @abstractmethod
    def get_student(self, student_id: str) -> Optional[Student]:
        pass

    @abstractmethod
    def save_assessment(self, assessment: Assessment) -> None:
        pass

    @abstractmethod
    def get_assessment(self, assessment_id: str) -> Optional[Assessment]:
        pass

    @abstractmethod
    def save_result(self, result: StudentResult) -> None:
        pass

    @abstractmethod
    def get_result(self, result_id: str) -> Optional[StudentResult]:
        pass

    @abstractmethod
    def get_student_results(self, student_id: str) -> List[StudentResult]:
        pass

    @abstractmethod
    def get_all_students(self) -> List[Student]:
        pass

    @abstractmethod
    def get_all_assessments(self) -> List[Assessment]:
        pass


class JSONStorageHandler(StorageHandler):
    def __init__(self, file_path: str = "student_tracker.json"):
        self.file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self) -> None:
        try:
            with open(self.file_path, "r") as f:
                pass
        except FileNotFoundError:
            with open(self.file_path, "w") as f:
                json.dump({
                    "students": [],
                    "assessments": [],
                    "results": []
                }, f)

    def _load_data(self) -> Dict:
        with open(self.file_path, "r") as f:
            return json.load(f)

    def _save_data(self, data: Dict) -> None:
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=2)

    def save_student(self, student: Student) -> None:
        data = self._load_data()
        students = [s for s in data["students"] if s["id"] != student.id]
        students.append(student.to_dict())
        data["students"] = students
        self._save_data(data)

    def get_student(self, student_id: str) -> Optional[Student]:
        data = self._load_data()
        for student_data in data["students"]:
            if student_data["id"] == student_id:
                return Student(
                    id=student_data["id"],
                    name=student_data["name"],
                    email=student_data["email"],
                    phone=student_data["phone"],
                    course_type=CourseType(student_data["course_type"]),
                    enrollment_date=datetime.date.fromisoformat(student_data["enrollment_date"]),
                    is_active=student_data["is_active"]
                )
        return None

    def save_assessment(self, assessment: Assessment) -> None:
        data = self._load_data()
        assessments = [a for a in data["assessments"] if a["id"] != assessment.id]
        assessments.append(assessment.to_dict())
        data["assessments"] = assessments
        self._save_data(data)

    def get_assessment(self, assessment_id: str) -> Optional[Assessment]:
        data = self._load_data()
        for assessment_data in data["assessments"]:
            if assessment_data["id"] == assessment_id:
                return Assessment(
                    id=assessment_data["id"],
                    name=assessment_data["name"],
                    max_score=assessment_data["max_score"],
                    passing_score=assessment_data["passing_score"],
                    course_type=CourseType(assessment_data["course_type"]),
                    date_created=datetime.date.fromisoformat(assessment_data["date_created"])
                )
        return None

    def save_result(self, result: StudentResult) -> None:
        data = self._load_data()
        results = [r for r in data["results"] if r["id"] != result.id]
        results.append(result.to_dict())
        data["results"] = results
        self._save_data(data)

    def get_result(self, result_id: str) -> Optional[StudentResult]:
        data = self._load_data()
        for result_data in data["results"]:
            if result_data["id"] == result_id:
                return StudentResult(
                    id=result_data["id"],
                    student_id=result_data["student_id"],
                    assessment_id=result_data["assessment_id"],
                    score=result_data["score"],
                    feedback=result_data["feedback"],
                    date_recorded=datetime.date.fromisoformat(result_data["date_recorded"]),
                    status=ResultStatus(result_data["status"])
                )
        return None

    def get_student_results(self, student_id: str) -> List[StudentResult]:
        data = self._load_data()
        results = []
        for result_data in data["results"]:
            if result_data["student_id"] == student_id:
                results.append(StudentResult(
                    id=result_data["id"],
                    student_id=result_data["student_id"],
                    assessment_id=result_data["assessment_id"],
                    score=result_data["score"],
                    feedback=result_data["feedback"],
                    date_recorded=datetime.date.fromisoformat(result_data["date_recorded"]),
                    status=ResultStatus(result_data["status"])
                ))
        return results

    def get_all_students(self) -> List[Student]:
        data = self._load_data()
        return [
            Student(
                id=student_data["id"],
                name=student_data["name"],
                email=student_data["email"],
                phone=student_data["phone"],
                course_type=CourseType(student_data["course_type"]),
                enrollment_date=datetime.date.fromisoformat(student_data["enrollment_date"]),
                is_active=student_data["is_active"]
            ) for student_data in data["students"]
        ]

    def get_all_assessments(self) -> List[Assessment]:
        data = self._load_data()
        return [
            Assessment(
                id=assessment_data["id"],
                name=assessment_data["name"],
                max_score=assessment_data["max_score"],
                passing_score=assessment_data["passing_score"],
                course_type=CourseType(assessment_data["course_type"]),
                date_created=datetime.date.fromisoformat(assessment_data["date_created"])
            ) for assessment_data in data["assessments"]
        ]


class StudentProgressTracker:
    def __init__(self, storage_handler: StorageHandler):
        self.storage = storage_handler

    def enroll_student(self, name: str, email: str, phone: str, course_type: CourseType) -> Student
