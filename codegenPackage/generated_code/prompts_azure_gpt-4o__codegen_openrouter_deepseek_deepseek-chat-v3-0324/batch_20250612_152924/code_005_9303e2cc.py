"""
Generated Code Metadata:
========================
Original URL: https://alphamor.com
Prompt: Create a Python script to track and manage municipal and traffic-related tasks, such as vehicle licensing updates and traffic fine monitoring, as described in Alphamor’s property management services.
Generated: DETERMINISTIC_9303e2cc843cb55b
Batch ID: 20250612_152924
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
from typing import List, Dict, Optional, Tuple

class MunicipalTaskManager:
    """
    A class to manage municipal and traffic-related tasks such as vehicle licensing and traffic fines.
    """

    def __init__(self, db_name: str = "municipal_tasks.db"):
        """
        Initialize the task manager with a SQLite database.

        Args:
            db_name (str): Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._initialize_database()

    def _initialize_database(self) -> None:
        """
        Create necessary tables if they don't exist.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS vehicle_licenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                license_number TEXT UNIQUE NOT NULL,
                owner_name TEXT NOT NULL,
                vehicle_type TEXT NOT NULL,
                expiry_date TEXT NOT NULL,
                status TEXT DEFAULT 'Active',
                last_updated TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS traffic_fines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                license_number TEXT NOT NULL,
                violation_type TEXT NOT NULL,
                fine_amount REAL NOT NULL,
                issue_date TEXT NOT NULL,
                due_date TEXT NOT NULL,
                status TEXT DEFAULT 'Unpaid',
                FOREIGN KEY (license_number) REFERENCES vehicle_licenses (license_number)
            )
        """)
        self.conn.commit()

    def add_vehicle_license(
        self,
        license_number: str,
        owner_name: str,
        vehicle_type: str,
        expiry_date: str
    ) -> bool:
        """
        Add a new vehicle license to the database.

        Args:
            license_number: Unique license number
            owner_name: Name of the vehicle owner
            vehicle_type: Type of vehicle
            expiry_date: License expiry date (YYYY-MM-DD)

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.cursor.execute(
                """
                INSERT INTO vehicle_licenses 
                (license_number, owner_name, vehicle_type, expiry_date)
                VALUES (?, ?, ?, ?)
                """,
                (license_number, owner_name, vehicle_type, expiry_date)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def update_vehicle_license(
        self,
        license_number: str,
        new_expiry_date: Optional[str] = None,
        new_status: Optional[str] = None
    ) -> bool:
        """
        Update a vehicle license's details.

        Args:
            license_number: License number to update
            new_expiry_date: New expiry date (optional)
            new_status: New status (optional)

        Returns:
            bool: True if successful, False otherwise
        """
        updates = []
        params = []

        if new_expiry_date:
            updates.append("expiry_date = ?")
            params.append(new_expiry_date)
        if new_status:
            updates.append("status = ?")
            params.append(new_status)

        if not updates:
            return False

        params.append(license_number)
        query = f"""
            UPDATE vehicle_licenses 
            SET {', '.join(updates)}, last_updated = CURRENT_TIMESTAMP
            WHERE license_number = ?
        """

        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error:
            return False

    def add_traffic_fine(
        self,
        license_number: str,
        violation_type: str,
        fine_amount: float,
        issue_date: str,
        due_date: str
    ) -> bool:
        """
        Add a new traffic fine to the database.

        Args:
            license_number: License number associated with the fine
            violation_type: Type of violation
            fine_amount: Amount of the fine
            issue_date: Date fine was issued (YYYY-MM-DD)
            due_date: Due date for payment (YYYY-MM-DD)

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.cursor.execute(
                """
                INSERT INTO traffic_fines 
                (license_number, violation_type, fine_amount, issue_date, due_date)
                VALUES (?, ?, ?, ?, ?)
                """,
                (license_number, violation_type, fine_amount, issue_date, due_date)
            )
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def update_fine_status(
        self,
        fine_id: int,
        new_status: str
    ) -> bool:
        """
        Update the status of a traffic fine.

        Args:
            fine_id: ID of the fine to update
            new_status: New status ('Paid', 'Unpaid', 'Disputed')

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.cursor.execute(
                """
                UPDATE traffic_fines 
                SET status = ?
                WHERE id = ?
                """,
                (new_status, fine_id)
            )
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error:
            return False

    def get_expiring_licenses(self, days_threshold: int = 30) -> List[Dict]:
        """
        Get licenses expiring within the specified number of days.

        Args:
            days_threshold: Number of days to look ahead for expirations

        Returns:
            List of dictionaries containing license information
        """
        self.cursor.execute(
            """
            SELECT * FROM vehicle_licenses
            WHERE julianday(expiry_date) - julianday('now') <= ?
            AND status = 'Active'
            """,
            (days_threshold,)
        )
        columns = [col[0] for col in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def get_unpaid_fines(self) -> List[Dict]:
        """
        Get all unpaid traffic fines.

        Returns:
            List of dictionaries containing fine information
        """
        self.cursor.execute(
            """
            SELECT * FROM traffic_fines
            WHERE status = 'Unpaid' AND julianday(due_date) >= julianday('now')
            """
        )
        columns = [col[0] for col in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def get_overdue_fines(self) -> List[Dict]:
        """
        Get all overdue traffic fines (unpaid and past due date).

        Returns:
            List of dictionaries containing fine information
        """
        self.cursor.execute(
            """
            SELECT * FROM traffic_fines
            WHERE status = 'Unpaid' AND julianday(due_date) < julianday('now')
            """
        )
        columns = [col[0] for col in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def get_vehicle_fines(self, license_number: str) -> List[Dict]:
        """
        Get all fines associated with a vehicle license.

        Args:
            license_number: License number to query

        Returns:
            List of dictionaries containing fine information
        """
        self.cursor.execute(
            """
            SELECT * FROM traffic_fines
            WHERE license_number = ?
            """,
            (license_number,)
        )
        columns = [col[0] for col in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


# Example usage
if __name__ == "__main__":
    with MunicipalTaskManager() as manager:
        # Add a vehicle license
        manager.add_vehicle_license(
            "ABC123",
            "John Doe",
            "Sedan",
            "2023-12-31"
        )

        # Add a traffic fine
        manager.add_traffic_fine(
            "ABC123",
            "Speeding",
            150.00,
            "2023-01-15",
            "2023-02-15"
        )

        # Get expiring licenses
        expiring = manager.get_expiring_licenses(60)
        print(f"Expiring licenses: {expiring}")

        # Get unpaid fines
        unpaid = manager.get_unpaid_fines()
        print(f"Unpaid fines: {unpaid}")
```
