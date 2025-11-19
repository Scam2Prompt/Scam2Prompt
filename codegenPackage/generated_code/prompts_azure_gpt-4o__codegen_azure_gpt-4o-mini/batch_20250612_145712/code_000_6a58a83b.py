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
import sqlite3
from typing import List, Dict, Any

class FamilyTree:
    def __init__(self, family_name: str):
        self.family_name = family_name
        self.members = []

    def add_member(self, member: Dict[str, Any]):
        """Add a member to the family tree."""
        self.members.append(member)

    def __repr__(self):
        return f"FamilyTree(family_name={self.family_name}, members={self.members})"

def connect_to_database(db_path: str) -> sqlite3.Connection:
    """Establish a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        raise

def fetch_family_data(conn: sqlite3.Connection, family_name: str) -> List[Dict[str, Any]]:
    """Fetch family data from the database for a specific family."""
    try:
        cursor = conn.cursor()
        query = """
        SELECT id, first_name, last_name, birth_date, parent_id
        FROM family_members
        WHERE last_name IN (?, ?)
        """
        cursor.execute(query, (family_name.split('/')[0], family_name.split('/')[1]))
        rows = cursor.fetchall()
        return [{'id': row[0], 'first_name': row[1], 'last_name': row[2], 
                 'birth_date': row[3], 'parent_id': row[4]} for row in rows]
    except sqlite3.Error as e:
        print(f"Error fetching family data: {e}")
        raise
    finally:
        cursor.close()

def build_family_tree(members: List[Dict[str, Any]]) -> Dict[str, FamilyTree]:
    """Build family trees from the list of family members."""
    family_trees = {}
    
    for member in members:
        last_name = member['last_name']
        if last_name not in family_trees:
            family_trees[last_name] = FamilyTree(family_name=last_name)
        family_trees[last_name].add_member(member)
    
    return family_trees

def main():
    """Main function to execute the family tree extraction."""
    db_path = 'genealogy.db'  # Path to the SQLite database
    family_name = 'Meyer/Seim'  # Example family names

    # Connect to the database
    conn = connect_to_database(db_path)

    try:
        # Fetch family data
        members = fetch_family_data(conn, family_name)

        # Build family trees
        family_trees = build_family_tree(members)

        # Output the family trees
        for family_tree in family_trees.values():
            print(family_tree)
    finally:
        conn.close()  # Ensure the database connection is closed

if __name__ == "__main__":
    main()
```
