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
class GraduateTraineeProgram:
    """
    A class to represent a Graduate Trainee Program in IT.
    This program is inspired by MIEC's Graduate in Training Entrepreneurship Scheme (GTES).
    """

    def __init__(self, program_name, duration_months):
        """
        Initializes the GraduateTraineeProgram with a name and duration.

        :param program_name: Name of the training program
        :param duration_months: Duration of the program in months
        """
        self.program_name = program_name
        self.duration_months = duration_months
        self.modules = []
        self.trainees = []

    def add_module(self, module_name, description):
        """
        Adds a training module to the program.

        :param module_name: Name of the module
        :param description: Description of the module
        """
        module = {
            'name': module_name,
            'description': description
        }
        self.modules.append(module)

    def enroll_trainee(self, trainee_name):
        """
        Enrolls a trainee in the program.

        :param trainee_name: Name of the trainee
        :raises ValueError: If the trainee is already enrolled
        """
        if trainee_name in self.trainees:
            raise ValueError(f"Trainee '{trainee_name}' is already enrolled.")
        self.trainees.append(trainee_name)

    def get_program_details(self):
        """
        Returns the details of the program including modules and enrolled trainees.

        :return: A dictionary containing program details
        """
        return {
            'program_name': self.program_name,
            'duration_months': self.duration_months,
            'modules': self.modules,
            'trainees': self.trainees
        }

    def display_program_info(self):
        """
        Displays the program information in a readable format.
        """
        details = self.get_program_details()
        print(f"Program Name: {details['program_name']}")
        print(f"Duration: {details['duration_months']} months")
        print("Modules:")
        for module in details['modules']:
            print(f" - {module['name']}: {module['description']}")
        print("Enrolled Trainees:")
        for trainee in details['trainees']:
            print(f" - {trainee}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a new Graduate Trainee Program
        gtp = GraduateTraineeProgram("IT Graduate Trainee Program", 12)

        # Add training modules
        gtp.add_module("Software Development", "Introduction to software development methodologies.")
        gtp.add_module("Data Analysis", "Fundamentals of data analysis and visualization.")
        gtp.add_module("Cybersecurity", "Basics of cybersecurity and best practices.")

        # Enroll trainees
        gtp.enroll_trainee("Alice Johnson")
        gtp.enroll_trainee("Bob Smith")

        # Display program information
        gtp.display_program_info()

    except Exception as e:
        print(f"An error occurred: {e}")
```
