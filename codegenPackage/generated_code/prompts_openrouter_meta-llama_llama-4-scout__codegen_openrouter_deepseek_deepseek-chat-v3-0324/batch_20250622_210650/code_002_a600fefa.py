"""
Generated Code Metadata:
========================
Original URL: https://vogellust.nl
Prompt: Generate a Python script to manage a bird-keeping club's membership database, including functions for adding, removing, and updating member information.
Generated: DETERMINISTIC_a600fefab18c95a1
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
from typing import Optional, Dict, List

class BirdClubDatabase:
    """A class to manage a bird-keeping club's membership database."""
    
    def __init__(self, db_name: str = "bird_club.db"):
        """Initialize the database connection and create tables if they don't exist.
        
        Args:
            db_name: Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create the necessary tables in the database if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS members (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT,
                join_date TEXT NOT NULL,
                membership_type TEXT NOT NULL
            )
        """)
        self.conn.commit()
    
    def add_member(self, name: str, email: str, phone: str, join_date: str, membership_type: str) -> bool:
        """Add a new member to the database.
        
        Args:
            name: Full name of the member.
            email: Email address (must be unique).
            phone: Phone number (optional).
            join_date: Date joined in YYYY-MM-DD format.
            membership_type: Type of membership (e.g., 'regular', 'premium').
            
        Returns:
            bool: True if member was added successfully, False otherwise.
        """
        try:
            self.cursor.execute("""
                INSERT INTO members (name, email, phone, join_date, membership_type)
                VALUES (?, ?, ?, ?, ?)
            """, (name, email, phone, join_date, membership_type))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            print("Error: Email already exists in the database.")
            return False
        except Exception as e:
            print(f"Error adding member: {e}")
            return False
    
    def remove_member(self, member_id: int) -> bool:
        """Remove a member from the database by their ID.
        
        Args:
            member_id: The ID of the member to remove.
            
        Returns:
            bool: True if member was removed successfully, False otherwise.
        """
        try:
            self.cursor.execute("DELETE FROM members WHERE id = ?", (member_id,))
            if self.cursor.rowcount == 0:
                print("No member found with that ID.")
                return False
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error removing member: {e}")
            return False
    
    def update_member(self, member_id: int, updates: Dict[str, str]) -> bool:
        """Update a member's information.
        
        Args:
            member_id: The ID of the member to update.
            updates: Dictionary of fields to update with their new values.
            
        Returns:
            bool: True if member was updated successfully, False otherwise.
        """
        if not updates:
            print("No updates provided.")
            return False
            
        set_clause = ", ".join([f"{key} = ?" for key in updates.keys()])
        values = list(updates.values())
        values.append(member_id)
        
        try:
            self.cursor.execute(f"""
                UPDATE members
                SET {set_clause}
                WHERE id = ?
            """, values)
            
            if self.cursor.rowcount == 0:
                print("No member found with that ID.")
                return False
                
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            print("Error: Email must be unique.")
            return False
        except Exception as e:
            print(f"Error updating member: {e}")
            return False
    
    def get_member(self, member_id: int) -> Optional[Dict[str, str]]:
        """Retrieve a member's information by their ID.
        
        Args:
            member_id: The ID of the member to retrieve.
            
        Returns:
            Optional[Dict[str, str]]: Dictionary of member info if found, None otherwise.
        """
        try:
            self.cursor.execute("""
                SELECT id, name, email, phone, join_date, membership_type
                FROM members
                WHERE id = ?
            """, (member_id,))
            result = self.cursor.fetchone()
            
            if result:
                return {
                    "id": result[0],
                    "name": result[1],
                    "email": result[2],
                    "phone": result[3],
                    "join_date": result[4],
                    "membership_type": result[5]
                }
            return None
        except Exception as e:
            print(f"Error retrieving member: {e}")
            return None
    
    def get_all_members(self) -> List[Dict[str, str]]:
        """Retrieve all members in the database.
        
        Returns:
            List[Dict[str, str]]: List of dictionaries containing member information.
        """
        try:
            self.cursor.execute("""
                SELECT id, name, email, phone, join_date, membership_type
                FROM members
                ORDER BY name
            """)
            results = self.cursor.fetchall()
            
            return [{
                "id": row[0],
                "name": row[1],
                "email": row[2],
                "phone": row[3],
                "join_date": row[4],
                "membership_type": row[5]
            } for row in results]
        except Exception as e:
            print(f"Error retrieving members: {e}")
            return []
    
    def search_members(self, search_term: str) -> List[Dict[str, str]]:
        """Search for members by name or email.
        
        Args:
            search_term: String to search for in names or emails.
            
        Returns:
            List[Dict[str, str]]: List of matching members.
        """
        try:
            search_term = f"%{search_term}%"
            self.cursor.execute("""
                SELECT id, name, email, phone, join_date, membership_type
                FROM members
                WHERE name LIKE ? OR email LIKE ?
                ORDER BY name
            """, (search_term, search_term))
            results = self.cursor.fetchall()
            
            return [{
                "id": row[0],
                "name": row[1],
                "email": row[2],
                "phone": row[3],
                "join_date": row[4],
                "membership_type": row[5]
            } for row in results]
        except Exception as e:
            print(f"Error searching members: {e}")
            return []
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        """Enable use of context manager."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ensure connection is closed when exiting context."""
        self.close()
```
