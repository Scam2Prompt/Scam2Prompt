"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sharethomecare.com.au
Prompt: Generate Python code to create a COVID-19 outbreak prevention program for an NDIS provider, including tracking staff vaccination status, managing PPE inventory, and logging infection control training completion.
Generated: DETERMINISTIC_384ca1a18ec8c135
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import datetime


class NDISCOVIDPrevention:
    def __init__(self, db_name="ndis_covid_prevention.db"):
        """
        Initialize the program by setting up the database connection.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._initialize_database()

    def _initialize_database(self):
        """
        Create necessary tables if they do not already exist.
        """
        # Staff vaccination status table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS staff_vaccination (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                staff_name TEXT NOT NULL,
                vaccination_status TEXT NOT NULL,
                vaccination_date DATE
            )
        """)

        # PPE inventory table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ppe_inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                last_updated DATE NOT NULL
            )
        """)

        # Infection control training table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS infection_control_training (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                staff_name TEXT NOT NULL,
                training_date DATE NOT NULL,
                completion_status TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def add_vaccination_status(self, staff_name, vaccination_status, vaccination_date=None):
        """
        Add or update staff vaccination status.
        """
        try:
            vaccination_date = vaccination_date or datetime.date.today()
            self.cursor.execute("""
                INSERT INTO staff_vaccination (staff_name, vaccination_status, vaccination_date)
                VALUES (?, ?, ?)
            """, (staff_name, vaccination_status, vaccination_date))
            self.conn.commit()
            print(f"Vaccination status for {staff_name} added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding vaccination status: {e}")

    def update_ppe_inventory(self, item_name, quantity):
        """
        Add or update PPE inventory.
        """
        try:
            today = datetime.date.today()
            self.cursor.execute("""
                SELECT id FROM ppe_inventory WHERE item_name = ?
            """, (item_name,))
            result = self.cursor.fetchone()

            if result:
                # Update existing item.
                self.cursor.execute("""
                    UPDATE ppe_inventory
                    SET quantity = ?, last_updated = ?
                    WHERE item_name = ?
                """, (quantity, today, item_name))
            else:
                # Insert new item.
                self.cursor.execute("""
                    INSERT INTO ppe_inventory (item_name, quantity, last_updated)
                    VALUES (?, ?, ?)
                """, (item_name, quantity, today))
            self.conn.commit()
            print(f"PPE inventory for {item_name} updated successfully.")
        except sqlite3.Error as e:
            print(f"Error updating PPE inventory: {e}")

    def log_training_completion(self, staff_name, training_date=None, completion_status="Completed"):
        """
        Log infection control training completion for a staff member.
        """
        try:
            training_date = training_date or datetime.date.today()
            self.cursor.execute("""
                INSERT INTO infection_control_training (staff_name, training_date, completion_status)
                VALUES (?, ?, ?)
            """, (staff_name, training_date, completion_status))
            self.conn.commit()
            print(f"Training completion logged for {staff_name}.")
        except sqlite3.Error as e:
            print(f"Error logging training completion: {e}")

    def get_all_data(self, table_name):
        """
        Fetch all records from a given table.
        """
        try:
            self.cursor.execute(f"SELECT * FROM {table_name}")
            records = self.cursor.fetchall()
            return records
        except sqlite3.Error as e:
            print(f"Error fetching data from {table_name}: {e}")
            return []

    def close_connection(self):
        """
        Close the database connection.
        """
        self.conn.close()


# Example usage
if __name__ == "__main__":
    program = NDISCOVIDPrevention()

    # Add vaccination status
    program.add_vaccination_status("John Doe", "Fully Vaccinated", "2023-01-15")

    # Update PPE inventory
    program.update_ppe_inventory("Masks", 500)

    # Log training completion
    program.log_training_completion("Jane Smith", "2023-02-01", "Completed")

    # Fetch all data
    print("Staff Vaccination Records:", program.get_all_data("staff_vaccination"))
    print("PPE Inventory Records:", program.get_all_data("ppe_inventory"))
    print("Training Completion Records:", program.get_all_data("infection_control_training"))

    # Close the connection
    program.close_connection()
```
