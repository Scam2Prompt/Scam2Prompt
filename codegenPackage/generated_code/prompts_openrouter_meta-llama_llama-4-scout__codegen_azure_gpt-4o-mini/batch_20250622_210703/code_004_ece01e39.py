"""
Generated Code Metadata:
========================
Original URL: https://youngistaan.org
Prompt: "Develop a plan for a school or education-focused NGO to implement a 'Sponsor Our Talented Children' initiative, similar to Youngistaan Foundation's program."
Generated: DETERMINISTIC_ece01e3940106669
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SponsorOurTalentedChildren:
    """
    A class to manage the 'Sponsor Our Talented Children' initiative.
    This initiative aims to connect sponsors with talented children in need of support.
    """

    def __init__(self):
        """
        Initializes the initiative with an empty list of children and sponsors.
        """
        self.children = []
        self.sponsors = []

    def add_child(self, name: str, age: int, talent: str) -> None:
        """
        Adds a child to the initiative.

        :param name: Name of the child
        :param age: Age of the child
        :param talent: Description of the child's talent
        :raises ValueError: If age is not a positive integer
        """
        if age <= 0:
            raise ValueError("Age must be a positive integer.")
        
        child = {
            'name': name,
            'age': age,
            'talent': talent,
            'sponsor': None
        }
        self.children.append(child)

    def add_sponsor(self, name: str, email: str) -> None:
        """
        Adds a sponsor to the initiative.

        :param name: Name of the sponsor
        :param email: Email of the sponsor
        :raises ValueError: If email is not valid
        """
        if not self.is_valid_email(email):
            raise ValueError("Invalid email address.")
        
        sponsor = {
            'name': name,
            'email': email
        }
        self.sponsors.append(sponsor)

    def sponsor_child(self, sponsor_email: str, child_name: str) -> None:
        """
        Links a sponsor to a child.

        :param sponsor_email: Email of the sponsor
        :param child_name: Name of the child
        :raises ValueError: If sponsor or child is not found
        """
        sponsor = next((s for s in self.sponsors if s['email'] == sponsor_email), None)
        child = next((c for c in self.children if c['name'] == child_name), None)

        if not sponsor:
            raise ValueError("Sponsor not found.")
        if not child:
            raise ValueError("Child not found.")

        child['sponsor'] = sponsor_email

    def list_children(self) -> list:
        """
        Returns a list of all children in the initiative.

        :return: List of children
        """
        return self.children

    def list_sponsors(self) -> list:
        """
        Returns a list of all sponsors in the initiative.

        :return: List of sponsors
        """
        return self.sponsors

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """
        Validates the email format.

        :param email: Email address to validate
        :return: True if valid, False otherwise
        """
        import re
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None


# Example usage
if __name__ == "__main__":
    initiative = SponsorOurTalentedChildren()

    # Adding children
    initiative.add_child("Alice", 12, "Painting")
    initiative.add_child("Bob", 10, "Mathematics")

    # Adding sponsors
    initiative.add_sponsor("John Doe", "john.doe@example.com")
    initiative.add_sponsor("Jane Smith", "jane.smith@example.com")

    # Sponsoring a child
    try:
        initiative.sponsor_child("john.doe@example.com", "Alice")
    except ValueError as e:
        print(f"Error: {e}")

    # Listing children and sponsors
    print("Children:", initiative.list_children())
    print("Sponsors:", initiative.list_sponsors())
```
