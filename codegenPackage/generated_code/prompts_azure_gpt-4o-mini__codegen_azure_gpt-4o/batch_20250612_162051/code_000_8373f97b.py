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

# Database setup
DB_NAME = "volunteer_registration.db"

def initialize_database():
    """
    Initializes the database and creates the volunteers table if it doesn't exist.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS volunteers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL,
                city TEXT NOT NULL,
                registration_date TEXT NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def register_volunteer(name, email, phone, city):
    """
    Registers a new volunteer in the database.

    Args:
        name (str): Full name of the volunteer.
        email (str): Email address of the volunteer.
        phone (str): Phone number of the volunteer.
        city (str): City of residence of the volunteer.

    Returns:
        str: Success or error message.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('''
            INSERT INTO volunteers (name, email, phone, city, registration_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, email, phone, city, registration_date))
        conn.commit()
        return "Volunteer registered successfully!"
    except sqlite3.IntegrityError:
        return "Error: A volunteer with this email already exists."
    except sqlite3.Error as e:
        return f"Database error: {e}"
    finally:
        conn.close()

def list_volunteers():
    """
    Retrieves and displays all registered volunteers.

    Returns:
        list: A list of dictionaries containing volunteer details.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM volunteers')
        rows = cursor.fetchall()
        volunteers = []
        for row in rows:
            volunteers.append({
                "id": row[0],
                "name": row[1],
                "email": row[2],
                "phone": row[3],
                "city": row[4],
                "registration_date": row[5]
            })
        return volunteers
    except sqlite3.Error as e:
        print(f"Error retrieving volunteers: {e}")
        return []
    finally:
        conn.close()

# Main program
if __name__ == "__main__":
    initialize_database()
    print("Welcome to the Volunteer Registration System!")
    
    while True:
        print("\nMenu:")
        print("1. Register a new volunteer")
        print("2. List all volunteers")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            name = input("Enter full name: ").strip()
            email = input("Enter email: ").strip()
            phone = input("Enter phone number: ").strip()
            city = input("Enter city: ").strip()
            message = register_volunteer(name, email, phone, city)
            print(message)
        elif choice == "2":
            volunteers = list_volunteers()
            if volunteers:
                print("\nRegistered Volunteers:")
                for v in volunteers:
                    print(f"ID: {v['id']}, Name: {v['name']}, Email: {v['email']}, "
                          f"Phone: {v['phone']}, City: {v['city']}, Registered On: {v['registration_date']}")
            else:
                print("No volunteers found.")
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```
