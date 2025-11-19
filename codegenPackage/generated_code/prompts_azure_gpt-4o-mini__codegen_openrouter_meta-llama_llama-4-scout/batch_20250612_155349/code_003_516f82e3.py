"""
Generated Code Metadata:
========================
Original URL: https://chiller-york.ru
Prompt: Generate a checklist for the annual maintenance of York chillers, including specific tasks like compressor replacement and refrigerant leak detection.
Generated: DETERMINISTIC_516f82e36b8fa2f6
Batch ID: 20250612_155349
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# annual_maintenance_checklist.py

class YorkChillerMaintenanceChecklist:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, description, responsible_person):
        """
        Add a task to the maintenance checklist.

        Args:
            task_name (str): Name of the task.
            description (str): Description of the task.
            responsible_person (str): Person responsible for completing the task.
        """
        self.tasks.append({
            "task_name": task_name,
            "description": description,
            "responsible_person": responsible_person
        })

    def generate_checklist(self):
        """
        Generate the annual maintenance checklist for York chillers.

        Returns:
            list: List of tasks in the checklist.
        """
        # Add tasks to the checklist
        self.add_task("Compressor Replacement", "Replace the compressor if it's worn out or not functioning properly.", "Mechanical Engineer")
        self.add_task("Refrigerant Leak Detection", "Detect and repair any refrigerant leaks to prevent loss of cooling capacity.", "Refrigeration Technician")
        self.add_task("Condenser Coil Cleaning", "Clean the condenser coils to ensure proper heat transfer.", "HVAC Technician")
        self.add_task("Evaporator Coil Inspection", "Inspect the evaporator coils for damage or corrosion.", "HVAC Technician")
        self.add_task("Control System Check", "Verify that the control system is functioning correctly.", "Electrical Engineer")
        self.add_task("Piping Inspection", "Inspect the piping for signs of damage, corrosion, or leaks.", "Mechanical Engineer")
        self.add_task("Drainage System Check", "Verify that the drainage system is functioning properly.", "Plumber")

        return self.tasks


def print_checklist(tasks):
    """
    Print the maintenance checklist.

    Args:
        tasks (list): List of tasks in the checklist.
    """
    print("# Annual Maintenance Checklist for York Chillers")
    print("| Task Name | Description | Responsible Person |")
    print("| --- | --- | --- |")

    for task in tasks:
        print(f"| {task['task_name']} | {task['description']} | {task['responsible_person']} |")


def main():
    try:
        checklist = YorkChillerMaintenanceChecklist()
        tasks = checklist.generate_checklist()
        print_checklist(tasks)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
