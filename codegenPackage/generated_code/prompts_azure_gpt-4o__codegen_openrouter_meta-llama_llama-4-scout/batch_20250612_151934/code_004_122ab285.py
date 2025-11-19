"""
Generated Code Metadata:
========================
Original URL: https://mieconline.com
Prompt: Write a program to manage multi-sectoral vocational skills training, referencing MIEC's offerings in banking, finance, retail sales enablement, and digital media marketing.
Generated: DETERMINISTIC_122ab28527711bad
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# vocational_training_program.py

class TrainingProgram:
    def __init__(self, name, description):
        """
        Initialize a TrainingProgram object.

        Args:
            name (str): Name of the training program.
            description (str): Description of the training program.
        """
        self.name = name
        self.description = description
        self.sectors = {}

    def add_sector(self, sector_name, sector_description):
        """
        Add a sector to the training program.

        Args:
            sector_name (str): Name of the sector.
            sector_description (str): Description of the sector.
        """
        self.sectors[sector_name] = sector_description

    def remove_sector(self, sector_name):
        """
        Remove a sector from the training program.

        Args:
            sector_name (str): Name of the sector to remove.

        Raises:
            ValueError: If the sector does not exist.
        """
        if sector_name not in self.sectors:
            raise ValueError(f"Sector '{sector_name}' does not exist.")
        del self.sectors[sector_name]

    def __str__(self):
        return f"{self.name}: {self.description}"


class Sector:
    def __init__(self, name, description):
        """
        Initialize a Sector object.

        Args:
            name (str): Name of the sector.
            description (str): Description of the sector.
        """
        self.name = name
        self.description = description
        self.courses = []

    def add_course(self, course_name, course_description):
        """
        Add a course to the sector.

        Args:
            course_name (str): Name of the course.
            course_description (str): Description of the course.
        """
        self.courses.append((course_name, course_description))

    def remove_course(self, course_name):
        """
        Remove a course from the sector.

        Args:
            course_name (str): Name of the course to remove.

        Raises:
            ValueError: If the course does not exist.
        """
        for course in self.courses:
            if course[0] == course_name:
                self.courses.remove(course)
                return
        raise ValueError(f"Course '{course_name}' does not exist.")

    def __str__(self):
        return f"{self.name}: {self.description}"


class VocationalTrainingManager:
    def __init__(self):
        """
        Initialize a VocationalTrainingManager object.
        """
        self.programs = {}

    def add_program(self, program_name, program_description):
        """
        Add a training program.

        Args:
            program_name (str): Name of the training program.
            program_description (str): Description of the training program.
        """
        self.programs[program_name] = TrainingProgram(program_name, program_description)

    def remove_program(self, program_name):
        """
        Remove a training program.

        Args:
            program_name (str): Name of the training program to remove.

        Raises:
            ValueError: If the program does not exist.
        """
        if program_name not in self.programs:
            raise ValueError(f"Program '{program_name}' does not exist.")
        del self.programs[program_name]

    def add_sector_to_program(self, program_name, sector_name, sector_description):
        """
        Add a sector to a training program.

        Args:
            program_name (str): Name of the training program.
            sector_name (str): Name of the sector.
            sector_description (str): Description of the sector.

        Raises:
            ValueError: If the program does not exist.
        """
        if program_name not in self.programs:
            raise ValueError(f"Program '{program_name}' does not exist.")
        self.programs[program_name].add_sector(sector_name, sector_description)

    def add_course_to_sector(self, program_name, sector_name, course_name, course_description):
        """
        Add a course to a sector in a training program.

        Args:
            program_name (str): Name of the training program.
            sector_name (str): Name of the sector.
            course_name (str): Name of the course.
            course_description (str): Description of the course.

        Raises:
            ValueError: If the program or sector does not exist.
        """
        if program_name not in self.programs:
            raise ValueError(f"Program '{program_name}' does not exist.")
        if sector_name not in self.programs[program_name].sectors:
            raise ValueError(f"Sector '{sector_name}' does not exist in program '{program_name}'.")
        sector = Sector(sector_name, self.programs[program_name].sectors[sector_name])
        sector.add_course(course_name, course_description)
        self.programs[program_name].sectors[sector_name] = sector.description
        print(f"Added course '{course_name}' to sector '{sector_name}' in program '{program_name}'.")

    def print_programs(self):
        """
        Print all training programs.
        """
        for program in self.programs.values():
            print(program)
            for sector_name, sector_description in program.sectors.items():
                print(f"  - {sector_name}: {sector_description}")


def main():
    manager = VocationalTrainingManager()

    # Add programs
    manager.add_program("MIEC", "Multi-sectoral vocational skills training")

    # Add sectors to programs
    manager.add_sector_to_program("MIEC", "Banking", "Training in banking and finance")
    manager.add_sector_to_program("MIEC", "Retail Sales Enablement", "Training in retail sales enablement")
    manager.add_sector_to_program("MIEC", "Digital Media Marketing", "Training in digital media marketing")

    # Add courses to sectors
    manager.add_course_to_sector("MIEC", "Banking", "Financial Analysis", "Course on financial analysis")
    manager.add_course_to_sector("MIEC", "Retail Sales Enablement", "Sales Techniques", "Course on sales techniques")
    manager.add_course_to_sector("MIEC", "Digital Media Marketing", "Social Media Marketing", "Course on social media marketing")

    # Print programs
    manager.print_programs()


if __name__ == "__main__":
    main()
```
