"""
Generated Code Metadata:
========================
Original URL: https://cle.com
Prompt: Generate code to create a searchable database of CLE International conferences, including fields for conference name, location, date, and topic (e.g., Tribal Water Law or Florida Eminent Domain).
Generated: DETERMINISTIC_33f85743bbeb729e
Batch ID: 20250612_150440
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
from typing import List, Dict, Optional

class CLEConferenceDatabase:
    """
    A class to manage a searchable database of CLE International conferences.
    """
    
    def __init__(self, db_name: str = "cle_conferences.db"):
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
            CREATE TABLE IF NOT EXISTS conferences (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                location TEXT NOT NULL,
                date TEXT NOT NULL,
                topic TEXT NOT NULL
            )
        """)
        self.conn.commit()
    
    def add_conference(self, name: str, location: str, date: str, topic: str) -> int:
        """
        Add a new conference to the database.
        
        Args:
            name: Conference name
            location: Conference location
            date: Conference date (format: YYYY-MM-DD)
            topic: Conference topic
            
        Returns:
            The ID of the newly inserted conference
            
        Raises:
            ValueError: If date format is invalid
        """
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
            
        self.cursor.execute("""
            INSERT INTO conferences (name, location, date, topic)
            VALUES (?, ?, ?, ?)
        """, (name, location, date, topic))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def search_conferences(
        self,
        name: Optional[str] = None,
        location: Optional[str] = None,
        date: Optional[str] = None,
        topic: Optional[str] = None
    ) -> List[Dict[str, str]]:
        """
        Search for conferences based on various criteria.
        
        Args:
            name: Conference name (partial match)
            location: Conference location (partial match)
            date: Conference date (exact match, format: YYYY-MM-DD)
            topic: Conference topic (partial match)
            
        Returns:
            List of dictionaries containing conference information
            
        Raises:
            ValueError: If date format is invalid when provided
        """
        query = "SELECT * FROM conferences WHERE 1=1"
        params = []
        
        if name:
            query += " AND name LIKE ?"
            params.append(f"%{name}%")
            
        if location:
            query += " AND location LIKE ?"
            params.append(f"%{location}%")
            
        if date:
            try:
                datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
            query += " AND date = ?"
            params.append(date)
            
        if topic:
            query += " AND topic LIKE ?"
            params.append(f"%{topic}%")
            
        self.cursor.execute(query, params)
        columns = [col[0] for col in self.cursor.description]
        results = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
        return results
    
    def get_all_conferences(self) -> List[Dict[str, str]]:
        """Get all conferences in the database."""
        self.cursor.execute("SELECT * FROM conferences")
        columns = [col[0] for col in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    def delete_conference(self, conference_id: int) -> bool:
        """
        Delete a conference from the database.
        
        Args:
            conference_id: ID of the conference to delete
            
        Returns:
            True if deletion was successful, False otherwise
        """
        self.cursor.execute("DELETE FROM conferences WHERE id = ?", (conference_id,))
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


# Example usage
if __name__ == "__main__":
    with CLEConferenceDatabase() as db:
        # Add sample conferences
        db.add_conference(
            name="Tribal Water Law Conference",
            location="Denver, CO",
            date="2023-11-15",
            topic="Tribal Water Law"
        )
        
        db.add_conference(
            name="Florida Eminent Domain Summit",
            location="Orlando, FL",
            date="2023-12-05",
            topic="Florida Eminent Domain"
        )
        
        # Search for conferences
        print("All conferences:")
        for conference in db.get_all_conferences():
            print(conference)
        
        print("\nSearch for water-related conferences:")
        results = db.search_conferences(topic="Water")
        for conference in results:
            print(conference)
```
