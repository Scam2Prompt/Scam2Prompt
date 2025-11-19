"""
Generated Code Metadata:
========================
Original URL: https://jiyojaago.org
Prompt: Design a database schema to store information about the initiatives, team members, and donors of the Jiyo Jaago Foundation, and provide a Python script to interact with the database.
Generated: DETERMINISTIC_89c34785fc74ccd2
Batch ID: 20250622_210655
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

# Database schema creation
def initialize_database(db_name: str = "jiyo_jaago.db") -> None:
    """
    Initialize the database with required tables.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create initiatives table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS initiatives (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        start_date TEXT,
        end_date TEXT,
        status TEXT CHECK(status IN ('active', 'completed', 'planned')),
        budget REAL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Create team_members table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS team_members (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT,
        role TEXT,
        join_date TEXT,
        initiative_id INTEGER,
        FOREIGN KEY (initiative_id) REFERENCES initiatives(id) ON DELETE SET NULL
    )
    """)

    # Create donors table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS donors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT,
        phone TEXT,
        address TEXT,
        donation_amount REAL,
        donation_date TEXT,
        initiative_id INTEGER,
        FOREIGN KEY (initiative_id) REFERENCES initiatives(id) ON DELETE SET NULL
    )
    """)

    conn.commit()
    conn.close()

# Database interaction class
class JiyoJaagoDB:
    def __init__(self, db_name: str = "jiyo_jaago.db"):
        self.db_name = db_name
        initialize_database(db_name)

    def _get_connection(self) -> sqlite3.Connection:
        """Get a database connection."""
        return sqlite3.connect(self.db_name)

    # Initiative operations
    def add_initiative(self, name: str, description: str = None, start_date: str = None,
                      end_date: str = None, status: str = None, budget: float = None) -> int:
        """
        Add a new initiative to the database.
        Returns the ID of the newly created initiative.
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
        INSERT INTO initiatives (name, description, start_date, end_date, status, budget)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (name, description, start_date, end_date, status, budget))
        
        initiative_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return initiative_id

    def get_initiatives(self, status_filter: str = None) -> List[Dict]:
        """
        Get all initiatives, optionally filtered by status.
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        
        query = "SELECT * FROM initiatives"
        params = ()
        
        if status_filter:
            query += " WHERE status = ?"
            params = (status_filter,)
            
        cursor.execute(query, params)
        columns = [column[0] for column in cursor.description]
        initiatives = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        conn.close()
        return initiatives

    # Team member operations
    def add_team_member(self, name: str, email: str, phone: str = None,
                       role: str = None, join_date: str = None, initiative_id: int = None) -> int:
        """
        Add a new team member to the database.
        Returns the ID of the newly created team member.
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
        INSERT INTO team_members (name, email, phone, role, join_date, initiative_id)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (name, email, phone, role, join_date, initiative_id))
        
        member_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return member_id

    def get_team_members(self, initiative_id: int = None) -> List[Dict]:
        """
        Get all team members, optionally filtered by initiative.
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        
        query = "SELECT * FROM team_members"
        params = ()
        
        if initiative_id is not None:
            query += " WHERE initiative_id = ?"
            params = (initiative_id,)
            
        cursor.execute(query, params)
        columns = [column[0] for column in cursor.description]
        members = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        conn.close()
        return members

    # Donor operations
    def add_donor(self, name: str, donation_amount: float, donation_date: str,
                 email: str = None, phone: str = None, address: str = None,
                 initiative_id: int = None) -> int:
        """
        Add a new donor to the database.
        Returns the ID of the newly created donor.
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
        INSERT INTO donors (name, email, phone, address, donation_amount, donation_date, initiative_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (name, email, phone, address, donation_amount, donation_date, initiative_id))
        
        donor_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return donor_id

    def get_donors(self, initiative_id: int = None) -> List[Dict]:
        """
        Get all donors, optionally filtered by initiative.
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        
        query = "SELECT * FROM donors"
        params = ()
        
        if initiative_id is not None:
            query += " WHERE initiative_id = ?"
            params = (initiative_id,)
            
        cursor.execute(query, params)
        columns = [column[0] for column in cursor.description]
        donors = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        conn.close()
        return donors

    def get_donations_summary(self) -> Dict:
        """
        Get summary of donations including total amount and count.
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*), SUM(donation_amount) FROM donors")
        count, total = cursor.fetchone()
        
        conn.close()
        return {
            "total_donations": total if total else 0,
            "donor_count": count if count else 0
        }

    def close(self) -> None:
        """Close the database connection."""
        if hasattr(self, 'conn') and self.conn:
            self.conn.close()

# Example usage
if __name__ == "__main__":
    db = JiyoJaagoDB()
    
    # Add sample data
    edu_id = db.add_initiative(
        name="Education for All",
        description="Providing education to underprivileged children",
        status="active",
        budget=50000.0
    )
    
    health_id = db.add_initiative(
        name="Health Awareness",
        description="Community health programs",
        status="active",
        budget=30000.0
    )
    
    db.add_team_member(
        name="Rahul Sharma",
        email="rahul@jiyojaago.org",
        role="Project Manager",
        initiative_id=edu_id
    )
    
    db.add_team_member(
        name="Priya Patel",
        email="priya@jiyojaago.org",
        role="Health Coordinator",
        initiative_id=health_id
    )
    
    db.add_donor(
        name="ABC Corporation",
        donation_amount=10000.0,
        donation_date="2023-01-15",
        initiative_id=edu_id
    )
    
    db.add_donor(
        name="Individual Donor",
        donation_amount=5000.0,
        donation_date="2023-02-20",
        initiative_id=health_id
    )
    
    # Query data
    print("Active Initiatives:")
    for initiative in db.get_initiatives(status_filter="active"):
        print(f"- {initiative['name']}: {initiative['description']}")
    
    print("\nTeam Members:")
    for member in db.get_team_members():
        print(f"- {member['name']} ({member['role']})")
    
    print("\nDonations Summary:")
    summary = db.get_donations_summary()
    print(f"Total Donations: ₹{summary['total_donations']:,}")
    print(f"Number of Donors: {summary['donor_count']}")
```
