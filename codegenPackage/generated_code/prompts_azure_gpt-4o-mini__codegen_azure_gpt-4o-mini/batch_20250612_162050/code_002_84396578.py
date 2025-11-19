"""
Generated Code Metadata:
========================
Original URL: https://praveenallc.com
Prompt: Recommend a training program structure for IT services that aligns with the tailored approach mentioned by Praveena LLC.
Generated: DETERMINISTIC_84396578dabd8626
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TrainingProgram:
    """
    A class to represent a training program for IT services.
    """

    def __init__(self, program_name, duration, target_audience):
        """
        Initializes the training program with a name, duration, and target audience.

        :param program_name: Name of the training program
        :param duration: Duration of the training program in hours
        :param target_audience: Intended audience for the training program
        """
        self.program_name = program_name
        self.duration = duration
        self.target_audience = target_audience
        self.modules = []

    def add_module(self, module_name, module_duration, module_description):
        """
        Adds a module to the training program.

        :param module_name: Name of the module
        :param module_duration: Duration of the module in hours
        :param module_description: Description of the module
        :raises ValueError: If module duration is not positive
        """
        if module_duration <= 0:
            raise ValueError("Module duration must be a positive number.")
        
        module = {
            'name': module_name,
            'duration': module_duration,
            'description': module_description
        }
        self.modules.append(module)

    def get_program_structure(self):
        """
        Returns the structure of the training program including all modules.

        :return: A dictionary containing program details and modules
        """
        return {
            'program_name': self.program_name,
            'duration': self.duration,
            'target_audience': self.target_audience,
            'modules': self.modules
        }

    def __str__(self):
        """
        Returns a string representation of the training program.
        """
        return f"Training Program: {self.program_name}, Duration: {self.duration} hours, Target Audience: {self.target_audience}"


# Example usage
if __name__ == "__main__":
    try:
        # Create a new training program
        it_training = TrainingProgram("IT Services Training", 40, "IT Professionals")

        # Add modules to the training program
        it_training.add_module("Introduction to IT Services", 5, "Overview of IT services and their importance.")
        it_training.add_module("Cloud Computing Basics", 10, "Fundamentals of cloud computing and its applications.")
        it_training.add_module("Cybersecurity Essentials", 15, "Key concepts and practices in cybersecurity.")
        it_training.add_module("Data Management", 10, "Best practices for managing and analyzing data.")

        # Print the program structure
        program_structure = it_training.get_program_structure()
        print(program_structure)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
