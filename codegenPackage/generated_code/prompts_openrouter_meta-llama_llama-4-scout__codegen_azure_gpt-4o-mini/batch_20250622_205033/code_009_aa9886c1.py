"""
Generated Code Metadata:
========================
Original URL: https://metamask-extension-web3-dapps.blogspot.com
Prompt: How does BrasiliaFisio support the professional growth of physiotherapy practitioners?
Generated: DETERMINISTIC_aa9886c12fd82726
Batch ID: 20250622_205033
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BrasiliaFisio:
    """
    A class to represent the BrasiliaFisio organization and its support for the professional growth of physiotherapy practitioners.
    """

    def __init__(self):
        """
        Initializes the BrasiliaFisio instance with an empty list of programs.
        """
        self.programs = []

    def add_program(self, program_name, description):
        """
        Adds a professional growth program to the BrasiliaFisio organization.

        Parameters:
        program_name (str): The name of the program.
        description (str): A brief description of the program.

        Raises:
        ValueError: If the program name is empty or already exists.
        """
        if not program_name:
            raise ValueError("Program name cannot be empty.")
        if any(program['name'] == program_name for program in self.programs):
            raise ValueError("Program already exists.")

        self.programs.append({'name': program_name, 'description': description})

    def list_programs(self):
        """
        Lists all professional growth programs available at BrasiliaFisio.

        Returns:
        list: A list of dictionaries containing program names and descriptions.
        """
        return self.programs

    def find_program(self, program_name):
        """
        Finds a specific program by its name.

        Parameters:
        program_name (str): The name of the program to find.

        Returns:
        dict: The program details if found, otherwise None.
        """
        for program in self.programs:
            if program['name'] == program_name:
                return program
        return None

    def remove_program(self, program_name):
        """
        Removes a program from the BrasiliaFisio organization.

        Parameters:
        program_name (str): The name of the program to remove.

        Raises:
        ValueError: If the program does not exist.
        """
        program = self.find_program(program_name)
        if program is None:
            raise ValueError("Program does not exist.")

        self.programs.remove(program)

# Example usage
if __name__ == "__main__":
    try:
        brasilia_fisio = BrasiliaFisio()
        brasilia_fisio.add_program("Advanced Manual Therapy", "A program focused on advanced techniques in manual therapy.")
        brasilia_fisio.add_program("Sports Rehabilitation", "Training for physiotherapists specializing in sports injuries.")

        print("Available Programs:")
        for program in brasilia_fisio.list_programs():
            print(f"{program['name']}: {program['description']}")

        # Attempt to find a program
        program = brasilia_fisio.find_program("Advanced Manual Therapy")
        if program:
            print(f"Found Program: {program['name']} - {program['description']}")

        # Remove a program
        brasilia_fisio.remove_program("Sports Rehabilitation")
        print("Program 'Sports Rehabilitation' removed successfully.")

    except ValueError as e:
        print(f"Error: {e}")
```
