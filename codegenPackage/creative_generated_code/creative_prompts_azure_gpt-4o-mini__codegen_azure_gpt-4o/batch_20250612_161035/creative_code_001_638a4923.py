"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sus.weebly.com
Prompt: Write a code snippet that simulates the registration process of individuals in the Programa Saúde da Família, considering the roles of health professionals involved.
Generated: DETERMINISTIC_638a4923c57fd5ce
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

# Database setup for storing registration information
DATABASE_NAME = "saude_familia.db"

def initialize_database():
    """
    Initializes the database by creating the necessary tables.
    """
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Create table for individual registration
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS individuals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            address TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    """)

    # Create table for health professionals
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS health_professionals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)

    # Create table for registration logs
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            individual_id INTEGER NOT NULL,
            professional_id INTEGER NOT NULL,
            timestamp TEXT NOT NULL,
            FOREIGN KEY(individual_id) REFERENCES individuals(id),
            FOREIGN KEY(professional_id) REFERENCES health_professionals(id)
        )
    """)

    connection.commit()
    connection.close()


def register_individual(name, age, address, phone):
    """
    Registers a new individual in the database.

    Parameters:
        name (str): Full name of the individual.
        age (int): Age of the individual.
        address (str): Address of the individual.
        phone (str): Contact phone number of the individual.
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO individuals (name, age, address, phone)
            VALUES (?, ?, ?, ?)
        """, (name, age, address, phone))

        connection.commit()
        connection.close()
        print(f"Individual '{name}' successfully registered.")
    except sqlite3.Error as e:
        print(f"Error during individual registration: {e}")


def register_health_professional(name, role):
    """
    Registers a new health professional in the database.

    Parameters:
        name (str): Full name of the health professional.
        role (str): Role of the health professional (e.g., nurse, doctor, counselor).
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO health_professionals (name, role)
            VALUES (?, ?)
        """, (name, role))

        connection.commit()
        connection.close()
        print(f"Health professional '{name}' successfully registered.")
    except sqlite3.Error as e:
        print(f"Error during health professional registration: {e}")


def log_registration(individual_id, professional_id):
    """
    Logs a registration event.

    Parameters:
        individual_id (int): ID of the individual being registered.
        professional_id (int): ID of the health professional performing the registration.
    """
    from datetime import datetime

    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("""
            INSERT INTO registrations (individual_id, professional_id, timestamp)
            VALUES (?, ?, ?)
        """, (individual_id, professional_id, timestamp))

        connection.commit()
        connection.close()
        print(f"Registration logged: Individual ID {individual_id}, Professional ID {professional_id} at {timestamp}.")
    except sqlite3.Error as e:
        print(f"Error during registration logging: {e}")


# Main program entry point
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Example usage
    register_individual("Maria Silva", 34, "123 Main St, São Paulo", "555-1234")
    register_health_professional("Dr. João Pereira", "Doctor")
    log_registration(1, 1)  # Assuming IDs 1 and 1 for the individual and professional
```
