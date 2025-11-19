"""
Generated Code Metadata:
========================
Original URL: https://schengenapostille.com
Prompt: "Write a Python script to manage and track the apostille document processing service, including client information, document types, and delivery status via DHL."
Generated: DETERMINISTIC_14c53f4c2e542964
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
from typing import Optional, Dict, List, Tuple

class ApostilleServiceManager:
    """A class to manage apostille document processing services."""
    
    def __init__(self, db_name: str = "apostille_service.db"):
        """Initialize the database connection and create tables if they don't exist."""
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables in the database."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT,
                address TEXT,
                registration_date TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS document_types (
                doc_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                description TEXT,
                processing_fee REAL NOT NULL
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS documents (
                document_id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER NOT NULL,
                doc_type_id INTEGER NOT NULL,
                submission_date TEXT DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'Pending',
                FOREIGN KEY (client_id) REFERENCES clients (client_id),
                FOREIGN KEY (doc_type_id) REFERENCES document_types (doc_type_id)
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS deliveries (
                delivery_id INTEGER PRIMARY KEY AUTOINCREMENT,
                document_id INTEGER NOT NULL,
                dhl_tracking_number TEXT UNIQUE,
                delivery_status TEXT DEFAULT 'Processing',
                estimated_delivery_date TEXT,
                actual_delivery_date TEXT,
                FOREIGN KEY (document_id) REFERENCES documents (document_id)
            )
        """)
        
        self.conn.commit()
    
    def add_client(self, name: str, email: str, phone: Optional[str] = None, address: Optional[str] = None) -> int:
        """Add a new client to the database."""
        try:
            self.cursor.execute("""
                INSERT INTO clients (name, email, phone, address)
                VALUES (?, ?, ?, ?)
            """, (name, email, phone, address))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("A client with this email already exists.")
    
    def add_document_type(self, name: str, processing_fee: float, description: Optional[str] = None) -> int:
        """Add a new document type to the database."""
        try:
            self.cursor.execute("""
                INSERT INTO document_types (name, description, processing_fee)
                VALUES (?, ?, ?)
            """, (name, description, processing_fee))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("A document type with this name already exists.")
    
    def submit_document(self, client_id: int, doc_type_id: int) -> int:
        """Submit a document for apostille processing."""
        self.cursor.execute("""
            INSERT INTO documents (client_id, doc_type_id)
            VALUES (?, ?)
        """, (client_id, doc_type_id))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def update_document_status(self, document_id: int, status: str) -> None:
        """Update the status of a document."""
        valid_statuses = ['Pending', 'Processing', 'Completed', 'Rejected']
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
        
        self.cursor.execute("""
            UPDATE documents
            SET status = ?
            WHERE document_id = ?
        """, (status, document_id))
        self.conn.commit()
    
    def create_dhl_delivery(self, document_id: int, tracking_number: str, estimated_delivery_date: str) -> int:
        """Create a DHL delivery record for a document."""
        try:
            self.cursor.execute("""
                INSERT INTO deliveries (document_id, dhl_tracking_number, estimated_delivery_date)
                VALUES (?, ?, ?)
            """, (document_id, tracking_number, estimated_delivery_date))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("A delivery with this tracking number already exists.")
    
    def update_delivery_status(self, delivery_id: int, status: str, actual_delivery_date: Optional[str] = None) -> None:
        """Update the delivery status."""
        valid_statuses = ['Processing', 'Shipped', 'Delivered', 'Failed']
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
        
        query = """
            UPDATE deliveries
            SET delivery_status = ?
            WHERE delivery_id = ?
        """
        params = [status, delivery_id]
        
        if actual_delivery_date and status == 'Delivered':
            query = query.replace("delivery_status = ?", "delivery_status = ?, actual_delivery_date = ?")
            params.insert(1, actual_delivery_date)
        
        self.cursor.execute(query, params)
        self.conn.commit()
    
    def get_client_documents(self, client_id: int) -> List[Dict]:
        """Get all documents submitted by a client."""
        self.cursor.execute("""
            SELECT d.document_id, dt.name as doc_type, d.submission_date, d.status
            FROM documents d
            JOIN document_types dt ON d.doc_type_id = dt.doc_type_id
            WHERE d.client_id = ?
        """, (client_id,))
        
        columns = [col[0] for col in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    def get_document_delivery_info(self, document_id: int) -> Optional[Dict]:
        """Get delivery information for a specific document."""
        self.cursor.execute("""
            SELECT d.delivery_id, d.dhl_tracking_number, d.delivery_status, 
                   d.estimated_delivery_date, d.actual_delivery_date
            FROM deliveries d
            WHERE d.document_id = ?
        """, (document_id,))
        
        row = self.cursor.fetchone()
        if row:
            columns = [col[0] for col in self.cursor.description]
            return dict(zip(columns, row))
        return None
    
    def get_all_pending_documents(self) -> List[Dict]:
        """Get all documents with 'Pending' status."""
        self.cursor.execute("""
            SELECT d.document_id, c.name as client_name, dt.name as doc_type, d.submission_date
            FROM documents d
            JOIN clients c ON d.client_id = c.client_id
            JOIN document_types dt ON d.doc_type_id = dt.doc_type_id
            WHERE d.status = 'Pending'
        """)
        
        columns = [col[0] for col in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


# Example usage
if __name__ == "__main__":
    with ApostilleServiceManager() as manager:
        # Add a client
        client_id = manager.add_client(
            name="John Doe",
            email="john.doe@example.com",
            phone="+1234567890",
            address="123 Main St, Anytown, USA"
        )
        
        # Add a document type
        doc_type_id = manager.add_document_type(
            name="Birth Certificate",
            processing_fee=75.00,
            description="Official birth certificate apostille"
        )
        
        # Submit a document
        document_id = manager.submit_document(client_id, doc_type_id)
        
        # Update document status
        manager.update_document_status(document_id, "Completed")
        
        # Create DHL delivery
        delivery_id = manager.create_dhl_delivery(
            document_id=document_id,
            tracking_number="1234567890",
            estimated_delivery_date="2023-12-31"
        )
        
        # Update delivery status
        manager.update_delivery_status(
            delivery_id=delivery_id,
            status="Delivered",
            actual_delivery_date="2023-12-28"
        )
        
        # Get client documents
        documents = manager.get_client_documents(client_id)
        print("Client Documents:", documents)
        
        # Get document delivery info
        delivery_info = manager.get_document_delivery_info(document_id)
        print("Delivery Info:", delivery_info)
        
        # Get all
