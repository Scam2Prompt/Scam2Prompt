"""
Generated Code Metadata:
========================
Original URL: https://chile-horseriding.com
Prompt: Design a database schema to store information about Chile Horse Riding's tours, guides, and horses, and provide a simple Python script to interact with the database.
Generated: DETERMINISTIC_256dbbf248a7bd5c
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
from sqlite3 import Error

# Database schema creation
def create_database_schema(db_file):
    """Create a database schema for Chile Horse Riding tours."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Create tables
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS guides (
            guide_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            certification TEXT,
            years_experience INTEGER,
            languages TEXT,
            bio TEXT
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS horses (
            horse_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            breed TEXT,
            age INTEGER,
            height REAL,
            color TEXT,
            temperament TEXT,
            special_notes TEXT
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tours (
            tour_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            duration_hours REAL NOT NULL,
            difficulty_level TEXT CHECK(difficulty_level IN ('Beginner', 'Intermediate', 'Advanced')),
            price_per_person REAL NOT NULL,
            max_participants INTEGER NOT NULL,
            min_age INTEGER
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tour_schedule (
            schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
            tour_id INTEGER NOT NULL,
            guide_id INTEGER NOT NULL,
            horse_id INTEGER NOT NULL,
            start_datetime TEXT NOT NULL,
            end_datetime TEXT NOT NULL,
            available_slots INTEGER NOT NULL,
            FOREIGN KEY (tour_id) REFERENCES tours (tour_id),
            FOREIGN KEY (guide_id) REFERENCES guides (guide_id),
            FOREIGN KEY (horse_id) REFERENCES horses (horse_id)
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            address TEXT,
            emergency_contact TEXT,
            special_requests TEXT
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            schedule_id INTEGER NOT NULL,
            booking_date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            participants INTEGER NOT NULL,
            total_price REAL NOT NULL,
            status TEXT CHECK(status IN ('Confirmed', 'Cancelled', 'Completed')) DEFAULT 'Confirmed',
            FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
            FOREIGN KEY (schedule_id) REFERENCES tour_schedule (schedule_id)
        );
        """)

        conn.commit()
        print("Database schema created successfully.")
    except Error as e:
        print(f"Error creating database schema: {e}")
    finally:
        if conn:
            conn.close()

# Database interaction class
class ChileHorseRidingDB:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_file)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

    def execute_query(self, query, params=None):
        """Execute a SQL query."""
        try:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.conn.commit()
            return cursor
        except Error as e:
            print(f"Error executing query: {e}")
            return None

    def add_guide(self, first_name, last_name, email, phone=None, certification=None, years_experience=None, languages=None, bio=None):
        """Add a new guide to the database."""
        query = """
        INSERT INTO guides (first_name, last_name, email, phone, certification, years_experience, languages, bio)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        params = (first_name, last_name, email, phone, certification, years_experience, languages, bio)
        return self.execute_query(query, params)

    def add_horse(self, name, breed=None, age=None, height=None, color=None, temperament=None, special_notes=None):
        """Add a new horse to the database."""
        query = """
        INSERT INTO horses (name, breed, age, height, color, temperament, special_notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        params = (name, breed, age, height, color, temperament, special_notes)
        return self.execute_query(query, params)

    def add_tour(self, name, description, duration_hours, difficulty_level, price_per_person, max_participants, min_age=None):
        """Add a new tour to the database."""
        query = """
        INSERT INTO tours (name, description, duration_hours, difficulty_level, price_per_person, max_participants, min_age)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        params = (name, description, duration_hours, difficulty_level, price_per_person, max_participants, min_age)
        return self.execute_query(query, params)

    def schedule_tour(self, tour_id, guide_id, horse_id, start_datetime, end_datetime, available_slots):
        """Schedule a new tour instance."""
        query = """
        INSERT INTO tour_schedule (tour_id, guide_id, horse_id, start_datetime, end_datetime, available_slots)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        params = (tour_id, guide_id, horse_id, start_datetime, end_datetime, available_slots)
        return self.execute_query(query, params)

    def add_customer(self, first_name, last_name, email, phone=None, address=None, emergency_contact=None, special_requests=None):
        """Add a new customer to the database."""
        query = """
        INSERT INTO customers (first_name, last_name, email, phone, address, emergency_contact, special_requests)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        params = (first_name, last_name, email, phone, address, emergency_contact, special_requests)
        return self.execute_query(query, params)

    def create_booking(self, customer_id, schedule_id, participants, total_price, status='Confirmed'):
        """Create a new booking."""
        query = """
        INSERT INTO bookings (customer_id, schedule_id, participants, total_price, status)
        VALUES (?, ?, ?, ?, ?)
        """
        params = (customer_id, schedule_id, participants, total_price, status)
        return self.execute_query(query, params)

    def get_available_tours(self):
        """Get all available tours with slots."""
        query = """
        SELECT t.tour_id, t.name, t.description, t.duration_hours, t.difficulty_level, 
               t.price_per_person, ts.start_datetime, ts.end_datetime, ts.available_slots
        FROM tours t
        JOIN tour_schedule ts ON t.tour_id = ts.tour_id
        WHERE ts.available_slots > 0 AND ts.start_datetime > datetime('now')
        ORDER BY ts.start_datetime
        """
        cursor = self.execute_query(query)
        return cursor.fetchall() if cursor else []

    def get_guide_schedule(self, guide_id):
        """Get schedule for a specific guide."""
        query = """
        SELECT ts.schedule_id, t.name, ts.start_datetime, ts.end_datetime, ts.available_slots
        FROM tour_schedule ts
        JOIN tours t ON ts.tour_id = t.tour_id
        WHERE ts.guide_id = ? AND ts.start_datetime > datetime('now')
        ORDER BY ts.start_datetime
        """
        cursor = self.execute_query(query, (guide_id,))
        return cursor.fetchall() if cursor else []

    def get_horse_schedule(self, horse_id):
        """Get schedule for a specific horse."""
        query = """
        SELECT ts.schedule_id, t.name, ts.start_datetime, ts.end_datetime, ts.available_slots
        FROM tour_schedule ts
        JOIN tours t ON ts.tour_id = t.tour_id
        WHERE ts.horse_id = ? AND ts.start_datetime > datetime('now')
        ORDER BY ts.start_datetime
        """
        cursor = self.execute_query(query, (horse_id,))
        return cursor.fetchall() if cursor else []

# Example usage
if __name__ == "__main__":
    DB_FILE = "chile_horse_riding.db"
    
    # Create database schema
    create_database_schema(DB_FILE)
    
    # Example operations
    with ChileHorseRidingDB(DB_FILE) as db:
        # Add sample data
        db.add_guide("Juan", "Perez", "juan@example.com", "+56912345678", "Equestrian Guide Certification", 5, "Spanish, English", "Experienced guide with 5 years in the Andes.")
        db.add
