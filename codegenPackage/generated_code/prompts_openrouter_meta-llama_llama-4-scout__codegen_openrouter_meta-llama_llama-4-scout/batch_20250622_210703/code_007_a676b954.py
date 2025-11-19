"""
Generated Code Metadata:
========================
Original URL: https://market2024.qboda.es
Prompt: Suggest a set of features for a wedding planning mobile app, incorporating QBoda's services, such as vendor listing, appointment scheduling, and exclusive discounts.
Generated: DETERMINISTIC_a676b95422ab47bd
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# wedding_planning_app.py

import os
import sqlite3
from typing import Dict, List

class Vendor:
    """Represents a wedding vendor."""

    def __init__(self, id: int, name: str, category: str, rating: float):
        """
        Initializes a Vendor object.

        Args:
        id (int): Unique vendor ID.
        name (str): Vendor name.
        category (str): Vendor category (e.g., photographer, caterer).
        rating (float): Vendor rating (out of 5).
        """
        self.id = id
        self.name = name
        self.category = category
        self.rating = rating

class WeddingPlanningApp:
    """Simulates a wedding planning mobile app."""

    def __init__(self, db_name: str = "wedding_planning.db"):
        """
        Initializes the WeddingPlanningApp.

        Args:
        db_name (str): Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Creates the necessary tables in the database."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS vendors (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                rating REAL NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY,
                vendor_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                time TEXT NOT NULL,
                FOREIGN KEY (vendor_id) REFERENCES vendors (id)
            )
        """)
        self.conn.commit()

    def add_vendor(self, vendor: Vendor):
        """Adds a vendor to the database."""
        self.cursor.execute("""
            INSERT INTO vendors (id, name, category, rating)
            VALUES (?, ?, ?, ?)
        """, (vendor.id, vendor.name, vendor.category, vendor.rating))
        self.conn.commit()

    def get_vendors(self, category: str = None) -> List[Vendor]:
        """
        Retrieves a list of vendors.

        Args:
        category (str): Optional category filter.

        Returns:
        List[Vendor]: List of vendors.
        """
        if category:
            self.cursor.execute("""
                SELECT * FROM vendors
                WHERE category = ?
            """, (category,))
        else:
            self.cursor.execute("""
                SELECT * FROM vendors
            """)
        rows = self.cursor.fetchall()
        return [Vendor(*row) for row in rows]

    def schedule_appointment(self, vendor_id: int, date: str, time: str):
        """
        Schedules an appointment with a vendor.

        Args:
        vendor_id (int): ID of the vendor.
        date (str): Date of the appointment.
        time (str): Time of the appointment.
        """
        self.cursor.execute("""
            INSERT INTO appointments (vendor_id, date, time)
            VALUES (?, ?, ?)
        """, (vendor_id, date, time))
        self.conn.commit()

    def get_appointments(self, vendor_id: int = None) -> List[Dict]:
        """
        Retrieves a list of appointments.

        Args:
        vendor_id (int): Optional vendor ID filter.

        Returns:
        List[Dict]: List of appointments.
        """
        if vendor_id:
            self.cursor.execute("""
                SELECT * FROM appointments
                WHERE vendor_id = ?
            """, (vendor_id,))
        else:
            self.cursor.execute("""
                SELECT * FROM appointments
            """)
        rows = self.cursor.fetchall()
        return [{"id": row[0], "vendor_id": row[1], "date": row[2], "time": row[3]} for row in rows]

    def apply_exclusive_discount(self, vendor_id: int, discount: float):
        """
        Applies an exclusive discount to a vendor.

        Args:
        vendor_id (int): ID of the vendor.
        discount (float): Discount percentage.
        """
        # Simulate applying a discount (this may vary based on actual QBoda services)
        print(f"Applied {discount}% discount to vendor {vendor_id}")

def main():
    app = WeddingPlanningApp()

    # Add some vendors
    vendors = [
        Vendor(1, "Photographer John", "Photographer", 4.5),
        Vendor(2, "Caterer Jane", "Caterer", 4.8),
        Vendor(3, "DJ Mike", "DJ", 4.2)
    ]
    for vendor in vendors:
        app.add_vendor(vendor)

    # Get vendors
    all_vendors = app.get_vendors()
    print("All Vendors:")
    for vendor in all_vendors:
        print(f"{vendor.name} ({vendor.category}) - {vendor.rating}/5")

    # Schedule appointments
    app.schedule_appointment(1, "2024-09-20", "10:00 AM")
    app.schedule_appointment(2, "2024-09-22", "2:00 PM")

    # Get appointments
    appointments = app.get_appointments()
    print("\nAppointments:")
    for appointment in appointments:
        print(f"Vendor ID: {appointment['vendor_id']}, Date: {appointment['date']}, Time: {appointment['time']}")

    # Apply exclusive discount
    app.apply_exclusive_discount(1, 10)

if __name__ == "__main__":
    main()
```
