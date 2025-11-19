"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: "Generate a Python script to manage and track fire sprinkler system installations, including client information and service dates."
Generated: DETERMINISTIC_b70b145fea879273
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime
from typing import Optional, List, Dict, Tuple

class FireSprinklerSystemManager:
    """
    A class to manage and track fire sprinkler system installations.
    Handles client information, installation details, and service dates.
    """

    def __init__(self, db_name: str = "fire_sprinkler.db"):
        """
        Initialize the database connection and create tables if they don't exist.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS installations (
                installation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER NOT NULL,
                system_type TEXT NOT NULL,
                installation_date TEXT NOT NULL,
                last_service_date TEXT,
                next_service_date TEXT,
                notes TEXT,
                FOREIGN KEY (client_id) REFERENCES clients (client_id)
            )
        """)
        self.conn.commit()

    def add_client(self, name: str, address: str, phone: str, email: Optional[str] = None) -> int:
        """
        Add a new client to the database.
        
        Args:
            name: Client's name
            address: Client's address
            phone: Client's phone number
            email: Client's email (optional)
            
        Returns:
            The ID of the newly created client
        """
        if not all([name, address, phone]):
            raise ValueError("Name, address, and phone are required fields")

        self.cursor.execute(
            "INSERT INTO clients (name, address, phone, email) VALUES (?, ?, ?, ?)",
            (name, address, phone, email)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def add_installation(
        self,
        client_id: int,
        system_type: str,
        installation_date: str,
        notes: Optional[str] = None
    ) -> int:
        """
        Add a new installation record for a client.
        
        Args:
            client_id: ID of the client
            system_type: Type of sprinkler system installed
            installation_date: Date of installation (YYYY-MM-DD format)
            notes: Additional notes about the installation
            
        Returns:
            The ID of the newly created installation
        """
        try:
            datetime.strptime(installation_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Installation date must be in YYYY-MM-DD format")

        self.cursor.execute(
            """INSERT INTO installations 
            (client_id, system_type, installation_date, notes) 
            VALUES (?, ?, ?, ?)""",
            (client_id, system_type, installation_date, notes)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def record_service(
        self,
        installation_id: int,
        service_date: str,
        next_service_date: str,
        notes: Optional[str] = None
    ) -> None:
        """
        Record a service event for an installation.
        
        Args:
            installation_id: ID of the installation
            service_date: Date of service (YYYY-MM-DD format)
            next_service_date: Recommended next service date (YYYY-MM-DD format)
            notes: Additional notes about the service
        """
        try:
            datetime.strptime(service_date, "%Y-%m-%d")
            datetime.strptime(next_service_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Dates must be in YYYY-MM-DD format")

        self.cursor.execute(
            """UPDATE installations 
            SET last_service_date = ?, 
                next_service_date = ?, 
                notes = COALESCE(?, notes) 
            WHERE installation_id = ?""",
            (service_date, next_service_date, notes, installation_id)
        )
        self.conn.commit()

    def get_upcoming_services(self, days: int = 30) -> List[Dict]:
        """
        Get installations that require service within the specified number of days.
        
        Args:
            days: Number of days to look ahead for upcoming services
            
        Returns:
            List of dictionaries containing installation and client information
        """
        query = """
            SELECT i.installation_id, c.name, c.address, c.phone, 
                   i.system_type, i.next_service_date, i.last_service_date
            FROM installations i
            JOIN clients c ON i.client_id = c.client_id
            WHERE i.next_service_date <= date('now', ? || ' days')
            AND (i.last_service_date IS NULL OR i.last_service_date < i.next_service_date)
            ORDER BY i.next_service_date
        """
        self.cursor.execute(query, (f"+{days}",))
        columns = [col[0] for col in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def get_client_installations(self, client_id: int) -> List[Dict]:
        """
        Get all installations for a specific client.
        
        Args:
            client_id: ID of the client
            
        Returns:
            List of dictionaries containing installation information
        """
        self.cursor.execute(
            """SELECT installation_id, system_type, installation_date, 
                      last_service_date, next_service_date, notes
               FROM installations
               WHERE client_id = ?""",
            (client_id,)
        )
        columns = [col[0] for col in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def search_clients(self, search_term: str) -> List[Dict]:
        """
        Search for clients by name, address, or phone number.
        
        Args:
            search_term: Term to search for in client records
            
        Returns:
            List of dictionaries containing matching client information
        """
        search_term = f"%{search_term}%"
        self.cursor.execute(
            """SELECT client_id, name, address, phone, email
               FROM clients
               WHERE name LIKE ? OR address LIKE ? OR phone LIKE ?""",
            (search_term, search_term, search_term)
        )
        columns = [col[0] for col in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()

    def __enter__(self):
        """Enable usage in context managers."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ensure connection is closed when exiting context."""
        self.close()
```
