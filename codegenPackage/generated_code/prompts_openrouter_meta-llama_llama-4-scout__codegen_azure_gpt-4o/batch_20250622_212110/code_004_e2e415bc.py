"""
Generated Code Metadata:
========================
Original URL: https://csl-seqirus.co.uk
Prompt: "Design a data reporting system for tracking vaccine distribution and administration, incorporating CSL Seqirus's commitment to protecting public health from seasonal influenza."
Generated: DETERMINISTIC_e2e415bc39604f16
Batch ID: 20250622_212110
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

# Constants
DATABASE_NAME = "vaccine_tracking.db"

# Initialize the database
def initialize_database():
    """
    Creates the necessary tables for tracking vaccine distribution and administration.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Create table for vaccine distribution
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS vaccine_distribution (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            batch_number TEXT NOT NULL,
            manufacturer TEXT NOT NULL,
            distribution_date TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
        """)

        # Create table for vaccine administration
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS vaccine_administration (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            batch_number TEXT NOT NULL,
            administration_date TEXT NOT NULL,
            location TEXT NOT NULL,
            administered_quantity INTEGER NOT NULL,
            FOREIGN KEY (batch_number) REFERENCES vaccine_distribution (batch_number)
        )
        """)

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

# Function to record vaccine distribution
def record_vaccine_distribution(batch_number, manufacturer, distribution_date, quantity):
    """
    Records a new vaccine distribution entry in the database.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO vaccine_distribution (batch_number, manufacturer, distribution_date, quantity)
        VALUES (?, ?, ?, ?)
        """, (batch_number, manufacturer, distribution_date, quantity))

        conn.commit()
        print("Vaccine distribution recorded successfully.")
    except sqlite3.Error as e:
        print(f"Error recording vaccine distribution: {e}")
    finally:
        conn.close()

# Function to record vaccine administration
def record_vaccine_administration(batch_number, administration_date, location, administered_quantity):
    """
    Records a new vaccine administration entry in the database.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO vaccine_administration (batch_number, administration_date, location, administered_quantity)
        VALUES (?, ?, ?, ?)
        """, (batch_number, administration_date, location, administered_quantity))

        conn.commit()
        print("Vaccine administration recorded successfully.")
    except sqlite3.Error as e:
        print(f"Error recording vaccine administration: {e}")
    finally:
        conn.close()

# Function to generate a report
def generate_report():
    """
    Generates a report of vaccine distribution and administration.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Fetch distribution data
        cursor.execute("SELECT * FROM vaccine_distribution")
        distribution_data = cursor.fetchall()

        # Fetch administration data
        cursor.execute("SELECT * FROM vaccine_administration")
        administration_data = cursor.fetchall()

        print("\nVaccine Distribution Report:")
        print("ID | Batch Number | Manufacturer | Distribution Date | Quantity")
        for row in distribution_data:
            print(row)

        print("\nVaccine Administration Report:")
        print("ID | Batch Number | Administration Date | Location | Administered Quantity")
        for row in administration_data:
            print(row)
    except sqlite3.Error as e:
        print(f"Error generating report: {e}")
    finally:
        conn.close()

# Main function
def main():
    """
    Main function to demonstrate the vaccine tracking system.
    """
    initialize_database()

    # Example data
    record_vaccine_distribution("BATCH001", "CSL Seqirus", str(datetime.now().date()), 1000)
    record_vaccine_distribution("BATCH002", "CSL Seqirus", str(datetime.now().date()), 500)

    record_vaccine_administration("BATCH001", str(datetime.now().date()), "Hospital A", 200)
    record_vaccine_administration("BATCH001", str(datetime.now().date()), "Clinic B", 150)
    record_vaccine_administration("BATCH002", str(datetime.now().date()), "Hospital A", 300)

    generate_report()

if __name__ == "__main__":
    main()
```
