"""
Generated Code Metadata:
========================
Original URL: https://meyerseim.com
Prompt: Design a data model to represent family relationships and genealogical information, taking into account the collection of over 4000 people mentioned on the website.
Generated: DETERMINISTIC_3380015ba127854c
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Optional
import uuid


class Person:
    """
    Represents an individual in the family tree.
    """
    def __init__(self, first_name: str, last_name: str, birth_date: Optional[str] = None, death_date: Optional[str] = None):
        self.id = str(uuid.uuid4())  # Unique identifier for the person
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date  # Format: YYYY-MM-DD
        self.death_date = death_date  # Format: YYYY-MM-DD
        self.parents: List['Person'] = []  # List of parent objects
        self.children: List['Person'] = []  # List of child objects
        self.spouse: Optional['Person'] = None  # Spouse object (if any)

    def add_parent(self, parent: 'Person'):
        """
        Adds a parent to the person's parent list.
        """
        if len(self.parents) >= 2:
            raise ValueError("A person cannot have more than two parents.")
        self.parents.append(parent)
        parent.children.append(self)  # Automatically add this person as a child of the parent

    def add_child(self, child: 'Person'):
        """
        Adds a child to the person's child list.
        """
        self.children.append(child)
        child.add_parent(self)  # Automatically add this person as a parent of the child

    def set_spouse(self, spouse: 'Person'):
        """
        Sets the spouse for the person.
        """
        if self.spouse is not None:
            raise ValueError(f"{self.first_name} {self.last_name} is already married.")
        self.spouse = spouse
        spouse.spouse = self  # Automatically set this person as the spouse of the other person

    def __repr__(self):
        return f"Person({self.first_name} {self.last_name}, ID: {self.id})"


class FamilyTree:
    """
    Represents the entire family tree.
    """
    def __init__(self):
        self.members: List[Person] = []  # List of all people in the family tree

    def add_member(self, person: Person):
        """
        Adds a person to the family tree.
        """
        self.members.append(person)

    def find_person_by_id(self, person_id: str) -> Optional[Person]:
        """
        Finds a person in the family tree by their unique ID.
        """
        for member in self.members:
            if member.id == person_id:
                return member
        return None

    def find_person_by_name(self, first_name: str, last_name: str) -> List[Person]:
        """
        Finds all people in the family tree with the given name.
        """
        return [member for member in self.members if member.first_name == first_name and member.last_name == last_name]

    def __repr__(self):
        return f"FamilyTree({len(self.members)} members)"


# Example usage:
if __name__ == "__main__":
    try:
        # Create family tree
        family_tree = FamilyTree()

        # Create individuals
        john = Person("John", "Doe", "1980-01-01")
        jane = Person("Jane", "Smith", "1985-05-15")
        child = Person("Baby", "Doe", "2010-06-20")

        # Add members to the family tree
        family_tree.add_member(john)
        family_tree.add_member(jane)
        family_tree.add_member(child)

        # Establish relationships
        john.set_spouse(jane)
        john.add_child(child)

        # Print family tree details
        print(family_tree)
        print(john)
        print(jane)
        print(child)

    except Exception as e:
        print(f"Error: {e}")
```
