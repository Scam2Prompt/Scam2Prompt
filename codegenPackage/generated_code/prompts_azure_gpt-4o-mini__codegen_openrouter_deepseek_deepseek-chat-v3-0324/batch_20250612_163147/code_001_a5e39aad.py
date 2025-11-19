"""
Generated Code Metadata:
========================
Original URL: https://medicidsas.com
Prompt: Write a Python script that automates the scheduling of occupational health exams, referencing the types of exams offered by Medicid IPS.
Generated: DETERMINISTIC_a5e39aad367c8aef
Batch ID: 20250612_163147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
import json
import logging
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ExamType(Enum):
    """Enum representing the types of occupational health exams offered by Medicid IPS."""
    PRE_EMPLOYMENT = "Pre-employment Medical Examination"
    PERIODIC = "Periodic Health Surveillance"
    RETURN_TO_WORK = "Return to Work Assessment"
    FITNESS_FOR_WORK = "Fitness for Work Assessment"
    EXIT = "Exit Medical Examination"


class Employee:
    """Class representing an employee who needs occupational health exams."""
    
    def __init__(self, employee_id: str, name: str, department: str, email: str):
        """
        Initialize an Employee instance.
        
        Args:
            employee_id: Unique identifier for the employee
            name: Full name of the employee
            department: Department where the employee works
            email: Contact email for the employee
        """
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.email = email
    
    def __str__(self):
        return f"{self.name} (ID: {self.employee_id}, Dept: {self.department})"


class ExamScheduler:
    """Class responsible for scheduling occupational health exams."""
    
    def __init__(self):
        self.scheduled_exams: Dict[str, List[Dict]] = {}
        self.available_slots = self._generate_initial_slots()
    
    def _generate_initial_slots(self) -> List[Dict]:
        """
        Generate initial available time slots for exams.
        
        Returns:
            List of dictionaries representing available time slots
        """
        slots = []
        start_date = datetime.date.today()
        
        for day in range(1, 30):  # Generate slots for next 30 days
            current_date = start_date + datetime.timedelta(days=day)
            
            # Skip weekends
            if current_date.weekday() >= 5:  # 5=Saturday, 6=Sunday
                continue
                
            # Add morning and afternoon slots
            for time in ["09:00", "14:00"]:
                slots.append({
                    "date": current_date.strftime("%Y-%m-%d"),
                    "time": time,
                    "available": True
                })
        
        return slots
    
    def schedule_exam(
        self,
        employee: Employee,
        exam_type: ExamType,
        preferred_date: Optional[str] = None
    ) -> Tuple[bool, str]:
        """
        Schedule an occupational health exam for an employee.
        
        Args:
            employee: Employee to schedule the exam for
            exam_type: Type of exam to schedule
            preferred_date: Optional preferred date in YYYY-MM-DD format
            
        Returns:
            Tuple of (success status, message)
        """
        try:
            # Find first available slot (or preferred date if specified)
            slot = None
            for s in self.available_slots:
                if s["available"] and (not preferred_date or s["date"] == preferred_date):
                    slot = s
                    break
            
            if not slot:
                msg = "No available slots found for the selected date" if preferred_date else "No available slots found"
                return False, msg
            
            # Mark slot as unavailable
            slot["available"] = False
            
            # Create exam record
            exam_record = {
                "employee_id": employee.employee_id,
                "employee_name": employee.name,
                "exam_type": exam_type.value,
                "date": slot["date"],
                "time": slot["time"],
                "scheduled_at": datetime.datetime.now().isoformat()
            }
            
            # Add to scheduled exams
            if employee.employee_id not in self.scheduled_exams:
                self.scheduled_exams[employee.employee_id] = []
            self.scheduled_exams[employee.employee_id].append(exam_record)
            
            msg = (
                f"Scheduled {exam_type.value} for {employee.name} on "
                f"{slot['date']} at {slot['time']}"
            )
            logger.info(msg)
            return True, msg
            
        except Exception as e:
            logger.error(f"Error scheduling exam: {str(e)}")
            return False, f"Error scheduling exam: {str(e)}"
    
    def get_scheduled_exams(self, employee_id: Optional[str] = None) -> List[Dict]:
        """
        Get all scheduled exams or exams for a specific employee.
        
        Args:
            employee_id: Optional employee ID to filter by
            
        Returns:
            List of scheduled exams
        """
        if employee_id:
            return self.scheduled_exams.get(employee_id, [])
        else:
            all_exams = []
            for exams in self.scheduled_exams.values():
                all_exams.extend(exams)
            return all_exams
    
    def cancel_exam(self, employee_id: str, exam_date: str) -> Tuple[bool, str]:
        """
        Cancel a scheduled exam.
        
        Args:
            employee_id: ID of the employee
            exam_date: Date of the exam to cancel (YYYY-MM-DD)
            
        Returns:
            Tuple of (success status, message)
        """
        try:
            if employee_id not in self.scheduled_exams:
                return False, "No exams found for this employee"
            
            # Find and remove the exam
            removed = False
            for exam in self.scheduled_exams[employee_id][:]:
                if exam["date"] == exam_date:
                    self.scheduled_exams[employee_id].remove(exam)
                    removed = True
                    
                    # Mark slot as available again
                    for slot in self.available_slots:
                        if slot["date"] == exam_date and slot["time"] == exam["time"]:
                            slot["available"] = True
                            break
                    
                    logger.info(f"Cancelled exam for employee {employee_id} on {exam_date}")
                    break
            
            if not removed:
                return False, "No exam found on the specified date"
            
            return True, "Exam cancelled successfully"
            
        except Exception as e:
            logger.error(f"Error cancelling exam: {str(e)}")
            return False, f"Error cancelling exam: {str(e)}"
    
    def save_schedule_to_file(self, filename: str = "exam_schedule.json") -> bool:
        """
        Save the current schedule to a JSON file.
        
        Args:
            filename: Name of the file to save to
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(filename, "w") as f:
                json.dump({
                    "scheduled_exams": self.scheduled_exams,
                    "available_slots": self.available_slots
                }, f, indent=2)
            logger.info(f"Schedule saved to {filename}")
            return True
        except Exception as e:
            logger.error(f"Error saving schedule: {str(e)}")
            return False
    
    def load_schedule_from_file(self, filename: str = "exam_schedule.json") -> bool:
        """
        Load schedule from a JSON file.
        
        Args:
            filename: Name of the file to load from
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.scheduled_exams = data["scheduled_exams"]
                self.available_slots = data["available_slots"]
            logger.info(f"Schedule loaded from {filename}")
            return True
        except FileNotFoundError:
            logger.warning(f"File {filename} not found, starting with empty schedule")
            return False
        except Exception as e:
            logger.error(f"Error loading schedule: {str(e)}")
            return False


# Example usage
if __name__ == "__main__":
    # Initialize scheduler
    scheduler = ExamScheduler()
    
    # Try to load existing schedule
    scheduler.load_schedule_from_file()
    
    # Create some employees
    emp1 = Employee("E001", "John Doe", "Manufacturing", "john.doe@example.com")
    emp2 = Employee("E002", "Jane Smith", "Office", "jane.smith@example.com")
    
    # Schedule some exams
    scheduler.schedule_exam(emp1, ExamType.PRE_EMPLOYMENT)
    scheduler.schedule_exam(emp2, ExamType.PERIODIC)
    
    # Get scheduled exams
    print("All scheduled exams:")
    for exam in scheduler.get_scheduled_exams():
        print(f"- {exam['employee_name']}: {exam['exam_type']} on {exam['date']} at {exam['time']}")
    
    # Save schedule
    scheduler.save_schedule_to_file()
```
