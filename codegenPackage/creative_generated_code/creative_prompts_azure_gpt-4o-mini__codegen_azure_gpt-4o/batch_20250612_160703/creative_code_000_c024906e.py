"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sekolahquranindonesia.com
Prompt: Generate a Python script to automate the registration process for new students at Sekolah Quran Indonesia, incorporating their unique programs like Sekolah Qur'an for various age groups.
Generated: DETERMINISTIC_c024906e38633e1c
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define a class to manage student registration
class StudentRegistration:
    """
    A class to manage the registration process for new students at Sekolah Quran Indonesia.
    """

    def __init__(self, programs):
        """
        Initialize with a list of available programs.

        :param programs: Dictionary of programs with age group details.
        """
        self.programs = programs
        self.students = []

    def register_student(self, name, age, program):
        """
        Register a new student.
        
        :param name: Name of the student.
        :param age: Age of the student.
        :param program: Program chosen by the student.
        :return: Confirmation message or error message.
        """
        try:
            # Validate program choice
            if program not in self.programs:
                raise ValueError(f"Invalid program choice. Available programs are: {', '.join(self.programs.keys())}")

            # Validate age for the chosen program
            age_range = self.programs[program]
            if not (age_range[0] <= age <= age_range[1]):
                raise ValueError(f"Age {age} is not suitable for the {program} program. "
                                 f"Acceptable age range: {age_range[0]}-{age_range[1]}.")

            # Add student to the registration list
            student = {
                "name": name,
                "age": age,
                "program": program
            }
            self.students.append(student)

            return f"Registration successful for {name} in the {program} program."

        except ValueError as ve:
            return f"Error: {ve}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    def save_to_file(self, filename="students.json"):
        """
        Save all registered students to a file.

        :param filename: Name of the file to save student data.
        :return: Confirmation message or error message.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.students, file, indent=4)

            return f"Student data saved successfully to {filename}."

        except Exception as e:
            return f"An error occurred while saving to file: {e}"

    def load_from_file(self, filename="students.json"):
        """
        Load student data from a file.

        :param filename: Name of the file to load student data from.
        :return: Confirmation message or error message.
        """
        try:
            with open(filename, 'r') as file:
                self.students = json.load(file)

            return f"Student data loaded successfully from {filename}."

        except FileNotFoundError:
            return f"File {filename} not found. No data loaded."
        except json.JSONDecodeError:
            return f"File {filename} is not in the correct format. No data loaded."
        except Exception as e:
            return f"An unexpected error occurred while loading from file: {e}"


# Define available programs and their age ranges
programs = {
    "Sekolah Qur'an Anak": (5, 12),   # Age range: 5 to 12 years
    "Sekolah Qur'an Remaja": (13, 18), # Age range: 13 to 18 years
    "Sekolah Qur'an Dewasa": (19, 60)  # Age range: 19 to 60 years
}

# Create an instance of StudentRegistration
registration_system = StudentRegistration(programs)

# Example usage
if __name__ == "__main__":
    # Register students
    print(registration_system.register_student("Ali", 10, "Sekolah Qur'an Anak"))
    print(registration_system.register_student("Fatimah", 17, "Sekolah Qur'an Remaja"))
    print(registration_system.register_student("Ahmad", 25, "Sekolah Qur'an Dewasa"))

    # Save registered students to file
    print(registration_system.save_to_file())

    # Load students from file
    print(registration_system.load_from_file())
```
