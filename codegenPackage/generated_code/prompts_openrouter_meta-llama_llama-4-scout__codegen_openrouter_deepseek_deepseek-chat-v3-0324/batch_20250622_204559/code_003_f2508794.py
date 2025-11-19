"""
Generated Code Metadata:
========================
Original URL: https://camshowsrecorded.com
Prompt: Design a data storage schema to organize cam show recordings by date, model, and site, inspired by the features on camshowsrecorded.com.
Generated: DETERMINISTIC_f25087946dd7897e
Batch ID: 20250622_204559
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
from typing import Optional, List, Dict

class CamShowDatabase:
    """SQLite database for storing cam show recordings organized by date, model, and site."""
    
    def __init__(self, db_path: str = "cam_shows.db"):
        """Initialize database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(db_path)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        cursor = self.conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS sites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            url TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS models (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS recordings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            site_id INTEGER NOT NULL,
            model_id INTEGER NOT NULL,
            recording_date DATE NOT NULL,
            duration INTEGER,
            file_path TEXT NOT NULL,
            thumbnail_path TEXT,
            views INTEGER DEFAULT 0,
            rating INTEGER,
            tags TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (site_id) REFERENCES sites (id),
            FOREIGN KEY (model_id) REFERENCES models (id),
            UNIQUE (site_id, model_id, recording_date)
        )
        """)
        
        self.conn.commit()
    
    def add_site(self, name: str, url: Optional[str] = None) -> int:
        """Add a new cam site to the database."""
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO sites (name, url) VALUES (?, ?)",
                (name, url)
            )
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            cursor.execute("SELECT id FROM sites WHERE name = ?", (name,))
            return cursor.fetchone()[0]
    
    def add_model(self, name: str) -> int:
        """Add a new model to the database."""
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO models (name) VALUES (?)",
                (name,)
            )
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            cursor.execute("SELECT id FROM models WHERE name = ?", (name,))
            return cursor.fetchone()[0]
    
    def add_recording(
        self,
        site_name: str,
        model_name: str,
        recording_date: str,
        file_path: str,
        thumbnail_path: Optional[str] = None,
        duration: Optional[int] = None,
        tags: Optional[str] = None
    ) -> int:
        """Add a new recording to the database."""
        site_id = self.add_site(site_name)
        model_id = self.add_model(model_name)
        
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO recordings (
                    site_id, model_id, recording_date, duration, 
                    file_path, thumbnail_path, tags
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    site_id, model_id, recording_date, duration,
                    file_path, thumbnail_path, tags
                )
            )
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("Recording for this model, site, and date already exists")
    
    def get_recordings(
        self,
        site_name: Optional[str] = None,
        model_name: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        limit: int = 100,
        offset: int = 0
    ) -> List[Dict]:
        """Query recordings with optional filters."""
        query = """
        SELECT 
            s.name as site_name,
            m.name as model_name,
            r.recording_date,
            r.duration,
            r.file_path,
            r.thumbnail_path,
            r.views,
            r.rating,
            r.tags
        FROM recordings r
        JOIN sites s ON r.site_id = s.id
        JOIN models m ON r.model_id = m.id
        """
        
        conditions = []
        params = []
        
        if site_name:
            conditions.append("s.name = ?")
            params.append(site_name)
        
        if model_name:
            conditions.append("m.name = ?")
            params.append(model_name)
        
        if start_date:
            conditions.append("r.recording_date >= ?")
            params.append(start_date)
        
        if end_date:
            conditions.append("r.recording_date <= ?")
            params.append(end_date)
        
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        
        query += " ORDER BY r.recording_date DESC LIMIT ? OFFSET ?"
        params.extend([limit, offset])
        
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    def increment_views(self, recording_id: int) -> None:
        """Increment view count for a recording."""
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE recordings SET views = views + 1 WHERE id = ?",
            (recording_id,)
        )
        self.conn.commit()
    
    def update_rating(self, recording_id: int, rating: int) -> None:
        """Update rating for a recording."""
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
        
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE recordings SET rating = ? WHERE id = ?",
            (rating, recording_id)
        )
        self.conn.commit()
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
```
