"""
Generated Code Metadata:
========================
Original URL: https://proximus-client.was-systems.com
Prompt: Generate code for tracking the source of client acquisition (e.g., call, social networks, recommendation) as described on the Proximus client site.
Generated: DETERMINISTIC_913c03545c02bbcf
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# client_acquisition_tracker.py

from enum import Enum
from datetime import datetime
from typing import Optional, Dict, List
import sqlite3
from sqlite3 import Error
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AcquisitionSource(Enum):
    """Enumeration of possible client acquisition sources."""
    CALL = "Call"
    SOCIAL_NETWORK = "Social Network"
    RECOMMENDATION = "Recommendation"
    WEBSITE = "Website"
    EMAIL = "Email"
    OTHER = "Other"

class ClientAcquisitionTracker:
    """Class to track client acquisition sources and related information."""
    
    def __init__(self, db_path: str = "client_acquisition.db"):
        """Initialize the tracker with database connection.
        
        Args:
            db_path: Path to SQLite database file.
        """
        self.db_path = db_path
        self.conn = None
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Initialize the database with required tables."""
        try:
            self.conn = sqlite3.connect(self.db_path)
            cursor = self.conn.cursor()
            
            # Create acquisition sources table if not exists
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS acquisition_sources (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    source TEXT NOT NULL,
                    description TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create clients table if not exists
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT,
                    phone TEXT,
                    acquisition_source_id INTEGER,
                    acquisition_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    notes TEXT,
                    FOREIGN KEY (acquisition_source_id) REFERENCES acquisition_sources(id)
                )
            """)
            
            # Insert default acquisition sources if they don't exist
            for source in AcquisitionSource:
                cursor.execute(
                    "INSERT OR IGNORE INTO acquisition_sources (source) VALUES (?)",
                    (source.value,)
                )
            
            self.conn.commit()
            
        except Error as e:
            logger.error(f"Database initialization error: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
    
    def add_client(
        self,
        name: str,
        acquisition_source: AcquisitionSource,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        notes: Optional[str] = None,
        acquisition_date: Optional[datetime] = None
    ) -> int:
        """Add a new client with acquisition information.
        
        Args:
            name: Client name
            acquisition_source: Source of acquisition
            email: Client email (optional)
            phone: Client phone number (optional)
            notes: Additional notes (optional)
            acquisition_date: Date of acquisition (optional, defaults to now)
            
        Returns:
            ID of the newly created client record
            
        Raises:
            ValueError: If required fields are missing
            sqlite3.Error: If database operation fails
        """
        if not name or not acquisition_source:
            raise ValueError("Name and acquisition source are required")
        
        try:
            cursor = self.conn.cursor()
            
            # Get the source ID
            cursor.execute(
                "SELECT id FROM acquisition_sources WHERE source = ?",
                (acquisition_source.value,)
            )
            source_id = cursor.fetchone()[0]
            
            # Insert client record
            cursor.execute(
                """
                INSERT INTO clients (
                    name, email, phone, acquisition_source_id, notes, acquisition_date
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    name,
                    email,
                    phone,
                    source_id,
                    notes,
                    acquisition_date or datetime.now()
                )
            )
            
            client_id = cursor.lastrowid
            self.conn.commit()
            logger.info(f"Added new client with ID {client_id}")
            return client_id
            
        except Error as e:
            self.conn.rollback()
            logger.error(f"Error adding client: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
    
    def get_client(self, client_id: int) -> Dict:
        """Retrieve client information by ID.
        
        Args:
            client_id: ID of the client to retrieve
            
        Returns:
            Dictionary with client information
            
        Raises:
            sqlite3.Error: If database operation fails
        """
        try:
            cursor = self.conn.cursor()
            
            cursor.execute(
                """
                SELECT 
                    c.id, c.name, c.email, c.phone, 
                    a.source, c.acquisition_date, c.notes
                FROM clients c
                JOIN acquisition_sources a ON c.acquisition_source_id = a.id
                WHERE c.id = ?
                """,
                (client_id,)
            )
            
            row = cursor.fetchone()
            if not row:
                return {}
            
            return {
                "id": row[0],
                "name": row[1],
                "email": row[2],
                "phone": row[3],
                "acquisition_source": row[4],
                "acquisition_date": row[5],
                "notes": row[6]
            }
            
        except Error as e:
            logger.error(f"Error retrieving client: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
    
    def get_clients_by_source(
        self, 
        source: AcquisitionSource,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> List[Dict]:
        """Retrieve clients acquired through a specific source.
        
        Args:
            source: Acquisition source to filter by
            start_date: Optional start date for filtering
            end_date: Optional end date for filtering
            
        Returns:
            List of dictionaries with client information
            
        Raises:
            sqlite3.Error: If database operation fails
        """
        try:
            cursor = self.conn.cursor()
            
            query = """
                SELECT 
                    c.id, c.name, c.email, c.phone, 
                    a.source, c.acquisition_date, c.notes
                FROM clients c
                JOIN acquisition_sources a ON c.acquisition_source_id = a.id
                WHERE a.source = ?
            """
            params = [source.value]
            
            if start_date:
                query += " AND c.acquisition_date >= ?"
                params.append(start_date)
            
            if end_date:
                query += " AND c.acquisition_date <= ?"
                params.append(end_date)
            
            query += " ORDER BY c.acquisition_date DESC"
            
            cursor.execute(query, tuple(params))
            
            clients = []
            for row in cursor.fetchall():
                clients.append({
                    "id": row[0],
                    "name": row[1],
                    "email": row[2],
                    "phone": row[3],
                    "acquisition_source": row[4],
                    "acquisition_date": row[5],
                    "notes": row[6]
                })
            
            return clients
            
        except Error as e:
            logger.error(f"Error retrieving clients by source: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
    
    def get_acquisition_stats(
        self,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> Dict[str, int]:
        """Get statistics of client acquisition by source.
        
        Args:
            start_date: Optional start date for filtering
            end_date: Optional end date for filtering
            
        Returns:
            Dictionary with acquisition source as key and count as value
            
        Raises:
            sqlite3.Error: If database operation fails
        """
        try:
            cursor = self.conn.cursor()
            
            query = """
                SELECT 
                    a.source, COUNT(c.id) as count
                FROM acquisition_sources a
                LEFT JOIN clients c ON a.id = c.acquisition_source_id
            """
            params = []
            
            if start_date or end_date:
                query += " WHERE "
                conditions = []
                
                if start_date:
                    conditions.append("c.acquisition_date >= ?")
                    params.append(start_date)
                
                if end_date:
                    conditions.append("c.acquisition_date <= ?")
                    params.append(end_date)
                
                query += " AND ".join(conditions)
            
            query += " GROUP BY a.source ORDER BY count DESC"
            
            cursor.execute(query, tuple(params))
            
            stats = {}
            for row in cursor.fetchall():
                stats[row[0]] = row[1]
            
            return stats
            
        except Error as e:
            logger.error(f"Error retrieving acquisition stats: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
    
    def close(self) -> None:
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            self.conn = None
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()

# Example usage
if
