"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.azrvservices.com
Prompt: Develop a system to track RV repair technician certifications (RVIA Master Certified) and ongoing training compliance, ensuring high-quality service standards.
Generated: DETERMINISTIC_1db98b64178ecfc7
Batch ID: 20250612_145203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime

class RVTechCertificationSystem:
    def __init__(self, db_name='rv_tech_certifications.db'):
        """Initialize the database connection and create the necessary tables."""
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create the tables for storing technician data and their certifications."""
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS technicians (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    phone TEXT
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS certifications (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    technician_id INTEGER,
                    certification_date DATE NOT NULL,
                    expiration_date DATE NOT NULL,
                    training_completed BOOLEAN NOT NULL DEFAULT FALSE,
                    FOREIGN KEY (technician_id) REFERENCES technicians (id)
                )
            ''')

    def add_technician(self, name, email, phone):
        """Add a new technician to the database."""
        try:
            with self.connection:
                self.connection.execute('''
                    INSERT INTO technicians (name, email, phone) VALUES (?, ?, ?)
                ''', (name, email, phone))
        except sqlite3.IntegrityError:
            print(f"Error: Technician with email {email} already exists.")

    def add_certification(self, technician_id, certification_date, expiration_date, training_completed=False):
        """Add a certification record for a technician."""
        try:
            with self.connection:
                self.connection.execute('''
                    INSERT INTO certifications (technician_id, certification_date, expiration_date, training_completed)
                    VALUES (?, ?, ?, ?)
                ''', (technician_id, certification_date, expiration_date, training_completed))
        except sqlite3.IntegrityError:
            print(f"Error: Certification for technician ID {technician_id} already exists.")

    def get_technician_certifications(self, technician_id):
        """Retrieve all certifications for a specific technician."""
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT * FROM certifications WHERE technician_id = ?
        ''', (technician_id,))
        return cursor.fetchall()

    def check_certification_status(self, technician_id):
        """Check if a technician's certification is still valid."""
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT expiration_date FROM certifications WHERE technician_id = ?
            ORDER BY expiration_date DESC LIMIT 1
        ''', (technician_id,))
        result = cursor.fetchone()
        if result:
            expiration_date = datetime.strptime(result[0], '%Y-%m-%d').date()
            return expiration_date > datetime.now().date()
        return False

    def mark_training_completed(self, technician_id):
        """Mark training as completed for the most recent certification."""
        with self.connection:
            self.connection.execute('''
                UPDATE certifications SET training_completed = TRUE
                WHERE technician_id = ?
                ORDER BY certification_date DESC LIMIT 1
            ''', (technician_id,))

    def close(self):
        """Close the database connection."""
        self.connection.close()


# Example usage
if __name__ == "__main__":
    system = RVTechCertificationSystem()

    # Adding technicians
    system.add_technician('John Doe', 'john.doe@example.com', '555-1234')
    system.add_technician('Jane Smith', 'jane.smith@example.com', '555-5678')

    # Adding certifications
    system.add_certification(1, '2023-01-15', '2024-01-15')
    system.add_certification(2, '2023-03-10', '2024-03-10')

    # Checking certification status
    print(system.check_certification_status(1))  # True or False

    # Marking training as completed
    system.mark_training_completed(1)

    # Fetching technician certifications
    certifications = system.get_technician_certifications(1)
    print(certifications)

    # Close the system
    system.close()
```
