"""
Generated Code Metadata:
========================
Original URL: https://gra-pro-canv.webflow.io
Prompt: "Create a template for a grants program playbook, including sections for understanding roles and responsibilities, and planning disbursements."
Generated: DETERMINISTIC_f45d2b31ff15c702
Batch ID: 20250622_212142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Grants Program Playbook Template

This template provides a structured approach to managing a grants program,
including defining roles and responsibilities, and planning disbursements.
"""

class GrantsProgramPlaybook:
    """
    A template for creating a grants program playbook.
    """

    def __init__(self, program_name):
        """
        Initialize the playbook with a program name.
        
        Args:
            program_name (str): The name of the grants program.
        """
        self.program_name = program_name
        self.roles_responsibilities = {}
        self.disbursement_plan = {}
        self.other_sections = {}

    def add_roles_responsibilities(self, role, responsibilities):
        """
        Add roles and their corresponding responsibilities to the playbook.
        
        Args:
            role (str): The name of the role (e.g., "Program Manager").
            responsibilities (list): List of responsibilities for the role.
            
        Raises:
            ValueError: If role is empty or responsibilities list is empty.
        """
        if not role or not responsibilities:
            raise ValueError("Role and responsibilities cannot be empty.")
        
        if not isinstance(responsibilities, list):
            raise ValueError("Responsibilities must be provided as a list.")
            
        self.roles_responsibilities[role] = responsibilities

    def add_disbursement_plan(self, phase, tasks):
        """
        Add a disbursement phase with associated tasks.
        
        Args:
            phase (str): The name of the disbursement phase (e.g., "Initial Disbursement").
            tasks (list): List of tasks to complete in this phase.
            
        Raises:
            ValueError: If phase is empty or tasks list is empty.
        """
        if not phase or not tasks:
            raise ValueError("Phase and tasks cannot be empty.")
            
        if not isinstance(tasks, list):
            raise ValueError("Tasks must be provided as a list.")
            
        self.disbursement_plan[phase] = tasks

    def add_section(self, section_name, content):
        """
        Add an additional custom section to the playbook.
        
        Args:
            section_name (str): The name of the section.
            content (str/dict/list): The content for the section.
            
        Raises:
            ValueError: If section_name is empty.
        """
        if not section_name:
            raise ValueError("Section name cannot be empty.")
            
        self.other_sections[section_name] = content

    def generate_playbook(self):
        """
        Generate the complete playbook structure as a dictionary.
        
        Returns:
            dict: The complete playbook structure.
        """
        playbook = {
            "program_name": self.program_name,
            "roles_and_responsibilities": self.roles_responsibilities,
            "disbursement_plan": self.disbursement_plan,
            "additional_sections": self.other_sections
        }
        return playbook

# Example usage
if __name__ == "__main__":
    try:
        # Initialize playbook
        playbook = GrantsProgramPlaybook("Community Development Grants")
        
        # Add roles and responsibilities
        playbook.add_roles_responsibilities(
            "Program Manager",
            ["Oversee program execution", "Coordinate with stakeholders", "Monitor grantee performance"]
        )
        
        playbook.add_roles_responsibilities(
            "Finance Officer",
            ["Manage disbursements", "Track budgets", "Prepare financial reports"]
        )
        
        # Add disbursement plan
        playbook.add_disbursement_plan(
            "Initial Disbursement",
            ["Review applications", "Verify eligibility", "Transfer first 30% of funds"]
        )
        
        playbook.add_disbursement_plan(
            "Final Disbursement",
            ["Review progress reports", "Verify deliverables", "Transfer remaining funds"]
        )
        
        # Add additional section
        playbook.add_section(
            "Evaluation Criteria",
            ["Impact potential", "Feasibility", "Sustainability"]
        )
        
        # Generate and print playbook
        print(playbook.generate_playbook())
        
    except ValueError as e:
        print(f"Error creating playbook: {e}")
```
