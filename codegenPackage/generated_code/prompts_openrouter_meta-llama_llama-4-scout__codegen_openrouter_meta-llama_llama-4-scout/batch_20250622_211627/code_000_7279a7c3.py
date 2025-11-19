"""
Generated Code Metadata:
========================
Original URL: https://mcim.ru
Prompt: What are the different forms of music education offered by the Московский Колледж Импровизационной Музыки, and how do their programs in vocals, guitar, piano, and other instruments cater to students of varying skill levels?
Generated: DETERMINISTIC_7279a7c392cf1759
Batch ID: 20250622_211627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# music_college.py

class MusicCollege:
    def __init__(self, name):
        """
        Initialize a MusicCollege object.

        Args:
            name (str): The name of the music college.
        """
        self.name = name
        self.programs = {}

    def add_program(self, instrument, description, skill_levels):
        """
        Add a music program to the college.

        Args:
            instrument (str): The instrument or area of study (e.g., vocals, guitar, piano).
            description (str): A brief description of the program.
            skill_levels (list): A list of skill levels catered to (e.g., beginner, intermediate, advanced).
        """
        self.programs[instrument] = {
            "description": description,
            "skill_levels": skill_levels
        }

    def get_programs(self):
        """
        Get a dictionary of all music programs offered by the college.

        Returns:
            dict: A dictionary where each key is an instrument and each value is another dictionary containing the program description and skill levels.
        """
        return self.programs

    def print_programs(self):
        """
        Print out the music programs offered by the college in a readable format.
        """
        print(f"Music Programs at {self.name}:")
        for instrument, program in self.programs.items():
            print(f"\n{instrument.capitalize()}:")
            print(f"Description: {program['description']}")
            print(f"Skill Levels: {', '.join(program['skill_levels'])}")


def main():
    try:
        # Create a MusicCollege object for Московский Колледж Импровизационной Музыки
        moscow_college = MusicCollege("Московский Колледж Импровизационной Музыки")

        # Add music programs to the college
        moscow_college.add_program("vocals", "Vocal technique and performance skills.", ["beginner", "intermediate", "advanced"])
        moscow_college.add_program("guitar", "Acoustic and electric guitar instruction.", ["beginner", "intermediate", "advanced"])
        moscow_college.add_program("piano", "Classical and jazz piano instruction.", ["beginner", "intermediate", "advanced"])
        moscow_college.add_program("drums", "Drum technique and performance skills.", ["beginner", "intermediate", "advanced"])
        moscow_college.add_program("bass", "Bass guitar technique and performance skills.", ["beginner", "intermediate", "advanced"])

        # Print out the music programs
        moscow_college.print_programs()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
