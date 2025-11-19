"""
Generated Code Metadata:
========================
Original URL: https://ydmc.edu.np
Prompt: Compare the features of BBS, B Ed, and MBS programs offered by YDMC in terms of course duration and career prospects.
Generated: DETERMINISTIC_4cac908052a2733e
Batch ID: 20250622_205217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Program:
    """
    A class to represent an academic program.
    """

    def __init__(self, name, duration, career_prospects):
        """
        Initializes the Program with name, duration, and career prospects.

        :param name: str - The name of the program
        :param duration: str - The duration of the program
        :param career_prospects: list - A list of potential career paths
        """
        self.name = name
        self.duration = duration
        self.career_prospects = career_prospects

    def display_info(self):
        """
        Displays the information of the program.
        """
        print(f"Program Name: {self.name}")
        print(f"Duration: {self.duration}")
        print("Career Prospects:")
        for prospect in self.career_prospects:
            print(f"- {prospect}")
        print("\n")


def main():
    """
    Main function to compare the features of BBS, B Ed, and MBS programs.
    """
    try:
        # Define the programs offered by YDMC
        bbs = Program(
            name="Bachelor of Business Studies (BBS)",
            duration="4 years",
            career_prospects=[
                "Business Analyst",
                "Marketing Manager",
                "Financial Consultant",
                "Entrepreneur"
            ]
        )

        b_ed = Program(
            name="Bachelor of Education (B Ed)",
            duration="2 years",
            career_prospects=[
                "School Teacher",
                "Educational Consultant",
                "Curriculum Developer",
                "Education Administrator"
            ]
        )

        mbs = Program(
            name="Master of Business Studies (MBS)",
            duration="2 years",
            career_prospects=[
                "Business Manager",
                "Operations Manager",
                "Project Manager",
                "Strategic Planner"
            ]
        )

        # Display information for each program
        bbs.display_info()
        b_ed.display_info()
        mbs.display_info()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
