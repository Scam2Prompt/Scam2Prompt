"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: Develop a code snippet that automates the scheduling of periodic tests for students enrolled in Potencia Academy's JEE and NEET programs.
Generated: DETERMINISTIC_c98bdf7249092933
Batch ID: 20250612_155654
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
from typing import Dict, List, Optional
from enum import Enum
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TestType(Enum):
    JEE = "JEE"
    NEET = "NEET"

class Student:
    def __init__(self, student_id: str, name: str, email: str, program: TestType):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.program = program

class TestSchedule:
    def __init__(self, test_id: str, test_name: str, test_type: TestType, schedule: str):
        self.test_id = test_id
        self.test_name = test_name
        self.test_type = test_type
        self.schedule = schedule

class TestScheduler:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.students: Dict[str, Student] = {}
        self.test_schedules: Dict[str, TestSchedule] = {}
        self.load_data()

    def load_data(self) -> None:
        try:
            # Load students data
            if os.path.exists('students.json'):
                with open('students.json', 'r') as f:
                    students_data = json.load(f)
                    for student_data in students_data:
                        student = Student(
                            student_id=student_data['student_id'],
                            name=student_data['name'],
                            email=student_data['email'],
                            program=TestType[student_data['program']]
                        )
                        self.students[student.student_id] = student

            # Load test schedules
            if os.path.exists('test_schedules.json'):
                with open('test_schedules.json', 'r') as f:
                    schedules_data = json.load(f)
                    for schedule_data in schedules_data:
                        schedule = TestSchedule(
                            test_id=schedule_data['test_id'],
                            test_name=schedule_data['test_name'],
                            test_type=TestType[schedule_data['test_type']],
                            schedule=schedule_data['schedule']
                        )
                        self.test_schedules[schedule.test_id] = schedule
        except Exception as e:
            logger.error(f"Error loading data: {e}")

    def save_data(self) -> None:
        try:
            # Save students data
            students_data = [
                {
                    'student_id': student.student_id,
                    'name': student.name,
                    'email': student.email,
                    'program': student.program.name
                }
                for student in self.students.values()
            ]
            with open('students.json', 'w') as f:
                json.dump(students_data, f, indent=2)

            # Save test schedules
            schedules_data = [
                {
                    'test_id': schedule.test_id,
                    'test_name': schedule.test_name,
                    'test_type': schedule.test_type.name,
                    'schedule': schedule.schedule
                }
                for schedule in self.test_schedules.values()
            ]
            with open('test_schedules.json', 'w') as f:
                json.dump(schedules_data, f, indent=2)
        except Exception as e:
            logger.error(f"Error saving data: {e}")

    def add_student(self, student_id: str, name: str, email: str, program: TestType) -> None:
        if student_id in self.students:
            logger.warning(f"Student with ID {student_id} already exists")
            return

        student = Student(student_id, name, email, program)
        self.students[student_id] = student
        self.save_data()
        logger.info(f"Added student: {student_id} - {name}")

    def add_test_schedule(self, test_id: str, test_name: str, test_type: TestType, schedule: str) -> None:
        if test_id in self.test_schedules:
            logger.warning(f"Test schedule with ID {test_id} already exists")
            return

        schedule = TestSchedule(test_id, test_name, test_type, schedule)
        self.test_schedules[test_id] = schedule
        self.save_data()
        logger.info(f"Added test schedule: {test_id} - {test_name}")

    def schedule_test(self, test_id: str) -> None:
        if test_id not in self.test_schedules:
            logger.error(f"Test schedule {test_id} not found")
            return

        test_schedule = self.test_schedules[test_id]
        
        def notify_students():
            students_to_notify = [
                student for student in self.students.values() 
                if student.program == test_schedule.test_type
            ]
            
            for student in students_to_notify:
                logger.info(
                    f"Notifying student {student.name} ({student.email}) "
                    f"about test {test_schedule.test_name}"
                )
                # In a real implementation, send email/notification here

        try:
            trigger = CronTrigger.from_crontab(test_schedule.schedule)
            self.scheduler.add_job(
                notify_students,
                trigger=trigger,
                id=test_id,
                name=f"Test Notification: {test_schedule.test_name}"
            )
            logger.info(f"Scheduled test {test_schedule.test_name} with cron {test_schedule.schedule}")
        except Exception as e:
            logger.error(f"Error scheduling test {test_id}: {e}")

    def start_scheduler(self) -> None:
        try:
            self.scheduler.start()
            logger.info("Test scheduler started")
            
            # Schedule all existing tests
            for test_id in self.test_schedules:
                self.schedule_test(test_id)
        except Exception as e:
            logger.error(f"Error starting scheduler: {e}")

    def stop_scheduler(self) -> None:
        try:
            self.scheduler.shutdown()
            logger.info("Test scheduler stopped")
        except Exception as e:
            logger.error(f"Error stopping scheduler: {e}")

# Example usage
if __name__ == "__main__":
    scheduler = TestScheduler()
    
    # Add sample data
    scheduler.add_student("S001", "Rahul Sharma", "rahul@example.com", TestType.JEE)
    scheduler.add_student("S002", "Priya Patel", "priya@example.com", TestType.NEET)
    
    scheduler.add_test_schedule(
        "T001", 
        "JEE Weekly Test", 
        TestType.JEE, 
        "0 9 * * 6"  # Every Saturday at 9 AM
    )
    scheduler.add_test_schedule(
        "T002", 
        "NEET Monthly Test", 
        TestType.NEET, 
        "0 10 1 * *"  # 1st of every month at 10 AM
    )
    
    scheduler.start_scheduler()
    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        scheduler.stop_scheduler()
```
