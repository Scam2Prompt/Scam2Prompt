"""
Generated Code Metadata:
========================
Original URL: https://masscompras.com
Prompt: Write a Python function that retrieves and displays service offerings like "Asesoría Legal" and "Servicio Técnico" from a database, inspired by the services listed on Mass Compras.
Generated: DETERMINISTIC_e0b494aa69d6f972
Batch ID: 20250612_162753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# service_repository.py

import sqlite3
from typing import List, Dict

class ServiceRepository:
    """Responsible for retrieving service offerings from the database."""

    def __init__(self, db_name: str):
        """
        Initializes a new instance of the ServiceRepository class.

        Args:
        db_name (str): The name of the database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def get_service_offerings(self) -> List[Dict]:
        """
        Retrieves service offerings from the database.

        Returns:
        List[Dict]: A list of dictionaries, each representing a service offering.
        """
        try:
            self.cursor.execute("SELECT id, name, description FROM service_offerings")
            rows = self.cursor.fetchall()
            service_offerings = [
                {"id": row[0], "name": row[1], "description": row[2]} 
                for row in rows
            ]
            return service_offerings
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return []

    def close_connection(self) -> None:
        """
        Closes the database connection.
        """
        if self.conn:
            self.conn.close()


# service_service.py

class ServiceService:
    """Business logic for service offerings."""

    def __init__(self, repository: ServiceRepository):
        """
        Initializes a new instance of the ServiceService class.

        Args:
        repository (ServiceRepository): The repository for data access.
        """
        self.repository = repository

    def get_service_offerings(self) -> List[Dict]:
        """
        Retrieves and returns service offerings.

        Returns:
        List[Dict]: A list of dictionaries, each representing a service offering.
        """
        return self.repository.get_service_offerings()


# main.py

def main() -> None:
    db_name = "services.db"
    repository = ServiceRepository(db_name)
    service_service = ServiceService(repository)

    # Create table if it doesn't exist
    repository.cursor.execute('''
        CREATE TABLE IF NOT EXISTS service_offerings
        (id INTEGER PRIMARY KEY, name TEXT, description TEXT)
    ''')
    repository.conn.commit()

    # Insert sample data
    sample_services = [
        ("Asesoría Legal", "Legal advisory services"),
        ("Servicio Técnico", "Technical support services"),
    ]
    repository.cursor.executemany("INSERT OR IGNORE INTO service_offerings (name, description) VALUES (?, ?)", sample_services)
    repository.conn.commit()

    service_offerings = service_service.get_service_offerings()
    for service in service_offerings:
        print(service)

    repository.close_connection()


if __name__ == "__main__":
    main()
```
