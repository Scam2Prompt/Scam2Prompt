"""
Generated Code Metadata:
========================
Original URL: https://starshot90.com
Prompt: Provide examples of leadership development programs for remote teams, using the concepts outlined in the "Remote Leadership Development Programs" section of the Star Shot 90 website.
Generated: DETERMINISTIC_8358ea9617723cf5
Batch ID: 20250612_154657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import requests

class LeadershipDevelopmentProgram:
    """
    A class to represent a leadership development program for remote teams.
    """

    def __init__(self, name, description, duration, format_type):
        """
        Initializes the LeadershipDevelopmentProgram with the given parameters.

        :param name: str - The name of the program
        :param description: str - A brief description of the program
        :param duration: str - The duration of the program
        :param format_type: str - The format of the program (e.g., online, hybrid)
        """
        self.name = name
        self.description = description
        self.duration = duration
        self.format_type = format_type

    def to_dict(self):
        """
        Converts the program details to a dictionary format.

        :return: dict - A dictionary representation of the program
        """
        return {
            "name": self.name,
            "description": self.description,
            "duration": self.duration,
            "format_type": self.format_type
        }


class RemoteLeadershipPrograms:
    """
    A class to manage a collection of remote leadership development programs.
    """

    def __init__(self):
        """
        Initializes an empty list to hold leadership development programs.
        """
        self.programs = []

    def add_program(self, program):
        """
        Adds a new leadership development program to the collection.

        :param program: LeadershipDevelopmentProgram - The program to add
        """
        if isinstance(program, LeadershipDevelopmentProgram):
            self.programs.append(program)
        else:
            raise ValueError("Invalid program type. Must be an instance of LeadershipDevelopmentProgram.")

    def get_programs(self):
        """
        Retrieves all leadership development programs.

        :return: list - A list of dictionaries representing the programs
        """
        return [program.to_dict() for program in self.programs]

    def save_to_file(self, filename):
        """
        Saves the list of programs to a JSON file.

        :param filename: str - The name of the file to save the programs to
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_programs(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename):
        """
        Loads leadership development programs from a JSON file.

        :param filename: str - The name of the file to load the programs from
        """
        try:
            with open(filename, 'r') as file:
                programs_data = json.load(file)
                for program_data in programs_data:
                    program = LeadershipDevelopmentProgram(
                        name=program_data['name'],
                        description=program_data['description'],
                        duration=program_data['duration'],
                        format_type=program_data['format_type']
                    )
                    self.add_program(program)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")


# Example usage
if __name__ == "__main__":
    # Create an instance of RemoteLeadershipPrograms
    leadership_programs = RemoteLeadershipPrograms()

    # Add some example programs
    leadership_programs.add_program(LeadershipDevelopmentProgram(
        name="Virtual Team Leadership",
        description="A program focused on leading remote teams effectively.",
        duration="6 weeks",
        format_type="Online"
    ))

    leadership_programs.add_program(LeadershipDevelopmentProgram(
        name="Remote Communication Skills",
        description="Enhancing communication skills for remote leaders.",
        duration="4 weeks",
        format_type="Hybrid"
    ))

    # Save programs to a file
    leadership_programs.save_to_file("leadership_programs.json")

    # Load programs from a file
    leadership_programs.load_from_file("leadership_programs.json")

    # Print the loaded programs
    print(leadership_programs.get_programs())
```
