"""
Generated Code Metadata:
========================
Original URL: https://mandosecurity.com
Prompt: Generate a code snippet for a training management system that tracks the training progress of security personnel, inspired by Mando Security's Training Academy offerings.
Generated: DETERMINISTIC_70f3442ab71f8c64
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# training_management_system.py

import datetime

class TrainingModule:
    """
    Represents a training module in the system.
    """
    def __init__(self, module_name, duration_hours):
        """
        Initialize a training module with a name and duration.
        :param module_name: Name of the training module.
        :param duration_hours: Duration of the module in hours.
        """
        self.module_name = module_name
        self.duration_hours = duration_hours


class SecurityPersonnel:
    """
    Represents a security personnel undergoing training.
    """
    def __init__(self, personnel_id, name):
        """
        Initialize a security personnel with an ID and name.
        :param personnel_id: Unique identifier for the personnel.
        :param name: Name of the personnel.
        """
        self.personnel_id = personnel_id
        self.name = name
        self.training_progress = {}  # Tracks progress for each module

    def enroll_in_module(self, module):
        """
        Enroll the personnel in a training module.
        :param module: TrainingModule instance.
        """
        if module.module_name not in self.training_progress:
            self.training_progress[module.module_name] = {
                "status": "Enrolled",
                "completion_date": None
            }
        else:
            raise ValueError(f"Already enrolled in module: {module.module_name}")

    def complete_module(self, module_name):
        """
        Mark a training module as completed.
        :param module_name: Name of the module to mark as completed.
        """
        if module_name in self.training_progress:
            self.training_progress[module_name]["status"] = "Completed"
            self.training_progress[module_name]["completion_date"] = datetime.date.today()
        else:
            raise ValueError(f"Not enrolled in module: {module_name}")

    def get_progress(self):
        """
        Get the training progress of the personnel.
        :return: Dictionary containing training progress.
        """
        return self.training_progress


class TrainingManagementSystem:
    """
    Main system to manage training for security personnel.
    """
    def __init__(self):
        """
        Initialize the training management system.
        """
        self.modules = {}  # Stores available training modules
        self.personnel = {}  # Stores registered security personnel

    def add_module(self, module_name, duration_hours):
        """
        Add a new training module to the system.
        :param module_name: Name of the module.
        :param duration_hours: Duration of the module in hours.
        """
        if module_name not in self.modules:
            self.modules[module_name] = TrainingModule(module_name, duration_hours)
        else:
            raise ValueError(f"Module already exists: {module_name}")

    def register_personnel(self, personnel_id, name):
        """
        Register a new security personnel in the system.
        :param personnel_id: Unique identifier for the personnel.
        :param name: Name of the personnel.
        """
        if personnel_id not in self.personnel:
            self.personnel[personnel_id] = SecurityPersonnel(personnel_id, name)
        else:
            raise ValueError(f"Personnel already registered: {personnel_id}")

    def enroll_personnel_in_module(self, personnel_id, module_name):
        """
        Enroll a personnel in a training module.
        :param personnel_id: ID of the personnel.
        :param module_name: Name of the module.
        """
        if personnel_id in self.personnel and module_name in self.modules:
            personnel = self.personnel[personnel_id]
            module = self.modules[module_name]
            personnel.enroll_in_module(module)
        else:
            raise ValueError("Invalid personnel ID or module name.")

    def complete_module_for_personnel(self, personnel_id, module_name):
        """
        Mark a module as completed for a personnel.
        :param personnel_id: ID of the personnel.
        :param module_name: Name of the module.
        """
        if personnel_id in self.personnel:
            personnel = self.personnel[personnel_id]
            personnel.complete_module(module_name)
        else:
            raise ValueError(f"Personnel not found: {personnel_id}")

    def get_personnel_progress(self, personnel_id):
        """
        Get the training progress of a personnel.
        :param personnel_id: ID of the personnel.
        :return: Training progress dictionary.
        """
        if personnel_id in self.personnel:
            personnel = self.personnel[personnel_id]
            return personnel.get_progress()
        else:
            raise ValueError(f"Personnel not found: {personnel_id}")


# Example usage (uncomment to test):
# tms = TrainingManagementSystem()
# tms.add_module("Fire Safety", 5)
# tms.add_module("Conflict Resolution", 3)
# tms.register_personnel("SP001", "John Doe")
# tms.enroll_personnel_in_module("SP001", "Fire Safety")
# tms.complete_module_for_personnel("SP001", "Fire Safety")
# print(tms.get_personnel_progress("SP001"))
```
