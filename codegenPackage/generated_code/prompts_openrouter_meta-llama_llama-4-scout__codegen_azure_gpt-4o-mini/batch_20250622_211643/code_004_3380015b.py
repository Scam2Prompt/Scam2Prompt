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
from typing import List, Optional, Dict
from dataclasses import dataclass, field

@dataclass
class Person:
    """Class to represent a person in the family tree."""
    id: int
    name: str
    birth_year: Optional[int] = None
    death_year: Optional[int] = None
    parents: List['Person'] = field(default_factory=list)
    children: List['Person'] = field(default_factory=list)

    def add_parent(self, parent: 'Person') -> None:
        """Add a parent to the person."""
        if parent not in self.parents:
            self.parents.append(parent)
            parent.children.append(self)

    def add_child(self, child: 'Person') -> None:
        """Add a child to the person."""
        if child not in self.children:
            self.children.append(child)
            child.parents.append(self)

    def get_age(self, current_year: Optional[int] = None) -> Optional[int]:
        """Calculate the age of the person based on the current year."""
        if current_year is None:
            from datetime import datetime
            current_year = datetime.now().year
        if self.death_year:
            return self.death_year - self.birth_year
        return current_year - self.birth_year if self.birth_year else None

@dataclass
class FamilyTree:
    """Class to represent a family tree containing multiple people."""
    people: Dict[int, Person] = field(default_factory=dict)

    def add_person(self, person: Person) -> None:
        """Add a person to the family tree."""
        if person.id in self.people:
            raise ValueError(f"Person with ID {person.id} already exists.")
        self.people[person.id] = person

    def find_person(self, person_id: int) -> Optional[Person]:
        """Find a person by their ID."""
        return self.people.get(person_id)

    def get_family_relationships(self, person_id: int) -> Dict[str, List[str]]:
        """Get family relationships for a given person."""
        person = self.find_person(person_id)
        if not person:
            raise ValueError(f"Person with ID {person_id} not found.")
        
        relationships = {
            "parents": [parent.name for parent in person.parents],
            "children": [child.name for child in person.children]
        }
        return relationships

# Example usage
if __name__ == "__main__":
    # Create a family tree
    family_tree = FamilyTree()

    # Create some people
    alice = Person(id=1, name="Alice", birth_year=1980)
    bob = Person(id=2, name="Bob", birth_year=1975)
    charlie = Person(id=3, name="Charlie", birth_year=2005)

    # Add people to the family tree
    family_tree.add_person(alice)
    family_tree.add_person(bob)
    family_tree.add_person(charlie)

    # Establish relationships
    alice.add_child(charlie)
    bob.add_child(charlie)

    # Get family relationships
    relationships = family_tree.get_family_relationships(3)
    print(relationships)  # Output: {'parents': ['Alice', 'Bob'], 'children': []}
```
