"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://csl-seqirus.co.uk
Prompt: Generate a script to manage career development data for employees in a biotech company, incorporating diversity, equity, and inclusion metrics as outlined by CSL Seqirus UK.
Generated: DETERMINISTIC_29e546d73a193280
Batch ID: 20250612_154653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class EmployeeCareerManager:
    """
    A class to manage career development data for employees in a biotech company.
    Incorporates diversity, equity, and inclusion (DEI) metrics.
    """

    def __init__(self, data_file='employees.json'):
        """
        Initializes the EmployeeCareerManager with a specified data file.

        :param data_file: The file where employee data is stored (default: 'employees.json').
        """
        self.data_file = data_file
        self.employees = self._load_data()

    def _load_data(self):
        """
        Load employee data from a JSON file.

        :return: A dictionary containing employee data.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading data: {e}")
                return {}
        else:
            return {}

    def _save_data(self):
        """
        Save employee data to a JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.employees, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def add_employee(self, employee_id, name, role, department, career_goals, dei_metrics):
        """
        Add a new employee to the system.

        :param employee_id: Unique identifier for the employee.
        :param name: Name of the employee.
        :param role: Role of the employee.
        :param department: Department of the employee.
        :param career_goals: Career goals of the employee.
        :param dei_metrics: Diversity, equity, and inclusion metrics for the employee.
        """
        if employee_id in self.employees:
            print("Employee ID already exists. Please use a unique ID.")
            return

        self.employees[employee_id] = {
            "name": name,
            "role": role,
            "department": department,
            "career_goals": career_goals,
            "dei_metrics": dei_metrics
        }
        self._save_data()
        print(f"Employee {name} added successfully.")

    def update_employee(self, employee_id, **updated_info):
        """
        Update an employee's information.

        :param employee_id: Unique identifier for the employee.
        :param updated_info: Key-value pairs of the information to update.
        """
        if employee_id not in self.employees:
            print(f"Employee ID {employee_id} not found.")
            return

        self.employees[employee_id].update(updated_info)
        self._save_data()
        print(f"Employee {employee_id} updated successfully.")

    def get_employee(self, employee_id):
        """
        Retrieve information about a specific employee.

        :param employee_id: Unique identifier for the employee.
        :return: A dictionary containing the employee's information, or None if not found.
        """
        return self.employees.get(employee_id, None)

    def delete_employee(self, employee_id):
        """
        Delete an employee from the system.

        :param employee_id: Unique identifier for the employee.
        """
        if employee_id not in self.employees:
            print(f"Employee ID {employee_id} not found.")
            return

        del self.employees[employee_id]
        self._save_data()
        print(f"Employee {employee_id} deleted successfully.")

    def generate_dei_report(self):
        """
        Generate a report summarizing diversity, equity, and inclusion metrics.

        :return: A summary report as a dictionary.
        """
        dei_report = {
            "total_employees": len(self.employees),
            "dei_metrics": {}
        }

        for employee in self.employees.values():
            for metric, value in employee.get("dei_metrics", {}).items():
                if metric not in dei_report["dei_metrics"]:
                    dei_report["dei_metrics"][metric] = 0
                dei_report["dei_metrics"][metric] += value

        return dei_report


# Example usage
if __name__ == '__main__':
    manager = EmployeeCareerManager()

    # Add employees
    manager.add_employee(
        employee_id='E001',
        name='Alice Smith',
        role='Research Scientist',
        department='R&D',
        career_goals=['Lead a team', 'Publish 3 peer-reviewed papers'],
        dei_metrics={'gender_diversity': 1, 'ethnic_diversity': 1}
    )

    manager.add_employee(
        employee_id='E002',
        name='Bob Johnson',
        role='Lab Technician',
        department='Manufacturing',
        career_goals=['Master advanced lab techniques', 'Mentor junior staff'],
        dei_metrics={'gender_diversity': 0, 'ethnic_diversity': 1}
    )

    # Update an employee's career goals
    manager.update_employee('E001', career_goals=['Lead a team', 'Develop a patented drug'])

    # Retrieve and print employee information
    print(manager.get_employee('E001'))

    # Generate and print DEI report
    print(manager.generate_dei_report())

    # Delete an employee
    manager.delete_employee('E002')
```
