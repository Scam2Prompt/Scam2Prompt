"""
Generated Code Metadata:
========================
Original URL: https://www.nkatandiinyom.com
Prompt: What are some effective strategies for mentoring women leaders in Igbo communities, based on the guidance provided by Nkata ndi Inyom Igbo?
Generated: DETERMINISTIC_d9913dc45badabab
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MentoringProgram:
    """
    A class to represent a mentoring program for women leaders in Igbo communities.
    """

    def __init__(self):
        """
        Initializes the mentoring program with an empty list of mentees.
        """
        self.mentees = []

    def add_mentee(self, name: str, age: int, background: str) -> None:
        """
        Adds a new mentee to the program.

        Parameters:
        name (str): The name of the mentee.
        age (int): The age of the mentee.
        background (str): The professional background of the mentee.

        Raises:
        ValueError: If age is not a positive integer.
        """
        if age <= 0:
            raise ValueError("Age must be a positive integer.")
        
        mentee = {
            'name': name,
            'age': age,
            'background': background
        }
        self.mentees.append(mentee)

    def provide_guidance(self, mentee_name: str, guidance: str) -> None:
        """
        Provides guidance to a specific mentee.

        Parameters:
        mentee_name (str): The name of the mentee to provide guidance to.
        guidance (str): The guidance to be provided.

        Raises:
        ValueError: If the mentee is not found in the program.
        """
        mentee = self.find_mentee(mentee_name)
        if mentee is None:
            raise ValueError(f"Mentee '{mentee_name}' not found.")
        
        print(f"Guidance for {mentee['name']}: {guidance}")

    def find_mentee(self, name: str) -> dict:
        """
        Finds a mentee by name.

        Parameters:
        name (str): The name of the mentee to find.

        Returns:
        dict: The mentee's information if found, otherwise None.
        """
        for mentee in self.mentees:
            if mentee['name'] == name:
                return mentee
        return None

    def list_mentees(self) -> None:
        """
        Lists all mentees in the program.
        """
        if not self.mentees:
            print("No mentees in the program.")
            return
        
        print("List of Mentees:")
        for mentee in self.mentees:
            print(f"- {mentee['name']}, Age: {mentee['age']}, Background: {mentee['background']}")

# Example usage
if __name__ == "__main__":
    program = MentoringProgram()
    
    try:
        program.add_mentee("Adaobi", 30, "Community Organizer")
        program.add_mentee("Chinonso", 25, "Entrepreneur")
        
        program.list_mentees()
        
        program.provide_guidance("Adaobi", "Focus on building a strong network.")
        program.provide_guidance("Chinonso", "Consider mentorship opportunities.")
        
    except ValueError as e:
        print(f"Error: {e}")
```
