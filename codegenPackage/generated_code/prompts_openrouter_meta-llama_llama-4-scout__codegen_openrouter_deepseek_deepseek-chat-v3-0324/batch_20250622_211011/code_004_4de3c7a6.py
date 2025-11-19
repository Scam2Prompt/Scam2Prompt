"""
Generated Code Metadata:
========================
Original URL: https://ssdsd.netlify.app
Prompt: Design a database schema to store and manage the metadata for the various PDF files, such as title, subject, and date, for easy retrieval and searching.
Generated: DETERMINISTIC_4de3c7a6b346ad70
Batch ID: 20250622_211011
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
from typing import Optional

def create_database_schema(db_path: str = "pdf_metadata.db") -> None:
    """
    Creates the database schema for storing PDF metadata.
    
    Args:
        db_path: Path to the SQLite database file.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Create the PDF metadata table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pdf_metadata (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_path TEXT NOT NULL UNIQUE,
            file_name TEXT NOT NULL,
            title TEXT,
            author TEXT,
            subject TEXT,
            keywords TEXT,
            creation_date TEXT,
            modification_date TEXT,
            page_count INTEGER,
            file_size INTEGER,
            is_archived BOOLEAN DEFAULT 0,
            last_accessed TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        # Create indexes for faster searching
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_title ON pdf_metadata(title)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_author ON pdf_metadata(author)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_subject ON pdf_metadata(subject)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_keywords ON pdf_metadata(keywords)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_creation_date ON pdf_metadata(creation_date)")
        
        conn.commit()
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

def insert_pdf_metadata(
    db_path: str,
    file_path: str,
    file_name: str,
    title: Optional[str] = None,
    author: Optional[str] = None,
    subject: Optional[str] = None,
    keywords: Optional[str] = None,
    creation_date: Optional[str] = None,
    modification_date: Optional[str] = None,
    page_count: Optional[int] = None,
    file_size: Optional[int] = None,
    is_archived: bool = False
) -> bool:
    """
    Inserts PDF metadata into the database.
    
    Args:
        db_path: Path to the SQLite database file.
        file_path: Full path to the PDF file.
        file_name: Name of the PDF file.
        title: Title of the PDF document.
        author: Author of the PDF document.
        subject: Subject of the PDF document.
        keywords: Keywords associated with the PDF.
        creation_date: Date when the PDF was created.
        modification_date: Date when the PDF was last modified.
        page_count: Number of pages in the PDF.
        file_size: Size of the PDF file in bytes.
        is_archived: Whether the PDF is archived.
        
    Returns:
        True if insertion was successful, False otherwise.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        current_time = datetime.now().isoformat()
        
        cursor.execute("""
        INSERT INTO pdf_metadata (
            file_path, file_name, title, author, subject, keywords,
            creation_date, modification_date, page_count, file_size,
            is_archived, last_accessed, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            file_path, file_name, title, author, subject, keywords,
            creation_date, modification_date, page_count, file_size,
            is_archived, current_time, current_time
        ))
        
        conn.commit()
        return True
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        if conn:
            conn.rollback()
        return False
    finally:
        if conn:
            conn.close()

def update_last_accessed(db_path: str, file_path: str) -> bool:
    """
    Updates the last accessed timestamp for a PDF.
    
    Args:
        db_path: Path to the SQLite database file.
        file_path: Full path to the PDF file.
        
    Returns:
        True if update was successful, False otherwise.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        current_time = datetime.now().isoformat()
        
        cursor.execute("""
        UPDATE pdf_metadata 
        SET last_accessed = ?, updated_at = ?
        WHERE file_path = ?
        """, (current_time, current_time, file_path))
        
        conn.commit()
        return cursor.rowcount > 0
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        if conn:
            conn.rollback()
        return False
    finally:
        if conn:
            conn.close()

def search_pdfs(
    db_path: str,
    title: Optional[str] = None,
    author: Optional[str] = None,
    subject: Optional[str] = None,
    keywords: Optional[str] = None,
    min_creation_date: Optional[str] = None,
    max_creation_date: Optional[str] = None,
    limit: int = 100
) -> list:
    """
    Searches for PDFs based on metadata criteria.
    
    Args:
        db_path: Path to the SQLite database file.
        title: Title to search for (partial match).
        author: Author to search for (partial match).
        subject: Subject to search for (partial match).
        keywords: Keywords to search for (partial match).
        min_creation_date: Minimum creation date (inclusive).
        max_creation_date: Maximum creation date (inclusive).
        limit: Maximum number of results to return.
        
    Returns:
        List of matching PDF metadata dictionaries.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        query = "SELECT * FROM pdf_metadata WHERE 1=1"
        params = []
        
        if title:
            query += " AND title LIKE ?"
            params.append(f"%{title}%")
        if author:
            query += " AND author LIKE ?"
            params.append(f"%{author}%")
        if subject:
            query += " AND subject LIKE ?"
            params.append(f"%{subject}%")
        if keywords:
            query += " AND keywords LIKE ?"
            params.append(f"%{keywords}%")
        if min_creation_date:
            query += " AND creation_date >= ?"
            params.append(min_creation_date)
        if max_creation_date:
            query += " AND creation_date <= ?"
            params.append(max_creation_date)
            
        query += " ORDER BY last_accessed DESC LIMIT ?"
        params.append(limit)
        
        cursor.execute(query, params)
        results = cursor.fetchall()
        
        return [dict(row) for row in results]
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        if conn:
            conn.close()
```
