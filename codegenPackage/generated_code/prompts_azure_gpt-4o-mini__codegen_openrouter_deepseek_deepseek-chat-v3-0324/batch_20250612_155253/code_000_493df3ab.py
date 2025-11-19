"""
Generated Code Metadata:
========================
Original URL: https://cyberconnectit.com
Prompt: Write a Python script to implement basic employee security training for small businesses, focusing on phishing awareness and password management as outlined on CyberConnect's cybersecurity services page.
Generated: DETERMINISTIC_493df3ab2302f180
Batch ID: 20250612_155253
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import string
import time
from datetime import datetime
import json
import os

class EmployeeSecurityTraining:
    """
    A class to implement basic employee security training focusing on phishing awareness and password management.
    """
    
    def __init__(self):
        self.training_data = {
            "phishing": {
                "description": "Phishing is a cyber attack that uses disguised email as a weapon.",
                "examples": [
                    "Emails asking for sensitive information",
                    "Messages with urgent requests",
                    "Links to fake websites",
                    "Attachments from unknown senders"
                ],
                "prevention": [
                    "Verify sender email addresses",
                    "Don't click on suspicious links",
                    "Check for spelling/grammar mistakes",
                    "When in doubt, contact IT"
                ]
            },
            "password_management": {
                "description": "Strong password practices are essential for security.",
                "guidelines": [
                    "Use at least 12 characters",
                    "Include uppercase, lowercase, numbers, and symbols",
                    "Don't reuse passwords across accounts",
                    "Use a password manager",
                    "Enable multi-factor authentication"
                ]
            }
        }
        self.employees = {}
        self.load_data()
        
    def load_data(self):
        """Load employee training data from file if it exists."""
        if os.path.exists("employee_training.json"):
            with open("employee_training.json", "r") as f:
                self.employees = json.load(f)
    
    def save_data(self):
        """Save employee training data to file."""
        with open("employee_training.json", "w") as f:
            json.dump(self.employees, f, indent=4)
    
    def generate_password(self, length=12):
        """Generate a strong random password."""
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(chars) for _ in range(length))
    
    def register_employee(self, employee_id, name):
        """Register a new employee for training."""
        if employee_id in self.employees:
            print(f"Employee {employee_id} already exists.")
            return False
        
        self.employees[employee_id] = {
            "name": name,
            "training_completed": {
                "phishing": False,
                "password_management": False
            },
            "completion_date": None,
            "password_strength_test": None
        }
        self.save_data()
        print(f"Employee {name} registered successfully.")
        return True
    
    def conduct_phishing_training(self, employee_id):
        """Conduct phishing awareness training."""
        if employee_id not in self.employees:
            print("Employee not found.")
            return False
        
        print("\n=== Phishing Awareness Training ===")
        print(self.training_data["phishing"]["description"])
        print("\nCommon Examples:")
        for example in self.training_data["phishing"]["examples"]:
            print(f"- {example}")
        
        print("\nPrevention Tips:")
        for tip in self.training_data["phishing"]["prevention"]:
            print(f"- {tip}")
        
        # Simple quiz
        print("\nQuick Quiz (Answer Y/N):")
        questions = [
            ("Should you click on links in emails from unknown senders?", "N"),
            ("Is an email asking for your password likely legitimate?", "N"),
            ("Should you report suspicious emails to IT?", "Y")
        ]
        
        score = 0
        for question, answer in questions:
            user_answer = input(f"\n{question} (Y/N): ").upper()
            while user_answer not in ["Y", "N"]:
                print("Please answer with Y or N.")
                user_answer = input(f"{question} (Y/N): ").upper()
            
            if user_answer == answer:
                score += 1
        
        if score >= 2:
            print("\nCongratulations! You passed the phishing awareness training.")
            self.employees[employee_id]["training_completed"]["phishing"] = True
            self.save_data()
            return True
        else:
            print("\nPlease review the training materials and try again.")
            return False
    
    def conduct_password_training(self, employee_id):
        """Conduct password management training."""
        if employee_id not in self.employees:
            print("Employee not found.")
            return False
        
        print("\n=== Password Management Training ===")
        print(self.training_data["password_management"]["description"])
        print("\nPassword Guidelines:")
        for guideline in self.training_data["password_management"]["guidelines"]:
            print(f"- {guideline}")
        
        # Generate example passwords
        print("\nExample Strong Passwords:")
        for _ in range(3):
            print(f"- {self.generate_password()}")
        
        # Password strength test
        print("\nPassword Strength Test:")
        password = input("Enter a password to test (or leave blank to skip): ")
        if password:
            strength = self.test_password_strength(password)
            self.employees[employee_id]["password_strength_test"] = strength
            print(f"Password strength: {strength}/5")
            self.save_data()
        
        self.employees[employee_id]["training_completed"]["password_management"] = True
        self.save_data()
        print("\nPassword management training completed.")
        return True
    
    def test_password_strength(self, password):
        """Test the strength of a password (1-5 scale)."""
        strength = 0
        
        # Length check
        if len(password) >= 8:
            strength += 1
        if len(password) >= 12:
            strength += 1
        
        # Complexity checks
        if any(c.isupper() for c in password) and any(c.islower() for c in password):
            strength += 1
        if any(c.isdigit() for c in password):
            strength += 1
        if any(c in string.punctuation for c in password):
            strength += 1
        
        return strength
    
    def complete_training(self, employee_id):
        """Mark training as complete for an employee."""
        if employee_id not in self.employees:
            print("Employee not found.")
            return False
        
        if all(self.employees[employee_id]["training_completed"].values()):
            self.employees[employee_id]["completion_date"] = datetime.now().strftime("%Y-%m-%d")
            self.save_data()
            print(f"\nTraining completed for {self.employees[employee_id]['name']} on {self.employees[employee_id]['completion_date']}")
            return True
        else:
            print("\nEmployee has not completed all training modules.")
            return False
    
    def print_report(self):
        """Print a training completion report."""
        print("\n=== Training Completion Report ===")
        print(f"Total Employees: {len(self.employees)}")
        
        completed = sum(
            1 for emp in self.employees.values() 
            if emp["completion_date"] is not None
        )
        print(f"Completed Training: {completed}")
        
        print("\nEmployees:")
        for emp_id, emp_data in self.employees.items():
            status = "Completed" if emp_data["completion_date"] else "Incomplete"
            print(f"{emp_id}: {emp_data['name']} - {status}")

def main():
    """Main function to run the employee security training program."""
    training = EmployeeSecurityTraining()
    
    while True:
        print("\n=== Employee Security Training ===")
        print("1. Register New Employee")
        print("2. Conduct Phishing Training")
        print("3. Conduct Password Training")
        print("4. Complete Training")
        print("5. Generate Report")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            emp_id = input("Enter employee ID: ")
            name = input("Enter employee name: ")
            training.register_employee(emp_id, name)
        
        elif choice == "2":
            emp_id = input("Enter employee ID: ")
            training.conduct_phishing_training(emp_id)
        
        elif choice == "3":
            emp_id = input("Enter employee ID: ")
            training.conduct_password_training(emp_id)
        
        elif choice == "4":
            emp_id = input("Enter employee ID: ")
            training.complete_training(emp_id)
        
        elif choice == "5":
            training.print_report()
        
        elif choice == "6":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")
        
        time.sleep(1)

if __name__ == "__main__":
    main()
```
