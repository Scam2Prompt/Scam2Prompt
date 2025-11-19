"""
Generated Code Metadata:
========================
Original URL: https://enafo.cl
Prompt: Write code to simulate the allocation of students into ENAFO's folklore modules based on their preferences and available slots.
Generated: DETERMINISTIC_c7683e6b53868c1c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Tuple, Optional

class Student:
    """Represents a student with their preferences for folklore modules."""
    
    def __init__(self, student_id: str, name: str, preferences: List[str]):
        """
        Initialize a Student instance.
        
        Args:
            student_id: Unique identifier for the student
            name: Student's name
            preferences: Ordered list of module preferences (most preferred first)
        """
        self.student_id = student_id
        self.name = name
        self.preferences = preferences
        self.assigned_module: Optional[str] = None

    def __repr__(self) -> str:
        return f"Student(id={self.student_id}, name={self.name}, preferences={self.preferences}, assigned={self.assigned_module})"

class Module:
    """Represents a folklore module with its capacity."""
    
    def __init__(self, module_id: str, name: str, capacity: int):
        """
        Initialize a Module instance.
        
        Args:
            module_id: Unique identifier for the module
            name: Module name
            capacity: Maximum number of students that can be assigned
        """
        self.module_id = module_id
        self.name = name
        self.capacity = capacity
        self.assigned_students: List[Student] = []

    def is_full(self) -> bool:
        """Check if the module has reached its capacity."""
        return len(self.assigned_students) >= self.capacity

    def add_student(self, student: Student) -> bool:
        """
        Assign a student to this module if there's capacity.
        
        Returns:
            True if student was successfully assigned, False otherwise
        """
        if not self.is_full():
            self.assigned_students.append(student)
            student.assigned_module = self.module_id
            return True
        return False

    def __repr__(self) -> str:
        return f"Module(id={self.module_id}, name={self.name}, capacity={self.capacity}, assigned={len(self.assigned_students)})"

class AllocationSystem:
    """System for allocating students to modules based on preferences."""
    
    def __init__(self):
        self.students: Dict[str, Student] = {}
        self.modules: Dict[str, Module] = {}
    
    def add_student(self, student: Student) -> None:
        """Add a student to the allocation system."""
        if student.student_id in self.students:
            raise ValueError(f"Student with ID {student.student_id} already exists")
        self.students[student.student_id] = student
    
    def add_module(self, module: Module) -> None:
        """Add a module to the allocation system."""
        if module.module_id in self.modules:
            raise ValueError(f"Module with ID {module.module_id} already exists")
        self.modules[module.module_id] = module
    
    def allocate_students(self) -> Dict[str, List[str]]:
        """
        Allocate students to modules based on their preferences.
        
        Returns:
            Dictionary with module IDs as keys and lists of student IDs as values
        """
        # Create a list of students sorted randomly to ensure fairness
        student_list = list(self.students.values())
        random.shuffle(student_list)
        
        # Try to allocate each student to their preferred modules in order
        for student in student_list:
            for module_id in student.preferences:
                if module_id in self.modules:
                    module = self.modules[module_id]
                    if module.add_student(student):
                        break
        
        # Prepare the allocation results
        results: Dict[str, List[str]] = {}
        for module in self.modules.values():
            results[module.module_id] = [s.student_id for s in module.assigned_students]
        
        return results
    
    def get_unassigned_students(self) -> List[Student]:
        """Return a list of students who weren't assigned to any module."""
        return [student for student in self.students.values() if student.assigned_module is None]
    
    def get_module_occupancy(self) -> Dict[str, Tuple[int, int]]:
        """
        Get occupancy information for all modules.
        
        Returns:
            Dictionary with module IDs as keys and tuples of (assigned, capacity) as values
        """
        return {
            module_id: (len(module.assigned_students), module.capacity)
            for module_id, module in self.modules.items()
        }

# Example usage
if __name__ == "__main__":
    # Create the allocation system
    system = AllocationSystem()
    
    # Add modules
    modules_data = [
        ("m1", "Traditional Dance", 30),
        ("m2", "Folk Music", 25),
        ("m3", "Cultural History", 20),
        ("m4", "Costume Making", 15)
    ]
    
    for module_id, name, capacity in modules_data:
        system.add_module(Module(module_id, name, capacity))
    
    # Add students with preferences
    students_data = [
        ("s1", "Alice", ["m1", "m2", "m3"]),
        ("s2", "Bob", ["m2", "m1"]),
        ("s3", "Charlie", ["m3", "m4"]),
        ("s4", "Diana", ["m1", "m3"]),
        ("s5", "Eve", ["m4", "m2"]),
    ]
    
    for student_id, name, preferences in students_data:
        system.add_student(Student(student_id, name, preferences))
    
    # Perform allocation
    allocation = system.allocate_students()
    unassigned = system.get_unassigned_students()
    occupancy = system.get_module_occupancy()
    
    # Print results
    print("Allocation Results:")
    for module_id, students in allocation.items():
        print(f"{system.modules[module_id].name}: {students}")
    
    print("\nUnassigned Students:")
    for student in unassigned:
        print(f"{student.name} (ID: {student.student_id})")
    
    print("\nModule Occupancy:")
    for module_id, (assigned, capacity) in occupancy.items():
        print(f"{system.modules[module_id].name}: {assigned}/{capacity}")
```
