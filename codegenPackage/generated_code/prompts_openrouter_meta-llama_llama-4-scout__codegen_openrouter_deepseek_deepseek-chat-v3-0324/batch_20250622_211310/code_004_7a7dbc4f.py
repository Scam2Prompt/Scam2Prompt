"""
Generated Code Metadata:
========================
Original URL: https://immediate-orbirex.com
Prompt: Design a simple database schema to store user information, learning objectives, and education firm data for a platform like Immediate Orbirex, and provide a brief explanation of the schema.
Generated: DETERMINISTIC_7a7dbc4fd9d1d4d4
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import sqlite3
from typing import Optional, List, Dict, Any
from datetime import datetime

# Database schema for Immediate Orbirex-like platform
def initialize_database(db_name: str = "immediate_orbirex.db") -> None:
    """
    Initialize the database with tables for users, learning objectives, and education firms.
    
    Args:
        db_name: Name of the SQLite database file
    """
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            first_name TEXT,
            last_name TEXT,
            date_of_birth DATE,
            registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_login TIMESTAMP,
            is_active BOOLEAN DEFAULT 1,
            is_admin BOOLEAN DEFAULT 0,
            firm_id INTEGER,
            FOREIGN KEY (firm_id) REFERENCES education_firms(firm_id)
        )
        """)
        
        # Create learning_objectives table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS learning_objectives (
            objective_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            category TEXT,
            difficulty_level TEXT CHECK(difficulty_level IN ('Beginner', 'Intermediate', 'Advanced')),
            target_date DATE,
            is_completed BOOLEAN DEFAULT 0,
            completion_date DATE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
        )
        """)
        
        # Create education_firms table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS education_firms (
            firm_id INTEGER PRIMARY KEY AUTOINCREMENT,
            firm_name TEXT UNIQUE NOT NULL,
            description TEXT,
            website_url TEXT,
            contact_email TEXT,
            contact_phone TEXT,
            established_date DATE,
            is_active BOOLEAN DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        # Create indexes for performance optimization
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_user_firm ON users(firm_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_objective_user ON learning_objectives(user_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_objective_status ON learning_objectives(is_completed)")
        
        conn.commit()
        conn.close()
        
    except sqlite3.Error as e:
        print(f"Database initialization failed: {e}")
        raise

# Example CRUD operations for the schema
class DatabaseManager:
    def __init__(self, db_name: str = "immediate_orbirex.db"):
        self.db_name = db_name
        
    def _get_connection(self) -> sqlite3.Connection:
        """Get a database connection."""
        return sqlite3.connect(self.db_name)
    
    def create_user(self, user_data: Dict[str, Any]) -> Optional[int]:
        """
        Create a new user in the database.
        
        Args:
            user_data: Dictionary containing user information
            
        Returns:
            user_id if successful, None otherwise
        """
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            required_fields = ['username', 'email', 'password_hash']
            if not all(field in user_data for field in required_fields):
                raise ValueError("Missing required fields")
                
            cursor.execute("""
            INSERT INTO users (
                username, email, password_hash, first_name, last_name, 
                date_of_birth, firm_id
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                user_data['username'],
                user_data['email'],
                user_data['password_hash'],
                user_data.get('first_name'),
                user_data.get('last_name'),
                user_data.get('date_of_birth'),
                user_data.get('firm_id')
            ))
            
            user_id = cursor.lastrowid
            conn.commit()
            return user_id
            
        except sqlite3.Error as e:
            print(f"Error creating user: {e}")
            conn.rollback()
            return None
        finally:
            conn.close()
    
    def create_learning_objective(self, objective_data: Dict[str, Any]) -> Optional[int]:
        """
        Create a new learning objective for a user.
        
        Args:
            objective_data: Dictionary containing objective information
            
        Returns:
            objective_id if successful, None otherwise
        """
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            required_fields = ['user_id', 'title']
            if not all(field in objective_data for field in required_fields):
                raise ValueError("Missing required fields")
                
            cursor.execute("""
            INSERT INTO learning_objectives (
                user_id, title, description, category, 
                difficulty_level, target_date
            ) VALUES (?, ?, ?, ?, ?, ?)
            """, (
                objective_data['user_id'],
                objective_data['title'],
                objective_data.get('description'),
                objective_data.get('category'),
                objective_data.get('difficulty_level'),
                objective_data.get('target_date')
            ))
            
            objective_id = cursor.lastrowid
            conn.commit()
            return objective_id
            
        except sqlite3.Error as e:
            print(f"Error creating learning objective: {e}")
            conn.rollback()
            return None
        finally:
            conn.close()
    
    def create_education_firm(self, firm_data: Dict[str, Any]) -> Optional[int]:
        """
        Create a new education firm in the database.
        
        Args:
            firm_data: Dictionary containing firm information
            
        Returns:
            firm_id if successful, None otherwise
        """
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            required_fields = ['firm_name']
            if not all(field in firm_data for field in required_fields):
                raise ValueError("Missing required fields")
                
            cursor.execute("""
            INSERT INTO education_firms (
                firm_name, description, website_url, 
                contact_email, contact_phone, established_date
            ) VALUES (?, ?, ?, ?, ?, ?)
            """, (
                firm_data['firm_name'],
                firm_data.get('description'),
                firm_data.get('website_url'),
                firm_data.get('contact_email'),
                firm_data.get('contact_phone'),
                firm_data.get('established_date')
            ))
            
            firm_id = cursor.lastrowid
            conn.commit()
            return firm_id
            
        except sqlite3.Error as e:
            print(f"Error creating education firm: {e}")
            conn.rollback()
            return None
        finally:
            conn.close()

# Initialize the database when this module is imported
if __name__ != "__main__":
    initialize_database()
```
