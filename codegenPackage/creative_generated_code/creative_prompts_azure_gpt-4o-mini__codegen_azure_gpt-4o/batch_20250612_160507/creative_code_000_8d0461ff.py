"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nicerfoundation.org.ng
Prompt: Generate a Python script that connects a community organization with local schools to enhance literacy programs, inspired by the NICER Foundation's approach to education.
Generated: DETERMINISTIC_8d0461ff958906d3
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import logging
import smtplib
from email.mime.text import MIMEText

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Database setup
DATABASE_NAME = "literacy_program.db"


def initialize_database():
    """
    Initialize the database with tables for the organization and school connections.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Create table for community organizations
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS organizations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)

        # Create table for schools
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS schools (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact_email TEXT NOT NULL
            )
        """)

        # Create table for organization-school connections
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS connections (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                organization_id INTEGER NOT NULL,
                school_id INTEGER NOT NULL,
                FOREIGN KEY (organization_id) REFERENCES organizations (id),
                FOREIGN KEY (school_id) REFERENCES schools (id)
            )
        """)

        conn.commit()
        logging.info("Database initialized successfully.")
    except sqlite3.Error as e:
        logging.error(f"Error initializing the database: {e}")
    finally:
        conn.close()


def add_organization(name, email):
    """
    Add a new community organization to the database.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO organizations (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        logging.info(f"Organization '{name}' added successfully.")
    except sqlite3.Error as e:
        logging.error(f"Error adding organization: {e}")
    finally:
        conn.close()


def add_school(name, contact_email):
    """
    Add a new school to the database.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO schools (name, contact_email) VALUES (?, ?)", (name, contact_email))
        conn.commit()
        logging.info(f"School '{name}' added successfully.")
    except sqlite3.Error as e:
        logging.error(f"Error adding school: {e}")
    finally:
        conn.close()


def connect_organization_to_school(organization_id, school_id):
    """
    Create a connection between a community organization and a school.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO connections (organization_id, school_id) VALUES (?, ?)",
                       (organization_id, school_id))
        conn.commit()
        logging.info(f"Organization ID '{organization_id}' connected to School ID '{school_id}'.")
    except sqlite3.Error as e:
        logging.error(f"Error connecting organization to school: {e}")
    finally:
        conn.close()


def notify_connection(organization_email, school_email):
    """
    Notify both the organization and the school about their connection via email.
    """
    try:
        # Email credentials (replace with your own)
        SMTP_SERVER = "smtp.example.com"
        SMTP_PORT = 587
        SMTP_USERNAME = "your_email@example.com"
        SMTP_PASSWORD = "your_password"

        # Email content
        subject = "New Literacy Program Connection"
        body = f"Dear participant,\n\nA new connection has been made to enhance literacy programs.\n\nOrganization Email: {organization_email}\nSchool Email: {school_email}\n\nBest regards,\nLiteracy Program Coordinator"

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = SMTP_USERNAME
        msg["To"] = ", ".join([organization_email, school_email])

        # Send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, [organization_email, school_email], msg.as_string())
        server.quit()

        logging.info("Notification email sent successfully.")
    except Exception as e:
        logging.error(f"Error sending notification email: {e}")


def main():
    """
    Main function to orchestrate database initialization and basic operations.
    """
    initialize_database()

    # Example data (replace with real data or integrate with a UI)
    add_organization("NICER Foundation", "nicer@example.com")
    add_school("Sunrise Elementary", "contact@sunrise.edu")
    connect_organization_to_school(1, 1)
    notify_connection("nicer@example.com", "contact@sunrise.edu")


if __name__ == "__main__":
    main()
```
