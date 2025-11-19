"""
Generated Code Metadata:
========================
Original URL: https://teeny-activity-colossal.on-fleek.app
Prompt: "Generate a Python script to create a simple database for organizing comic book volumes and issues like 'Top G' #3.1 'Parallel Protocols'."
Generated: DETERMINISTIC_c1f9349d0596bbb3
Batch ID: 20250622_205030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import Optional, List, Tuple

class ComicBookDatabase:
    """
    A simple database for organizing comic book volumes and issues.
    """

    def __init__(self, db_name: str = "comic_books.db"):
        """
        Initialize the database connection and create tables if they don't exist.
        
        Args:
            db_name: Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self) -> None:
        """Create the necessary tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS volumes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                publisher TEXT,
                year INTEGER,
                UNIQUE(title, publisher)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS issues (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                volume_id INTEGER NOT NULL,
                issue_number TEXT NOT NULL,
                title TEXT,
                release_date TEXT,
                FOREIGN KEY (volume_id) REFERENCES volumes(id),
                UNIQUE(volume_id, issue_number)
            )
        """)
        self.conn.commit()

    def add_volume(self, title: str, publisher: Optional[str] = None, year: Optional[int] = None) -> int:
        """
        Add a new comic volume to the database.
        
        Args:
            title: Title of the volume.
            publisher: Publisher of the volume.
            year: Year of publication.
            
        Returns:
            The ID of the newly inserted volume.
            
        Raises:
            sqlite3.IntegrityError: If volume already exists.
        """
        self.cursor.execute(
            "INSERT INTO volumes (title, publisher, year) VALUES (?, ?, ?)",
            (title, publisher, year)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def add_issue(self, volume_id: int, issue_number: str, title: Optional[str] = None, release_date: Optional[str] = None) -> int:
        """
        Add a new issue to a volume.
        
        Args:
            volume_id: ID of the parent volume.
            issue_number: Issue number (can include decimals like '3.1').
            title: Title of the issue.
            release_date: Release date as string (YYYY-MM-DD format recommended).
            
        Returns:
            The ID of the newly inserted issue.
            
        Raises:
            sqlite3.IntegrityError: If issue already exists or volume_id is invalid.
        """
        self.cursor.execute(
            "INSERT INTO issues (volume_id, issue_number, title, release_date) VALUES (?, ?, ?, ?)",
            (volume_id, issue_number, title, release_date)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def get_volumes(self) -> List[Tuple]:
        """Get all volumes from the database."""
        self.cursor.execute("SELECT * FROM volumes")
        return self.cursor.fetchall()

    def get_issues_by_volume(self, volume_id: int) -> List[Tuple]:
        """Get all issues for a specific volume."""
        self.cursor.execute("SELECT * FROM issues WHERE volume_id = ?", (volume_id,))
        return self.cursor.fetchall()

    def search_volumes(self, search_term: str) -> List[Tuple]:
        """Search volumes by title."""
        self.cursor.execute("SELECT * FROM volumes WHERE title LIKE ?", (f"%{search_term}%",))
        return self.cursor.fetchall()

    def search_issues(self, search_term: str) -> List[Tuple]:
        """Search issues by title."""
        self.cursor.execute("SELECT * FROM issues WHERE title LIKE ?", (f"%{search_term}%",))
        return self.cursor.fetchall()

    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()

    def __enter__(self):
        """Enable usage in 'with' statements."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ensure connection is closed when exiting 'with' block."""
        self.close()


# Example usage
if __name__ == "__main__":
    with ComicBookDatabase() as db:
        try:
            # Add a volume
            volume_id = db.add_volume("Top G", "Comic Publisher Inc.", 2023)
            
            # Add an issue to the volume
            db.add_issue(volume_id, "3.1", "Parallel Protocols", "2023-05-15")
            
            # Retrieve and print all volumes
            print("Volumes:")
            for volume in db.get_volumes():
                print(volume)
                
            # Retrieve and print issues for the volume
            print("\nIssues for Volume ID", volume_id)
            for issue in db.get_issues_by_volume(volume_id):
                print(issue)
                
        except sqlite3.Error as e:
            print(f"Database error: {e}")
```
