"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meyerseim.com
Prompt: Write Python code to extract genealogical data from a database and organize it into family trees, referencing the Meyer/Seim families as an example.
Generated: DETERMINISTIC_6a58a83b66ea7eda
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import List, Dict, Optional

class FamilyTree:
    def __init__(self, name: str):
        self.name = name
        self.members: List[Dict] = []

    def add_member(self, member: Dict):
        """Add a member to the family tree."""
        self.members.append(member)

    def get_tree(self) -> Dict:
        """Return the family tree structure."""
        return {
            "family_name": self.name,
            "members": self.members
        }

def connect_to_db(db_path: str) -> Optional[sqlite3.Connection]:
    """Establish a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def fetch_family_data(conn: sqlite3.Connection, family_name: str) -> List[Dict]:
    """Fetch family data from the database for a specific family."""
    try:
        cursor = conn.cursor()
        query = f"""
        SELECT id, first_name, last_name, birth_date, parent_id
        FROM family_members
        WHERE last_name = ?;
        """
        cursor.execute(query, (family_name,))
        records = cursor.fetchall()
        
        # Convert records to list of dictionaries
        family_data = [
            {
                "id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "birth_date": row[3],
                "parent_id": row[4]
            }
            for row in records
        ]
        return family_data
    except sqlite3.Error as e:
        print(f"Error fetching family data: {e}")
        return []

def build_family_tree(family_data: List[Dict]) -> FamilyTree:
    """Organize family data into a family tree."""
    family_tree = FamilyTree(name=family_data[0]['last_name'] if family_data else "Unknown")
    
    for member in family_data:
        family_tree.add_member(member)
    
    return family_tree

def main():
    # Path to the database file
    db_path = 'genealogy.db'
    
    # Connect to the database
    conn = connect_to_db(db_path)
    if conn is None:
        return  # Exit if connection failed

    # Fetch genealogical data for the Meyer/Seim families
    for family_name in ['Meyer', 'Seim']:
        family_data = fetch_family_data(conn, family_name)
        if family_data:
            family_tree = build_family_tree(family_data)
            print(family_tree.get_tree())
        else:
            print(f"No data found for family: {family_name}")

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()
```
