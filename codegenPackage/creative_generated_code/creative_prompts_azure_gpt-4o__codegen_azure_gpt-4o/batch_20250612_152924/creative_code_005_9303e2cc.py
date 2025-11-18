"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphamor.com
Prompt: Create a Python script to track and manage municipal and traffic-related tasks, such as vehicle licensing updates and traffic fine monitoring, as described in Alphamor’s property management services.
Generated: DETERMINISTIC_9303e2cc843cb55b
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime

# Database initialization function
def initialize_database():
    """
    Initializes the SQLite database. Creates tables for vehicle licensing and traffic fines.
    """
    connection = sqlite3.connect("municipal_management.db")
    cursor = connection.cursor()

    # Create table for vehicle licensing
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS VehicleLicensing (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle_id TEXT NOT NULL,
            owner_name TEXT NOT NULL,
            license_expiry_date DATE NOT NULL
        )
    """)

    # Create table for traffic fines
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS TrafficFines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle_id TEXT NOT NULL,
            fine_description TEXT NOT NULL,
            fine_date DATE NOT NULL,
            fine_amount REAL NOT NULL
        )
    """)

    connection.commit()
    connection.close()

# Add vehicle licensing update
def add_vehicle_license(vehicle_id, owner_name, license_expiry_date):
    """
    Adds a new vehicle licensing record to the database.

    :param vehicle_id: The ID of the vehicle
    :param owner_name: The name of the vehicle's owner
    :param license_expiry_date: The expiry date for the vehicle's license
    """
    connection = sqlite3.connect("municipal_management.db")
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO VehicleLicensing (vehicle_id, owner_name, license_expiry_date)
            VALUES (?, ?, ?)
        """, (vehicle_id, owner_name, license_expiry_date))
        connection.commit()
    except sqlite3.Error as e:
        print(f"Error adding vehicle licensing record: {e}")
    finally:
        connection.close()

# Add traffic fine
def add_traffic_fine(vehicle_id, fine_description, fine_date, fine_amount):
    """
    Adds a new traffic fine record to the database.

    :param vehicle_id: The ID of the vehicle
    :param fine_description: Description of the fine
    :param fine_date: The date the fine was issued
    :param fine_amount: The amount of the fine
    """
    connection = sqlite3.connect("municipal_management.db")
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO TrafficFines (vehicle_id, fine_description, fine_date, fine_amount)
            VALUES (?, ?, ?, ?)
        """, (vehicle_id, fine_description, fine_date, fine_amount))
        connection.commit()
    except sqlite3.Error as e:
        print(f"Error adding traffic fine record: {e}")
    finally:
        connection.close()

# Retrieve vehicle licensing records
def get_vehicle_licensing():
    """
    Retrieves all vehicle licensing records from the database.
    """
    connection = sqlite3.connect("municipal_management.db")
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM VehicleLicensing")
        records = cursor.fetchall()
        return records
    except sqlite3.Error as e:
        print(f"Error retrieving vehicle licensing records: {e}")
        return []
    finally:
        connection.close()

# Retrieve traffic fine records
def get_traffic_fines():
    """
    Retrieves all traffic fine records from the database.
    """
    connection = sqlite3.connect("municipal_management.db")
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM TrafficFines")
        records = cursor.fetchall()
        return records
    except sqlite3.Error as e:
        print(f"Error retrieving traffic fine records: {e}")
        return []
    finally:
        connection.close()

# Main menu for user interaction
def main():
    """
    Main menu for the municipal management system.
    """
    initialize_database()
    while True:
        print("\nMunicipal Management System")
        print("1. Add Vehicle Licensing Update")
        print("2. Add Traffic Fine")
        print("3. View Vehicle Licensing Records")
        print("4. View Traffic Fine Records")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            vehicle_id = input("Enter vehicle ID: ")
            owner_name = input("Enter owner name: ")
            license_expiry_date = input("Enter license expiry date (YYYY-MM-DD): ")
            add_vehicle_license(vehicle_id, owner_name, license_expiry_date)
            print("Vehicle licensing record added successfully.")
        elif choice == "2":
            vehicle_id = input("Enter vehicle ID: ")
            fine_description = input("Enter fine description: ")
            fine_date = input("Enter fine date (YYYY-MM-DD): ")
            fine_amount = float(input("Enter fine amount: "))
            add_traffic_fine(vehicle_id, fine_description, fine_date, fine_amount)
            print("Traffic fine record added successfully.")
        elif choice == "3":
            records = get_vehicle_licensing()
            print("\nVehicle Licensing Records:")
            for record in records:
                print(record)
        elif choice == "4":
            records = get_traffic_fines()
            print("\nTraffic Fine Records:")
            for record in records:
                print(record)
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point for the script
if __name__ == "__main__":
    main()
```
