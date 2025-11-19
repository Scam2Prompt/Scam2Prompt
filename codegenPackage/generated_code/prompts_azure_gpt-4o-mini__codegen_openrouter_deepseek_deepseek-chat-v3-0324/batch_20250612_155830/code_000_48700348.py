"""
Generated Code Metadata:
========================
Original URL: https://optimisenow.net
Prompt: How can I implement a Commercial Leads Management System (CLMS) to enhance my sales efforts and maximize revenue potential?
Generated: DETERMINISTIC_48700348f19e9032
Batch ID: 20250612_155830
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

class Lead:
    """Represents a commercial lead with relevant attributes."""
    
    def __init__(self, name: str, company: str, email: str, phone: str, 
                 product_interest: str, status: str = "New", 
                 last_contact: Optional[datetime] = None):
        self.name = name
        self.company = company
        self.email = email
        self.phone = phone
        self.product_interest = product_interest
        self.status = status  # New, Contacted, Qualified, Closed-Lost, Closed-Won
        self.last_contact = last_contact if last_contact else datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert Lead object to dictionary for easier serialization."""
        return {
            'name': self.name,
            'company': self.company,
            'email': self.email,
            'phone': self.phone,
            'product_interest': self.product_interest,
            'status': self.status,
            'last_contact': self.last_contact.isoformat()
        }

class CLMS:
    """Commercial Leads Management System implementation."""
    
    def __init__(self, db_path: str = 'leads.db'):
        """Initialize the CLMS with database connection."""
        self.db_path = db_path
        self._init_db()
    
    def _init_db(self) -> None:
        """Initialize database tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS leads (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    company TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    phone TEXT,
                    product_interest TEXT NOT NULL,
                    status TEXT NOT NULL,
                    last_contact TEXT NOT NULL
                )
            ''')
            conn.commit()
    
    def add_lead(self, lead: Lead) -> bool:
        """Add a new lead to the system."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO leads 
                    (name, company, email, phone, product_interest, status, last_contact)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    lead.name,
                    lead.company,
                    lead.email,
                    lead.phone,
                    lead.product_interest,
                    lead.status,
                    lead.last_contact.isoformat()
                ))
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            print(f"Lead with email {lead.email} already exists.")
            return False
        except Exception as e:
            print(f"Error adding lead: {e}")
            return False
    
    def update_lead_status(self, email: str, new_status: str) -> bool:
        """Update the status of an existing lead."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE leads 
                    SET status = ?, last_contact = ?
                    WHERE email = ?
                ''', (new_status, datetime.now().isoformat(), email))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error updating lead status: {e}")
            return False
    
    def get_lead(self, email: str) -> Optional[Lead]:
        """Retrieve a lead by email."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM leads WHERE email = ?', (email,))
                row = cursor.fetchone()
                if row:
                    return self._row_to_lead(row)
                return None
        except Exception as e:
            print(f"Error retrieving lead: {e}")
            return None
    
    def get_leads_by_status(self, status: str) -> List[Lead]:
        """Retrieve all leads with a specific status."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM leads WHERE status = ?', (status,))
                return [self._row_to_lead(row) for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error retrieving leads by status: {e}")
            return []
    
    def get_all_leads(self) -> List[Lead]:
        """Retrieve all leads in the system."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM leads')
                return [self._row_to_lead(row) for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error retrieving all leads: {e}")
            return []
    
    def _row_to_lead(self, row: tuple) -> Lead:
        """Convert a database row to a Lead object."""
        return Lead(
            name=row[1],
            company=row[2],
            email=row[3],
            phone=row[4],
            product_interest=row[5],
            status=row[6],
            last_contact=datetime.fromisoformat(row[7])
        )
    
    def generate_report(self) -> Dict[str, int]:
        """Generate a report of lead counts by status."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT status, COUNT(*) 
                    FROM leads 
                    GROUP BY status
                ''')
                return {row[0]: row[1] for row in cursor.fetchall()}
        except Exception as e:
            print(f"Error generating report: {e}")
            return {}

# Example usage
if __name__ == "__main__":
    clms = CLMS()
    
    # Add sample leads
    lead1 = Lead(
        name="John Doe",
        company="Acme Inc",
        email="john@acme.com",
        phone="123-456-7890",
        product_interest="Enterprise Software"
    )
    
    lead2 = Lead(
        name="Jane Smith",
        company="Globex Corp",
        email="jane@globex.com",
        phone="987-654-3210",
        product_interest="Cloud Services",
        status="Contacted"
    )
    
    clms.add_lead(lead1)
    clms.add_lead(lead2)
    
    # Update lead status
    clms.update_lead_status("john@acme.com", "Qualified")
    
    # Generate report
    report = clms.generate_report()
    print("Lead Status Report:")
    for status, count in report.items():
        print(f"{status}: {count}")
```
