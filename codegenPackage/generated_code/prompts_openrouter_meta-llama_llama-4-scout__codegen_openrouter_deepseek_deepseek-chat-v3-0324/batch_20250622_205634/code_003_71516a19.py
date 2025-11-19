"""
Generated Code Metadata:
========================
Original URL: https://www.arclerdesk.com
Prompt: Design a simple printer repair ticketing system using a database and a programming language of your choice, inspired by Arcler Desk's printer repair services.
Generated: DETERMINISTIC_71516a19a7be2ff2
Batch ID: 20250622_205634
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
from typing import Optional, List, Dict

class PrinterRepairSystem:
    """
    A simple printer repair ticketing system using SQLite database.
    """
    
    def __init__(self, db_name: str = "printer_repair.db"):
        """
        Initialize the system with a SQLite database.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.db_name = db_name
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """
        Create database tables if they don't exist.
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Create tickets table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tickets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_name TEXT NOT NULL,
                    contact_number TEXT NOT NULL,
                    printer_model TEXT NOT NULL,
                    issue_description TEXT NOT NULL,
                    status TEXT NOT NULL DEFAULT 'Open',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create technicians table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS technicians (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    specialization TEXT NOT NULL,
                    contact_number TEXT NOT NULL
                )
            """)
            
            # Create ticket_assignments table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ticket_assignments (
                    ticket_id INTEGER NOT NULL,
                    technician_id INTEGER NOT NULL,
                    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (ticket_id, technician_id),
                    FOREIGN KEY (ticket_id) REFERENCES tickets(id),
                    FOREIGN KEY (technician_id) REFERENCES technicians(id)
                )
            """)
            
            conn.commit()
    
    def create_ticket(
        self,
        customer_name: str,
        contact_number: str,
        printer_model: str,
        issue_description: str
    ) -> int:
        """
        Create a new repair ticket.
        
        Args:
            customer_name: Name of the customer
            contact_number: Customer's contact number
            printer_model: Printer model needing repair
            issue_description: Description of the issue
            
        Returns:
            ID of the created ticket
            
        Raises:
            ValueError: If any required field is empty
        """
        if not all([customer_name, contact_number, printer_model, issue_description]):
            raise ValueError("All fields are required")
            
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO tickets (
                    customer_name,
                    contact_number,
                    printer_model,
                    issue_description
                ) VALUES (?, ?, ?, ?)
            """, (customer_name, contact_number, printer_model, issue_description))
            conn.commit()
            return cursor.lastrowid
    
    def get_ticket(self, ticket_id: int) -> Optional[Dict]:
        """
        Retrieve a ticket by ID.
        
        Args:
            ticket_id: ID of the ticket to retrieve
            
        Returns:
            Dictionary with ticket details or None if not found
        """
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM tickets WHERE id = ?
            """, (ticket_id,))
            row = cursor.fetchone()
            return dict(row) if row else None
    
    def update_ticket_status(self, ticket_id: int, status: str) -> bool:
        """
        Update a ticket's status.
        
        Args:
            ticket_id: ID of the ticket to update
            status: New status ('Open', 'In Progress', 'Completed', 'Cancelled')
            
        Returns:
            True if update was successful, False otherwise
            
        Raises:
            ValueError: If status is invalid
        """
        valid_statuses = {'Open', 'In Progress', 'Completed', 'Cancelled'}
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
            
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE tickets 
                SET status = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            """, (status, ticket_id))
            conn.commit()
            return cursor.rowcount > 0
    
    def add_technician(
        self,
        name: str,
        specialization: str,
        contact_number: str
    ) -> int:
        """
        Add a new technician to the system.
        
        Args:
            name: Technician's name
            specialization: Area of expertise
            contact_number: Technician's contact number
            
        Returns:
            ID of the created technician record
            
        Raises:
            ValueError: If any required field is empty
        """
        if not all([name, specialization, contact_number]):
            raise ValueError("All fields are required")
            
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO technicians (name, specialization, contact_number)
                VALUES (?, ?, ?)
            """, (name, specialization, contact_number))
            conn.commit()
            return cursor.lastrowid
    
    def assign_technician(self, ticket_id: int, technician_id: int) -> bool:
        """
        Assign a technician to a ticket.
        
        Args:
            ticket_id: ID of the ticket
            technician_id: ID of the technician
            
        Returns:
            True if assignment was successful, False otherwise
            
        Raises:
            ValueError: If ticket or technician doesn't exist
        """
        if not self.get_ticket(ticket_id):
            raise ValueError("Ticket does not exist")
            
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM technicians WHERE id = ?", (technician_id,))
            if not cursor.fetchone():
                raise ValueError("Technician does not exist")
                
            try:
                cursor.execute("""
                    INSERT INTO ticket_assignments (ticket_id, technician_id)
                    VALUES (?, ?)
                """, (ticket_id, technician_id))
                conn.commit()
                return True
            except sqlite3.IntegrityError:
                return False
    
    def get_tickets_by_status(self, status: str) -> List[Dict]:
        """
        Get all tickets with a specific status.
        
        Args:
            status: Status to filter by
            
        Returns:
            List of ticket dictionaries
        """
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM tickets WHERE status = ?
            """, (status,))
            return [dict(row) for row in cursor.fetchall()]
    
    def get_assigned_technicians(self, ticket_id: int) -> List[Dict]:
        """
        Get all technicians assigned to a ticket.
        
        Args:
            ticket_id: ID of the ticket
            
        Returns:
            List of technician dictionaries
        """
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("""
                SELECT t.* FROM technicians t
                JOIN ticket_assignments ta ON t.id = ta.technician_id
                WHERE ta.ticket_id = ?
            """, (ticket_id,))
            return [dict(row) for row in cursor.fetchall()]
    
    def close(self) -> None:
        """
        Close the database connection (not needed for SQLite in this implementation).
        """
        pass

# Example usage
if __name__ == "__main__":
    system = PrinterRepairSystem()
    
    # Create a ticket
    ticket_id = system.create_ticket(
        customer_name="John Doe",
        contact_number="555-1234",
        printer_model="HP LaserJet Pro",
        issue_description="Paper jam and error lights"
    )
    print(f"Created ticket with ID: {ticket_id}")
    
    # Add a technician
    tech_id = system.add_technician(
        name="Jane Smith",
        specialization="Laser printers",
        contact_number="555-5678"
    )
    print(f"Added technician with ID: {tech_id}")
    
    # Assign technician to ticket
    if system.assign_technician(ticket_id, tech_id):
        print("Technician assigned successfully")
    
    # Update ticket status
    if system.update_ticket_status(ticket_id, "In Progress"):
        print("Ticket status updated")
    
    # Get ticket info
    ticket = system.get_ticket(ticket_id)
    print(f"Ticket details: {ticket}")
    
    # Get assigned technicians
    techs = system.get_assigned_technicians(ticket_id)
    print(f"Assigned technicians: {techs}")
```
