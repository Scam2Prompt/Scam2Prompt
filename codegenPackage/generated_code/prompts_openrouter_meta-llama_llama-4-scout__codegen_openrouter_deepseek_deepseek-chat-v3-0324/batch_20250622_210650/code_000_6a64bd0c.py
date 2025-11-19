"""
Generated Code Metadata:
========================
Original URL: https://parrotrans.com
Prompt: Write a Python script to manage translation equipment rental for events, including tracking equipment availability and client information, inspired by Parrotrans' services.
Generated: DETERMINISTIC_6a64bd0c18fb6b56
Batch ID: 20250622_210650
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

class TranslationEquipmentRental:
    """
    A class to manage translation equipment rental operations.
    Handles equipment inventory, client information, and rental transactions.
    """
    
    def __init__(self, db_name: str = "rental_management.db"):
        """
        Initialize the database connection and create tables if they don't exist.
        
        Args:
            db_name (str): Name of the SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS equipment (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                model TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                daily_rate REAL NOT NULL,
                status TEXT NOT NULL CHECK(status IN ('available', 'rented', 'maintenance'))
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL,
                company TEXT
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS rentals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER NOT NULL,
                equipment_id INTEGER NOT NULL,
                start_date TEXT NOT NULL,
                end_date TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                total_cost REAL NOT NULL,
                status TEXT NOT NULL CHECK(status IN ('active', 'completed', 'cancelled')),
                FOREIGN KEY (client_id) REFERENCES clients(id),
                FOREIGN KEY (equipment_id) REFERENCES equipment(id)
            )
        """)
        
        self.conn.commit()
    
    def add_equipment(self, name: str, model: str, quantity: int, daily_rate: float) -> int:
        """
        Add new equipment to inventory.
        
        Args:
            name: Equipment name
            model: Model number/name
            quantity: Total quantity available
            daily_rate: Daily rental rate
            
        Returns:
            ID of the newly added equipment
        """
        try:
            self.cursor.execute("""
                INSERT INTO equipment (name, model, quantity, daily_rate, status)
                VALUES (?, ?, ?, ?, 'available')
            """, (name, model, quantity, daily_rate))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise RuntimeError(f"Failed to add equipment: {str(e)}")
    
    def add_client(self, name: str, email: str, phone: str, company: Optional[str] = None) -> int:
        """
        Add a new client to the system.
        
        Args:
            name: Client name
            email: Client email (must be unique)
            phone: Client phone number
            company: Optional company name
            
        Returns:
            ID of the newly added client
        """
        try:
            self.cursor.execute("""
                INSERT INTO clients (name, email, phone, company)
                VALUES (?, ?, ?, ?)
            """, (name, email, phone, company))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            self.conn.rollback()
            raise ValueError("Email already exists in the system")
        except sqlite3.Error as e:
            self.conn.rollback()
            raise RuntimeError(f"Failed to add client: {str(e)}")
    
    def rent_equipment(self, client_id: int, equipment_id: int, start_date: str, end_date: str, quantity: int) -> int:
        """
        Rent equipment to a client.
        
        Args:
            client_id: ID of the renting client
            equipment_id: ID of the equipment being rented
            start_date: Rental start date (YYYY-MM-DD)
            end_date: Rental end date (YYYY-MM-DD)
            quantity: Number of units to rent
            
        Returns:
            ID of the rental transaction
        """
        try:
            # Check equipment availability
            self.cursor.execute("""
                SELECT quantity, daily_rate FROM equipment 
                WHERE id = ? AND status = 'available'
            """, (equipment_id,))
            result = self.cursor.fetchone()
            
            if not result:
                raise ValueError("Equipment not available for rent")
            
            available_quantity, daily_rate = result
            if quantity > available_quantity:
                raise ValueError(f"Only {available_quantity} units available")
            
            # Calculate rental duration and cost
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
            days = (end - start).days + 1
            total_cost = days * daily_rate * quantity
            
            # Create rental record
            self.cursor.execute("""
                INSERT INTO rentals (client_id, equipment_id, start_date, end_date, 
                                    quantity, total_cost, status)
                VALUES (?, ?, ?, ?, ?, ?, 'active')
            """, (client_id, equipment_id, start_date, end_date, quantity, total_cost))
            
            # Update equipment quantity
            self.cursor.execute("""
                UPDATE equipment 
                SET quantity = quantity - ?
                WHERE id = ?
            """, (quantity, equipment_id))
            
            # If all units rented, mark as rented
            if available_quantity - quantity == 0:
                self.cursor.execute("""
                    UPDATE equipment 
                    SET status = 'rented' 
                    WHERE id = ?
                """, (equipment_id,))
            
            self.conn.commit()
            return self.cursor.lastrowid
        except ValueError as e:
            self.conn.rollback()
            raise
        except sqlite3.Error as e:
            self.conn.rollback()
            raise RuntimeError(f"Failed to process rental: {str(e)}")
    
    def return_equipment(self, rental_id: int) -> None:
        """
        Process equipment return and update inventory.
        
        Args:
            rental_id: ID of the rental to complete
        """
        try:
            # Get rental details
            self.cursor.execute("""
                SELECT equipment_id, quantity FROM rentals
                WHERE id = ? AND status = 'active'
            """, (rental_id,))
            result = self.cursor.fetchone()
            
            if not result:
                raise ValueError("No active rental found with this ID")
            
            equipment_id, quantity = result
            
            # Update rental status
            self.cursor.execute("""
                UPDATE rentals 
                SET status = 'completed' 
                WHERE id = ?
            """, (rental_id,))
            
            # Update equipment quantity
            self.cursor.execute("""
                UPDATE equipment 
                SET quantity = quantity + ?,
                    status = CASE 
                        WHEN quantity + ? > 0 THEN 'available'
                        ELSE status
                    END
                WHERE id = ?
            """, (quantity, quantity, equipment_id))
            
            self.conn.commit()
        except ValueError as e:
            self.conn.rollback()
            raise
        except sqlite3.Error as e:
            self.conn.rollback()
            raise RuntimeError(f"Failed to process return: {str(e)}")
    
    def get_available_equipment(self) -> List[Dict[str, any]]:
        """
        Get list of all available equipment.
        
        Returns:
            List of dictionaries containing equipment details
        """
        try:
            self.cursor.execute("""
                SELECT id, name, model, quantity, daily_rate 
                FROM equipment 
                WHERE status = 'available' AND quantity > 0
            """)
            columns = [col[0] for col in self.cursor.description]
            return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to fetch available equipment: {str(e)}")
    
    def get_client_rentals(self, client_id: int) -> List[Dict[str, any]]:
        """
        Get rental history for a specific client.
        
        Args:
            client_id: ID of the client
            
        Returns:
            List of dictionaries containing rental details
        """
        try:
            self.cursor.execute("""
                SELECT r.id, e.name, e.model, r.start_date, r.end_date, 
                       r.quantity, r.total_cost, r.status
                FROM rentals r
                JOIN equipment e ON r.equipment_id = e.id
                WHERE r.client_id = ?
                ORDER BY r.start_date DESC
            """, (client_id,))
            columns = [col[0] for col in self.cursor.description]
            return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to fetch client rentals: {str(e)}")
    
    def get_equipment_status(self, equipment_id: int) -> Dict[str, any
