"""
Generated Code Metadata:
========================
Original URL: https://afunabb.cl
Prompt: Write a Python script to manage membership benefits for a labor union like AFUNABB Chillán, including tracking member information and benefits.
Generated: DETERMINISTIC_e4c56dee90dc1b4f
Batch ID: 20250622_212236
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
from typing import Optional, Dict, List, Tuple

class UnionMember:
    """Represents a union member with personal and benefit information."""
    
    def __init__(self, member_id: str, name: str, email: str, join_date: str, 
                 membership_status: str = 'active', benefits: Optional[Dict[str, bool]] = None):
        """
        Initialize a UnionMember instance.
        
        Args:
            member_id: Unique identifier for the member
            name: Full name of the member
            email: Contact email address
            join_date: Date when member joined (YYYY-MM-DD)
            membership_status: Current status (active/inactive)
            benefits: Dictionary of benefits and their status
        """
        self.member_id = member_id
        self.name = name
        self.email = email
        self.join_date = join_date
        self.membership_status = membership_status
        self.benefits = benefits or {
            'healthcare': False,
            'legal_assistance': False,
            'training_programs': False,
            'retirement_plan': False
        }

    def update_benefit(self, benefit_name: str, status: bool) -> bool:
        """
        Update a specific benefit status for the member.
        
        Args:
            benefit_name: Name of the benefit to update
            status: New status (True/False)
            
        Returns:
            bool: True if update was successful, False otherwise
        """
        if benefit_name in self.benefits:
            self.benefits[benefit_name] = status
            return True
        return False

    def get_benefit_status(self, benefit_name: str) -> Optional[bool]:
        """
        Get the current status of a specific benefit.
        
        Args:
            benefit_name: Name of the benefit to check
            
        Returns:
            Optional[bool]: Status of the benefit or None if not found
        """
        return self.benefits.get(benefit_name)

class UnionMembershipDB:
    """Database handler for union membership management."""
    
    def __init__(self, db_name: str = 'union_membership.db'):
        """
        Initialize the database connection.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS members (
                member_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                join_date TEXT NOT NULL,
                membership_status TEXT NOT NULL
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS benefits (
                member_id TEXT,
                benefit_name TEXT,
                status INTEGER,
                PRIMARY KEY (member_id, benefit_name),
                FOREIGN KEY (member_id) REFERENCES members (member_id)
            )
        ''')
        self.conn.commit()

    def add_member(self, member: UnionMember) -> bool:
        """
        Add a new member to the database.
        
        Args:
            member: UnionMember object to add
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.cursor.execute('''
                INSERT INTO members (member_id, name, email, join_date, membership_status)
                VALUES (?, ?, ?, ?, ?)
            ''', (member.member_id, member.name, member.email, 
                  member.join_date, member.membership_status))
            
            for benefit, status in member.benefits.items():
                self.cursor.execute('''
                    INSERT INTO benefits (member_id, benefit_name, status)
                    VALUES (?, ?, ?)
                ''', (member.member_id, benefit, int(status)))
            
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error adding member: {e}")
            self.conn.rollback()
            return False

    def get_member(self, member_id: str) -> Optional[UnionMember]:
        """
        Retrieve a member by their ID.
        
        Args:
            member_id: ID of the member to retrieve
            
        Returns:
            Optional[UnionMember]: Member object if found, None otherwise
        """
        try:
            self.cursor.execute('SELECT * FROM members WHERE member_id = ?', (member_id,))
            member_data = self.cursor.fetchone()
            
            if not member_data:
                return None
                
            self.cursor.execute('SELECT benefit_name, status FROM benefits WHERE member_id = ?', (member_id,))
            benefits_data = self.cursor.fetchall()
            
            benefits = {row[0]: bool(row[1]) for row in benefits_data}
            
            return UnionMember(
                member_id=member_data[0],
                name=member_data[1],
                email=member_data[2],
                join_date=member_data[3],
                membership_status=member_data[4],
                benefits=benefits
            )
        except sqlite3.Error as e:
            print(f"Error retrieving member: {e}")
            return None

    def update_member_status(self, member_id: str, new_status: str) -> bool:
        """
        Update a member's status (active/inactive).
        
        Args:
            member_id: ID of the member to update
            new_status: New status value
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.cursor.execute('''
                UPDATE members 
                SET membership_status = ?
                WHERE member_id = ?
            ''', (new_status, member_id))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error updating member status: {e}")
            self.conn.rollback()
            return False

    def update_member_benefit(self, member_id: str, benefit_name: str, status: bool) -> bool:
        """
        Update a specific benefit for a member.
        
        Args:
            member_id: ID of the member
            benefit_name: Name of the benefit to update
            status: New status of the benefit
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.cursor.execute('''
                INSERT OR REPLACE INTO benefits (member_id, benefit_name, status)
                VALUES (?, ?, ?)
            ''', (member_id, benefit_name, int(status)))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error updating member benefit: {e}")
            self.conn.rollback()
            return False

    def get_all_members(self, status_filter: Optional[str] = None) -> List[UnionMember]:
        """
        Retrieve all members, optionally filtered by status.
        
        Args:
            status_filter: Optional status to filter by (active/inactive)
            
        Returns:
            List[UnionMember]: List of member objects
        """
        try:
            query = 'SELECT member_id FROM members'
            params = ()
            
            if status_filter:
                query += ' WHERE membership_status = ?'
                params = (status_filter,)
                
            self.cursor.execute(query, params)
            member_ids = [row[0] for row in self.cursor.fetchall()]
            
            members = []
            for member_id in member_ids:
                member = self.get_member(member_id)
                if member:
                    members.append(member)
                    
            return members
        except sqlite3.Error as e:
            print(f"Error retrieving members: {e}")
            return []

    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()

class UnionMembershipCLI:
    """Command-line interface for union membership management."""
    
    def __init__(self):
        """Initialize the CLI with a database connection."""
        self.db = UnionMembershipDB()
        
    def display_menu(self) -> None:
        """Display the main menu options."""
        print("\nAFUNABB Chillán Membership Management")
        print("1. Add new member")
        print("2. View member details")
        print("3. Update member status")
        print("4. Update member benefits")
        print("5. List all members")
        print("6. Exit")

    def add_member_interactive(self) -> None:
        """Interactive prompt to add a new member."""
        print("\nAdd New Member")
        member_id = input("Member ID: ")
        name = input("Full Name: ")
        email = input("Email: ")
        join_date = datetime.now().strftime('%Y-%m-%d')
        
        member = UnionMember(member_id, name, email, join_date)
        
        print("\nSet Initial Benefits (y/n):")
        for benefit in member.benefits:
            response = input(f"{benefit.replace('_', ' ').title()}: ").lower()
            member.update_benefit(benefit, response == 'y')
        
        if self.db.add_member(member):
            print("Member added successfully!")
        else:
            print("Failed to add member.")

    def view_member_details(self
