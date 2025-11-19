"""
Generated Code Metadata:
========================
Original URL: https://youngistaan.org
Prompt: "Develop a plan for a school or education-focused NGO to implement a 'Sponsor Our Talented Children' initiative, similar to Youngistaan Foundation's program."
Generated: DETERMINISTIC_ece01e3940106669
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Sponsor Our Talented Children Initiative

## Overview
# This program aims to help a school or education-focused NGO implement a 'Sponsor Our Talented Children' initiative.
# It allows donors to sponsor talented children and track their educational progress.

## Requirements
# - Python 3.8+
# - SQLite3

import sqlite3
from datetime import datetime

# Database Connection Class
class DatabaseConnection:
    def __init__(self, db_name):
        """Initialize a database connection."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        """Create tables for children and donors."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS children (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                grade INTEGER NOT NULL,
                talent TEXT NOT NULL,
                sponsor_id INTEGER,
                FOREIGN KEY (sponsor_id) REFERENCES donors (id)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS donors (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL,
                sponsorship_date DATE
            )
        ''')

        self.conn.commit()

    def close_connection(self):
        """Close the database connection."""
        self.conn.close()


# Child Class
class Child:
    def __init__(self, id, name, age, grade, talent):
        """Initialize a Child object."""
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade
        self.talent = talent
        self.sponsor = None

    def __str__(self):
        return f"Child {self.id}: {self.name}, Age: {self.age}, Grade: {self.grade}, Talent: {self.talent}"


# Donor Class
class Donor:
    def __init__(self, id, name, email, phone):
        """Initialize a Donor object."""
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.sponsorship_date = datetime.now().strftime("%Y-%m-%d")
        self.child = None

    def __str__(self):
        return f"Donor {self.id}: {self.name}, Email: {self.email}, Phone: {self.phone}"


# Sponsor Initiative Class
class SponsorInitiative:
    def __init__(self, db_name):
        """Initialize the Sponsor Initiative."""
        self.db = DatabaseConnection(db_name)
        self.db.create_tables()

    def add_child(self, name, age, grade, talent):
        """Add a child to the initiative."""
        try:
            self.db.cursor.execute('INSERT INTO children (name, age, grade, talent) VALUES (?, ?, ?, ?)',
                                   (name, age, grade, talent))
            self.db.conn.commit()
            print(f"Child '{name}' added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding child: {e}")

    def add_donor(self, name, email, phone):
        """Add a donor to the initiative."""
        try:
            self.db.cursor.execute('INSERT INTO donors (name, email, phone) VALUES (?, ?, ?)',
                                   (name, email, phone))
            self.db.conn.commit()
            print(f"Donor '{name}' added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding donor: {e}")

    def sponsor_child(self, child_id, donor_id):
        """Sponsor a child."""
        try:
            self.db.cursor.execute('UPDATE children SET sponsor_id = ? WHERE id = ?', (donor_id, child_id))
            self.db.cursor.execute('UPDATE donors SET sponsorship_date = ? WHERE id = ?', (datetime.now().strftime("%Y-%m-%d"), donor_id))
            self.db.conn.commit()
            print(f"Child {child_id} sponsored by donor {donor_id} successfully.")
        except sqlite3.Error as e:
            print(f"Error sponsoring child: {e}")

    def get_children(self):
        """Get all children in the initiative."""
        try:
            self.db.cursor.execute('SELECT * FROM children')
            children = self.db.cursor.fetchall()
            return [Child(*child) for child in children]
        except sqlite3.Error as e:
            print(f"Error getting children: {e}")
            return []

    def get_donors(self):
        """Get all donors in the initiative."""
        try:
            self.db.cursor.execute('SELECT * FROM donors')
            donors = self.db.cursor.fetchall()
            return [Donor(*donor) for donor in donors]
        except sqlite3.Error as e:
            print(f"Error getting donors: {e}")
            return []

    def close(self):
        """Close the database connection."""
        self.db.close_connection()


# Example Usage
if __name__ == "__main__":
    initiative = SponsorInitiative('sponsor_initiative.db')

    while True:
        print("\n1. Add Child")
        print("2. Add Donor")
        print("3. Sponsor Child")
        print("4. Get Children")
        print("5. Get Donors")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter child's name: ")
            age = int(input("Enter child's age: "))
            grade = int(input("Enter child's grade: "))
            talent = input("Enter child's talent: ")
            initiative.add_child(name, age, grade, talent)
        elif choice == "2":
            name = input("Enter donor's name: ")
            email = input("Enter donor's email: ")
            phone = input("Enter donor's phone: ")
            initiative.add_donor(name, email, phone)
        elif choice == "3":
            child_id = int(input("Enter child's ID: "))
            donor_id = int(input("Enter donor's ID: "))
            initiative.sponsor_child(child_id, donor_id)
        elif choice == "4":
            children = initiative.get_children()
            for child in children:
                print(child)
        elif choice == "5":
            donors = initiative.get_donors()
            for donor in donors:
                print(donor)
        elif choice == "6":
            initiative.close()
            break
        else:
            print("Invalid option. Please choose a valid option.")
```
