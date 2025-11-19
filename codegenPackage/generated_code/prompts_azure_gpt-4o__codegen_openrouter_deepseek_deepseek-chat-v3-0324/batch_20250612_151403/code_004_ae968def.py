"""
Generated Code Metadata:
========================
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Suggest a Python library for generating and managing links for an online tool catalog, similar to the "Gerar link" feature mentioned on the Anhanguera Ferramentas website.
Generated: DETERMINISTIC_ae968def736391cd
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import secrets
import string
from typing import Optional
from datetime import datetime, timedelta
from dataclasses import dataclass
import sqlite3
from sqlite3 import Error

@dataclass
class Link:
    id: str
    tool_id: str
    created_at: datetime
    expires_at: Optional[datetime] = None
    is_active: bool = True

class LinkManager:
    def __init__(self, db_path: str = "links.db"):
        """Initialize the link manager with database connection."""
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        """Initialize the database tables if they don't exist."""
        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS links (
                    id TEXT PRIMARY KEY,
                    tool_id TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    expires_at TEXT,
                    is_active INTEGER NOT NULL
                )
            """)
            
            conn.commit()
        except Error as e:
            print(f"Database error: {e}")
        finally:
            if conn:
                conn.close()

    def _generate_link_id(self, length: int = 16) -> str:
        """Generate a random link ID."""
        alphabet = string.ascii_letters + string.digits
        return ''.join(secrets.choice(alphabet) for _ in range(length))

    def create_link(
        self,
        tool_id: str,
        expires_after: Optional[timedelta] = None
    ) -> Link:
        """Create a new link for a tool."""
        link_id = self._generate_link_id()
        created_at = datetime.now()
        expires_at = None
        
        if expires_after:
            expires_at = created_at + expires_after
        
        link = Link(
            id=link_id,
            tool_id=tool_id,
            created_at=created_at,
            expires_at=expires_at
        )
        
        self._save_link(link)
        return link

    def _save_link(self, link: Link):
        """Save a link to the database."""
        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute("""
                INSERT INTO links (id, tool_id, created_at, expires_at, is_active)
                VALUES (?, ?, ?, ?, ?)
            """, (
                link.id,
                link.tool_id,
                link.created_at.isoformat(),
                link.expires_at.isoformat() if link.expires_at else None,
                int(link.is_active)
            ))
            
            conn.commit()
        except Error as e:
            print(f"Database error: {e}")
        finally:
            if conn:
                conn.close()

    def get_link(self, link_id: str) -> Optional[Link]:
        """Retrieve a link by its ID."""
        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT * FROM links WHERE id = ?
            """, (link_id,))
            
            row = cursor.fetchone()
            if not row:
                return None
                
            return Link(
                id=row['id'],
                tool_id=row['tool_id'],
                created_at=datetime.fromisoformat(row['created_at']),
                expires_at=datetime.fromisoformat(row['expires_at']) if row['expires_at'] else None,
                is_active=bool(row['is_active'])
            )
        except Error as e:
            print(f"Database error: {e}")
            return None
        finally:
            if conn:
                conn.close()

    def deactivate_link(self, link_id: str) -> bool:
        """Deactivate a link."""
        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute("""
                UPDATE links SET is_active = 0 WHERE id = ?
            """, (link_id,))
            
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Database error: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def is_link_valid(self, link_id: str) -> bool:
        """Check if a link is valid (active and not expired)."""
        link = self.get_link(link_id)
        if not link or not link.is_active:
            return False
            
        if link.expires_at and datetime.now() > link.expires_at:
            return False
            
        return True
```
