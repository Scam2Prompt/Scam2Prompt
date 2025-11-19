"""
Generated Code Metadata:
========================
Original URL: https://veristenlabs.com
Prompt: Develop a basic data logging system for tracking blood pressure and oxygen levels over time, including data visualization.
Generated: DETERMINISTIC_4c67bdb348fa31b7
Batch ID: 20250622_212817
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
import matplotlib.pyplot as plt
from typing import Optional, List, Tuple

class HealthLogger:
    """
    A class to log and visualize blood pressure and oxygen level data.
    """

    def __init__(self, db_name: str = "health_data.db"):
        """
        Initialize the logger with a SQLite database connection.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self._create_table()

    def _create_table(self) -> None:
        """
        Create the health_data table if it doesn't exist.
        """
        query = """
        CREATE TABLE IF NOT EXISTS health_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME NOT NULL,
            systolic INTEGER NOT NULL,
            diastolic INTEGER NOT NULL,
            oxygen_level INTEGER NOT NULL,
            notes TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def log_data(
        self,
        systolic: int,
        diastolic: int,
        oxygen_level: int,
        notes: Optional[str] = None
    ) -> None:
        """
        Log new health data entry.
        
        Args:
            systolic: Systolic blood pressure
            diastolic: Diastolic blood pressure
            oxygen_level: Blood oxygen level (SpO2)
            notes: Optional notes about the reading
        """
        if systolic <= 0 or diastolic <= 0 or oxygen_level <= 0:
            raise ValueError("All values must be positive numbers")
            
        if systolic < diastolic:
            raise ValueError("Systolic must be greater than diastolic")

        query = """
        INSERT INTO health_data (timestamp, systolic, diastolic, oxygen_level, notes)
        VALUES (?, ?, ?, ?, ?)
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.conn.execute(query, (timestamp, systolic, diastolic, oxygen_level, notes))
        self.conn.commit()

    def get_all_data(self) -> List[Tuple]:
        """
        Retrieve all logged health data.
        
        Returns:
            List of tuples containing all health data records
        """
        query = "SELECT * FROM health_data ORDER BY timestamp ASC"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def visualize_data(self, days: Optional[int] = None) -> None:
        """
        Generate plots for blood pressure and oxygen levels over time.
        
        Args:
            days: Number of days to visualize (None for all data)
        """
        data = self.get_all_data()
        if not data:
            print("No data available to visualize")
            return

        timestamps = []
        systolic = []
        diastolic = []
        oxygen = []

        for record in data:
            record_time = datetime.strptime(record[1], "%Y-%m-%d %H:%M:%S")
            if days is None or (datetime.now() - record_time).days <= days:
                timestamps.append(record_time)
                systolic.append(record[2])
                diastolic.append(record[3])
                oxygen.append(record[4])

        if not timestamps:
            print(f"No data available for the last {days} days")
            return

        plt.figure(figsize=(12, 8))

        # Blood pressure plot
        plt.subplot(2, 1, 1)
        plt.plot(timestamps, systolic, label="Systolic", color="red")
        plt.plot(timestamps, diastolic, label="Diastolic", color="blue")
        plt.title("Blood Pressure Over Time")
        plt.ylabel("mmHg")
        plt.legend()
        plt.grid(True)

        # Oxygen level plot
        plt.subplot(2, 1, 2)
        plt.plot(timestamps, oxygen, label="Oxygen Level", color="green")
        plt.title("Blood Oxygen Level Over Time")
        plt.ylabel("SpO2 %")
        plt.xlabel("Date/Time")
        plt.legend()
        plt.grid(True)

        plt.tight_layout()
        plt.show()

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
    with HealthLogger() as logger:
        # Sample data logging
        try:
            logger.log_data(120, 80, 98, "Morning reading")
            logger.log_data(118, 78, 97, "Afternoon reading")
            logger.log_data(122, 82, 96, "Evening reading")
        except ValueError as e:
            print(f"Error logging data: {e}")

        # Visualize last 7 days of data
        logger.visualize_data(days=7)
```
