"""
Generated Code Metadata:
========================
Original URL: https://inmaculada.edu.ec
Prompt: "Generate a description of a bilingual educational institution in Quito, Ecuador that offers programs from initial education to high school, incorporating Christian values."
Generated: DETERMINISTIC_11c0edd0d90a73a0
Batch ID: 20250622_204729
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BilingualEducationalInstitution:
    """
    A class to represent a bilingual educational institution in Quito, Ecuador.
    
    Attributes:
        name (str): The name of the institution.
        location (str): The location of the institution.
        programs (list): A list of educational programs offered.
        values (list): A list of core values upheld by the institution.
    """

    def __init__(self, name, location):
        """
        Initializes the BilingualEducationalInstitution with a name and location.
        
        Args:
            name (str): The name of the institution.
            location (str): The location of the institution.
        """
        self.name = name
        self.location = location
        self.programs = []
        self.values = ["Christian values", "Respect", "Integrity", "Excellence"]

    def add_program(self, program):
        """
        Adds a new educational program to the institution.
        
        Args:
            program (str): The name of the program to be added.
        
        Raises:
            ValueError: If the program is already in the list of programs.
        """
        if program in self.programs:
            raise ValueError(f"The program '{program}' is already offered.")
        self.programs.append(program)

    def get_description(self):
        """
        Returns a description of the institution including its programs and values.
        
        Returns:
            str: A formatted description of the institution.
        """
        description = f"{self.name} is a bilingual educational institution located in {self.location}.\n"
        description += "We offer programs from initial education to high school, including:\n"
        description += ", ".join(self.programs) + ".\n"
        description += "Our core values include: " + ", ".join(self.values) + "."
        return description


# Example usage
if __name__ == "__main__":
    try:
        institution = BilingualEducationalInstitution("Escuela Bilingüe Quito", "Quito, Ecuador")
        institution.add_program("Initial Education")
        institution.add_program("Primary Education")
        institution.add_program("Secondary Education")
        
        # Print the description of the institution
        print(institution.get_description())
    except Exception as e:
        print(f"An error occurred: {e}")
```
