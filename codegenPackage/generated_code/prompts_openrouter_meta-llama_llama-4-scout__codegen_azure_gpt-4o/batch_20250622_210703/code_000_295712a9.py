"""
Generated Code Metadata:
========================
Original URL: https://afms.in
Prompt: Write a Python script to manage housekeeping services, including scheduling and employee assignment, for a facility management company like Ashvi Facility Management Services.
Generated: DETERMINISTIC_295712a98c063808
Batch ID: 20250622_210703
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

class HousekeepingManager:
    def __init__(self):
        # Initialize schedules and employees
        self.schedules = []  # List to store scheduled tasks
        self.employees = []  # List to store employee details

    def add_employee(self, name, contact):
        """
        Add a new employee to the system.
        :param name: Name of the employee
        :param contact: Contact information of the employee
        """
        employee = {
            "id": len(self.employees) + 1,
            "name": name,
            "contact": contact
        }
        self.employees.append(employee)
        print(f"Employee {name} added successfully.")

    def schedule_task(self, task_name, date, time, employee_id):
        """
        Schedule a housekeeping task.
        :param task_name: Name of the task
        :param date: Date of the task (YYYY-MM-DD)
        :param time: Time of the task (HH:MM)
        :param employee_id: ID of the assigned employee
        """
        # Validate date and time format
        try:
            task_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            task_time = datetime.datetime.strptime(time, "%H:%M").time()
        except ValueError:
            print("Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.")
            return

        # Check if employee exists
        employee = next((emp for emp in self.employees if emp["id"] == employee_id), None)
        if not employee:
            print(f"Employee with ID {employee_id} not found.")
            return

        # Create and store the task
        task = {
            "task_name": task_name,
            "date": str(task_date),
            "time": str(task_time),
            "employee_id": employee_id,
            "employee_name": employee["name"]
        }
        self.schedules.append(task)
        print(f"Task '{task_name}' scheduled successfully for {date} at {time}.")

    def view_schedules(self):
        """
        View all scheduled tasks.
        """
        if not self.schedules:
            print("No tasks scheduled.")
            return

        print("Scheduled Tasks:")
        for task in self.schedules:
            print(f"Task: {task['task_name']}, Date: {task['date']}, Time: {task['time']}, "
                  f"Assigned to: {task['employee_name']} (ID: {task['employee_id']})")

    def view_employees(self):
        """
        View all employees.
        """
        if not self.employees:
            print("No employees available.")
            return

        print("Employees:")
        for emp in self.employees:
            print(f"ID: {emp['id']}, Name: {emp['name']}, Contact: {emp['contact']}")

    def save_data(self, filename="housekeeping_data.json"):
        """
        Save schedules and employees to a JSON file.
        :param filename: Name of the file to save data
        """
        data = {
            "employees": self.employees,
            "schedules": self.schedules
        }
        try:
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
            print(f"Data saved successfully to {filename}.")
        except IOError as e:
            print(f"Error saving data: {e}")

    def load_data(self, filename="housekeeping_data.json"):
        """
        Load schedules and employees from a JSON file.
        :param filename: Name of the file to load data
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.employees = data.get("employees", [])
                self.schedules = data.get("schedules", [])
            print(f"Data loaded successfully from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with empty data.")
        except json.JSONDecodeError as e:
            print(f"Error loading data: {e}")


# Example usage
if __name__ == "__main__":
    manager = HousekeepingManager()

    # Add employees
    manager.add_employee("John Doe", "123-456-7890")
    manager.add_employee("Jane Smith", "987-654-3210")

    # Schedule tasks
    manager.schedule_task("Room Cleaning", "2023-10-15", "10:00", 1)
    manager.schedule_task("Lobby Cleaning", "2023-10-15", "12:00", 2)

    # View schedules and employees
    manager.view_schedules()
    manager.view_employees()

    # Save and load data
    manager.save_data()
    manager.load_data()
```
