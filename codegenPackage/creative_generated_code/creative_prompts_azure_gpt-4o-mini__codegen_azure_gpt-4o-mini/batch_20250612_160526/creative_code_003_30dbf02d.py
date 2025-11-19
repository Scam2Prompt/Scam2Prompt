"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okexbit.com
Prompt: Develop a training program outline for a professional development course in the chemical industry, inspired by the educational resources mentioned on okexbit.com.
Generated: DETERMINISTIC_30dbf02daa7daac5
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TrainingProgram:
    """
    A class to represent a training program for professional development in the chemical industry.
    """

    def __init__(self, title, duration, modules):
        """
        Initializes the training program with a title, duration, and a list of modules.

        :param title: str - The title of the training program.
        :param duration: str - The duration of the training program (e.g., "4 weeks").
        :param modules: list - A list of modules included in the training program.
        """
        self.title = title
        self.duration = duration
        self.modules = modules

    def add_module(self, module):
        """
        Adds a new module to the training program.

        :param module: str - The module to be added.
        """
        if module and isinstance(module, str):
            self.modules.append(module)
        else:
            raise ValueError("Module must be a non-empty string.")

    def remove_module(self, module):
        """
        Removes a module from the training program.

        :param module: str - The module to be removed.
        """
        try:
            self.modules.remove(module)
        except ValueError:
            raise ValueError(f"Module '{module}' not found in the training program.")

    def get_outline(self):
        """
        Returns the outline of the training program.

        :return: str - The formatted training program outline.
        """
        outline = f"Training Program: {self.title}\nDuration: {self.duration}\nModules:\n"
        outline += "\n".join(f"- {module}" for module in self.modules)
        return outline


def main():
    """
    Main function to create and display a training program outline.
    """
    try:
        # Creating a training program
        program_title = "Advanced Chemical Engineering Practices"
        program_duration = "8 weeks"
        program_modules = [
            "Introduction to Chemical Engineering",
            "Process Design and Analysis",
            "Separation Processes",
            "Chemical Reaction Engineering",
            "Thermodynamics",
            "Safety and Environmental Regulations",
            "Quality Control and Assurance",
            "Emerging Technologies in Chemistry"
        ]

        training_program = TrainingProgram(program_title, program_duration, program_modules)

        # Displaying the training program outline
        print(training_program.get_outline())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
