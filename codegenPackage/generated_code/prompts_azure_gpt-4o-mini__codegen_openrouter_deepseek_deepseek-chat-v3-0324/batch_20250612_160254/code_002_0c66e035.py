"""
Generated Code Metadata:
========================
Original URL: https://colatraining.com
Prompt: Write a code snippet that integrates a booking system for vocational training courses, inspired by the course offerings at CoLa Training Services.
Generated: DETERMINISTIC_0c66e0356142e68e
Batch ID: 20250612_160254
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
from enum import Enum, auto


class CourseStatus(Enum):
    AVAILABLE = auto()
    FULL = auto()
    CANCELLED = auto()


class Course:
    def __init__(
        self,
        course_id: str,
        title: str,
        description: str,
        max_participants: int,
        start_date: datetime.date,
        end_date: datetime.date,
        price: float
    ):
        self.course_id = course_id
        self.title = title
        self.description = description
        self.max_participants = max_participants
        self.start_date = start_date
        self.end_date = end_date
        self.price = price
        self.participants: List[str] = []
        self.status = CourseStatus.AVAILABLE

    def add_participant(self, participant_id: str) -> bool:
        if self.status != CourseStatus.AVAILABLE:
            return False
        
        if len(self.participants) >= self.max_participants:
            self.status = CourseStatus.FULL
            return False
            
        self.participants.append(participant_id)
        if len(self.participants) == self.max_participants:
            self.status = CourseStatus.FULL
        return True

    def cancel_course(self) -> bool:
        if self.status == CourseStatus.CANCELLED:
            return False
            
        self.status = CourseStatus.CANCELLED
        return True

    def get_available_spots(self) -> int:
        return self.max_participants - len(self.participants)


class BookingSystem:
    def __init__(self):
        self.courses: Dict[str, Course] = {}
        self.bookings: Dict[str, List[str]] = {}  # participant_id: [course_ids]

    def add_course(self, course: Course) -> bool:
        if course.course_id in self.courses:
            return False
            
        self.courses[course.course_id] = course
        return True

    def book_course(self, participant_id: str, course_id: str) -> bool:
        if course_id not in self.courses:
            return False
            
        course = self.courses[course_id]
        success = course.add_participant(participant_id)
        
        if success:
            if participant_id not in self.bookings:
                self.bookings[participant_id] = []
            self.bookings[participant_id].append(course_id)
            
        return success

    def cancel_booking(self, participant_id: str, course_id: str) -> bool:
        if participant_id not in self.bookings or course_id not in self.bookings[participant_id]:
            return False
            
        if course_id not in self.courses:
            return False
            
        course = self.courses[course_id]
        try:
            course.participants.remove(participant_id)
            self.bookings[participant_id].remove(course_id)
            
            if course.status == CourseStatus.FULL and len(course.participants) < course.max_participants:
                course.status = CourseStatus.AVAILABLE
                
            return True
        except ValueError:
            return False

    def get_available_courses(self) -> List[Course]:
        return [course for course in self.courses.values() 
                if course.status == CourseStatus.AVAILABLE]

    def get_participant_bookings(self, participant_id: str) -> Optional[List[Course]]:
        if participant_id not in self.bookings:
            return None
            
        return [self.courses[course_id] 
                for course_id in self.bookings[participant_id] 
                if course_id in self.courses]


class PaymentSystem:
    @staticmethod
    def process_payment(amount: float, payment_details: Dict) -> bool:
        # In a real implementation, this would integrate with a payment gateway
        # For demo purposes, we'll just simulate successful payment
        return True


class BookingManager:
    def __init__(self):
        self.booking_system = BookingSystem()
        self.payment_system = PaymentSystem()

    def book_course_with_payment(
        self,
        participant_id: str,
        course_id: str,
        payment_details: Dict
    ) -> bool:
        if course_id not in self.booking_system.courses:
            return False
            
        course = self.booking_system.courses[course_id]
        
        if not self.payment_system.process_payment(course.price, payment_details):
            return False
            
        return self.booking_system.book_course(participant_id, course_id)

    def cancel_booking_with_refund(
        self,
        participant_id: str,
        course_id: str,
        refund_details: Dict
    ) -> bool:
        # In a real system, we would process refund here
        return self.booking_system.cancel_booking(participant_id, course_id)
```
