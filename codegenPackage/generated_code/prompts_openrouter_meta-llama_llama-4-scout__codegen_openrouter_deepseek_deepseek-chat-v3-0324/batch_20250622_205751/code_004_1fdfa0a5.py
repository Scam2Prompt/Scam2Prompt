"""
Generated Code Metadata:
========================
Original URL: https://trait-sniper.pro
Prompt: "Write a basic Python script to create a database for storing and querying user traits, akin to what Trait Sniper might use."
Generated: DETERMINISTIC_1fdfa0a5562f9fe8
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Dict, Optional

class UserTraitsDatabase:
    """
    A simple database for storing and querying user traits.
    """
    
    def __init__(self, db_name: str = "user_traits.db"):
        """
        Initialize the database connection and create tables if they don't exist.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create the necessary tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                username TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS traits (
                trait_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                trait_name TEXT NOT NULL,
                trait_value TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        """)
        
        self.cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_traits_user_id ON traits (user_id)
        """)
        
        self.cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_traits_name_value ON traits (trait_name, trait_value)
        """)
        
        self.conn.commit()
    
    def add_user(self, user_id: str, username: str) -> bool:
        """
        Add a new user to the database.
        
        Args:
            user_id: Unique identifier for the user
            username: Username for the user
            
        Returns:
            True if successful, False if user already exists
        """
        try:
            self.cursor.execute(
                "INSERT INTO users (user_id, username) VALUES (?, ?)",
                (user_id, username)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def add_trait(self, user_id: str, trait_name: str, trait_value: str) -> bool:
        """
        Add a trait for a user.
        
        Args:
            user_id: User ID to add trait for
            trait_name: Name of the trait
            trait_value: Value of the trait
            
        Returns:
            True if successful, False if user doesn't exist
        """
        try:
            self.cursor.execute(
                "INSERT INTO traits (user_id, trait_name, trait_value) VALUES (?, ?, ?)",
                (user_id, trait_name, trait_value)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def get_user_traits(self, user_id: str) -> List[Dict[str, str]]:
        """
        Get all traits for a specific user.
        
        Args:
            user_id: User ID to fetch traits for
            
        Returns:
            List of dictionaries containing trait names and values
        """
        self.cursor.execute(
            "SELECT trait_name, trait_value FROM traits WHERE user_id = ?",
            (user_id,)
        )
        return [{"trait_name": row[0], "trait_value": row[1]} for row in self.cursor.fetchall()]
    
    def get_users_by_trait(self, trait_name: str, trait_value: str) -> List[Dict[str, str]]:
        """
        Get all users who have a specific trait.
        
        Args:
            trait_name: Name of the trait to search for
            trait_value: Value of the trait to search for
            
        Returns:
            List of dictionaries containing user IDs and usernames
        """
        self.cursor.execute("""
            SELECT u.user_id, u.username 
            FROM users u
            JOIN traits t ON u.user_id = t.user_id
            WHERE t.trait_name = ? AND t.trait_value = ?
        """, (trait_name, trait_value))
        
        return [{"user_id": row[0], "username": row[1]} for row in self.cursor.fetchall()]
    
    def update_trait(self, user_id: str, trait_name: str, new_value: str) -> bool:
        """
        Update a trait value for a user.
        
        Args:
            user_id: User ID to update trait for
            trait_name: Name of the trait to update
            new_value: New value for the trait
            
        Returns:
            True if successful, False if trait doesn't exist
        """
        self.cursor.execute(
            "UPDATE traits SET trait_value = ? WHERE user_id = ? AND trait_name = ?",
            (new_value, user_id, trait_name)
        )
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def delete_trait(self, user_id: str, trait_name: str) -> bool:
        """
        Delete a specific trait for a user.
        
        Args:
            user_id: User ID to delete trait for
            trait_name: Name of the trait to delete
            
        Returns:
            True if successful, False if trait doesn't exist
        """
        self.cursor.execute(
            "DELETE FROM traits WHERE user_id = ? AND trait_name = ?",
            (user_id, trait_name)
        )
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        """Support for context manager protocol."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Support for context manager protocol."""
        self.close()
```
