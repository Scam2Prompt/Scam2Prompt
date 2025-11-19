"""
Generated Code Metadata:
========================
Original URL: https://hyperswap.network
Prompt: Create a library recommendation for managing user inquiries and quotes for a paving business, taking cues from the contact and request quote features on Bedford Paving's webpage.
Generated: DETERMINISTIC_43b06dad74365641
Batch ID: 20250612_162806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready implementation for managing user inquiries and quotes for a paving business:

```python
from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto
from typing import List, Optional
import re
import sqlite3
from sqlite3 import Error
from pathlib import Path


class InquiryType(Enum):
    """Types of customer inquiries."""
    GENERAL = auto()
    QUOTE_REQUEST = auto()
    SERVICE_QUESTION = auto()


@dataclass
class Customer:
    """Represents a customer making an inquiry."""
    name: str
    email: str
    phone: str
    address: str


@dataclass
class ServiceRequest:
    """Details about the paving service being requested."""
    service_type: str
    area_size: float  # in square feet
    preferred_date: Optional[datetime]
    additional_notes: str


@dataclass
class Quote:
    """Generated quote for a customer."""
    customer: Customer
    service_request: ServiceRequest
    amount: float
    expiration_date: datetime
    notes: str = ""


class PavingInquirySystem:
    """System for managing paving inquiries and quotes."""
    
    def __init__(self, db_path: str = "paving_inquiries.db"):
        """Initialize the system with database connection."""
        self.db_path = db_path
        self._init_db()
    
    def _init_db(self) -> None:
        """Initialize database tables if they don't exist."""
        sql_create_inquiries_table = """
        CREATE TABLE IF NOT EXISTS inquiries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            customer_email TEXT NOT NULL,
            customer_phone TEXT NOT NULL,
            customer_address TEXT NOT NULL,
            inquiry_type TEXT NOT NULL,
            service_type TEXT,
            area_size REAL,
            preferred_date TEXT,
            additional_notes TEXT,
            received_date TEXT NOT NULL,
            status TEXT DEFAULT 'new'
        );
        """
        
        sql_create_quotes_table = """
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            inquiry_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            expiration_date TEXT NOT NULL,
            notes TEXT,
            created_date TEXT NOT NULL,
            status TEXT DEFAULT 'pending',
            FOREIGN KEY (inquiry_id) REFERENCES inquiries (id)
        );
        """
        
        try:
            conn = self._create_connection()
            if conn is not None:
                cursor = conn.cursor()
                cursor.execute(sql_create_inquiries_table)
                cursor.execute(sql_create_quotes_table)
                conn.commit()
            else:
                raise Error("Failed to create database connection")
        except Error as e:
            print(f"Error initializing database: {e}")
            raise
        finally:
            if conn:
                conn.close()
    
    def _create_connection(self) -> sqlite3.Connection:
        """Create a database connection."""
        try:
            conn = sqlite3.connect(self.db_path)
            return conn
        except Error as e:
            print(f"Error connecting to database: {e}")
            raise
    
    def _validate_email(self, email: str) -> bool:
        """Validate email format."""
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None
    
    def _validate_phone(self, phone: str) -> bool:
        """Validate phone number format."""
        pattern = r"^\+?[\d\s-]{10,}$"
        return re.match(pattern, phone) is not None
    
    def record_inquiry(
        self,
        customer: Customer,
        inquiry_type: InquiryType,
        service_request: Optional[ServiceRequest] = None
    ) -> int:
        """
        Record a new customer inquiry.
        
        Args:
            customer: Customer making the inquiry
            inquiry_type: Type of inquiry
            service_request: Details about service (required for quotes)
        
        Returns:
            The ID of the created inquiry
            
        Raises:
            ValueError: If input validation fails
            Error: If database operation fails
        """
        if not self._validate_email(customer.email):
            raise ValueError("Invalid email format")
        
        if not self._validate_phone(customer.phone):
            raise ValueError("Invalid phone number format")
        
        if inquiry_type == InquiryType.QUOTE_REQUEST and not service_request:
            raise ValueError("Service request required for quote inquiries")
        
        sql = """
        INSERT INTO inquiries(
            customer_name, customer_email, customer_phone, customer_address,
            inquiry_type, service_type, area_size, preferred_date,
            additional_notes, received_date
        ) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        try:
            conn = self._create_connection()
            cursor = conn.cursor()
            
            service_type = service_request.service_type if service_request else None
            area_size = service_request.area_size if service_request else None
            preferred_date = service_request.preferred_date.isoformat() if (
                service_request and service_request.preferred_date
            ) else None
            additional_notes = service_request.additional_notes if service_request else None
            
            cursor.execute(sql, (
                customer.name,
                customer.email,
                customer.phone,
                customer.address,
                inquiry_type.name,
                service_type,
                area_size,
                preferred_date,
                additional_notes,
                datetime.now().isoformat()
            ))
            inquiry_id = cursor.lastrowid
            conn.commit()
            return inquiry_id
        except Error as e:
            print(f"Error recording inquiry: {e}")
            raise
        finally:
            if conn:
                conn.close()
    
    def generate_quote(self, inquiry_id: int, amount: float, expiration_days: int = 30, notes: str = "") -> int:
        """
        Generate a quote for an inquiry.
        
        Args:
            inquiry_id: ID of the inquiry to quote
            amount: Quote amount
            expiration_days: Days until quote expires
            notes: Additional notes about the quote
            
        Returns:
            The ID of the created quote
            
        Raises:
            ValueError: If input validation fails
            Error: If database operation fails
        """
        if amount <= 0:
            raise ValueError("Quote amount must be positive")
        
        if expiration_days <= 0:
            raise ValueError("Expiration days must be positive")
        
        expiration_date = datetime.now() + timedelta(days=expiration_days)
        
        sql = """
        INSERT INTO quotes(
            inquiry_id, amount, expiration_date, notes, created_date
        ) VALUES(?, ?, ?, ?, ?)
        """
        
        try:
            conn = self._create_connection()
            cursor = conn.cursor()
            
            cursor.execute(sql, (
                inquiry_id,
                amount,
                expiration_date.isoformat(),
                notes,
                datetime.now().isoformat()
            ))
            quote_id = cursor.lastrowid
            
            # Update inquiry status
            cursor.execute(
                "UPDATE inquiries SET status = 'quoted' WHERE id = ?",
                (inquiry_id,)
            )
            
            conn.commit()
            return quote_id
        except Error as e:
            print(f"Error generating quote: {e}")
            raise
        finally:
            if conn:
                conn.close()
    
    def get_pending_inquiries(self) -> List[dict]:
        """Retrieve all pending inquiries."""
        try:
            conn = self._create_connection()
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT * FROM inquiries 
                WHERE status = 'new' 
                ORDER BY received_date DESC
            """)
            
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
        except Error as e:
            print(f"Error fetching pending inquiries: {e}")
            raise
        finally:
            if conn:
                conn.close()
    
    def get_active_quotes(self) -> List[dict]:
        """Retrieve all active (not expired) quotes."""
        try:
            conn = self._create_connection()
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT q.*, i.customer_name, i.customer_email, i.service_type 
                FROM quotes q
                JOIN inquiries i ON q.inquiry_id = i.id
                WHERE q.status = 'pending' 
                AND q.expiration_date > ?
                ORDER BY q.expiration_date ASC
            """, (datetime.now().isoformat(),))
            
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
        except Error as e:
            print(f"Error fetching active quotes: {e}")
            raise
        finally:
            if conn:
                conn.close()
    
    def mark_quote_accepted(self, quote_id: int) -> None:
        """Mark a quote as accepted by the customer."""
        try:
            conn = self._create_connection()
            cursor = conn.cursor()
            
            cursor.execute("""
                UPDATE quotes 
                SET status = 'accepted' 
                WHERE id = ?
            """, (quote_id,))
            
            conn.commit()
        except Error as e:
            print(f"Error
