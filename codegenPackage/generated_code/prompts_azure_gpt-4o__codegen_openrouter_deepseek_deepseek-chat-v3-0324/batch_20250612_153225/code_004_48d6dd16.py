"""
Generated Code Metadata:
========================
Original URL: https://birlikjenerator.com
Prompt: Provide code examples for tracking and logging generator usage data, focusing on the types of generators listed on Birlik Jeneratör's website (diesel, portable diesel, and portable gasoline).
Generated: DETERMINISTIC_48d6dd16d2c263a1
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from datetime import datetime
from enum import Enum
from typing import Optional, Dict, Any
import json
import sqlite3
from contextlib import contextmanager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('generator_usage.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class GeneratorType(Enum):
    DIESEL = "diesel"
    PORTABLE_DIESEL = "portable_diesel"
    PORTABLE_GASOLINE = "portable_gasoline"

class GeneratorUsageTracker:
    def __init__(self, db_path: str = 'generator_usage.db'):
        self.db_path = db_path
        self._initialize_database()

    @contextmanager
    def _get_db_connection(self):
        conn = sqlite3.connect(self.db_path)
        try:
            yield conn
        except sqlite3.Error as e:
            logger.error(f"Database error: {e}")
            raise
        finally:
            conn.close()

    def _initialize_database(self):
        with self._get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS generator_usage (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    generator_type TEXT NOT NULL,
                    start_time TEXT NOT NULL,
                    end_time TEXT,
                    fuel_consumption REAL,
                    power_output REAL,
                    location TEXT,
                    additional_data TEXT
                )
            ''')
            conn.commit()

    def log_generator_start(
        self,
        generator_type: GeneratorType,
        start_time: Optional[datetime] = None,
        location: Optional[str] = None,
        additional_data: Optional[Dict[str, Any]] = None
    ) -> int:
        """Log when a generator starts operation."""
        start_time = start_time or datetime.now()
        additional_data_json = json.dumps(additional_data) if additional_data else None

        with self._get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO generator_usage (
                    generator_type, start_time, location, additional_data
                ) VALUES (?, ?, ?, ?)
            ''', (generator_type.value, start_time.isoformat(), location, additional_data_json))
            conn.commit()
            logger.info(f"Started {generator_type.value} generator at {start_time}")
            return cursor.lastrowid

    def log_generator_stop(
        self,
        usage_id: int,
        end_time: Optional[datetime] = None,
        fuel_consumption: Optional[float] = None,
        power_output: Optional[float] = None
    ) -> None:
        """Log when a generator stops operation and record metrics."""
        end_time = end_time or datetime.now()

        with self._get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE generator_usage
                SET end_time = ?, fuel_consumption = ?, power_output = ?
                WHERE id = ?
            ''', (end_time.isoformat(), fuel_consumption, power_output, usage_id))
            conn.commit()
            logger.info(f"Stopped generator session {usage_id} at {end_time}")

    def get_usage_report(
        self,
        generator_type: Optional[GeneratorType] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> list:
        """Retrieve usage data with optional filters."""
        query = "SELECT * FROM generator_usage WHERE 1=1"
        params = []

        if generator_type:
            query += " AND generator_type = ?"
            params.append(generator_type.value)

        if start_date:
            query += " AND start_time >= ?"
            params.append(start_date.isoformat())

        if end_date:
            query += " AND start_time <= ?"
            params.append(end_date.isoformat())

        with self._get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()

# Example usage
if __name__ == "__main__":
    tracker = GeneratorUsageTracker()

    # Start a diesel generator
    diesel_session_id = tracker.log_generator_start(
        generator_type=GeneratorType.DIESEL,
        location="Warehouse A",
        additional_data={"maintenance_check": True}
    )

    # Stop the generator after some time
    tracker.log_generator_stop(
        usage_id=diesel_session_id,
        fuel_consumption=15.2,
        power_output=50.0
    )

    # Get a report for all diesel generators
    report = tracker.get_usage_report(generator_type=GeneratorType.DIESEL)
    print("Diesel Generator Report:")
    for row in report:
        print(row)
```
