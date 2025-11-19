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
from datetime import date
from typing import List, Optional

class Person:
    """Represents an individual in the genealogical data model."""

    def __init__(self, 
                 id: int, 
                 first_name: str, 
                 last_name: str, 
                 birth_date: Optional[date] = None, 
                 death_date: Optional[date] = None):
        """
        Initializes a Person object.

        Args:
        id (int): Unique identifier for the person.
        first_name (str): First name of the person.
        last_name (str): Last name of the person.
        birth_date (Optional[date]): Birth date of the person. Defaults to None.
        death_date (Optional[date]): Death date of the person. Defaults to None.
        """
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.death_date = death_date
        self.spouse: Optional[Person] = None
        self.children: List[Person] = []
        self.parents: List[Person] = []

    def add_spouse(self, spouse: 'Person'):
        """Sets the spouse of the person."""
        self.spouse = spouse

    def add_child(self, child: 'Person'):
        """Adds a child to the person's children."""
        self.children.append(child)

    def add_parent(self, parent: 'Person'):
        """Adds a parent to the person's parents."""
        self.parents.append(parent)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class FamilyTree:
    """Represents a family tree data structure."""

    def __init__(self):
        """Initializes an empty family tree."""
        self.people: dict[int, Person] = {}

    def add_person(self, person: Person):
        """Adds a person to the family tree."""
        self.people[person.id] = person

    def get_person(self, id: int) -> Optional[Person]:
        """Retrieves a person from the family tree by ID."""
        return self.people.get(id)

    def add_relationship(self, parent_id: int, child_id: int):
        """
        Establishes a parent-child relationship between two people.

        Args:
        parent_id (int): ID of the parent.
        child_id (int): ID of the child.

        Raises:
        ValueError: If either parent or child is not in the family tree.
        """
        parent = self.get_person(parent_id)
        child = self.get_person(child_id)
        if parent is None or child is None:
            raise ValueError("Both parent and child must exist in the family tree.")
        parent.add_child(child)
        child.add_parent(parent)

    def add_spouse_relationship(self, person1_id: int, person2_id: int):
        """
        Establishes a spouse relationship between two people.

        Args:
        person1_id (int): ID of the first person.
        person2_id (int): ID of the second person.

        Raises:
        ValueError: If either person is not in the family tree.
        """
        person1 = self.get_person(person1_id)
        person2 = self.get_person(person2_id)
        if person1 is None or person2 is None:
            raise ValueError("Both people must exist in the family tree.")
        person1.add_spouse(person2)
        person2.add_spouse(person1)


# Example usage
if __name__ == "__main__":
    tree = FamilyTree()

    person1 = Person(1, "John", "Doe", date(1990, 1, 1))
    person2 = Person(2, "Jane", "Doe", date(1995, 6, 15))
    person3 = Person(3, "Jim", "Doe", date(1960, 3, 10))

    tree.add_person(person1)
    tree.add_person(person2)
    tree.add_person(person3)

    tree.add_relationship(3, 1)
    tree.add_relationship(3, 2)
    tree.add_spouse_relationship(1, 2)

    print(person1.first_name)  # John
    print(person1.spouse.first_name)  # Jane
    print([child.first_name for child in person3.children])  # ['John', 'Jane']
```
