"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aveaorg.com
Prompt: Generate code for a vocational education partnership management system that facilitates collaboration between schools and international organizations, inspired by AVEA's joint education programs.
Generated: DETERMINISTIC_d1a898b7ab869762
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# vocational_education_partnership.py

class Partnership:
    """
    Class representing a vocational education partnership between a school and an international organization.
    """
    
    def __init__(self, school_name, organization_name, program_details):
        """
        Initialize the partnership with school and organization details.

        Parameters:
        school_name (str): Name of the school
        organization_name (str): Name of the international organization
        program_details (str): Details about the joint education program
        """
        self.school_name = school_name
        self.organization_name = organization_name
        self.program_details = program_details
        self.partnership_id = self.generate_id()

    def generate_id(self):
        """
        Generate a unique partnership ID.

        Returns:
        str: Unique partnership ID
        """
        import uuid
        return str(uuid.uuid4())

    def __repr__(self):
        """
        String representation of the Partnership object.

        Returns:
        str: Summary of the partnership
        """
        return f"Partnership({self.school_name}, {self.organization_name}, {self.program_details})"


class PartnershipManager:
    """
    Class to manage multiple vocational education partnerships.
    """
    
    def __init__(self):
        """
        Initialize the PartnershipManager with an empty list of partnerships.
        """
        self.partnerships = []

    def add_partnership(self, school_name, organization_name, program_details):
        """
        Add a new partnership to the list.

        Parameters:
        school_name (str): Name of the school
        organization_name (str): Name of the international organization
        program_details (str): Details about the joint education program
        
        Raises:
        ValueError: If any of the parameters are empty
        """
        if not school_name or not organization_name or not program_details:
            raise ValueError("School name, organization name, and program details cannot be empty.")
            
        partnership = Partnership(school_name, organization_name, program_details)
        self.partnerships.append(partnership)

    def remove_partnership(self, partnership_id):
        """
        Remove a partnership from the list by partnership ID.

        Parameters:
        partnership_id (str): Unique ID of the partnership to remove
        
        Raises:
        ValueError: If the partnership ID does not exist
        """
        for partnership in self.partnerships:
            if partnership.partnership_id == partnership_id:
                self.partnerships.remove(partnership)
                return
        raise ValueError(f"Partnership ID {partnership_id} not found.")

    def get_partnerships(self):
        """
        Retrieve the list of all partnerships.

        Returns:
        list: List of partnerships
        """
        return self.partnerships

    def find_partnership_by_school(self, school_name):
        """
        Find all partnerships associated with a specific school.

        Parameters:
        school_name (str): Name of the school to search for
        
        Returns:
        list: List of partnerships that match the school name
        """
        return [partnership for partnership in self.partnerships if partnership.school_name == school_name]


# Example usage
if __name__ == "__main__":
    try:
        manager = PartnershipManager()
        manager.add_partnership("Springfield High", "AVEA International", "Joint vocational training program.")
        manager.add_partnership("Shelbyville High", "Global Education Org", "Skill development workshops.")
        
        print("Current Partnerships:")
        for partnership in manager.get_partnerships():
            print(partnership)

        # Remove a partnership
        print("\nRemoving a partnership...")
        partnership_id_to_remove = manager.partnerships[0].partnership_id
        manager.remove_partnership(partnership_id_to_remove)

        print("\nPartnerships after removal:")
        for partnership in manager.get_partnerships():
            print(partnership)

    except Exception as e:
        print(f"An error occurred: {e}")
```
