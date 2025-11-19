"""
Generated Code Metadata:
========================
Original URL: https://colegiodepsicologosoruro.org
Prompt: Generate code to integrate a discount system for psychological tests, as mentioned in the Colegio de Psicólogos de Oruro's partnership with AMI-Bolivia, using Python and a database management system.
Generated: DETERMINISTIC_dc09cf18a56fad9e
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime, timedelta
from typing import Optional, Union

class DiscountSystem:
    """
    A discount system for psychological tests integrated with a database.
    Handles discount codes, validation, and application to tests.
    """
    
    def __init__(self, db_path: str = "discount_system.db"):
        """
        Initialize the discount system with a SQLite database.
        
        Args:
            db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Create necessary tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Create discount_codes table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS discount_codes (
                    code TEXT PRIMARY KEY,
                    discount_percent INTEGER NOT NULL,
                    valid_from DATE NOT NULL,
                    valid_until DATE NOT NULL,
                    max_uses INTEGER NOT NULL,
                    current_uses INTEGER DEFAULT 0,
                    is_active BOOLEAN DEFAULT TRUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create test_applications table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS test_applications (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    test_id TEXT NOT NULL,
                    patient_id TEXT NOT NULL,
                    original_price REAL NOT NULL,
                    final_price REAL NOT NULL,
                    discount_code TEXT,
                    applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (discount_code) REFERENCES discount_codes(code)
                )
            """)
            
            conn.commit()
    
    def create_discount_code(
        self,
        code: str,
        discount_percent: int,
        valid_days: int,
        max_uses: int
    ) -> bool:
        """
        Create a new discount code.
        
        Args:
            code: The discount code string
            discount_percent: Percentage discount (0-100)
            valid_days: Number of days the code is valid from today
            max_uses: Maximum number of times this code can be used
            
        Returns:
            bool: True if creation was successful, False otherwise
        """
        if not (0 <= discount_percent <= 100):
            raise ValueError("Discount percent must be between 0 and 100")
        
        if valid_days <= 0:
            raise ValueError("Valid days must be positive")
        
        if max_uses <= 0:
            raise ValueError("Max uses must be positive")
        
        valid_from = datetime.now().date()
        valid_until = valid_from + timedelta(days=valid_days)
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO discount_codes (
                        code, discount_percent, valid_from, valid_until, max_uses
                    ) VALUES (?, ?, ?, ?, ?)
                """, (code, discount_percent, valid_from, valid_until, max_uses))
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            return False
    
    def validate_discount_code(self, code: str) -> dict:
        """
        Validate a discount code and return its details if valid.
        
        Args:
            code: The discount code to validate
            
        Returns:
            dict: Dictionary with code details if valid, None otherwise
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT * FROM discount_codes 
                WHERE code = ? AND is_active = TRUE
            """, (code,))
            
            result = cursor.fetchone()
            
            if not result:
                return None
                
            today = datetime.now().date()
            valid_from = datetime.strptime(result["valid_from"], "%Y-%m-%d").date()
            valid_until = datetime.strptime(result["valid_until"], "%Y-%m-%d").date()
            
            if today < valid_from or today > valid_until:
                return None
                
            if result["current_uses"] >= result["max_uses"]:
                return None
                
            return dict(result)
    
    def apply_discount_to_test(
        self,
        test_id: str,
        patient_id: str,
        original_price: float,
        discount_code: Optional[str] = None
    ) -> Union[dict, None]:
        """
        Apply a discount to a psychological test.
        
        Args:
            test_id: ID of the psychological test
            patient_id: ID of the patient
            original_price: Original price of the test
            discount_code: Optional discount code to apply
            
        Returns:
            dict: Dictionary with application details including final price
            None: If discount code is invalid
        """
        discount_details = None
        
        if discount_code:
            discount_details = self.validate_discount_code(discount_code)
            if not discount_details:
                return None
            
        final_price = original_price
        if discount_details:
            discount = original_price * (discount_details["discount_percent"] / 100)
            final_price = original_price - discount
            
            # Update discount code usage
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE discount_codes 
                    SET current_uses = current_uses + 1 
                    WHERE code = ?
                """, (discount_code,))
                conn.commit()
        
        # Record the test application
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO test_applications (
                    test_id, patient_id, original_price, final_price, discount_code
                ) VALUES (?, ?, ?, ?, ?)
            """, (test_id, patient_id, original_price, final_price, discount_code))
            conn.commit()
        
        return {
            "test_id": test_id,
            "patient_id": patient_id,
            "original_price": original_price,
            "final_price": final_price,
            "discount_code": discount_code,
            "discount_percent": discount_details["discount_percent"] if discount_details else 0
        }
    
    def get_test_application_history(
        self,
        patient_id: Optional[str] = None,
        test_id: Optional[str] = None,
        limit: int = 100
    ) -> list:
        """
        Get history of test applications with optional filters.
        
        Args:
            patient_id: Filter by patient ID
            test_id: Filter by test ID
            limit: Maximum number of records to return
            
        Returns:
            list: List of test application records
        """
        query = "SELECT * FROM test_applications"
        params = []
        conditions = []
        
        if patient_id:
            conditions.append("patient_id = ?")
            params.append(patient_id)
        
        if test_id:
            conditions.append("test_id = ?")
            params.append(test_id)
        
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        
        query += " ORDER BY applied_at DESC LIMIT ?"
        params.append(limit)
        
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(query, params)
            return [dict(row) for row in cursor.fetchall()]
    
    def deactivate_discount_code(self, code: str) -> bool:
        """
        Deactivate a discount code.
        
        Args:
            code: The discount code to deactivate
            
        Returns:
            bool: True if deactivation was successful, False otherwise
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE discount_codes 
                SET is_active = FALSE 
                WHERE code = ?
            """, (code,))
            conn.commit()
            return cursor.rowcount > 0
```
