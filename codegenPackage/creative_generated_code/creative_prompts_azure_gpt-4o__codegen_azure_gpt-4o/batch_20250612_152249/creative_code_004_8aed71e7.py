"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kataskeui.gr
Prompt: Suggest a library or tool to assist in supervising daily construction activities, with features for tracking progress and compliance with issued permits in Greece.
Generated: DETERMINISTIC_8aed71e765c22cbc
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Construction Supervisor Tool

This script provides a basic implementation for supervising daily construction activities. 
It uses an SQLite database to track progress and compliance with issued permits in Greece.

Features:
1. Record daily progress for construction sites.
2. Track compliance with permits.
3. Generate summary reports.
"""

import sqlite3
from datetime import datetime


class ConstructionSupervisor:
    def __init__(self, db_name="construction.db"):
        """
        Initializes the ConstructionSupervisor tool by connecting to the SQLite database.
        If the database does not exist, it creates necessary tables.

        :param db_name: Name of the SQLite database file
        """
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """
        Creates necessary tables for tracking construction progress and permits.
        """
        try:
            cursor = self.connection.cursor()
            # Table to store construction site information
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS construction_sites (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    site_name TEXT NOT NULL,
                    permit_number TEXT NOT NULL,
                    location TEXT NOT NULL,
                    start_date DATE NOT NULL
                )
            """)

            # Table to store daily progress updates
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS daily_progress (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    site_id INTEGER NOT NULL,
                    progress_date DATE NOT NULL,
                    progress_details TEXT NOT NULL,
                    compliance_status TEXT NOT NULL,
                    FOREIGN KEY (site_id) REFERENCES construction_sites (id)
                )
            """)

            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")
        finally:
            cursor.close()

    def add_construction_site(self, site_name, permit_number, location, start_date):
        """
        Adds a new construction site to the database.

        :param site_name: Name of the construction site
        :param permit_number: Permit number
        :param location: Location of the site
        :param start_date: Start date of construction
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO construction_sites (site_name, permit_number, location, start_date)
                VALUES (?, ?, ?, ?)
            """, (site_name, permit_number, location, start_date))
            self.connection.commit()
            print("Construction site added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding construction site: {e}")
        finally:
            cursor.close()

    def record_daily_progress(self, site_id, progress_details, compliance_status):
        """
        Records daily progress for a construction site.

        :param site_id: ID of the construction site
        :param progress_details: Details of the progress made
        :param compliance_status: Compliance status ("Compliant" or "Non-compliant")
        """
        try:
            cursor = self.connection.cursor()
            progress_date = datetime.now().date()
            cursor.execute("""
                INSERT INTO daily_progress (site_id, progress_date, progress_details, compliance_status)
                VALUES (?, ?, ?, ?)
            """, (site_id, progress_date, progress_details, compliance_status))
            self.connection.commit()
            print("Daily progress recorded successfully.")
        except sqlite3.Error as e:
            print(f"Error recording daily progress: {e}")
        finally:
            cursor.close()

    def generate_report(self):
        """
        Generates a summary report of all construction sites and their daily progress.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT s.site_name, s.permit_number, s.location, p.progress_date, p.progress_details, p.compliance_status
                FROM construction_sites s
                LEFT JOIN daily_progress p ON s.id = p.site_id
                ORDER BY s.site_name, p.progress_date
            """)
            report = cursor.fetchall()

            if report:
                print("Construction Sites Report:")
                for row in report:
                    print(f"Site Name: {row[0]}, Permit: {row[1]}, Location: {row[2]}, Date: {row[3]}, Progress: {row[4]}, Compliance: {row[5]}")
            else:
                print("No data available.")
        except sqlite3.Error as e:
            print(f"Error generating report: {e}")
        finally:
            cursor.close()

    def close_connection(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()
            print("Database connection closed.")


# Example usage
if __name__ == "__main__":
    supervisor = ConstructionSupervisor()

    # Add a new construction site
    supervisor.add_construction_site("Athens Mall Project", "GR12345", "Athens, Greece", "2023-10-01")

    # Record daily progress
    supervisor.record_daily_progress(1, "Foundation work completed", "Compliant")
    supervisor.record_daily_progress(1, "Structural reinforcement ongoing", "Compliant")

    # Generate report
    supervisor.generate_report()

    # Close connection
    supervisor.close_connection()
```
