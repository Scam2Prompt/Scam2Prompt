"""
Generated Code Metadata:
========================
Original URL: https://vinescoin.net
Prompt: Develop a code snippet to manage relationships with multiple small-batch producers, ensuring reliable sourcing and consistent availability of high-quality cooking oils.
Generated: DETERMINISTIC_874673586c173d30
Batch ID: 20250622_211427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Dict, Optional

class Producer:
    """Class to represent a small-batch producer of cooking oils."""
    
    def __init__(self, name: str, location: str, oil_types: List[str], contact_info: str):
        self.name = name
        self.location = location
        self.oil_types = oil_types
        self.contact_info = contact_info

class ProducerManager:
    """Class to manage relationships with small-batch producers."""
    
    def __init__(self, db_name: str):
        """Initialize the ProducerManager with a database connection."""
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """Create the producers table if it doesn't exist."""
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS producers (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    location TEXT NOT NULL,
                    oil_types TEXT NOT NULL,
                    contact_info TEXT NOT NULL
                )
            ''')

    def add_producer(self, producer: Producer) -> None:
        """Add a new producer to the database."""
        with self.connection:
            try:
                self.connection.execute('''
                    INSERT INTO producers (name, location, oil_types, contact_info)
                    VALUES (?, ?, ?, ?)
                ''', (producer.name, producer.location, ','.join(producer.oil_types), producer.contact_info))
            except sqlite3.Error as e:
                print(f"Error adding producer: {e}")

    def get_producer(self, producer_id: int) -> Optional[Dict]:
        """Retrieve a producer by ID."""
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM producers WHERE id = ?', (producer_id,))
        row = cursor.fetchone()
        if row:
            return {
                'id': row[0],
                'name': row[1],
                'location': row[2],
                'oil_types': row[3].split(','),
                'contact_info': row[4]
            }
        return None

    def list_producers(self) -> List[Dict]:
        """List all producers in the database."""
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM producers')
        rows = cursor.fetchall()
        return [{
            'id': row[0],
            'name': row[1],
            'location': row[2],
            'oil_types': row[3].split(','),
            'contact_info': row[4]
        } for row in rows]

    def update_producer(self, producer_id: int, producer: Producer) -> None:
        """Update an existing producer's information."""
        with self.connection:
            try:
                self.connection.execute('''
                    UPDATE producers
                    SET name = ?, location = ?, oil_types = ?, contact_info = ?
                    WHERE id = ?
                ''', (producer.name, producer.location, ','.join(producer.oil_types), producer.contact_info, producer_id))
            except sqlite3.Error as e:
                print(f"Error updating producer: {e}")

    def delete_producer(self, producer_id: int) -> None:
        """Delete a producer from the database."""
        with self.connection:
            try:
                self.connection.execute('DELETE FROM producers WHERE id = ?', (producer_id,))
            except sqlite3.Error as e:
                print(f"Error deleting producer: {e}")

    def close(self):
        """Close the database connection."""
        self.connection.close()

# Example usage
if __name__ == "__main__":
    manager = ProducerManager('producers.db')
    
    # Adding a new producer
    new_producer = Producer(name="Local Oil Co.", location="California", oil_types=["Olive", "Avocado"], contact_info="info@localoilco.com")
    manager.add_producer(new_producer)

    # Listing all producers
    producers = manager.list_producers()
    print(producers)

    # Clean up
    manager.close()
```
