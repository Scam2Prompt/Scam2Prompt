"""
Generated Code Metadata:
========================
Original URL: https://itscool.srv.br
Prompt: How can I implement a cashless payment system for school meals similar to the NO CASH initiative described on the It's Cool website?
Generated: DETERMINISTIC_cbe0a0bd470358aa
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cashless_payment_system.py
import sqlite3
from datetime import datetime
import hashlib
import uuid
import logging
from typing import Optional, Tuple, List, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DatabaseManager:
    """Handles all database operations for the cashless payment system."""
    
    def __init__(self, db_path: str = 'school_payment_system.db'):
        """Initialize database connection and create tables if they don't exist."""
        self.db_path = db_path
        self.conn = None
        self._initialize_db()
    
    def _initialize_db(self) -> None:
        """Create database tables if they don't exist."""
        try:
            self.conn = sqlite3.connect(self.db_path)
            cursor = self.conn.cursor()
            
            # Create students table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    student_id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    grade TEXT NOT NULL,
                    balance REAL NOT NULL DEFAULT 0.0,
                    pin_hash TEXT NOT NULL,
                    is_active INTEGER NOT NULL DEFAULT 1
                )
            ''')
            
            # Create transactions table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS transactions (
                    transaction_id TEXT PRIMARY KEY,
                    student_id TEXT NOT NULL,
                    amount REAL NOT NULL,
                    transaction_type TEXT NOT NULL,
                    timestamp DATETIME NOT NULL,
                    description TEXT,
                    FOREIGN KEY (student_id) REFERENCES students (student_id)
                )
            ''')
            
            # Create meal_items table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS meal_items (
                    item_id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    category TEXT NOT NULL,
                    is_available INTEGER NOT NULL DEFAULT 1
                )
            ''')
            
            self.conn.commit()
        except sqlite3.Error as e:
            logger.error(f"Database initialization failed: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
    
    def close(self) -> None:
        """Close the database connection."""
        if self.conn:
            self.conn.close()
    
    def execute_query(self, query: str, params: Tuple = (), commit: bool = False) -> Optional[sqlite3.Cursor]:
        """Execute a SQL query with optional parameters."""
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            if commit:
                self.conn.commit()
            return cursor
        except sqlite3.Error as e:
            logger.error(f"Query execution failed: {e}")
            if self.conn:
                self.conn.rollback()
            raise
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

class StudentAccount:
    """Represents a student account in the cashless payment system."""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
    
    def create_student(self, name: str, grade: str, initial_balance: float = 0.0, pin: str = None) -> str:
        """Create a new student account with a unique ID and PIN."""
        if pin is None:
            pin = str(uuid.uuid4().int)[:4]  # Generate a 4-digit PIN if not provided
        
        student_id = f"S{str(uuid.uuid4().int)[:8]}"
        pin_hash = self._hash_pin(pin)
        
        try:
            self.db.execute_query(
                '''INSERT INTO students (student_id, name, grade, balance, pin_hash)
                   VALUES (?, ?, ?, ?, ?)''',
                (student_id, name, grade, initial_balance, pin_hash),
                commit=True
            )
            logger.info(f"Created new student account: {student_id}")
            return student_id
        except sqlite3.Error as e:
            logger.error(f"Failed to create student account: {e}")
            raise
    
    def authenticate_student(self, student_id: str, pin: str) -> bool:
        """Authenticate a student using their ID and PIN."""
        try:
            cursor = self.db.execute_query(
                "SELECT pin_hash FROM students WHERE student_id = ? AND is_active = 1",
                (student_id,)
            )
            result = cursor.fetchone()
            if result:
                stored_hash = result[0]
                return self._verify_pin(pin, stored_hash)
            return False
        except sqlite3.Error as e:
            logger.error(f"Authentication failed for student {student_id}: {e}")
            raise
    
    def get_balance(self, student_id: str) -> float:
        """Get the current balance of a student's account."""
        try:
            cursor = self.db.execute_query(
                "SELECT balance FROM students WHERE student_id = ?",
                (student_id,)
            )
            result = cursor.fetchone()
            return result[0] if result else 0.0
        except sqlite3.Error as e:
            logger.error(f"Failed to get balance for student {student_id}: {e}")
            raise
    
    def add_funds(self, student_id: str, amount: float, description: str = "Funds added") -> bool:
        """Add funds to a student's account."""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        try:
            # Update balance
            self.db.execute_query(
                "UPDATE students SET balance = balance + ? WHERE student_id = ?",
                (amount, student_id),
                commit=True
            )
            
            # Record transaction
            self._record_transaction(
                student_id,
                amount,
                "DEPOSIT",
                description
            )
            
            logger.info(f"Added {amount} to student {student_id}'s account")
            return True
        except sqlite3.Error as e:
            logger.error(f"Failed to add funds to student {student_id}'s account: {e}")
            raise
    
    def make_purchase(self, student_id: str, amount: float, description: str = "Meal purchase") -> bool:
        """Deduct funds from a student's account for a purchase."""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        current_balance = self.get_balance(student_id)
        if current_balance < amount:
            raise ValueError("Insufficient funds")
        
        try:
            # Update balance
            self.db.execute_query(
                "UPDATE students SET balance = balance - ? WHERE student_id = ?",
                (amount, student_id),
                commit=True
            )
            
            # Record transaction
            self._record_transaction(
                student_id,
                -amount,
                "PURCHASE",
                description
            )
            
            logger.info(f"Deducted {amount} from student {student_id}'s account")
            return True
        except sqlite3.Error as e:
            logger.error(f"Failed to process purchase for student {student_id}: {e}")
            raise
    
    def get_transaction_history(self, student_id: str, limit: int = 10) -> List[Dict]:
        """Get transaction history for a student."""
        try:
            cursor = self.db.execute_query(
                '''SELECT transaction_id, amount, transaction_type, timestamp, description
                   FROM transactions
                   WHERE student_id = ?
                   ORDER BY timestamp DESC
                   LIMIT ?''',
                (student_id, limit)
            )
            
            transactions = []
            for row in cursor.fetchall():
                transactions.append({
                    'transaction_id': row[0],
                    'amount': row[1],
                    'type': row[2],
                    'timestamp': row[3],
                    'description': row[4]
                })
            
            return transactions
        except sqlite3.Error as e:
            logger.error(f"Failed to get transaction history for student {student_id}: {e}")
            raise
    
    def _record_transaction(self, student_id: str, amount: float, transaction_type: str, description: str) -> None:
        """Record a transaction in the database."""
        transaction_id = f"T{str(uuid.uuid4().int)[:8]}"
        timestamp = datetime.now().isoformat()
        
        self.db.execute_query(
            '''INSERT INTO transactions
               (transaction_id, student_id, amount, transaction_type, timestamp, description)
               VALUES (?, ?, ?, ?, ?, ?)''',
            (transaction_id, student_id, amount, transaction_type, timestamp, description),
            commit=True
        )
    
    @staticmethod
    def _hash_pin(pin: str) -> str:
        """Hash a PIN for secure storage."""
        return hashlib.sha256(pin.encode()).hexdigest()
    
    @staticmethod
    def _verify_pin(pin: str, stored_hash: str) -> bool:
        """Verify a PIN against its stored hash."""
        return hashlib.sha256(pin.encode()).hexdigest() == stored_hash

class MealManagement:
    """Manages meal items and categories in the system."""
    
    def __init__(self, db_manager: Database
