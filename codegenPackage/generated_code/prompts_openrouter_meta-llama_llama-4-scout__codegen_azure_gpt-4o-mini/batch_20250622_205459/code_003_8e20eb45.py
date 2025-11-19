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
class CommunityEducationProgram:
    """
    A class to represent a community-based education program focused on digital literacy and numeracy skills.
    """

    def __init__(self, program_name, target_community):
        """
        Initializes the CommunityEducationProgram with a name and target community.

        :param program_name: str - The name of the education program.
        :param target_community: str - The community that the program aims to serve.
        """
        self.program_name = program_name
        self.target_community = target_community
        self.courses = []
        self.participants = []

    def add_course(self, course_name, course_description):
        """
        Adds a new course to the program.

        :param course_name: str - The name of the course.
        :param course_description: str - A brief description of the course.
        """
        course = {
            'name': course_name,
            'description': course_description
        }
        self.courses.append(course)
        print(f"Course '{course_name}' added successfully.")

    def register_participant(self, participant_name):
        """
        Registers a new participant in the program.

        :param participant_name: str - The name of the participant.
        """
        if participant_name not in self.participants:
            self.participants.append(participant_name)
            print(f"Participant '{participant_name}' registered successfully.")
        else:
            print(f"Participant '{participant_name}' is already registered.")

    def display_program_info(self):
        """
        Displays the program information including courses and registered participants.
        """
        print(f"Program Name: {self.program_name}")
        print(f"Target Community: {self.target_community}")
        print("Courses Offered:")
        for course in self.courses:
            print(f"- {course['name']}: {course['description']}")
        print("Registered Participants:")
        for participant in self.participants:
            print(f"- {participant}")

    def run_program(self):
        """
        Simulates running the program by displaying the program info.
        """
        try:
            self.display_program_info()
        except Exception as e:
            print(f"An error occurred while running the program: {e}")

# Example usage
if __name__ == "__main__":
    # Create a new community education program
    program = CommunityEducationProgram("Digital Skills for All", "Local Community Center")

    # Add courses to the program
    program.add_course("Introduction to Computers", "Learn the basics of computer usage.")
    program.add_course("Basic Math Skills", "Enhance your numeracy skills for everyday tasks.")

    # Register participants
    program.register_participant("Alice Johnson")
    program.register_participant("Bob Smith")

    # Run the program to display information
    program.run_program()
```
