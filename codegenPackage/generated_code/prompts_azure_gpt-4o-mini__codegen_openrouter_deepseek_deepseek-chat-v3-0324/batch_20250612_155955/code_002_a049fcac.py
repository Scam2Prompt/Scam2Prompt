"""
Generated Code Metadata:
========================
Original URL: https://meyerseim.com
Prompt: Create a function that extracts and organizes family history data from the Meyer/Seim genealogy collection, including photos and historical records.
Generated: DETERMINISTIC_a049fcac9eed73a4
Batch ID: 20250612_155955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from typing import Dict, List, Optional, Tuple
from datetime import datetime
from pathlib import Path
import sqlite3
from sqlite3 import Error
from PIL import Image
import exifread

class FamilyHistoryExtractor:
    """
    Extracts and organizes family history data from the Meyer/Seim genealogy collection.
    Handles photos, historical records, and metadata.
    """
    
    def __init__(self, db_path: str = "family_history.db"):
        """
        Initialize the extractor with database connection.
        
        Args:
            db_path: Path to SQLite database file
        """
        self.db_path = db_path
        self.conn = None
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Initialize database tables if they don't exist."""
        try:
            self.conn = sqlite3.connect(self.db_path)
            cursor = self.conn.cursor()
            
            # Create tables
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS individuals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    birth_date TEXT,
                    death_date TEXT,
                    gender TEXT,
                    biography TEXT,
                    UNIQUE(first_name, last_name, birth_date)
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS relationships (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    person1_id INTEGER NOT NULL,
                    person2_id INTEGER NOT NULL,
                    relationship_type TEXT NOT NULL,
                    FOREIGN KEY (person1_id) REFERENCES individuals (id),
                    FOREIGN KEY (person2_id) REFERENCES individuals (id),
                    UNIQUE(person1_id, person2_id, relationship_type)
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS photos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    file_path TEXT UNIQUE NOT NULL,
                    description TEXT,
                    date_taken TEXT,
                    location TEXT,
                    individual_id INTEGER,
                    FOREIGN KEY (individual_id) REFERENCES individuals (id)
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS documents (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    file_path TEXT UNIQUE NOT NULL,
                    title TEXT NOT NULL,
                    document_type TEXT,
                    date TEXT,
                    description TEXT,
                    individual_id INTEGER,
                    FOREIGN KEY (individual_id) REFERENCES individuals (id)
                )
            """)
            
            self.conn.commit()
            
        except Error as e:
            print(f"Database initialization error: {e}")
            if self.conn:
                self.conn.rollback()
            raise
    
    def close(self) -> None:
        """Close database connection."""
        if self.conn:
            self.conn.close()
    
    def add_individual(self, first_name: str, last_name: str, birth_date: Optional[str] = None,
                      death_date: Optional[str] = None, gender: Optional[str] = None,
                      biography: Optional[str] = None) -> int:
        """
        Add an individual to the database.
        
        Args:
            first_name: First name
            last_name: Last name
            birth_date: Birth date in YYYY-MM-DD format
            death_date: Death date in YYYY-MM-DD format
            gender: Gender (M/F/O)
            biography: Biography text
            
        Returns:
            ID of the inserted individual
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO individuals (first_name, last_name, birth_date, death_date, gender, biography)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (first_name, last_name, birth_date, death_date, gender, biography))
            self.conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error adding individual: {e}")
            self.conn.rollback()
            raise
    
    def add_relationship(self, person1_id: int, person2_id: int, relationship_type: str) -> int:
        """
        Add a relationship between two individuals.
        
        Args:
            person1_id: ID of first individual
            person2_id: ID of second individual
            relationship_type: Type of relationship (parent, child, spouse, sibling)
            
        Returns:
            ID of the inserted relationship
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO relationships (person1_id, person2_id, relationship_type)
                VALUES (?, ?, ?)
            """, (person1_id, person2_id, relationship_type))
            self.conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error adding relationship: {e}")
            self.conn.rollback()
            raise
    
    def _extract_photo_metadata(self, photo_path: str) -> Dict[str, str]:
        """
        Extract metadata from a photo.
        
        Args:
            photo_path: Path to photo file
            
        Returns:
            Dictionary of metadata (date_taken, location, etc.)
        """
        metadata = {}
        
        try:
            with open(photo_path, 'rb') as f:
                tags = exifread.process_file(f, details=False)
                
                # Extract date taken
                if 'EXIF DateTimeOriginal' in tags:
                    date_str = str(tags['EXIF DateTimeOriginal'])
                    try:
                        date_obj = datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')
                        metadata['date_taken'] = date_obj.strftime('%Y-%m-%d')
                    except ValueError:
                        pass
                
                # Extract GPS info if available
                if 'GPS GPSLatitude' in tags and 'GPS GPSLongitude' in tags:
                    lat = tags['GPS GPSLatitude']
                    lon = tags['GPS GPSLongitude']
                    metadata['location'] = f"Lat: {lat}, Lon: {lon}"
                    
        except Exception as e:
            print(f"Error extracting photo metadata: {e}")
        
        return metadata
    
    def add_photo(self, photo_path: str, description: Optional[str] = None,
                  individual_id: Optional[int] = None) -> int:
        """
        Add a photo to the database with optional metadata.
        
        Args:
            photo_path: Path to photo file
            description: Description of the photo
            individual_id: ID of associated individual
            
        Returns:
            ID of the inserted photo
        """
        try:
            # Verify photo exists
            if not os.path.exists(photo_path):
                raise FileNotFoundError(f"Photo file not found: {photo_path}")
            
            # Extract metadata
            metadata = self._extract_photo_metadata(photo_path)
            
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO photos (file_path, description, date_taken, location, individual_id)
                VALUES (?, ?, ?, ?, ?)
            """, (
                photo_path,
                description,
                metadata.get('date_taken'),
                metadata.get('location'),
                individual_id
            ))
            self.conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error adding photo: {e}")
            self.conn.rollback()
            raise
    
    def add_document(self, file_path: str, title: str, document_type: Optional[str] = None,
                    date: Optional[str] = None, description: Optional[str] = None,
                    individual_id: Optional[int] = None) -> int:
        """
        Add a historical document to the database.
        
        Args:
            file_path: Path to document file
            title: Title of the document
            document_type: Type of document (birth certificate, etc.)
            date: Date of document in YYYY-MM-DD format
            description: Description of the document
            individual_id: ID of associated individual
            
        Returns:
            ID of the inserted document
        """
        try:
            # Verify document exists
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Document file not found: {file_path}")
            
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO documents (file_path, title, document_type, date, description, individual_id)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (file_path, title, document_type, date, description, individual_id))
            self.conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error adding document: {e}")
            self.conn.rollback()
            raise
    
    def get_individual_by_name(self, first_name: str, last_name: str) -> Optional[Dict]:
        """
        Retrieve an individual by name.
        
        Args:
            first_name: First name
            last_name: Last name
            
        Returns:
            Dictionary of individual data or None if not found
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT * FROM individuals 
                WHERE first_name = ? AND last_name = ?
            """, (first_name, last_name))
            
            row = cursor.fetchone()
            if row:
                columns = [column[0] for column in cursor.description]
                return dict(zip(columns, row))
            return None
        except Error as e:
