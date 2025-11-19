"""
Generated Code Metadata:
========================
Original URL: https://gcapmarkets.com
Prompt: Write code to simulate employee development programs in a financial company, incorporating the core values of ethics and continuous improvement as described by GCap Markets.
Generated: DETERMINISTIC_00d7e164132ffb3e
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from enum import Enum
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import json

class ProgramStatus(Enum):
    """Enum representing the status of a development program."""
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class ProgramType(Enum):
    """Enum representing types of development programs."""
    ETHICS_TRAINING = "Ethics Training"
    TECHNICAL_SKILLS = "Technical Skills"
    LEADERSHIP = "Leadership"
    COMPLIANCE = "Compliance"
    CONTINUOUS_IMPROVEMENT = "Continuous Improvement"

class Employee:
    """Class representing an employee in the financial company."""
    
    def __init__(self, employee_id: str, name: str, department: str, position: str):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.position = position
        self.enrolled_programs: List['DevelopmentProgram'] = []
        self.completed_programs: List['DevelopmentProgram'] = []
    
    def enroll_in_program(self, program: 'DevelopmentProgram') -> bool:
        """Enroll employee in a development program."""
        if program not in self.enrolled_programs and program.status == ProgramStatus.NOT_STARTED:
            self.enrolled_programs.append(program)
            program.participants.append(self)
            return True
        return False
    
    def complete_program(self, program: 'DevelopmentProgram') -> bool:
        """Mark a program as completed for the employee."""
        if program in self.enrolled_programs and program.status == ProgramStatus.IN_PROGRESS:
            self.enrolled_programs.remove(program)
            self.completed_programs.append(program)
            return True
        return False
    
    def get_program_progress(self) -> Dict[str, int]:
        """Get the progress of the employee's development programs."""
        return {
            "enrolled": len(self.enrolled_programs),
            "completed": len(self.completed_programs)
        }
    
    def __repr__(self) -> str:
        return f"Employee({self.employee_id}, {self.name}, {self.department})"

class DevelopmentProgram:
    """Class representing a development program."""
    
    def __init__(
        self,
        program_id: str,
        name: str,
        program_type: ProgramType,
        start_date: datetime,
        end_date: datetime,
        max_participants: int = 20
    ):
        self.program_id = program_id
        self.name = name
        self.program_type = program_type
        self.start_date = start_date
        self.end_date = end_date
        self.max_participants = max_participants
        self.status = ProgramStatus.NOT_STARTED
        self.participants: List[Employee] = []
    
    def start_program(self) -> bool:
        """Start the development program if not already started."""
        if self.status == ProgramStatus.NOT_STARTED and datetime.now() >= self.start_date:
            self.status = ProgramStatus.IN_PROGRESS
            return True
        return False
    
    def complete_program(self) -> bool:
        """Mark the program as completed."""
        if self.status == ProgramStatus.IN_PROGRESS and datetime.now() >= self.end_date:
            self.status = ProgramStatus.COMPLETED
            return True
        return False
    
    def cancel_program(self) -> bool:
        """Cancel the program."""
        if self.status in [ProgramStatus.NOT_STARTED, ProgramStatus.IN_PROGRESS]:
            self.status = ProgramStatus.CANCELLED
            return True
        return False
    
    def is_full(self) -> bool:
        """Check if the program has reached maximum participants."""
        return len(self.participants) >= self.max_participants
    
    def get_participant_count(self) -> int:
        """Get the number of participants in the program."""
        return len(self.participants)
    
    def __repr__(self) -> str:
        return f"DevelopmentProgram({self.program_id}, {self.name}, {self.program_type.value})"

class DevelopmentProgramSimulator:
    """Class to simulate employee development programs."""
    
    def __init__(self):
        self.employees: List[Employee] = []
        self.programs: List[DevelopmentProgram] = []
    
    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the simulator."""
        self.employees.append(employee)
    
    def create_program(
        self,
        name: str,
        program_type: ProgramType,
        start_date: datetime,
        duration_days: int,
        max_participants: int = 20
    ) -> DevelopmentProgram:
        """Create and add a new development program."""
        program_id = f"PROG-{random.randint(1000, 9999)}"
        end_date = start_date + timedelta(days=duration_days)
        program = DevelopmentProgram(
            program_id=program_id,
            name=name,
            program_type=program_type,
            start_date=start_date,
            end_date=end_date,
            max_participants=max_participants
        )
        self.programs.append(program)
        return program
    
    def enroll_employee_in_program(
        self,
        employee_id: str,
        program_id: str
    ) -> bool:
        """Enroll an employee in a program."""
        employee = next((e for e in self.employees if e.employee_id == employee_id), None)
        program = next((p for p in self.programs if p.program_id == program_id), None)
        
        if employee and program and not program.is_full():
            return employee.enroll_in_program(program)
        return False
    
    def simulate_program_progress(self, days: int = 30) -> None:
        """Simulate the progress of programs over a number of days."""
        current_date = datetime.now()
        for program in self.programs:
            if program.status == ProgramStatus.NOT_STARTED and current_date >= program.start_date:
                program.start_program()
            elif program.status == ProgramStatus.IN_PROGRESS and current_date >= program.end_date:
                program.complete_program()
                for participant in program.participants:
                    participant.complete_program(program)
    
    def get_employee_progress_report(self, employee_id: str) -> Optional[Dict]:
        """Generate a progress report for an employee."""
        employee = next((e for e in self.employees if e.employee_id == employee_id), None)
        if not employee:
            return None
        
        return {
            "employee_id": employee.employee_id,
            "name": employee.name,
            "department": employee.department,
            "enrolled_programs": [p.name for p in employee.enrolled_programs],
            "completed_programs": [p.name for p in employee.completed_programs],
            "total_enrolled": len(employee.enrolled_programs),
            "total_completed": len(employee.completed_programs)
        }
    
    def get_program_report(self, program_id: str) -> Optional[Dict]:
        """Generate a report for a specific program."""
        program = next((p for p in self.programs if p.program_id == program_id), None)
        if not program:
            return None
        
        return {
            "program_id": program.program_id,
            "name": program.name,
            "type": program.program_type.value,
            "status": program.status.value,
            "start_date": program.start_date.strftime("%Y-%m-%d"),
            "end_date": program.end_date.strftime("%Y-%m-%d"),
            "participants": [p.name for p in program.participants],
            "participant_count": program.get_participant_count(),
            "max_participants": program.max_participants
        }
    
    def save_to_file(self, filename: str) -> bool:
        """Save the current state to a JSON file."""
        try:
            data = {
                "employees": [
                    {
                        "employee_id": e.employee_id,
                        "name": e.name,
                        "department": e.department,
                        "position": e.position,
                        "enrolled_programs": [p.program_id for p in e.enrolled_programs],
                        "completed_programs": [p.program_id for p in e.completed_programs]
                    } for e in self.employees
                ],
                "programs": [
                    {
                        "program_id": p.program_id,
                        "name": p.name,
                        "type": p.program_type.value,
                        "start_date": p.start_date.strftime("%Y-%m-%d"),
                        "end_date": p.end_date.strftime("%Y-%m-%d"),
                        "max_participants": p.max_participants,
                        "status": p.status.value,
                        "participants": [e.employee_id for e in p.participants]
                    } for p in self.programs
                ]
            }
            
            with open(filename, 'w') as f:
                json.dump(data, f
