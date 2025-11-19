"""
Generated Code Metadata:
========================
Original URL: https://erasmusmais.pt
Prompt: What is the role of the Portuguese National Agency (AN-Erasmus+) in managing Erasmus+ programs in Portugal?
Generated: DETERMINISTIC_a3646d7f57bae1ac
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ErasmusPlusAgency:
    """
    A class to represent the Portuguese National Agency (AN-Erasmus+) 
    responsible for managing Erasmus+ programs in Portugal.
    """

    def __init__(self):
        """
        Initializes the ErasmusPlusAgency with default attributes.
        """
        self.programs = []
        self.partners = []

    def add_program(self, program_name: str, description: str) -> None:
        """
        Adds a new Erasmus+ program to the agency's list.

        Args:
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

    def add_partner(self, partner_name: str) -> None:
        """
        Adds a new partner organization to the agency's list.

        Args:
            partner_name (str): The name of the partner organization.

        Raises:
            ValueError: If the partner name is empty or already exists.
        """
        if not partner_name:
            raise ValueError("Partner name cannot be empty.")
        if partner_name in self.partners:
            raise ValueError("Partner already exists.")

        self.partners.append(partner_name)

    def get_programs(self) -> list:
        """
        Returns a list of all Erasmus+ programs managed by the agency.

        Returns:
            list: A list of dictionaries containing program names and descriptions.
        """
        return self.programs

    def get_partners(self) -> list:
        """
        Returns a list of all partner organizations associated with the agency.

        Returns:
            list: A list of partner organization names.
        """
        return self.partners

    def manage_program(self, program_name: str) -> str:
        """
        Manages a specific Erasmus+ program.

        Args:
            program_name (str): The name of the program to manage.

        Returns:
            str: A message indicating the management status of the program.

        Raises:
            ValueError: If the program does not exist.
        """
        if not any(program['name'] == program_name for program in self.programs):
            raise ValueError("Program does not exist.")

        # Simulate management actions
        return f"Managing program: {program_name}"

# Example usage
if __name__ == "__main__":
    agency = ErasmusPlusAgency()
    
    try:
        agency.add_program("Erasmus for All", "A program to support education and training.")
        agency.add_partner("University of Lisbon")
        
        print(agency.get_programs())
        print(agency.get_partners())
        
        print(agency.manage_program("Erasmus for All"))
    except ValueError as e:
        print(f"Error: {e}")
```
