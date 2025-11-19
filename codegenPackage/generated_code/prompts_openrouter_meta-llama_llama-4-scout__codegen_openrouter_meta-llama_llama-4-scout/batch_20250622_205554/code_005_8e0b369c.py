"""
Generated Code Metadata:
========================
Original URL: https://mieconline.com
Prompt: "Develop a training plan for a graduate trainee program in IT, inspired by MIEC's Graduate in Training Entrepreneurship Scheme (GTES)."
Generated: DETERMINISTIC_8e0b369c08fa46c8
Batch ID: 20250622_205554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# training_plan.py

class TrainingPlan:
    """
    A class representing a training plan for a graduate trainee program in IT.

    Attributes:
    ----------
    trainee_name : str
        The name of the trainee.
    program_name : str
        The name of the program.
    duration : int
        The duration of the program in weeks.
    modules : list
        A list of training modules.

    Methods:
    -------
    add_module(module_name, duration, description)
        Adds a new training module to the plan.
    remove_module(module_name)
        Removes a training module from the plan.
    display_plan()
        Displays the training plan.
    """

    def __init__(self, trainee_name, program_name, duration):
        """
        Initializes a TrainingPlan object.

        Args:
        ----
        trainee_name (str): The name of the trainee.
        program_name (str): The name of the program.
        duration (int): The duration of the program in weeks.
        """
        self.trainee_name = trainee_name
        self.program_name = program_name
        self.duration = duration
        self.modules = []

    def add_module(self, module_name, duration, description):
        """
        Adds a new training module to the plan.

        Args:
        ----
        module_name (str): The name of the module.
        duration (int): The duration of the module in weeks.
        description (str): A brief description of the module.

        Raises:
        ------
        ValueError: If the module duration exceeds the program duration.
        """
        if sum(m['duration'] for m in self.modules) + duration > self.duration:
            raise ValueError("Module duration exceeds program duration")

        self.modules.append({
            'name': module_name,
            'duration': duration,
            'description': description
        })

    def remove_module(self, module_name):
        """
        Removes a training module from the plan.

        Args:
        ----
        module_name (str): The name of the module to remove.

        Raises:
        ------
        ValueError: If the module does not exist in the plan.
        """
        for module in self.modules:
            if module['name'] == module_name:
                self.modules.remove(module)
                return

        raise ValueError("Module not found in the plan")

    def display_plan(self):
        """
        Displays the training plan.
        """
        print(f"Training Plan for {self.trainee_name} - {self.program_name}")
        print("---------------------------------------------------------")
        print(f"Duration: {self.duration} weeks")
        print("Modules:")
        for i, module in enumerate(self.modules, start=1):
            print(f"{i}. {module['name']} ({module['duration']} weeks)")
            print(f"   Description: {module['description']}")


def main():
    try:
        # Create a new training plan
        plan = TrainingPlan("John Doe", "Graduate Trainee Program", 12)

        # Add training modules
        plan.add_module("Introduction to IT", 2, "Overview of IT concepts")
        plan.add_module("Programming Fundamentals", 4, "Introduction to programming languages")
        plan.add_module("Data Structures and Algorithms", 4, "Data structures and algorithms")

        # Display the training plan
        plan.display_plan()

        # Remove a module
        plan.remove_module("Programming Fundamentals")

        # Display the updated training plan
        print("\nUpdated Training Plan:")
        plan.display_plan()

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
