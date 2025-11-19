"""
Generated Code Metadata:
========================
Original URL: https://nicerfoundation.org.ng
Prompt: Develop a plan for a community-based education program using digital literacy and numeracy skills, inspired by the NICER Foundation's mission and goals.
Generated: DETERMINISTIC_8e20eb457ea31371
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# community_education_program.py

class CommunityEducationProgram:
    """
    A program aimed at improving digital literacy and numeracy skills in the community.

    Inspired by the NICER Foundation's mission and goals.
    """

    def __init__(self, program_name, target_audience, goals):
        """
        Initialize the community education program.

        Args:
            program_name (str): The name of the program.
            target_audience (str): The target audience of the program.
            goals (list): A list of goals for the program.
        """
        self.program_name = program_name
        self.target_audience = target_audience
        self.goals = goals
        self.participants = []
        self.courses = []

    def add_participant(self, participant):
        """
        Add a participant to the program.

        Args:
            participant (str): The name of the participant.

        Raises:
            ValueError: If the participant is already in the program.
        """
        if participant in self.participants:
            raise ValueError("Participant already exists in the program.")
        self.participants.append(participant)

    def add_course(self, course):
        """
        Add a course to the program.

        Args:
            course (Course): The course to add.

        Raises:
            ValueError: If the course is already in the program.
        """
        if course in self.courses:
            raise ValueError("Course already exists in the program.")
        self.courses.append(course)

    def display_program_info(self):
        """
        Display information about the program.
        """
        print(f"Program Name: {self.program_name}")
        print(f"Target Audience: {self.target_audience}")
        print(f"Goals: {', '.join(self.goals)}")
        print(f"Participants: {', '.join(self.participants)}")
        print("Courses:")
        for course in self.courses:
            print(course)


class Course:
    """
    A course in the community education program.
    """

    def __init__(self, name, description, topics):
        """
        Initialize the course.

        Args:
            name (str): The name of the course.
            description (str): A brief description of the course.
            topics (list): A list of topics covered in the course.
        """
        self.name = name
        self.description = description
        self.topics = topics

    def __str__(self):
        """
        Return a string representation of the course.
        """
        return f"{self.name}: {self.description}, Topics: {', '.join(self.topics)}"


def main():
    try:
        # Create a community education program
        program = CommunityEducationProgram(
            "Digital Literacy and Numeracy Program",
            "Adults in the local community",
            ["Improve digital literacy", "Improve numeracy skills", "Enhance employability"]
        )

        # Create courses
        digital_literacy_course = Course(
            "Digital Literacy",
            "Learn basic computer skills and online safety",
            ["Basic computer skills", "Online safety", "Digital citizenship"]
        )
        numeracy_course = Course(
            "Numeracy Skills",
            "Learn basic math concepts and their applications",
            ["Basic math concepts", "Measurement and data", "Financial literacy"]
        )

        # Add courses to the program
        program.add_course(digital_literacy_course)
        program.add_course(numeracy_course)

        # Add participants to the program
        program.add_participant("John Doe")
        program.add_participant("Jane Smith")

        # Display program information
        program.display_program_info()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
