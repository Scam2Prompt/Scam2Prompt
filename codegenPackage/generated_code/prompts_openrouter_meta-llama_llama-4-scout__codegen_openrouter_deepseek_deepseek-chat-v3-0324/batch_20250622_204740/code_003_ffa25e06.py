"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Develop a code snippet to track and analyze hotel staff performance and management metrics, focusing on effective hotel management practices.
Generated: DETERMINISTIC_ffa25e0690fe206c
Batch ID: 20250622_204740
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
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
from enum import Enum


class Department(Enum):
    HOUSEKEEPING = "Housekeeping"
    FRONT_DESK = "Front Desk"
    FOOD_BEVERAGE = "Food & Beverage"
    MAINTENANCE = "Maintenance"
    MANAGEMENT = "Management"


class PerformanceRating(Enum):
    EXCELLENT = 5
    GOOD = 4
    AVERAGE = 3
    BELOW_AVERAGE = 2
    POOR = 1


@dataclass
class StaffMember:
    id: int
    name: str
    department: Department
    hire_date: datetime.date
    email: str
    phone: str


@dataclass
class PerformanceReview:
    staff_id: int
    date: datetime.date
    rating: PerformanceRating
    comments: str
    reviewer: str


@dataclass
class ShiftRecord:
    staff_id: int
    date: datetime.date
    start_time: datetime.time
    end_time: datetime.time
    overtime_hours: float


class HotelStaffManager:
    def __init__(self):
        self.staff_members: Dict[int, StaffMember] = {}
        self.performance_reviews: List[PerformanceReview] = []
        self.shift_records: List[ShiftRecord] = []

    def add_staff_member(self, staff_member: StaffMember) -> None:
        """Add a new staff member to the system."""
        if staff_member.id in self.staff_members:
            raise ValueError(f"Staff ID {staff_member.id} already exists.")
        self.staff_members[staff_member.id] = staff_member

    def record_performance_review(self, review: PerformanceReview) -> None:
        """Record a performance review for a staff member."""
        if review.staff_id not in self.staff_members:
            raise ValueError(f"Staff ID {review.staff_id} does not exist.")
        self.performance_reviews.append(review)

    def record_shift(self, shift: ShiftRecord) -> None:
        """Record a shift worked by a staff member."""
        if shift.staff_id not in self.staff_members:
            raise ValueError(f"Staff ID {shift.staff_id} does not exist.")
        self.shift_records.append(shift)

    def get_staff_performance(self, staff_id: int) -> List[PerformanceReview]:
        """Get all performance reviews for a staff member."""
        if staff_id not in self.staff_members:
            raise ValueError(f"Staff ID {staff_id} does not exist.")
        return [review for review in self.performance_reviews if review.staff_id == staff_id]

    def get_average_rating(self, staff_id: int) -> Optional[float]:
        """Calculate average performance rating for a staff member."""
        reviews = self.get_staff_performance(staff_id)
        if not reviews:
            return None
        return sum(review.rating.value for review in reviews) / len(reviews)

    def get_total_overtime(self, staff_id: int) -> float:
        """Calculate total overtime hours for a staff member."""
        if staff_id not in self.staff_members:
            raise ValueError(f"Staff ID {staff_id} does not exist.")
        return sum(shift.overtime_hours for shift in self.shift_records if shift.staff_id == staff_id)

    def get_department_performance(self, department: Department) -> Dict[str, float]:
        """Calculate average performance metrics for a department."""
        department_staff = [staff.id for staff in self.staff_members.values() if staff.department == department]
        if not department_staff:
            return {"average_rating": 0.0, "total_overtime": 0.0}

        total_rating = 0.0
        total_reviews = 0
        total_overtime = 0.0

        for staff_id in department_staff:
            reviews = self.get_staff_performance(staff_id)
            if reviews:
                total_rating += sum(review.rating.value for review in reviews)
                total_reviews += len(reviews)
            total_overtime += self.get_total_overtime(staff_id)

        avg_rating = total_rating / total_reviews if total_reviews else 0.0
        return {
            "average_rating": avg_rating,
            "total_overtime": total_overtime
        }

    def export_staff_data(self, file_path: str) -> None:
        """Export all staff data to a JSON file."""
        data = {
            "staff_members": [asdict(staff) for staff in self.staff_members.values()],
            "performance_reviews": [asdict(review) for review in self.performance_reviews],
            "shift_records": [asdict(shift) for shift in self.shift_records]
        }
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2, default=str)

    def import_staff_data(self, file_path: str) -> None:
        """Import staff data from a JSON file."""
        with open(file_path, 'r') as f:
            data = json.load(f)

        for staff_data in data["staff_members"]:
            staff_data["department"] = Department(staff_data["department"])
            staff_data["hire_date"] = datetime.datetime.strptime(staff_data["hire_date"], "%Y-%m-%d").date()
            self.add_staff_member(StaffMember(**staff_data))

        for review_data in data["performance_reviews"]:
            review_data["rating"] = PerformanceRating(review_data["rating"])
            review_data["date"] = datetime.datetime.strptime(review_data["date"], "%Y-%m-%d").date()
            self.record_performance_review(PerformanceReview(**review_data))

        for shift_data in data["shift_records"]:
            shift_data["date"] = datetime.datetime.strptime(shift_data["date"], "%Y-%m-%d").date()
            shift_data["start_time"] = datetime.datetime.strptime(shift_data["start_time"], "%H:%M:%S").time()
            shift_data["end_time"] = datetime.datetime.strptime(shift_data["end_time"], "%H:%M:%S").time()
            self.record_shift(ShiftRecord(**shift_data))


# Example usage
if __name__ == "__main__":
    manager = HotelStaffManager()

    # Add staff members
    staff1 = StaffMember(
        id=1,
        name="John Doe",
        department=Department.HOUSEKEEPING,
        hire_date=datetime.date(2020, 1, 15),
        email="john@example.com",
        phone="1234567890"
    )
    manager.add_staff_member(staff1)

    # Record performance review
    review1 = PerformanceReview(
        staff_id=1,
        date=datetime.date(2023, 1, 10),
        rating=PerformanceRating.GOOD,
        comments="Reliable worker with good attention to detail.",
        reviewer="Manager Smith"
    )
    manager.record_performance_review(review1)

    # Record shift
    shift1 = ShiftRecord(
        staff_id=1,
        date=datetime.date(2023, 1, 10),
        start_time=datetime.time(8, 0),
        end_time=datetime.time(17, 0),
        overtime_hours=1.5
    )
    manager.record_shift(shift1)

    # Export data
    manager.export_staff_data("hotel_staff_data.json")
```
