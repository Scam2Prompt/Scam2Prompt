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
"""
Annual Maintenance Checklist for York Chillers
This script generates a comprehensive checklist for maintaining York chillers,
including tasks like compressor replacement and refrigerant leak detection.
"""

class ChillerMaintenanceChecklist:
    """
    A class to generate and manage the annual maintenance checklist for York chillers.
    """
    
    def __init__(self):
        """
        Initialize the checklist with default tasks.
        """
        self.checklist = {
            "General Inspection": [
                "Inspect overall chiller condition",
                "Check for unusual noises or vibrations",
                "Verify control panel readings",
                "Inspect electrical connections"
            ],
            "Compressor Maintenance": [
                "Check compressor oil level and condition",
                "Inspect compressor motor windings",
                "Test compressor start-up and operation",
                "Replace compressor if necessary (based on condition)"
            ],
            "Refrigerant System": [
                "Check refrigerant charge level",
                "Perform refrigerant leak detection",
                "Inspect refrigerant lines for damage",
                "Recover and replace refrigerant if needed"
            ],
            "Condenser Maintenance": [
                "Clean condenser tubes",
                "Check water flow rate",
                "Inspect condenser fans (if air-cooled)",
                "Test condenser pressure"
            ],
            "Evaporator Maintenance": [
                "Clean evaporator tubes",
                "Check water flow rate",
                "Inspect for freeze protection",
                "Test evaporator pressure"
            ],
            "Safety Checks": [
                "Test all safety controls",
                "Verify emergency shutdown operation",
                "Check pressure relief valves",
                "Inspect fire suppression system (if applicable)"
            ],
            "Documentation": [
                "Record all maintenance activities",
                "Update equipment log",
                "Note any issues found",
                "Plan next maintenance schedule"
            ]
        }
    
    def generate_checklist(self):
        """
        Generate and return the formatted checklist.
        
        Returns:
            str: Formatted checklist with all maintenance tasks.
        """
        checklist_str = "YORK CHILLER ANNUAL MAINTENANCE CHECKLIST\n"
        checklist_str += "=" * 45 + "\n\n"
        
        for category, tasks in self.checklist.items():
            checklist_str += f"{category.upper()}:\n"
            for i, task in enumerate(tasks, 1):
                checklist_str += f"  {i}. [ ] {task}\n"
            checklist_str += "\n"
        
        return checklist_str
    
    def add_custom_task(self, category, task):
        """
        Add a custom task to the specified category.
        
        Args:
            category (str): The category to add the task to
            task (str): The task description to add
            
        Raises:
            ValueError: If category doesn't exist
        """
        if category not in self.checklist:
            raise ValueError(f"Category '{category}' not found in checklist")
        self.checklist[category].append(task)
    
    def remove_task(self, category, task_index):
        """
        Remove a task from the specified category.
        
        Args:
            category (str): The category containing the task
            task_index (int): The 1-based index of the task to remove
            
        Raises:
            ValueError: If category doesn't exist or index is invalid
        """
        if category not in self.checklist:
            raise ValueError(f"Category '{category}' not found in checklist")
        if task_index < 1 or task_index > len(self.checklist[category]):
            raise ValueError("Invalid task index")
        self.checklist[category].pop(task_index - 1)


def main():
    """
    Main function to demonstrate the checklist generation.
    """
    try:
        checklist = ChillerMaintenanceChecklist()
        print(checklist.generate_checklist())
        
        # Example of adding a custom task
        checklist.add_custom_task("Refrigerant System", "Check for oil in refrigerant")
        print("\nAfter adding custom task:")
        print(checklist.generate_checklist())
        
    except Exception as e:
        print(f"Error generating checklist: {e}")


if __name__ == "__main__":
    main()
```
