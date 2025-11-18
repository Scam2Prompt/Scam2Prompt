"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astoricrypto.com
Prompt: Develop a mentorship program framework for new crypto investors, offering one-on-one guidance, similar to AstoriCrypto's free mentorship initiative.
Generated: DETERMINISTIC_7cf8aa4e96822bb9
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Mentor:
    """
    A class to represent a mentor in the mentorship program.
    """

    def __init__(self, name, expertise):
        """
        Initializes a new Mentor instance.

        Args:
            name (str): The name of the mentor.
            expertise (str): The area of expertise of the mentor.
        """
        self.name = name
        self.expertise = expertise
        self.mentees = []

    def add_mentee(self, mentee):
        """
        Adds a mentee to the mentor's list.

        Args:
            mentee (Mentee): The mentee to be added.
        """
        self.mentees.append(mentee)

    def show_mentees(self):
        """
        Displays the list of mentees under this mentor.
        """
        if not self.mentees:
            print(f"{self.name} has no mentees.")
        else:
            print(f"{self.name}'s Mentees:")
            for mentee in self.mentees:
                print(f"- {mentee.name}")


class Mentee:
    """
    A class to represent a mentee in the mentorship program.
    """

    def __init__(self, name, investment_level):
        """
        Initializes a new Mentee instance.

        Args:
            name (str): The name of the mentee.
            investment_level (str): The level of investment knowledge (e.g., beginner, intermediate, advanced).
        """
        self.name = name
        self.investment_level = investment_level


class MentorshipProgram:
    """
    A class to manage a mentorship program for new crypto investors.
    """

    def __init__(self):
        """
        Initializes a new MentorshipProgram instance.
        """
        self.mentors = []

    def add_mentor(self, mentor):
        """
        Adds a mentor to the mentorship program.

        Args:
            mentor (Mentor): The mentor to be added.
        """
        self.mentors.append(mentor)

    def find_mentor(self, expertise):
        """
        Finds a mentor based on their area of expertise.

        Args:
            expertise (str): The area of expertise to search for.

        Returns:
            Mentor or None: The mentor with the specified expertise or None if not found.
        """
        for mentor in self.mentors:
            if mentor.expertise.lower() == expertise.lower():
                return mentor
        return None

    def match_mentee_with_mentor(self, mentee_name, investment_level, expertise):
        """
        Matches a mentee with a mentor based on investment level and expertise.

        Args:
            mentee_name (str): The name of the mentee.
            investment_level (str): The level of investment knowledge of the mentee.
            expertise (str): The area of expertise of the mentor.

        Returns:
            str: A message indicating the result of the matching process.
        """
        mentor = self.find_mentor(expertise)
        
        # Error handling for mentor not found
        if mentor is None:
            return f"No mentor found with expertise in {expertise}."

        # Create a new mentee instance
        mentee = Mentee(mentee_name, investment_level)
        
        # Add mentee to the mentor's list
        mentor.add_mentee(mentee)
        return f"{mentee_name} has been successfully matched with mentor {mentor.name}."


# Example usage
if __name__ == "__main__":
    # Create the mentorship program
    mentorship_program = MentorshipProgram()

    # Add mentors to the program
    mentorship_program.add_mentor(Mentor("Alice", "Blockchain Technology"))
    mentorship_program.add_mentor(Mentor("Bob", "Trading Strategies"))

    # Match mentees with mentors
    print(mentorship_program.match_mentee_with_mentor("John Doe", "beginner", "Blockchain Technology"))
    print(mentorship_program.match_mentee_with_mentor("Jane Smith", "intermediate", "Trading Strategies"))
    print(mentorship_program.match_mentee_with_mentor("Emily Johnson", "beginner", "Investing Fundamentals"))  # Non-existent expertise
```
