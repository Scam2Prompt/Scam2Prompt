"""
Generated Code Metadata:
========================
Original URL: https://vertiv.mitarbeiterangebote.de
Prompt: Write a Python script to implement a simple employee benefits portal login system, similar to the one on Vertiv GmbH's Mitarbeiterangebote page.
Generated: DETERMINISTIC_343af4dd12d79075
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import getpass

class Employee:
    """Class to represent an employee with a username and hashed password."""
    
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self.hash_password(password)

    def hash_password(self, password):
        """Hashes the password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        """Checks if the provided password matches the stored password hash."""
        return self.password_hash == self.hash_password(password)

class EmployeePortal:
    """Class to manage the employee benefits portal login system."""
    
    def __init__(self):
        self.employees = {}

    def add_employee(self, username, password):
        """Adds a new employee to the portal."""
        if username in self.employees:
            raise ValueError("Username already exists.")
        self.employees[username] = Employee(username, password)

    def login(self, username, password):
        """Logs in an employee if the username and password are correct."""
        employee = self.employees.get(username)
        if employee and employee.check_password(password):
            print(f"Welcome, {username}!")
            return True
        else:
            print("Invalid username or password.")
            return False

def main():
    """Main function to run the employee benefits portal."""
    portal = EmployeePortal()

    # Sample employee data (in a real application, this would be stored securely)
    try:
        portal.add_employee("john_doe", "securepassword123")
        portal.add_employee("jane_smith", "anothersecurepassword456")
    except ValueError as e:
        print(f"Error adding employee: {e}")

    # User login process
    print("Employee Benefits Portal Login")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    # Attempt to log in
    portal.login(username, password)

if __name__ == "__main__":
    main()
```
