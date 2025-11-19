"""
Generated Code Metadata:
========================
Original URL: https://meyerseim.com
Prompt: Develop a plan for integrating historical photos into a genealogy database, considering the media attached to person bios on the Meyer/Seim Families website.
Generated: DETERMINISTIC_4f72ee792d14df08
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sqlite3
from datetime import datetime
from PIL import Image

# Database schema for genealogy database
# Table: people
# Columns: id (INTEGER PRIMARY KEY), first_name (TEXT), last_name (TEXT), birth_date (TEXT), death_date (TEXT)

# Table: photos
# Columns: id (INTEGER PRIMARY KEY), person_id (INTEGER), file_path (TEXT), description (TEXT), upload_date (TEXT)
# Foreign Key: person_id references people(id)

# Function to initialize the database
def initialize_database(db_path):
    """
    Initialize the genealogy database with required tables.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Create people table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS people (
                id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                birth_date TEXT,
                death_date TEXT
            )
        ''')

        # Create photos table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS photos (
                id INTEGER PRIMARY KEY,
                person_id INTEGER NOT NULL,
                file_path TEXT NOT NULL,
                description TEXT,
                upload_date TEXT NOT NULL,
                FOREIGN KEY (person_id) REFERENCES people (id)
            )
        ''')

        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

# Function to add a person to the database
def add_person(db_path, first_name, last_name, birth_date=None, death_date=None):
    """
    Add a person to the genealogy database.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO people (first_name, last_name, birth_date, death_date)
            VALUES (?, ?, ?, ?)
        ''', (first_name, last_name, birth_date, death_date))

        conn.commit()
        return cursor.lastrowid  # Return the ID of the newly added person
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

# Function to add a photo to the database
def add_photo(db_path, person_id, file_path, description=None):
    """
    Add a photo to the genealogy database and associate it with a person.
    """
    try:
        # Validate that the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        # Validate that the file is an image
        try:
            with Image.open(file_path) as img:
                img.verify()  # Verify that the file is a valid image
        except Exception as e:
            raise ValueError(f"Invalid image file: {file_path}. Error: {e}")

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Insert photo record into the database
        cursor.execute('''
            INSERT INTO photos (person_id, file_path, description, upload_date)
            VALUES (?, ?, ?, ?)
        ''', (person_id, file_path, description, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

        conn.commit()
        return cursor.lastrowid  # Return the ID of the newly added photo
    except (sqlite3.Error, FileNotFoundError, ValueError) as e:
        print(f"Error adding photo: {e}")
    finally:
        conn.close()

# Function to retrieve all photos for a person
def get_photos_for_person(db_path, person_id):
    """
    Retrieve all photos associated with a person from the database.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT file_path, description, upload_date
            FROM photos
            WHERE person_id = ?
        ''', (person_id,))

        photos = cursor.fetchall()
        return photos
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        conn.close()

# Example usage
if __name__ == "__main__":
    # Path to the SQLite database
    db_path = "genealogy.db"

    # Initialize the database
    initialize_database(db_path)

    # Add a person
    person_id = add_person(db_path, "John", "Doe", "1900-01-01", "1980-12-31")
    print(f"Added person with ID: {person_id}")

    # Add a photo for the person
    photo_id = add_photo(db_path, person_id, "path/to/photo.jpg", "John Doe's portrait")
    print(f"Added photo with ID: {photo_id}")

    # Retrieve and display all photos for the person
    photos = get_photos_for_person(db_path, person_id)
    for photo in photos:
        print(f"Photo: {photo}")
```
