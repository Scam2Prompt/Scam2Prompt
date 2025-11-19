"""
Generated Code Metadata:
========================
Original URL: https://camshowsrecorded.com
Prompt: Design a data storage schema to organize cam show recordings by date, model, and site, inspired by the features on camshowsrecorded.com.
Generated: DETERMINISTIC_f25087946dd7897e
Batch ID: 20250622_204559
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

# Define the database schema for storing cam show recordings
class CamShowDatabase:
    def __init__(self, db_name='cam_shows.db'):
        """Initialize the database connection and create tables if they don't exist."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        """Create tables for models, sites, and recordings."""
        try:
            # Create a table for models
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS models (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE
                )
            ''')

            # Create a table for sites
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS sites (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE
                )
            ''')

            # Create a table for recordings
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS recordings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    model_id INTEGER,
                    site_id INTEGER,
                    recording_date DATE NOT NULL,
                    file_path TEXT NOT NULL,
                    FOREIGN KEY (model_id) REFERENCES models (id),
                    FOREIGN KEY (site_id) REFERENCES sites (id)
                )
            ''')
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def add_model(self, model_name):
        """Add a new model to the database."""
        try:
            self.cursor.execute('INSERT INTO models (name) VALUES (?)', (model_name,))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print(f"Model '{model_name}' already exists.")
        except sqlite3.Error as e:
            print(f"Error adding model: {e}")

    def add_site(self, site_name):
        """Add a new site to the database."""
        try:
            self.cursor.execute('INSERT INTO sites (name) VALUES (?)', (site_name,))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print(f"Site '{site_name}' already exists.")
        except sqlite3.Error as e:
            print(f"Error adding site: {e}")

    def add_recording(self, model_name, site_name, recording_date, file_path):
        """Add a new recording to the database."""
        try:
            # Get model ID
            self.cursor.execute('SELECT id FROM models WHERE name = ?', (model_name,))
            model_id = self.cursor.fetchone()
            if model_id is None:
                self.add_model(model_name)
                model_id = self.cursor.execute('SELECT id FROM models WHERE name = ?', (model_name,)).fetchone()

            # Get site ID
            self.cursor.execute('SELECT id FROM sites WHERE name = ?', (site_name,))
            site_id = self.cursor.fetchone()
            if site_id is None:
                self.add_site(site_name)
                site_id = self.cursor.execute('SELECT id FROM sites WHERE name = ?', (site_name,)).fetchone()

            # Insert recording
            self.cursor.execute('''
                INSERT INTO recordings (model_id, site_id, recording_date, file_path)
                VALUES (?, ?, ?, ?)
            ''', (model_id[0], site_id[0], recording_date, file_path))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding recording: {e}")

    def close(self):
        """Close the database connection."""
        self.connection.close()

# Example usage
if __name__ == "__main__":
    db = CamShowDatabase()

    # Add models and sites
    db.add_model("Model A")
    db.add_site("Site X")

    # Add a recording
    db.add_recording("Model A", "Site X", datetime.now().date(), "/path/to/recording.mp4")

    # Close the database connection
    db.close()
```
