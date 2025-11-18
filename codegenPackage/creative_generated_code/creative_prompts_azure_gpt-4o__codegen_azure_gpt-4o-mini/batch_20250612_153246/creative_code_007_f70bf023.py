"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lenderlibrary.ca
Prompt: Write a program to convert Dominion Lending's mortgage documentation into a searchable database, categorizing data by property type, income type, and lender accreditation.
Generated: DETERMINISTIC_f70bf02315661101
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import pandas as pd
from typing import List, Tuple

# Define the database class for handling mortgage documentation
class MortgageDatabase:
    def __init__(self, db_name: str):
        """Initialize the database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create tables for properties, income types, and lenders if they don't exist."""
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS properties (
                    id INTEGER PRIMARY KEY,
                    property_type TEXT NOT NULL,
                    address TEXT NOT NULL,
                    UNIQUE(address)
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS income_types (
                    id INTEGER PRIMARY KEY,
                    income_type TEXT NOT NULL,
                    UNIQUE(income_type)
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS lenders (
                    id INTEGER PRIMARY KEY,
                    lender_name TEXT NOT NULL,
                    accreditation TEXT NOT NULL,
                    UNIQUE(lender_name)
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS mortgages (
                    id INTEGER PRIMARY KEY,
                    property_id INTEGER NOT NULL,
                    income_type_id INTEGER NOT NULL,
                    lender_id INTEGER NOT NULL,
                    loan_amount REAL NOT NULL,
                    FOREIGN KEY(property_id) REFERENCES properties(id),
                    FOREIGN KEY(income_type_id) REFERENCES income_types(id),
                    FOREIGN KEY(lender_id) REFERENCES lenders(id)
                )
            ''')

    def insert_property(self, property_type: str, address: str):
        """Insert a new property into the database."""
        try:
            with self.conn:
                self.conn.execute('''
                    INSERT INTO properties (property_type, address)
                    VALUES (?, ?)
                ''', (property_type, address))
        except sqlite3.IntegrityError:
            print(f"Property with address '{address}' already exists.")

    def insert_income_type(self, income_type: str):
        """Insert a new income type into the database."""
        try:
            with self.conn:
                self.conn.execute('''
                    INSERT INTO income_types (income_type)
                    VALUES (?)
                ''', (income_type,))
        except sqlite3.IntegrityError:
            print(f"Income type '{income_type}' already exists.")

    def insert_lender(self, lender_name: str, accreditation: str):
        """Insert a new lender into the database."""
        try:
            with self.conn:
                self.conn.execute('''
                    INSERT INTO lenders (lender_name, accreditation)
                    VALUES (?, ?)
                ''', (lender_name, accreditation))
        except sqlite3.IntegrityError:
            print(f"Lender '{lender_name}' already exists.")

    def insert_mortgage(self, property_id: int, income_type_id: int, lender_id: int, loan_amount: float):
        """Insert a new mortgage entry into the database."""
        with self.conn:
            self.conn.execute('''
                INSERT INTO mortgages (property_id, income_type_id, lender_id, loan_amount)
                VALUES (?, ?, ?, ?)
            ''', (property_id, income_type_id, lender_id, loan_amount))

    def search_mortgages(self, property_type: str = None, income_type: str = None, lender_name: str = None) -> pd.DataFrame:
        """Search for mortgages based on the specified criteria and return results."""
        query = '''
            SELECT
                m.id, p.address, p.property_type, it.income_type, l.lender_name, m.loan_amount
            FROM
                mortgages m
            JOIN properties p ON m.property_id = p.id
            JOIN income_types it ON m.income_type_id = it.id
            JOIN lenders l ON m.lender_id = l.id
            WHERE
                (p.property_type = ? OR ? IS NULL)
                AND (it.income_type = ? OR ? IS NULL)
                AND (l.lender_name = ? OR ? IS NULL)
        '''
        parameters = (property_type, property_type, income_type, income_type, lender_name, lender_name)
        return pd.read_sql_query(query, self.conn, params=parameters)

    def close(self):
        """Close the database connection."""
        self.conn.close()

# Example usage
if __name__ == "__main__":
    db = MortgageDatabase("mortgages.db")
    
    # Sample data insertion
    db.insert_property("Residential", "123 Main St")
    db.insert_income_type("Salary")
    db.insert_lender("ABC Lending", "Approved")
    db.insert_mortgage(1, 1, 1, 250000.00)

    # Search for mortgages with specific criteria
    results = db.search_mortgages(property_type="Residential", income_type="Salary", lender_name="ABC Lending")
    print(results)

    db.close()
```
