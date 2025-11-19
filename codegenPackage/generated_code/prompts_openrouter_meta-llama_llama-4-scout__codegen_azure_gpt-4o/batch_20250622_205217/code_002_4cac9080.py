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
# Program to compare the features of BBS, B Ed, and MBS programs offered by YDMC
# in terms of course duration and career prospects.

# Define a class to represent a program
class Program:
    def __init__(self, name, duration, career_prospects):
        """
        Initialize a Program object.

        :param name: Name of the program (e.g., BBS, B Ed, MBS)
        :param duration: Duration of the program in years
        :param career_prospects: Career prospects associated with the program
        """
        self.name = name
        self.duration = duration
        self.career_prospects = career_prospects

    def __str__(self):
        """
        Return a string representation of the program.

        :return: String describing the program
        """
        return f"{self.name}: Duration - {self.duration} years, Career Prospects - {self.career_prospects}"


# Function to compare programs
def compare_programs(programs):
    """
    Compare the features of multiple programs.

    :param programs: List of Program objects
    :return: None
    """
    print("Comparison of Programs Offered by YDMC:")
    print("-" * 50)
    for program in programs:
        print(program)
    print("-" * 50)


# Main function
def main():
    """
    Main function to execute the program comparison.
    """
    try:
        # Define the programs offered by YDMC
        bbs = Program(
            name="BBS",
            duration=4,
            career_prospects="Business management, entrepreneurship, corporate jobs"
        )
        b_ed = Program(
            name="B Ed",
            duration=2,
            career_prospects="Teaching, educational administration, curriculum design"
        )
        mbs = Program(
            name="MBS",
            duration=2,
            career_prospects="Advanced business management, research, consultancy"
        )

        # List of programs
        programs = [bbs, b_ed, mbs]

        # Compare the programs
        compare_programs(programs)

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
