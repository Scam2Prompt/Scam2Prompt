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
import sqlite3
from typing import Optional, Dict, List, Any
import json
import os

class SDSChemicalDatabase:
    """
    A database for tracking chemical properties, hazards, and storage guidelines 
    based on Safety Data Sheet (SDS) information.
    """

    def __init__(self, db_path: str = "sds_database.db"):
        """
        Initialize the database connection and create tables if they don't exist.
        
        Args:
            db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self.conn = None
        self._initialize_db()

    def _initialize_db(self) -> None:
        """Create the database tables if they don't exist."""
        try:
            self.conn = sqlite3.connect(self.db_path)
            cursor = self.conn.cursor()

            # Create Chemicals table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Chemicals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    cas_number TEXT UNIQUE,
                    molecular_formula TEXT,
                    molecular_weight REAL,
                    UNIQUE(name, cas_number)
                )
            """)

            # Create Hazards table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Hazards (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    chemical_id INTEGER NOT NULL,
                    hazard_class TEXT NOT NULL,
                    hazard_category TEXT,
                    hazard_statement TEXT,
                    precautionary_statement TEXT,
                    FOREIGN KEY (chemical_id) REFERENCES Chemicals (id) ON DELETE CASCADE,
                    UNIQUE(chemical_id, hazard_class)
                )
            """)

            # Create Storage table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Storage (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    chemical_id INTEGER NOT NULL,
                    storage_conditions TEXT NOT NULL,
                    incompatible_materials TEXT,
                    special_handling TEXT,
                    FOREIGN KEY (chemical_id) REFERENCES Chemicals (id) ON DELETE CASCADE
                )
            """)

            # Create SDS table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS SDS (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    chemical_id INTEGER NOT NULL,
                    sds_version TEXT NOT NULL,
                    revision_date TEXT NOT NULL,
                    supplier_name TEXT NOT NULL,
                    sds_document_path TEXT,
                    FOREIGN KEY (chemical_id) REFERENCES Chemicals (id) ON DELETE CASCADE
                )
            """)

            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            raise
        except Exception as e:
            print(f"General error: {e}")
            raise

    def add_chemical(
        self,
        name: str,
        cas_number: Optional[str] = None,
        molecular_formula: Optional[str] = None,
        molecular_weight: Optional[float] = None
    ) -> int:
        """
        Add a new chemical to the database.
        
        Args:
            name: Name of the chemical.
            cas_number: CAS registry number (optional).
            molecular_formula: Molecular formula (optional).
            molecular_weight: Molecular weight (optional).
            
        Returns:
            The ID of the newly inserted chemical.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO Chemicals (name, cas_number, molecular_formula, molecular_weight)
                VALUES (?, ?, ?, ?)
            """, (name, cas_number, molecular_formula, molecular_weight))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            print(f"Chemical with name '{name}' and CAS number '{cas_number}' already exists.")
            raise
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            raise

    def add_hazard(
        self,
        chemical_id: int,
        hazard_class: str,
        hazard_category: Optional[str] = None,
        hazard_statement: Optional[str] = None,
        precautionary_statement: Optional[str] = None
    ) -> int:
        """
        Add hazard information for a chemical.
        
        Args:
            chemical_id: ID of the chemical.
            hazard_class: Hazard classification (e.g., "Flammable").
            hazard_category: Hazard category (optional).
            hazard_statement: Hazard statement (optional).
            precautionary_statement: Precautionary statement (optional).
            
        Returns:
            The ID of the newly inserted hazard.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO Hazards (
                    chemical_id, hazard_class, hazard_category, 
                    hazard_statement, precautionary_statement
                )
                VALUES (?, ?, ?, ?, ?)
            """, (chemical_id, hazard_class, hazard_category, hazard_statement, precautionary_statement))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            print(f"Hazard class '{hazard_class}' already exists for chemical ID {chemical_id}.")
            raise
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            raise

    def add_storage(
        self,
        chemical_id: int,
        storage_conditions: str,
        incompatible_materials: Optional[str] = None,
        special_handling: Optional[str] = None
    ) -> int:
        """
        Add storage information for a chemical.
        
        Args:
            chemical_id: ID of the chemical.
            storage_conditions: Storage conditions (e.g., "Store in a cool, dry place").
            incompatible_materials: Incompatible materials (optional).
            special_handling: Special handling instructions (optional).
            
        Returns:
            The ID of the newly inserted storage record.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO Storage (
                    chemical_id, storage_conditions, incompatible_materials, special_handling
                )
                VALUES (?, ?, ?, ?)
            """, (chemical_id, storage_conditions, incompatible_materials, special_handling))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            raise

    def add_sds(
        self,
        chemical_id: int,
        sds_version: str,
        revision_date: str,
        supplier_name: str,
        sds_document_path: Optional[str] = None
    ) -> int:
        """
        Add SDS information for a chemical.
        
        Args:
            chemical_id: ID of the chemical.
            sds_version: Version of the SDS.
            revision_date: Date of revision (format: YYYY-MM-DD).
            supplier_name: Name of the supplier.
            sds_document_path: Path to the SDS document (optional).
            
        Returns:
            The ID of the newly inserted SDS record.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO SDS (
                    chemical_id, sds_version, revision_date, supplier_name, sds_document_path
                )
                VALUES (?, ?, ?, ?, ?)
            """, (chemical_id, sds_version, revision_date, supplier_name, sds_document_path))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            raise

    def get_chemical(self, chemical_id: int) -> Optional[Dict[str, Any]]:
        """
        Retrieve a chemical and its associated information.
        
        Args:
            chemical_id: ID of the chemical to retrieve.
            
        Returns:
            A dictionary containing the chemical's information, or None if not found.
        """
        try:
            cursor = self.conn.cursor()

            # Get chemical info
            cursor.execute("SELECT * FROM Chemicals WHERE id = ?", (chemical_id,))
            chemical = cursor.fetchone()
            if not chemical:
                return None

            # Get hazards
            cursor.execute("SELECT * FROM Hazards WHERE chemical_id = ?", (chemical_id,))
            hazards = cursor.fetchall()

            # Get storage info
            cursor.execute("SELECT * FROM Storage WHERE chemical_id = ?", (chemical_id,))
            storage = cursor.fetchall()

            # Get SDS info
            cursor.execute("SELECT * FROM SDS WHERE chemical_id = ?", (chemical_id,))
            sds = cursor.fetchall()

            return {
                "chemical": {
                    "id": chemical[0],
                    "name": chemical[1],
                    "cas_number": chemical[2],
                    "molecular_formula": chemical[3],
                    "molecular_weight": chemical[4]
                },
                "hazards": [
                    {
                        "id": h[0],
                        "hazard_class": h[2],
                        "hazard_category": h[3],
                        "hazard_statement": h[4],
                        "precautionary_statement": h[5]
                    } for h in hazards
                ],
                "storage": [
                    {
                        "id": s[0],
                        "storage_conditions": s[2],
                        "incompatible_materials": s[3],
                        "special_handling": s[4]
                    } for s in storage
                ],
                "sds": [
                    {
                        "id
