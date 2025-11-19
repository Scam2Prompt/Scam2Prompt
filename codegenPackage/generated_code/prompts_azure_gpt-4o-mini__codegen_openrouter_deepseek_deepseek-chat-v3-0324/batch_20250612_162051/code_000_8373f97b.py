"""
Generated Code Metadata:
========================
Original URL: https://jiyojaago.org
Prompt: Generate a code snippet that implements a volunteer registration system for a non-governmental organization focused on promoting human values, similar to the initiatives of Jiyo Jaago Foundation.
Generated: DETERMINISTIC_8373f97bf8d53f44
Batch ID: 20250612_162051
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

class VolunteerRegistrationSystem:
    """
    A volunteer registration system for an NGO promoting human values.
    Handles volunteer sign-up, data storage, and retrieval.
    """

    def __init__(self, db_name: str = "volunteers.db"):
        """
        Initialize the system with a SQLite database connection.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self._create_tables()

    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS volunteers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT,
                age INTEGER,
                skills TEXT,
                availability TEXT,
                interests TEXT,
                registration_date TEXT NOT NULL,
                status TEXT DEFAULT 'active'
            )
        """)
        self.conn.commit()

    def register_volunteer(
        self,
        full_name: str,
        email: str,
        phone: Optional[str] = None,
        age: Optional[int] = None,
        skills: Optional[List[str]] = None,
        availability: Optional[str] = None,
        interests: Optional[List[str]] = None
    ) -> bool:
        """
        Register a new volunteer.
        
        Args:
            full_name: Volunteer's full name
            email: Email address (must be unique)
            phone: Phone number (optional)
            age: Age in years (optional)
            skills: List of skills (optional)
            availability: Availability details (optional)
            interests: List of interests (optional)
            
        Returns:
            bool: True if registration was successful, False otherwise
        """
        try:
            cursor = self.conn.cursor()
            registration_date = datetime.now().isoformat()
            
            cursor.execute("""
                INSERT INTO volunteers (
                    full_name, email, phone, age, skills, availability, 
                    interests, registration_date
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                full_name,
                email,
                phone,
                age,
                ", ".join(skills) if skills else None,
                availability,
                ", ".join(interests) if interests else None,
                registration_date
            ))
            
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            # Handle duplicate email
            return False
        except Exception as e:
            print(f"Error registering volunteer: {e}")
            return False

    def get_volunteer(self, email: str) -> Optional[Dict]:
        """
        Retrieve volunteer details by email.
        
        Args:
            email: Volunteer's email address
            
        Returns:
            dict: Volunteer details if found, None otherwise
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT * FROM volunteers WHERE email = ?
            """, (email,))
            
            row = cursor.fetchone()
            if row:
                return {
                    "id": row[0],
                    "full_name": row[1],
                    "email": row[2],
                    "phone": row[3],
                    "age": row[4],
                    "skills": row[5].split(", ") if row[5] else [],
                    "availability": row[6],
                    "interests": row[7].split(", ") if row[7] else [],
                    "registration_date": row[8],
                    "status": row[9]
                }
            return None
        except Exception as e:
            print(f"Error retrieving volunteer: {e}")
            return None

    def get_all_volunteers(self) -> List[Dict]:
        """
        Retrieve all registered volunteers.
        
        Returns:
            list: List of all volunteers' details
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM volunteers")
            
            volunteers = []
            for row in cursor.fetchall():
                volunteers.append({
                    "id": row[0],
                    "full_name": row[1],
                    "email": row[2],
                    "phone": row[3],
                    "age": row[4],
                    "skills": row[5].split(", ") if row[5] else [],
                    "availability": row[6],
                    "interests": row[7].split(", ") if row[7] else [],
                    "registration_date": row[8],
                    "status": row[9]
                })
            return volunteers
        except Exception as e:
            print(f"Error retrieving volunteers: {e}")
            return []

    def update_volunteer_status(self, email: str, status: str) -> bool:
        """
        Update a volunteer's status (active/inactive).
        
        Args:
            email: Volunteer's email address
            status: New status ('active' or 'inactive')
            
        Returns:
            bool: True if update was successful, False otherwise
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                UPDATE volunteers SET status = ? WHERE email = ?
            """, (status, email))
            
            self.conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error updating volunteer status: {e}")
            return False

    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()

    def __enter__(self):
        """Support for context manager protocol."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Support for context manager protocol."""
        self.close()


# Example usage
if __name__ == "__main__":
    with VolunteerRegistrationSystem() as system:
        # Register a volunteer
        success = system.register_volunteer(
            full_name="John Doe",
            email="john@example.com",
            phone="+1234567890",
            age=30,
            skills=["Teaching", "Public Speaking"],
            availability="Weekends",
            interests=["Education", "Community Service"]
        )
        
        if success:
            print("Volunteer registered successfully!")
        else:
            print("Registration failed (possibly duplicate email)")
        
        # Retrieve volunteer
        volunteer = system.get_volunteer("john@example.com")
        if volunteer:
            print(f"Found volunteer: {volunteer['full_name']}")
        
        # List all volunteers
        volunteers = system.get_all_volunteers()
        print(f"Total volunteers: {len(volunteers)}")
```
