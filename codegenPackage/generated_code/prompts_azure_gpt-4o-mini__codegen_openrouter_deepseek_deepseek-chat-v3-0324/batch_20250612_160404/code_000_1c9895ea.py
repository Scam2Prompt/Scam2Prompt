"""
Generated Code Metadata:
========================
Original URL: https://www.iaci.org
Prompt: Generate a code snippet that demonstrates how to implement a membership management system for an organization similar to the Idaho Association of Commerce & Industry (IACI).
Generated: DETERMINISTIC_1c9895ea09b5c309
Batch ID: 20250612_160404
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
from dataclasses import dataclass
from datetime import datetime
import hashlib
import uuid

@dataclass
class Member:
    """Represents a member in the membership system."""
    id: str
    name: str
    email: str
    membership_type: str
    join_date: str
    renewal_date: str
    is_active: bool
    contact_person: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class MembershipSystem:
    """Manages organization memberships with CRUD operations."""
    
    def __init__(self, db_path: str = "membership.db"):
        """Initialize the membership system with database connection."""
        self.conn = sqlite3.connect(db_path)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS members (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                membership_type TEXT NOT NULL,
                join_date TEXT NOT NULL,
                renewal_date TEXT NOT NULL,
                is_active INTEGER NOT NULL,
                contact_person TEXT,
                phone TEXT,
                address TEXT
            )
        """)
        self.conn.commit()
    
    def _generate_id(self) -> str:
        """Generate a unique ID for new members."""
        return str(uuid.uuid4())
    
    def add_member(self, name: str, email: str, membership_type: str,
                   join_date: str, renewal_date: str, is_active: bool,
                   contact_person: str = None, phone: str = None,
                   address: str = None) -> Member:
        """Add a new member to the system."""
        member_id = self._generate_id()
        member = Member(
            id=member_id,
            name=name,
            email=email,
            membership_type=membership_type,
            join_date=join_date,
            renewal_date=renewal_date,
            is_active=is_active,
            contact_person=contact_person,
            phone=phone,
            address=address
        )
        
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO members VALUES (
                    :id, :name, :email, :membership_type, :join_date,
                    :renewal_date, :is_active, :contact_person, :phone, :address
                )
            """, member.__dict__)
            self.conn.commit()
            return member
        except sqlite3.IntegrityError:
            raise ValueError("Email already exists in the system")
    
    def get_member(self, member_id: str) -> Optional[Member]:
        """Retrieve a member by their ID."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM members WHERE id = ?", (member_id,))
        row = cursor.fetchone()
        if row:
            return Member(*row)
        return None
    
    def get_member_by_email(self, email: str) -> Optional[Member]:
        """Retrieve a member by their email."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM members WHERE email = ?", (email,))
        row = cursor.fetchone()
        if row:
            return Member(*row)
        return None
    
    def update_member(self, member_id: str, **kwargs) -> Optional[Member]:
        """Update member information."""
        valid_fields = {
            'name', 'email', 'membership_type', 'join_date', 'renewal_date',
            'is_active', 'contact_person', 'phone', 'address'
        }
        
        for field in kwargs:
            if field not in valid_fields:
                raise ValueError(f"Invalid field: {field}")
        
        set_clause = ", ".join(f"{field} = ?" for field in kwargs)
        values = list(kwargs.values())
        values.append(member_id)
        
        cursor = self.conn.cursor()
        cursor.execute(f"""
            UPDATE members SET {set_clause} WHERE id = ?
        """, values)
        
        if cursor.rowcount == 0:
            return None
        
        self.conn.commit()
        return self.get_member(member_id)
    
    def delete_member(self, member_id: str) -> bool:
        """Delete a member from the system."""
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM members WHERE id = ?", (member_id,))
        self.conn.commit()
        return cursor.rowcount > 0
    
    def list_members(self, active_only: bool = False) -> List[Member]:
        """List all members, optionally filtering by active status."""
        cursor = self.conn.cursor()
        if active_only:
            cursor.execute("SELECT * FROM members WHERE is_active = 1")
        else:
            cursor.execute("SELECT * FROM members")
        
        return [Member(*row) for row in cursor.fetchall()]
    
    def search_members(self, query: str) -> List[Member]:
        """Search members by name or email."""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM members 
            WHERE name LIKE ? OR email LIKE ?
        """, (f"%{query}%", f"%{query}%"))
        return [Member(*row) for row in cursor.fetchall()]
    
    def renew_membership(self, member_id: str, new_renewal_date: str) -> Optional[Member]:
        """Renew a member's membership by updating renewal date."""
        return self.update_member(member_id, renewal_date=new_renewal_date, is_active=True)
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        """Support context manager protocol."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Support context manager protocol."""
        self.close()

# Example usage
if __name__ == "__main__":
    with MembershipSystem() as system:
        # Add a new member
        new_member = system.add_member(
            name="Acme Corp",
            email="contact@acme.com",
            membership_type="Corporate",
            join_date="2023-01-15",
            renewal_date="2024-01-15",
            is_active=True,
            contact_person="John Doe",
            phone="555-123-4567",
            address="123 Business St, Boise, ID"
        )
        print(f"Added member: {new_member.name}")
        
        # List all active members
        active_members = system.list_members(active_only=True)
        print(f"Active members: {len(active_members)}")
        
        # Renew a membership
        renewed_member = system.renew_membership(
            member_id=new_member.id,
            new_renewal_date="2025-01-15"
        )
        if renewed_member:
            print(f"Renewed member until: {renewed_member.renewal_date}")
```
