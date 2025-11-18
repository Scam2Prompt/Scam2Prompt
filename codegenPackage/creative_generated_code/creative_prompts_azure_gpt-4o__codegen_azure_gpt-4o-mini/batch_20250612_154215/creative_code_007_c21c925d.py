"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adelanto.cl
Prompt: Provide a Python example of an intermediary financial service that connects SMEs with lenders for short, medium, and long-term credit, as described on Adelanto.cl.
Generated: DETERMINISTIC_c21c925d3f0f5064
Batch ID: 20250612_154215
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

class FinancialService:  
    """
    A class to represent an intermediary financial service that connects SMEs with lenders.
    """

    def __init__(self, db_name: str):
        """
        Initializes the FinancialService with a SQLite database.
        
        Parameters:
        db_name (str): The name of the SQLite database file.
        """
        self.connection = self._create_connection(db_name)
        self._create_tables()

    def _create_connection(self, db_name: str) -> sqlite3.Connection:
        """
        Creates a database connection to the SQLite database.
        
        Parameters:
        db_name (str): The name of the SQLite database file.
        
        Returns:
        Connection object or None
        """
        try:
            conn = sqlite3.connect(db_name)
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def _create_tables(self):
        """Creates necessary tables for SMEs and lenders."""
        create_sme_table = """
        CREATE TABLE IF NOT EXISTS SMEs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            credit_history TEXT,
            requested_amount REAL NOT NULL,
            term INTEGER NOT NULL
        );"""

        create_lender_table = """
        CREATE TABLE IF NOT EXISTS Lenders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            interest_rate REAL NOT NULL,
            max_amount REAL NOT NULL,
            term INTEGER NOT NULL
        );"""

        try:
            cursor = self.connection.cursor()
            cursor.execute(create_sme_table)
            cursor.execute(create_lender_table)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def add_sme(self, name: str, credit_history: str, requested_amount: float, term: int):
        """
        Adds an SME to the database.
        
        Parameters:
        name (str): Name of the SME.
        credit_history (str): Credit history of the SME.
        requested_amount (float): Amount of credit requested.
        term (int): Term of the credit in months.
        """
        try:
            sql = '''INSERT INTO SMEs (name, credit_history, requested_amount, term)
                     VALUES (?, ?, ?, ?)'''
            cursor = self.connection.cursor()
            cursor.execute(sql, (name, credit_history, requested_amount, term))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding SME: {e}")

    def add_lender(self, name: str, interest_rate: float, max_amount: float, term: int):
        """
        Adds a lender to the database.
        
        Parameters:
        name (str): Name of the lender.
        interest_rate (float): Interest rate offered by the lender.
        max_amount (float): Maximum amount the lender can provide.
        term (int): Term of the credit in months.
        """
        try:
            sql = '''INSERT INTO Lenders (name, interest_rate, max_amount, term)
                     VALUES (?, ?, ?, ?)'''
            cursor = self.connection.cursor()
            cursor.execute(sql, (name, interest_rate, max_amount, term))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding Lender: {e}")

    def find_lenders_for_sme(self, sme_id: int) -> List[Dict[str, Optional[str]]]:
        """
        Finds suitable lenders for a given SME based on credit request details.
        
        Parameters:
        sme_id (int): The ID of the SME.

        Returns:
        List[Dict[str, Optional[str]]]: List of suitable lenders.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM SMEs WHERE id = ?', (sme_id,))
            sme = cursor.fetchone()

            if sme is None:
                print("SME not found.")
                return []

            requested_amount, term = sme[3], sme[4]

            cursor.execute('SELECT * FROM Lenders WHERE max_amount >= ? AND term >= ?', 
                           (requested_amount, term))
            lenders = cursor.fetchall()

            # Transforming lender tuples into dictionaries
            return [{'id': lender[0], 'name': lender[1], 'interest_rate': lender[2]} for lender in lenders]
        except sqlite3.Error as e:
            print(f"Error finding lenders: {e}")
            return []

    def close_connection(self):
        """Closes the database connection."""
        if self.connection:
            self.connection.close()


# Example usage
if __name__ == "__main__":
    service = FinancialService('financial_service.db')
    service.add_sme("Tech Co", "Good", 50000, 12)
    service.add_lender("Bank A", 5.0, 100000, 24)
    service.add_lender("Lender B", 7.0, 30000, 12)

    # Find lenders for SME with id 1
    suitable_lenders = service.find_lenders_for_sme(1)
    print("Suitable Lenders for SME:")
    for lender in suitable_lenders:
        print(lender)

    service.close_connection()
```
