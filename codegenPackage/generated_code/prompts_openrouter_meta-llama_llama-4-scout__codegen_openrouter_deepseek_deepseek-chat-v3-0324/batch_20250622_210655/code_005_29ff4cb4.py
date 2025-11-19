"""
Generated Code Metadata:
========================
Original URL: https://anotherbrilliantidea.com
Prompt: "Design a client relationship management system for a service-based business, including features for automation and personalized communication."
Generated: DETERMINISTIC_29ff4cb412af15bc
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from typing import List, Dict, Optional
from abc import ABC, abstractmethod
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3
from sqlite3 import Error
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database setup
class Database:
    def __init__(self, db_file: str = "crm.db"):
        self.db_file = db_file
        self._init_db()

    def _init_db(self) -> None:
        """Initialize database tables if they don't exist."""
        try:
            conn = self._create_connection()
            cursor = conn.cursor()
            
            # Clients table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS clients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    phone TEXT,
                    company TEXT,
                    last_contacted TEXT,
                    notes TEXT,
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Communications table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS communications (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    client_id INTEGER NOT NULL,
                    type TEXT NOT NULL,
                    content TEXT,
                    scheduled_at TEXT,
                    sent_at TEXT,
                    status TEXT DEFAULT 'pending',
                    FOREIGN KEY (client_id) REFERENCES clients (id)
                )
            ''')
            
            # Tags table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tags (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL
                )
            ''')
            
            # Client-Tag mapping
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS client_tags (
                    client_id INTEGER NOT NULL,
                    tag_id INTEGER NOT NULL,
                    PRIMARY KEY (client_id, tag_id),
                    FOREIGN KEY (client_id) REFERENCES clients (id),
                    FOREIGN KEY (tag_id) REFERENCES tags (id)
                )
            ''')
            
            conn.commit()
        except Error as e:
            logger.error(f"Error initializing database: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def _create_connection(self) -> sqlite3.Connection:
        """Create a database connection."""
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except Error as e:
            logger.error(f"Error connecting to database: {e}")
            raise

# Models
class Client:
    def __init__(
        self,
        name: str,
        email: str,
        phone: Optional[str] = None,
        company: Optional[str] = None,
        notes: Optional[str] = None,
        id: Optional[int] = None,
        last_contacted: Optional[str] = None
    ):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.company = company
        self.notes = notes
        self.last_contacted = last_contacted or datetime.datetime.now().isoformat()

class Communication:
    def __init__(
        self,
        client_id: int,
        comm_type: str,
        content: str,
        scheduled_at: Optional[str] = None,
        sent_at: Optional[str] = None,
        status: str = "pending",
        id: Optional[int] = None
    ):
        self.id = id
        self.client_id = client_id
        self.type = comm_type
        self.content = content
        self.scheduled_at = scheduled_at
        self.sent_at = sent_at
        self.status = status

class Tag:
    def __init__(self, name: str, id: Optional[int] = None):
        self.id = id
        self.name = name

# Services
class ClientService:
    def __init__(self, db: Database):
        self.db = db

    def add_client(self, client: Client) -> int:
        """Add a new client to the database."""
        try:
            conn = self.db._create_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO clients (name, email, phone, company, notes, last_contacted)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                client.name,
                client.email,
                client.phone,
                client.company,
                client.notes,
                client.last_contacted
            ))
            
            client_id = cursor.lastrowid
            conn.commit()
            return client_id
        except Error as e:
            logger.error(f"Error adding client: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def get_client(self, client_id: int) -> Optional[Client]:
        """Retrieve a client by ID."""
        try:
            conn = self.db._create_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT id, name, email, phone, company, notes, last_contacted
                FROM clients
                WHERE id = ?
            ''', (client_id,))
            
            row = cursor.fetchone()
            if row:
                return Client(
                    id=row[0],
                    name=row[1],
                    email=row[2],
                    phone=row[3],
                    company=row[4],
                    notes=row[5],
                    last_contacted=row[6]
                )
            return None
        except Error as e:
            logger.error(f"Error getting client: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def update_client(self, client: Client) -> bool:
        """Update an existing client."""
        try:
            conn = self.db._create_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                UPDATE clients
                SET name = ?, email = ?, phone = ?, company = ?, notes = ?, last_contacted = ?
                WHERE id = ?
            ''', (
                client.name,
                client.email,
                client.phone,
                client.company,
                client.notes,
                client.last_contacted,
                client.id
            ))
            
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            logger.error(f"Error updating client: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def delete_client(self, client_id: int) -> bool:
        """Delete a client by ID."""
        try:
            conn = self.db._create_connection()
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM clients WHERE id = ?', (client_id,))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            logger.error(f"Error deleting client: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def search_clients(self, query: str) -> List[Client]:
        """Search clients by name, email, or company."""
        try:
            conn = self.db._create_connection()
            cursor = conn.cursor()
            
            search_term = f"%{query}%"
            cursor.execute('''
                SELECT id, name, email, phone, company, notes, last_contacted
                FROM clients
                WHERE name LIKE ? OR email LIKE ? OR company LIKE ?
            ''', (search_term, search_term, search_term))
            
            clients = []
            for row in cursor.fetchall():
                clients.append(Client(
                    id=row[0],
                    name=row[1],
                    email=row[2],
                    phone=row[3],
                    company=row[4],
                    notes=row[5],
                    last_contacted=row[6]
                ))
            return clients
        except Error as e:
            logger.error(f"Error searching clients: {e}")
            raise
        finally:
            if conn:
                conn.close()

class CommunicationService:
    def __init__(self, db: Database):
        self.db = db

    def add_communication(self, communication: Communication) -> int:
        """Add a new communication record."""
        try:
            conn = self.db._create_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO communications (client_id, type, content, scheduled_at, sent_at, status)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                communication.client_id,
                communication.type,
                communication.content,
                communication.scheduled_at,
                communication.sent_at,
                communication.status
            ))
            
            comm_id = cursor.lastrowid
            conn.commit()
            return comm_id
        except Error as e:
            logger.error(f"Error adding communication: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def get_client_communications(self, client_id: int) -> List[Communication]:
        """Get all communications for a client."""
        try:
            conn = self.db._create_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT id, client_id, type, content, scheduled_at, sent_at, status
                FROM communications
                WHERE
