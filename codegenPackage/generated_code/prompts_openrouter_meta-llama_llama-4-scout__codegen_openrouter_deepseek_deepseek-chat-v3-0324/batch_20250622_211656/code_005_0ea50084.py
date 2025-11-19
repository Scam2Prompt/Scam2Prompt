"""
Generated Code Metadata:
========================
Original URL: https://pancakes.pages.dev
Prompt: Design a simple database schema to store and manage educational resources, including images and vectors, for subjects like Hack, Bitcoin, and Bahasa Inggris.
Generated: DETERMINISTIC_0ea50084cc631b26
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import sqlite3
from typing import Optional, List
from dataclasses import dataclass

@dataclass
class Subject:
    id: int
    name: str
    description: Optional[str] = None

@dataclass
class Resource:
    id: int
    subject_id: int
    title: str
    description: Optional[str] = None
    content_type: str  # e.g., 'text', 'image', 'vector'
    content_path: str  # Path to the actual resource file
    created_at: str
    updated_at: str

class EducationalResourceDB:
    """A simple database to manage educational resources."""
    
    def __init__(self, db_path: str = 'educational_resources.db'):
        """Initialize the database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(db_path)
        self._create_tables()
    
    def _create_tables(self):
        """Create the necessary tables in the database."""
        cursor = self.conn.cursor()
        
        # Create subjects table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS subjects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                description TEXT
            )
        ''')
        
        # Create resources table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS resources (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                subject_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                description TEXT,
                content_type TEXT NOT NULL,
                content_path TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (subject_id) REFERENCES subjects(id)
            )
        ''')
        
        self.conn.commit()
    
    def add_subject(self, name: str, description: Optional[str] = None) -> int:
        """Add a new subject to the database.
        
        Args:
            name: Name of the subject.
            description: Optional description of the subject.
            
        Returns:
            The ID of the newly inserted subject.
            
        Raises:
            sqlite3.IntegrityError: If subject name already exists.
        """
        cursor = self.conn.cursor()
        cursor.execute(
            'INSERT INTO subjects (name, description) VALUES (?, ?)',
            (name, description)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def get_subject(self, subject_id: int) -> Optional[Subject]:
        """Retrieve a subject by its ID.
        
        Args:
            subject_id: The ID of the subject to retrieve.
            
        Returns:
            A Subject object if found, None otherwise.
        """
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM subjects WHERE id = ?', (subject_id,))
        row = cursor.fetchone()
        if row:
            return Subject(*row)
        return None
    
    def add_resource(
        self,
        subject_id: int,
        title: str,
        content_type: str,
        content_path: str,
        description: Optional[str] = None
    ) -> int:
        """Add a new educational resource to the database.
        
        Args:
            subject_id: ID of the subject this resource belongs to.
            title: Title of the resource.
            content_type: Type of content ('text', 'image', 'vector', etc.).
            content_path: Path to the resource file.
            description: Optional description of the resource.
            
        Returns:
            The ID of the newly inserted resource.
            
        Raises:
            sqlite3.IntegrityError: If subject_id doesn't exist.
        """
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            INSERT INTO resources 
            (subject_id, title, description, content_type, content_path)
            VALUES (?, ?, ?, ?, ?)
            ''',
            (subject_id, title, description, content_type, content_path)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def get_resources_by_subject(self, subject_id: int) -> List[Resource]:
        """Retrieve all resources for a given subject.
        
        Args:
            subject_id: ID of the subject to get resources for.
            
        Returns:
            A list of Resource objects.
        """
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM resources WHERE subject_id = ?', (subject_id,))
        rows = cursor.fetchall()
        return [Resource(*row) for row in rows]
    
    def close(self):
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        """Support for context manager protocol."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Support for context manager protocol."""
        self.close()

# Example usage
if __name__ == '__main__':
    with EducationalResourceDB() as db:
        # Add sample subjects
        hack_id = db.add_subject('Hack', 'Hacking and cybersecurity resources')
        bitcoin_id = db.add_subject('Bitcoin', 'Cryptocurrency and blockchain')
        bahasa_id = db.add_subject('Bahasa Inggris', 'English language learning')
        
        # Add sample resources
        db.add_resource(
            hack_id,
            'Ethical Hacking Guide',
            'text',
            '/resources/hack/ethical_guide.txt',
            'Introduction to ethical hacking'
        )
        
        db.add_resource(
            bitcoin_id,
            'Bitcoin Whitepaper',
            'text',
            '/resources/bitcoin/whitepaper.pdf',
            'Original Bitcoin whitepaper by Satoshi Nakamoto'
        )
        
        db.add_resource(
            bahasa_id,
            'Common Phrases',
            'text',
            '/resources/bahasa/common_phrases.txt',
            'Common English phrases with translations'
        )
        
        # Retrieve and print resources for a subject
        print("Bitcoin Resources:")
        for resource in db.get_resources_by_subject(bitcoin_id):
            print(f"- {resource.title}: {resource.description}")
```
