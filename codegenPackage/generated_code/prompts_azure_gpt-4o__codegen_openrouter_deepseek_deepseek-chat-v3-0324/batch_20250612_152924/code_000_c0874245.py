"""
Generated Code Metadata:
========================
Original URL: https://rapidresponder.net
Prompt: Write Python code to simulate tracing stolen funds using a database of transaction records, incorporating methods for verifying ID points as described by Rapid Responder.
Generated: DETERMINISTIC_c08742450ac7120b
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Dict, Optional, Tuple
import hashlib
from datetime import datetime

class TransactionTracer:
    """
    A class to simulate tracing stolen funds using a database of transaction records.
    Incorporates methods for verifying ID points as described by Rapid Responder.
    """
    
    def __init__(self, db_path: str = "transactions.db"):
        """
        Initialize the TransactionTracer with a SQLite database connection.
        
        Args:
            db_path (str): Path to the SQLite database file. Defaults to "transactions.db".
        """
        self.db_path = db_path
        self.conn = None
        self._initialize_db()
    
    def _initialize_db(self) -> None:
        """Initialize the database with required tables if they don't exist."""
        try:
            self.conn = sqlite3.connect(self.db_path)
            cursor = self.conn.cursor()
            
            # Create transactions table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS transactions (
                    tx_id TEXT PRIMARY KEY,
                    sender_id TEXT NOT NULL,
                    receiver_id TEXT NOT NULL,
                    amount REAL NOT NULL,
                    timestamp DATETIME NOT NULL,
                    is_stolen BOOLEAN DEFAULT FALSE
                )
            """)
            
            # Create id_verification_points table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS id_verification_points (
                    point_id TEXT PRIMARY KEY,
                    user_id TEXT NOT NULL,
                    verification_type TEXT NOT NULL,
                    verification_data TEXT NOT NULL,
                    timestamp DATETIME NOT NULL,
                    is_valid BOOLEAN DEFAULT TRUE
                )
            """)
            
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database initialization error: {e}")
            if self.conn:
                self.conn.rollback()
            raise
    
    def add_transaction(self, tx_id: str, sender_id: str, receiver_id: str, 
                       amount: float, timestamp: datetime, is_stolen: bool = False) -> bool:
        """
        Add a transaction record to the database.
        
        Args:
            tx_id: Unique transaction ID
            sender_id: Sender's user ID
            receiver_id: Receiver's user ID
            amount: Transaction amount
            timestamp: Transaction timestamp
            is_stolen: Whether the funds are marked as stolen
            
        Returns:
            bool: True if transaction was added successfully, False otherwise
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO transactions 
                (tx_id, sender_id, receiver_id, amount, timestamp, is_stolen)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (tx_id, sender_id, receiver_id, amount, timestamp, is_stolen))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error adding transaction: {e}")
            self.conn.rollback()
            return False
    
    def mark_as_stolen(self, tx_id: str) -> bool:
        """
        Mark a transaction as containing stolen funds.
        
        Args:
            tx_id: Transaction ID to mark as stolen
            
        Returns:
            bool: True if update was successful, False otherwise
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                UPDATE transactions 
                SET is_stolen = TRUE 
                WHERE tx_id = ?
            """, (tx_id,))
            self.conn.commit()
            return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error marking transaction as stolen: {e}")
            self.conn.rollback()
            return False
    
    def add_id_verification_point(self, user_id: str, verification_type: str, 
                                 verification_data: str, timestamp: datetime) -> str:
        """
        Add an ID verification point to the database.
        
        Args:
            user_id: User ID being verified
            verification_type: Type of verification (e.g., "email", "phone", "document")
            verification_data: The verification data (hashed for privacy)
            timestamp: When the verification occurred
            
        Returns:
            str: The generated point_id, or empty string on failure
        """
        try:
            # Generate a unique point ID by hashing the data
            hash_input = f"{user_id}{verification_type}{verification_data}{timestamp}"
            point_id = hashlib.sha256(hash_input.encode()).hexdigest()
            
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO id_verification_points 
                (point_id, user_id, verification_type, verification_data, timestamp)
                VALUES (?, ?, ?, ?, ?)
            """, (point_id, user_id, verification_type, verification_data, timestamp))
            
            self.conn.commit()
            return point_id
        except sqlite3.Error as e:
            print(f"Error adding ID verification point: {e}")
            self.conn.rollback()
            return ""
    
    def verify_id_point(self, point_id: str) -> bool:
        """
        Verify an ID verification point.
        
        Args:
            point_id: The ID verification point to check
            
        Returns:
            bool: True if the point is valid, False otherwise
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT is_valid FROM id_verification_points 
                WHERE point_id = ?
            """, (point_id,))
            
            result = cursor.fetchone()
            return result is not None and result[0] == 1
        except sqlite3.Error as e:
            print(f"Error verifying ID point: {e}")
            return False
    
    def trace_funds(self, origin_tx_id: str, max_depth: int = 5) -> List[Dict]:
        """
        Trace stolen funds through subsequent transactions.
        
        Args:
            origin_tx_id: The original transaction ID containing stolen funds
            max_depth: Maximum levels of transactions to trace
            
        Returns:
            List[Dict]: List of transaction paths containing stolen funds
        """
        try:
            # First verify the origin transaction is marked as stolen
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT is_stolen FROM transactions 
                WHERE tx_id = ?
            """, (origin_tx_id,))
            
            result = cursor.fetchone()
            if not result or not result[0]:
                return []
            
            # Perform recursive tracing
            traced_paths = []
            self._recursive_trace(origin_tx_id, [], traced_paths, max_depth)
            return traced_paths
        except sqlite3.Error as e:
            print(f"Error tracing funds: {e}")
            return []
    
    def _recursive_trace(self, current_tx_id: str, current_path: List, 
                         traced_paths: List, remaining_depth: int) -> None:
        """
        Recursive helper function for tracing funds.
        """
        if remaining_depth <= 0:
            return
        
        try:
            cursor = self.conn.cursor()
            
            # Get the current transaction details
            cursor.execute("""
                SELECT tx_id, sender_id, receiver_id, amount, timestamp 
                FROM transactions 
                WHERE tx_id = ?
            """, (current_tx_id,))
            tx_data = cursor.fetchone()
            
            if not tx_data:
                return
            
            tx_id, sender_id, receiver_id, amount, timestamp = tx_data
            current_path.append({
                "tx_id": tx_id,
                "sender_id": sender_id,
                "receiver_id": receiver_id,
                "amount": amount,
                "timestamp": timestamp
            })
            
            # Find all transactions where the receiver is the sender
            cursor.execute("""
                SELECT tx_id FROM transactions 
                WHERE sender_id = ? AND tx_id != ?
            """, (receiver_id, tx_id))
            
            next_transactions = cursor.fetchall()
            
            if not next_transactions:
                traced_paths.append(current_path.copy())
            else:
                for next_tx in next_transactions:
                    self._recursive_trace(
                        next_tx[0], 
                        current_path.copy(), 
                        traced_paths, 
                        remaining_depth - 1
                    )
        except sqlite3.Error as e:
            print(f"Error in recursive tracing: {e}")
    
    def get_user_verification_score(self, user_id: str) -> float:
        """
        Calculate a verification score for a user based on their ID points.
        
        Args:
            user_id: The user ID to calculate score for
            
        Returns:
            float: Verification score between 0 and 1
        """
        try:
            cursor = self.conn.cursor()
            
            # Count valid verification points
            cursor.execute("""
                SELECT COUNT(*) FROM id_verification_points 
                WHERE user_id = ? AND is_valid = TRUE
            """, (user_id,))
            valid_points = cursor.fetchone()[0] or 0
            
            # Count total verification points
            cursor.execute("""
                SELECT COUNT(*) FROM id_verification_points 
                WHERE user_id = ?
            """, (user_id,))
            total_points = cursor.fetchone()[0] or 1  # Avoid division by zero
            
            return valid_points / total
