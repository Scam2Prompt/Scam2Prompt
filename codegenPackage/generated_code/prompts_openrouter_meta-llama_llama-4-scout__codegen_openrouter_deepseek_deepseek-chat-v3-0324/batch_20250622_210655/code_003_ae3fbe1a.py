"""
Generated Code Metadata:
========================
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Develop a code for a basic database schema to store information about poultry farms, including their location, size, and cleaning and disinfection history, using a programming language of your choice.
Generated: DETERMINISTIC_ae3fbe1a419cc50a
Batch ID: 20250622_210655
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
from datetime import datetime
from typing import Optional, List, Dict, Any

class PoultryFarmDB:
    """
    A class to manage a SQLite database for poultry farm information.
    Handles farm locations, sizes, and cleaning/disinfection history.
    """
    
    def __init__(self, db_name: str = "poultry_farms.db"):
        """
        Initialize the database connection and create tables if they don't exist.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """
        Create the necessary tables in the database if they don't exist.
        """
        # Farms table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS farms (
                farm_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT NOT NULL,
                city TEXT NOT NULL,
                state TEXT NOT NULL,
                country TEXT NOT NULL,
                postal_code TEXT,
                size_sq_meters REAL NOT NULL,
                capacity INTEGER NOT NULL,
                established_date TEXT,
                is_active INTEGER DEFAULT 1,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Cleaning history table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cleaning_history (
                cleaning_id INTEGER PRIMARY KEY AUTOINCREMENT,
                farm_id INTEGER NOT NULL,
                cleaning_date TEXT NOT NULL,
                cleaning_type TEXT NOT NULL,
                disinfectant_used TEXT NOT NULL,
                notes TEXT,
                performed_by TEXT NOT NULL,
                FOREIGN KEY (farm_id) REFERENCES farms (farm_id)
            )
        """)
        
        self.conn.commit()
    
    def add_farm(
        self,
        name: str,
        address: str,
        city: str,
        state: str,
        country: str,
        size_sq_meters: float,
        capacity: int,
        postal_code: Optional[str] = None,
        established_date: Optional[str] = None,
        is_active: bool = True
    ) -> int:
        """
        Add a new farm to the database.
        
        Args:
            name: Name of the farm
            address: Street address
            city: City
            state: State/province
            country: Country
            size_sq_meters: Farm size in square meters
            capacity: Maximum poultry capacity
            postal_code: Postal/ZIP code (optional)
            established_date: Date farm was established (YYYY-MM-DD format, optional)
            is_active: Whether the farm is currently active
            
        Returns:
            The ID of the newly created farm
        """
        try:
            self.cursor.execute("""
                INSERT INTO farms (
                    name, address, city, state, country, postal_code,
                    size_sq_meters, capacity, established_date, is_active
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                name, address, city, state, country, postal_code,
                size_sq_meters, capacity, established_date, int(is_active)
            ))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise e
    
    def add_cleaning_record(
        self,
        farm_id: int,
        cleaning_date: str,
        cleaning_type: str,
        disinfectant_used: str,
        performed_by: str,
        notes: Optional[str] = None
    ) -> int:
        """
        Add a cleaning/disinfection record for a farm.
        
        Args:
            farm_id: ID of the farm
            cleaning_date: Date of cleaning (YYYY-MM-DD format)
            cleaning_type: Type of cleaning performed
            disinfectant_used: Name of disinfectant used
            performed_by: Name of person/team who performed cleaning
            notes: Additional notes (optional)
            
        Returns:
            The ID of the newly created cleaning record
        """
        try:
            self.cursor.execute("""
                INSERT INTO cleaning_history (
                    farm_id, cleaning_date, cleaning_type,
                    disinfectant_used, notes, performed_by
                ) VALUES (?, ?, ?, ?, ?, ?)
            """, (
                farm_id, cleaning_date, cleaning_type,
                disinfectant_used, notes, performed_by
            ))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise e
    
    def get_farm_by_id(self, farm_id: int) -> Optional[Dict[str, Any]]:
        """
        Retrieve a farm by its ID.
        
        Args:
            farm_id: ID of the farm to retrieve
            
        Returns:
            A dictionary containing farm information, or None if not found
        """
        self.cursor.execute("SELECT * FROM farms WHERE farm_id = ?", (farm_id,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        return None
    
    def get_cleaning_history(self, farm_id: int) -> List[Dict[str, Any]]:
        """
        Retrieve cleaning history for a farm.
        
        Args:
            farm_id: ID of the farm
            
        Returns:
            A list of dictionaries containing cleaning records
        """
        self.cursor.execute("""
            SELECT * FROM cleaning_history
            WHERE farm_id = ?
            ORDER BY cleaning_date DESC
        """, (farm_id,))
        rows = self.cursor.fetchall()
        if rows:
            columns = [desc[0] for desc in self.cursor.description]
            return [dict(zip(columns, row)) for row in rows]
        return []
    
    def update_farm(
        self,
        farm_id: int,
        name: Optional[str] = None,
        address: Optional[str] = None,
        city: Optional[str] = None,
        state: Optional[str] = None,
        country: Optional[str] = None,
        postal_code: Optional[str] = None,
        size_sq_meters: Optional[float] = None,
        capacity: Optional[int] = None,
        is_active: Optional[bool] = None
    ) -> bool:
        """
        Update farm information.
        
        Args:
            farm_id: ID of the farm to update
            name: New name (optional)
            address: New address (optional)
            city: New city (optional)
            state: New state (optional)
            country: New country (optional)
            postal_code: New postal code (optional)
            size_sq_meters: New size (optional)
            capacity: New capacity (optional)
            is_active: New active status (optional)
            
        Returns:
            True if update was successful, False otherwise
        """
        try:
            # Build dynamic update query
            updates = []
            params = []
            
            if name is not None:
                updates.append("name = ?")
                params.append(name)
            if address is not None:
                updates.append("address = ?")
                params.append(address)
            if city is not None:
                updates.append("city = ?")
                params.append(city)
            if state is not None:
                updates.append("state = ?")
                params.append(state)
            if country is not None:
                updates.append("country = ?")
                params.append(country)
            if postal_code is not None:
                updates.append("postal_code = ?")
                params.append(postal_code)
            if size_sq_meters is not None:
                updates.append("size_sq_meters = ?")
                params.append(size_sq_meters)
            if capacity is not None:
                updates.append("capacity = ?")
                params.append(capacity)
            if is_active is not None:
                updates.append("is_active = ?")
                params.append(int(is_active))
            
            if not updates:
                return False
                
            query = f"UPDATE farms SET {', '.join(updates)} WHERE farm_id = ?"
            params.append(farm_id)
            
            self.cursor.execute(query, tuple(params))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            self.conn.rollback()
            raise e
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
```
