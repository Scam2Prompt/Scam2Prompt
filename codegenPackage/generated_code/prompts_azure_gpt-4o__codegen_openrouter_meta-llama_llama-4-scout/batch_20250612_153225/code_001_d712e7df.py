"""
Generated Code Metadata:
========================
Original URL: https://kimiyashimi.com
Prompt: Generate a script that uses the SDS (Safety Data Sheet) information to create a database for tracking chemical properties, hazards, and storage guidelines, referencing Kimia Shimi's emphasis on SDS documentation.
Generated: DETERMINISTIC_d712e7dfc4e9b97f
Batch ID: 20250612_153225
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
from typing import Dict

class ChemicalDatabase:
    def __init__(self, db_name: str):
        """
        Initialize a chemical database.

        Args:
        db_name (str): The name of the database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create tables for chemicals, hazards, and storage guidelines.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS chemicals
            (id INTEGER PRIMARY KEY, name TEXT NOT NULL, cas_number TEXT UNIQUE)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS hazards
            (id INTEGER PRIMARY KEY, chemical_id INTEGER, hazard_statement TEXT,
            precautionary_statement TEXT, FOREIGN KEY (chemical_id) REFERENCES chemicals (id))
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS storage_guidelines
            (id INTEGER PRIMARY KEY, chemical_id INTEGER, storage_condition TEXT,
            handling_procedure TEXT, FOREIGN KEY (chemical_id) REFERENCES chemicals (id))
        ''')

        self.conn.commit()

    def add_chemical(self, name: str, cas_number: str, hazards: Dict[str, str], storage_guidelines: Dict[str, str]):
        """
        Add a chemical to the database.

        Args:
        name (str): The name of the chemical.
        cas_number (str): The CAS number of the chemical.
        hazards (Dict[str, str]): A dictionary of hazard statements and precautionary statements.
        storage_guidelines (Dict[str, str]): A dictionary of storage conditions and handling procedures.
        """
        try:
            self.cursor.execute('INSERT INTO chemicals (name, cas_number) VALUES (?, ?)', (name, cas_number))
            chemical_id = self.cursor.lastrowid

            for hazard_statement, precautionary_statement in hazards.items():
                self.cursor.execute('INSERT INTO hazards (chemical_id, hazard_statement, precautionary_statement) VALUES (?, ?, ?)',
                                    (chemical_id, hazard_statement, precautionary_statement))

            for storage_condition, handling_procedure in storage_guidelines.items():
                self.cursor.execute('INSERT INTO storage_guidelines (chemical_id, storage_condition, handling_procedure) VALUES (?, ?, ?)',
                                    (chemical_id, storage_condition, handling_procedure))

            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding chemical: {e}")

    def get_chemical(self, cas_number: str):
        """
        Get a chemical from the database.

        Args:
        cas_number (str): The CAS number of the chemical.

        Returns:
        A dictionary containing the chemical's information.
        """
        try:
            self.cursor.execute('SELECT * FROM chemicals WHERE cas_number = ?', (cas_number,))
            chemical = self.cursor.fetchone()

            if chemical:
                chemical_id = chemical[0]
                hazards = self.get_hazards(chemical_id)
                storage_guidelines = self.get_storage_guidelines(chemical_id)

                return {
                    'name': chemical[1],
                    'cas_number': chemical[2],
                    'hazards': hazards,
                    'storage_guidelines': storage_guidelines
                }
            else:
                return None
        except sqlite3.Error as e:
            print(f"Error getting chemical: {e}")

    def get_hazards(self, chemical_id: int):
        """
        Get the hazards for a chemical.

        Args:
        chemical_id (int): The ID of the chemical.

        Returns:
        A dictionary of hazard statements and precautionary statements.
        """
        try:
            self.cursor.execute('SELECT hazard_statement, precautionary_statement FROM hazards WHERE chemical_id = ?', (chemical_id,))
            hazards = self.cursor.fetchall()

            return {hazard[0]: hazard[1] for hazard in hazards}
        except sqlite3.Error as e:
            print(f"Error getting hazards: {e}")

    def get_storage_guidelines(self, chemical_id: int):
        """
        Get the storage guidelines for a chemical.

        Args:
        chemical_id (int): The ID of the chemical.

        Returns:
        A dictionary of storage conditions and handling procedures.
        """
        try:
            self.cursor.execute('SELECT storage_condition, handling_procedure FROM storage_guidelines WHERE chemical_id = ?', (chemical_id,))
            storage_guidelines = self.cursor.fetchall()

            return {guideline[0]: guideline[1] for guideline in storage_guidelines}
        except sqlite3.Error as e:
            print(f"Error getting storage guidelines: {e}")

    def close(self):
        """
        Close the database connection.
        """
        self.conn.close()


def main():
    db = ChemicalDatabase('chemical_database.db')

    # Example usage:
    chemical_name = 'Example Chemical'
    cas_number = '1234-56-7'
    hazards = {
        'Hazard Statement 1': 'Precautionary Statement 1',
        'Hazard Statement 2': 'Precautionary Statement 2'
    }
    storage_guidelines = {
        'Storage Condition 1': 'Handling Procedure 1',
        'Storage Condition 2': 'Handling Procedure 2'
    }

    db.add_chemical(chemical_name, cas_number, hazards, storage_guidelines)

    chemical = db.get_chemical(cas_number)
    print(chemical)

    db.close()


if __name__ == '__main__':
    main()
```
