"""
Generated Code Metadata:
========================
Original URL: https://nicerfoundation.org.ng
Prompt: Generate a Python script that connects a community organization with local schools to enhance literacy programs, inspired by the NICER Foundation's approach to education.
Generated: DETERMINISTIC_8d0461ff958906d3
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# literacy_connector.py

import sqlite3
from typing import Dict, List

class LiteracyConnector:
    """
    Connects community organizations with local schools to enhance literacy programs.

    Attributes:
        db_name (str): Name of the SQLite database file.
    """

    def __init__(self, db_name: str = "literacy_connector.db"):
        """
        Initializes the LiteracyConnector instance.

        Args:
            db_name (str): Name of the SQLite database file. Defaults to "literacy_connector.db".
        """
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Creates the necessary tables in the SQLite database.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS organizations (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                contact_info TEXT NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS schools (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                address TEXT NOT NULL,
                contact_info TEXT NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS literacy_programs (
                id INTEGER PRIMARY KEY,
                organization_id INTEGER NOT NULL,
                school_id INTEGER NOT NULL,
                program_name TEXT NOT NULL,
                program_description TEXT,
                FOREIGN KEY (organization_id) REFERENCES organizations (id),
                FOREIGN KEY (school_id) REFERENCES schools (id)
            )
        """)
        self.conn.commit()

    def add_organization(self, name: str, description: str, contact_info: str):
        """
        Adds a community organization to the database.

        Args:
            name (str): Name of the organization.
            description (str): Description of the organization.
            contact_info (str): Contact information of the organization.

        Returns:
            int: ID of the added organization.
        """
        try:
            self.cursor.execute("INSERT INTO organizations (name, description, contact_info) VALUES (?, ?, ?)", (name, description, contact_info))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding organization: {e}")
            return None

    def add_school(self, name: str, address: str, contact_info: str):
        """
        Adds a local school to the database.

        Args:
            name (str): Name of the school.
            address (str): Address of the school.
            contact_info (str): Contact information of the school.

        Returns:
            int: ID of the added school.
        """
        try:
            self.cursor.execute("INSERT INTO schools (name, address, contact_info) VALUES (?, ?, ?)", (name, address, contact_info))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding school: {e}")
            return None

    def add_literacy_program(self, organization_id: int, school_id: int, program_name: str, program_description: str):
        """
        Adds a literacy program to the database.

        Args:
            organization_id (int): ID of the community organization.
            school_id (int): ID of the local school.
            program_name (str): Name of the literacy program.
            program_description (str): Description of the literacy program.

        Returns:
            int: ID of the added literacy program.
        """
        try:
            self.cursor.execute("INSERT INTO literacy_programs (organization_id, school_id, program_name, program_description) VALUES (?, ?, ?, ?)", (organization_id, school_id, program_name, program_description))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding literacy program: {e}")
            return None

    def get_organizations(self) -> List[Dict]:
        """
        Retrieves a list of community organizations.

        Returns:
            List[Dict]: List of dictionaries containing organization information.
        """
        try:
            self.cursor.execute("SELECT * FROM organizations")
            rows = self.cursor.fetchall()
            return [{"id": row[0], "name": row[1], "description": row[2], "contact_info": row[3]} for row in rows]
        except sqlite3.Error as e:
            print(f"Error retrieving organizations: {e}")
            return []

    def get_schools(self) -> List[Dict]:
        """
        Retrieves a list of local schools.

        Returns:
            List[Dict]: List of dictionaries containing school information.
        """
        try:
            self.cursor.execute("SELECT * FROM schools")
            rows = self.cursor.fetchall()
            return [{"id": row[0], "name": row[1], "address": row[2], "contact_info": row[3]} for row in rows]
        except sqlite3.Error as e:
            print(f"Error retrieving schools: {e}")
            return []

    def get_literacy_programs(self) -> List[Dict]:
        """
        Retrieves a list of literacy programs.

        Returns:
            List[Dict]: List of dictionaries containing literacy program information.
        """
        try:
            self.cursor.execute("""
                SELECT lp.id, o.name AS organization_name, s.name AS school_name, lp.program_name, lp.program_description
                FROM literacy_programs lp
                JOIN organizations o ON lp.organization_id = o.id
                JOIN schools s ON lp.school_id = s.id
            """)
            rows = self.cursor.fetchall()
            return [{"id": row[0], "organization_name": row[1], "school_name": row[2], "program_name": row[3], "program_description": row[4]} for row in rows]
        except sqlite3.Error as e:
            print(f"Error retrieving literacy programs: {e}")
            return []

    def close_connection(self):
        """
        Closes the SQLite database connection.
        """
        self.conn.close()


def main():
    connector = LiteracyConnector()

    # Add community organizations
    org1_id = connector.add_organization("NICER Foundation", "A non-profit organization focused on education", "info@nicerfoundation.org")
    org2_id = connector.add_organization("Local Literacy Group", "A local group promoting literacy", "info@localliteracygroup.org")

    # Add local schools
    school1_id = connector.add_school("Springfield Elementary", "123 Main St, Springfield", "info@springfieldes.org")
    school2_id = connector.add_school("Lincoln High School", "456 Elm St, Lincoln", "info@lincolnhs.org")

    # Add literacy programs
    program1_id = connector.add_literacy_program(org1_id, school1_id, "Reading Buddies", "A program pairing students with reading buddies")
    program2_id = connector.add_literacy_program(org2_id, school2_id, "Literacy Workshops", "A program offering literacy workshops for students")

    # Retrieve and print community organizations
    organizations = connector.get_organizations()
    print("Community Organizations:")
    for org in organizations:
        print(org)

    # Retrieve and print local schools
    schools = connector.get_schools()
    print("\nLocal Schools:")
    for school in schools:
        print(school)

    # Retrieve and print literacy programs
    literacy_programs = connector.get_literacy_programs()
    print("\nLiteracy Programs:")
    for program in literacy_programs:
        print(program)

    connector.close_connection()


if __name__ == "__main__":
    main()
```
