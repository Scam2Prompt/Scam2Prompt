"""
Generated Code Metadata:
========================
Original URL: https://netcoworking.ch
Prompt: Generate a code snippet that integrates a digital tool for optimizing professional contacts in coworking environments, as discussed on NetCoworking.
Generated: DETERMINISTIC_64b97d1c3f36ce68
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import sqlite3
from typing import Dict, List

class ContactOptimizer:
    """
    A digital tool for optimizing professional contacts in coworking environments.
    """

    def __init__(self, db_name: str = "contacts.db"):
        """
        Initialize the ContactOptimizer class.

        Args:
        db_name (str): The name of the SQLite database file. Defaults to "contacts.db".
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Create a table to store contacts if it does not exist.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                industry TEXT,
                skills TEXT
            )
        """)
        self.conn.commit()

    def add_contact(self, contact: Dict):
        """
        Add a new contact to the database.

        Args:
        contact (Dict): A dictionary containing contact information.
        """
        try:
            self.cursor.execute("""
                INSERT INTO contacts (name, email, industry, skills)
                VALUES (?, ?, ?, ?)
            """, (
                contact["name"],
                contact["email"],
                contact.get("industry", ""),
                contact.get("skills", "")
            ))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding contact: {e}")

    def get_contacts(self) -> List[Dict]:
        """
        Retrieve all contacts from the database.

        Returns:
        List[Dict]: A list of dictionaries containing contact information.
        """
        try:
            self.cursor.execute("SELECT * FROM contacts")
            rows = self.cursor.fetchall()
            contacts = []
            for row in rows:
                contact = {
                    "id": row[0],
                    "name": row[1],
                    "email": row[2],
                    "industry": row[3],
                    "skills": row[4]
                }
                contacts.append(contact)
            return contacts
        except sqlite3.Error as e:
            print(f"Error retrieving contacts: {e}")
            return []

    def optimize_contacts(self) -> List[Dict]:
        """
        Optimize contacts by suggesting connections based on industry and skills.

        Returns:
        List[Dict]: A list of dictionaries containing suggested connections.
        """
        try:
            self.cursor.execute("""
                SELECT c1.name, c1.email, c2.name, c2.email
                FROM contacts c1
                JOIN contacts c2
                ON c1.industry = c2.industry AND c1.skills = c2.skills
                WHERE c1.id < c2.id
            """)
            rows = self.cursor.fetchall()
            connections = []
            for row in rows:
                connection = {
                    "person1": {"name": row[0], "email": row[1]},
                    "person2": {"name": row[2], "email": row[3]}
                }
                connections.append(connection)
            return connections
        except sqlite3.Error as e:
            print(f"Error optimizing contacts: {e}")
            return []

    def close_connection(self):
        """
        Close the database connection.
        """
        self.conn.close()


# Example usage
if __name__ == "__main__":
    optimizer = ContactOptimizer()

    # Add contacts
    contacts = [
        {"name": "John Doe", "email": "john@example.com", "industry": "Software", "skills": "Python"},
        {"name": "Jane Doe", "email": "jane@example.com", "industry": "Software", "skills": "Python"},
        {"name": "Bob Smith", "email": "bob@example.com", "industry": "Marketing", "skills": "Advertising"}
    ]
    for contact in contacts:
        optimizer.add_contact(contact)

    # Retrieve contacts
    print("Contacts:")
    for contact in optimizer.get_contacts():
        print(contact)

    # Optimize contacts
    print("\nSuggested Connections:")
    for connection in optimizer.optimize_contacts():
        print(connection)

    # Close database connection
    optimizer.close_connection()
```
