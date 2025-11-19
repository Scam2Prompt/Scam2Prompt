"""
Generated Code Metadata:
========================
Original URL: https://bitcoinxcash.com
Prompt: Write a Python script to help manage event planning tasks, including budgeting, scheduling, and personnel allocation, for a small-scale event in Japan.
Generated: DETERMINISTIC_d78313ea0c794f67
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# event_planner.py

class Event:
    def __init__(self, name, date, location, budget):
        """
        Initialize an Event object.

        Args:
            name (str): Event name
            date (str): Event date (YYYY-MM-DD)
            location (str): Event location
            budget (float): Event budget
        """
        self.name = name
        self.date = date
        self.location = location
        self.budget = budget
        self.tasks = []
        self.personnel = {}

    def add_task(self, task_name, task_cost, task_deadline):
        """
        Add a task to the event.

        Args:
            task_name (str): Task name
            task_cost (float): Task cost
            task_deadline (str): Task deadline (YYYY-MM-DD)
        """
        self.tasks.append({
            'name': task_name,
            'cost': task_cost,
            'deadline': task_deadline
        })

    def add_personnel(self, name, role, hourly_rate):
        """
        Add personnel to the event.

        Args:
            name (str): Personnel name
            role (str): Personnel role
            hourly_rate (float): Personnel hourly rate
        """
        self.personnel[name] = {
            'role': role,
            'hourly_rate': hourly_rate,
            'hours_worked': 0
        }

    def calculate_total_cost(self):
        """
        Calculate the total cost of all tasks.

        Returns:
            float: Total cost
        """
        total_cost = sum(task['cost'] for task in self.tasks)
        return total_cost

    def calculate_personnel_cost(self):
        """
        Calculate the total cost of all personnel.

        Returns:
            float: Total personnel cost
        """
        total_personnel_cost = sum(personnel['hourly_rate'] * personnel['hours_worked'] for personnel in self.personnel.values())
        return total_personnel_cost

    def update_hours_worked(self, name, hours_worked):
        """
        Update the hours worked by a personnel.

        Args:
            name (str): Personnel name
            hours_worked (float): Hours worked
        """
        if name in self.personnel:
            self.personnel[name]['hours_worked'] = hours_worked
        else:
            print(f"Personnel '{name}' not found.")

    def display_event_details(self):
        """
        Display event details.
        """
        print(f"Event Name: {self.name}")
        print(f"Event Date: {self.date}")
        print(f"Event Location: {self.location}")
        print(f"Event Budget: ¥{self.budget:.2f}")

        print("\nTasks:")
        for task in self.tasks:
            print(f"- {task['name']}: ¥{task['cost']:.2f} (Deadline: {task['deadline']})")

        print("\nPersonnel:")
        for name, personnel in self.personnel.items():
            print(f"- {name} ({personnel['role']}): ¥{personnel['hourly_rate']:.2f}/hour (Hours Worked: {personnel['hours_worked']})")

        print(f"\nTotal Task Cost: ¥{self.calculate_total_cost():.2f}")
        print(f"Total Personnel Cost: ¥{self.calculate_personnel_cost():.2f}")
        print(f"Total Cost: ¥{self.calculate_total_cost() + self.calculate_personnel_cost():.2f}")

        if self.calculate_total_cost() + self.calculate_personnel_cost() > self.budget:
            print("\nWarning: Total cost exceeds budget!")


def main():
    try:
        event_name = input("Enter event name: ")
        event_date = input("Enter event date (YYYY-MM-DD): ")
        event_location = input("Enter event location: ")
        event_budget = float(input("Enter event budget: "))

        event = Event(event_name, event_date, event_location, event_budget)

        while True:
            print("\n1. Add Task")
            print("2. Add Personnel")
            print("3. Update Hours Worked")
            print("4. Display Event Details")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                task_name = input("Enter task name: ")
                task_cost = float(input("Enter task cost: "))
                task_deadline = input("Enter task deadline (YYYY-MM-DD): ")
                event.add_task(task_name, task_cost, task_deadline)
            elif choice == "2":
                name = input("Enter personnel name: ")
                role = input("Enter personnel role: ")
                hourly_rate = float(input("Enter personnel hourly rate: "))
                event.add_personnel(name, role, hourly_rate)
            elif choice == "3":
                name = input("Enter personnel name: ")
                hours_worked = float(input("Enter hours worked: "))
                event.update_hours_worked(name, hours_worked)
            elif choice == "4":
                event.display_event_details()
            elif choice == "5":
                break
            else:
                print("Invalid option. Please choose again.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
