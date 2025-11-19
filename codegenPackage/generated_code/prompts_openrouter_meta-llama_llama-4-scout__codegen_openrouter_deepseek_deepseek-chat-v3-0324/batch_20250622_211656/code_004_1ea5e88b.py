"""
Generated Code Metadata:
========================
Original URL: https://pdma.io
Prompt: Design a cybersecurity awareness program for a small business, incorporating best practices and strategies from the PDMA Technologies' cybersecurity training.
Generated: DETERMINISTIC_1ea5e88b93b4a0d5
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import os
from typing import List, Dict, Optional

# Configuration file path
CONFIG_FILE = "config.json"

class Employee:
    """Represents an employee participating in the cybersecurity awareness program."""
    def __init__(self, name: str, email: str, department: str):
        self.name = name
        self.email = email
        self.department = department
        self.training_completed: List[str] = []
        self.last_training_date: Optional[datetime.date] = None

    def complete_training(self, training_name: str) -> None:
        """Mark a training as completed for the employee."""
        if training_name not in self.training_completed:
            self.training_completed.append(training_name)
            self.last_training_date = datetime.date.today()

    def to_dict(self) -> Dict:
        """Convert employee data to a dictionary for serialization."""
        return {
            "name": self.name,
            "email": self.email,
            "department": self.department,
            "training_completed": self.training_completed,
            "last_training_date": self.last_training_date.isoformat() if self.last_training_date else None
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Employee':
        """Create an Employee instance from a dictionary."""
        employee = cls(data["name"], data["email"], data["department"])
        employee.training_completed = data.get("training_completed", [])
        last_date = data.get("last_training_date")
        employee.last_training_date = datetime.date.fromisoformat(last_date) if last_date else None
        return employee

class TrainingModule:
    """Represents a cybersecurity training module."""
    def __init__(self, name: str, description: str, content: str, frequency_days: int = 90):
        self.name = name
        self.description = description
        self.content = content
        self.frequency_days = frequency_days

    def to_dict(self) -> Dict:
        """Convert training module data to a dictionary for serialization."""
        return {
            "name": self.name,
            "description": self.description,
            "content": self.content,
            "frequency_days": self.frequency_days
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'TrainingModule':
        """Create a TrainingModule instance from a dictionary."""
        return cls(data["name"], data["description"], data["content"], data.get("frequency_days", 90))

class PhishingTest:
    """Represents a phishing simulation test."""
    def __init__(self, name: str, subject: str, content: str):
        self.name = name
        self.subject = subject
        self.content = content

    def to_dict(self) -> Dict:
        """Convert phishing test data to a dictionary for serialization."""
        return {
            "name": self.name,
            "subject": self.subject,
            "content": self.content
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'PhishingTest':
        """Create a PhishingTest instance from a dictionary."""
        return cls(data["name"], data["subject"], data["content"])

class CybersecurityProgram:
    """Main class for managing the cybersecurity awareness program."""
    def __init__(self):
        self.employees: List[Employee] = []
        self.training_modules: List[TrainingModule] = []
        self.phishing_tests: List[PhishingTest] = []
        self.config: Dict = {}
        self.load_config()

    def load_config(self) -> None:
        """Load configuration from file."""
        try:
            with open(CONFIG_FILE, "r") as f:
                self.config = json.load(f)
        except FileNotFoundError:
            self.config = {
                "smtp_server": "smtp.example.com",
                "smtp_port": 587,
                "smtp_username": "your_email@example.com",
                "smtp_password": "your_password",
                "admin_email": "admin@example.com"
            }
            self.save_config()

    def save_config(self) -> None:
        """Save configuration to file."""
        with open(CONFIG_FILE, "w") as f:
            json.dump(self.config, f, indent=2)

    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the program."""
        self.employees.append(employee)

    def add_training_module(self, module: TrainingModule) -> None:
        """Add a training module to the program."""
        self.training_modules.append(module)

    def add_phishing_test(self, test: PhishingTest) -> None:
        """Add a phishing test to the program."""
        self.phishing_tests.append(test)

    def send_email(self, to_email: str, subject: str, body: str) -> bool:
        """Send an email using configured SMTP settings."""
        try:
            msg = MIMEMultipart()
            msg["From"] = self.config["smtp_username"]
            msg["To"] = to_email
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            with smtplib.SMTP(self.config["smtp_server"], self.config["smtp_port"]) as server:
                server.starttls()
                server.login(self.config["smtp_username"], self.config["smtp_password"])
                server.send_message(msg)
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False

    def schedule_training(self) -> None:
        """Schedule training for employees based on their last completion date."""
        today = datetime.date.today()
        for employee in self.employees:
            for module in self.training_modules:
                needs_training = (
                    employee.last_training_date is None or
                    (today - employee.last_training_date).days >= module.frequency_days or
                    module.name not in employee.training_completed
                )
                if needs_training:
                    self.send_training_notification(employee, module)

    def send_training_notification(self, employee: Employee, module: TrainingModule) -> None:
        """Send a training notification to an employee."""
        subject = f"Cybersecurity Training: {module.name}"
        body = f"""Dear {employee.name},

You are due to complete the following cybersecurity training:
{module.name}

Description:
{module.description}

Training Content:
{module.content}

Please acknowledge completion of this training.

Best regards,
Cybersecurity Team
"""
        self.send_email(employee.email, subject, body)

    def conduct_phishing_test(self) -> None:
        """Conduct a random phishing test on employees."""
        if not self.phishing_tests:
            return

        test = random.choice(self.phishing_tests)
        for employee in self.employees:
            self.send_email(employee.email, test.subject, test.content)

    def save_data(self, filename: str = "cybersecurity_program_data.json") -> None:
        """Save program data to a file."""
        data = {
            "employees": [emp.to_dict() for emp in self.employees],
            "training_modules": [mod.to_dict() for mod in self.training_modules],
            "phishing_tests": [test.to_dict() for test in self.phishing_tests]
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

    def load_data(self, filename: str = "cybersecurity_program_data.json") -> None:
        """Load program data from a file."""
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.employees = [Employee.from_dict(emp) for emp in data.get("employees", [])]
                self.training_modules = [TrainingModule.from_dict(mod) for mod in data.get("training_modules", [])]
                self.phishing_tests = [PhishingTest.from_dict(test) for test in data.get("phishing_tests", [])]
        except FileNotFoundError:
            print("No existing data file found. Starting with empty program.")

# Example usage
if __name__ == "__main__":
    program = Cybersecurity
