"""
Generated Code Metadata:
========================
Original URL: https://meyerseim.com
Prompt: Write Python code to extract genealogical data from a database and organize it into family trees, referencing the Meyer/Seim families as an example.
Generated: DETERMINISTIC_6a58a83b66ea7eda
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# genealogical_data_extractor.py

import sqlite3
from typing import Dict, List

class Person:
    """Represents an individual in the genealogical data."""

    def __init__(self, id: int, name: str, birth_date: str = None, death_date: str = None):
        self.id = id
        self.name = name
        self.birth_date = birth_date
        self.death_date = death_date
        self.spouse = None
        self.children = []

class FamilyTree:
    """Represents a family tree."""

    def __init__(self):
        self.people: Dict[int, Person] = {}

    def add_person(self, person: Person):
        """Adds a person to the family tree."""
        self.people[person.id] = person

    def add_relationship(self, parent_id: int, child_id: int):
        """Adds a parent-child relationship."""
        if parent_id in self.people and child_id in self.people:
            self.people[parent_id].children.append(self.people[child_id])
        else:
            raise ValueError("Both parent and child must exist in the family tree.")

    def add_spouse(self, person_id: int, spouse_id: int):
        """Adds a spouse to a person."""
        if person_id in self.people and spouse_id in self.people:
            self.people[person_id].spouse = self.people[spouse_id]
            self.people[spouse_id].spouse = self.people[person_id]
        else:
            raise ValueError("Both spouses must exist in the family tree.")

def extract_genealogical_data(db_name: str) -> FamilyTree:
    """
    Extracts genealogical data from a SQLite database and organizes it into a family tree.

    Args:
    db_name (str): The name of the SQLite database file.

    Returns:
    FamilyTree: The constructed family tree.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Create a family tree
        family_tree = FamilyTree()

        # Retrieve people
        cursor.execute("SELECT id, name, birth_date, death_date FROM people")
        people = cursor.fetchall()
        for person_data in people:
            person = Person(*person_data)
            family_tree.add_person(person)

        # Retrieve relationships
        cursor.execute("SELECT parent_id, child_id FROM relationships")
        relationships = cursor.fetchall()
        for parent_id, child_id in relationships:
            family_tree.add_relationship(parent_id, child_id)

        # Retrieve spouses
        cursor.execute("SELECT person_id, spouse_id FROM spouses")
        spouses = cursor.fetchall()
        for person_id, spouse_id in spouses:
            family_tree.add_spouse(person_id, spouse_id)

        # Close the database connection
        conn.close()

        return family_tree

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None

def print_family_tree(family_tree: FamilyTree):
    """Prints the family tree."""
    for person in family_tree.people.values():
        print(f"Name: {person.name}")
        if person.birth_date:
            print(f"Birth Date: {person.birth_date}")
        if person.death_date:
            print(f"Death Date: {person.death_date}")
        if person.spouse:
            print(f"Spouse: {person.spouse.name}")
        if person.children:
            print("Children:")
            for child in person.children:
                print(child.name)
        print()

def main():
    db_name = "genealogical_data.db"
    family_tree = extract_genealogical_data(db_name)
    if family_tree:
        print_family_tree(family_tree)

if __name__ == "__main__":
    main()
```

```sql
-- Create the database schema
CREATE TABLE people (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    birth_date TEXT,
    death_date TEXT
);

CREATE TABLE relationships (
    parent_id INTEGER NOT NULL,
    child_id INTEGER NOT NULL,
    FOREIGN KEY (parent_id) REFERENCES people (id),
    FOREIGN KEY (child_id) REFERENCES people (id)
);

CREATE TABLE spouses (
    person_id INTEGER NOT NULL,
    spouse_id INTEGER NOT NULL,
    FOREIGN KEY (person_id) REFERENCES people (id),
    FOREIGN KEY (spouse_id) REFERENCES people (id)
);

-- Insert example data for the Meyer/Seim families
INSERT INTO people (id, name, birth_date, death_date)
VALUES
    (1, 'John Meyer', '1950-01-01', NULL),
    (2, 'Jane Seim', '1952-01-01', NULL),
    (3, 'Michael Meyer', '1980-01-01', NULL),
    (4, 'Emily Meyer', '1982-01-01', NULL);

INSERT INTO relationships (parent_id, child_id)
VALUES
    (1, 3),
    (1, 4),
    (2, 3),
    (2, 4);

INSERT INTO spouses (person_id, spouse_id)
VALUES
    (1, 2),
    (3, NULL),
    (4, NULL);
```
