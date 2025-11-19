"""
Generated Code Metadata:
========================
Original URL: https://fantom.de
Prompt: How can I implement a database programming solution for a client project based on the services offered by Fantom Internet Dienst?
Generated: DETERMINISTIC_983d175a97d79493
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fantom_internet_dienst.py

import sqlite3
from enum import Enum
from typing import Dict, List

class ServiceType(str, Enum):
    """ Enum for Fantom Internet Dienst services """
    INTERNET = "internet"
    TELEVISION = "television"
    PHONE = "phone"

class FantomInternetDienst:
    """ Class representing Fantom Internet Dienst database """

    def __init__(self, db_name: str):
        """
        Initialize the Fantom Internet Dienst database

        Args:
        db_name (str): Name of the database
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """ Create tables in the database """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers
            (id INTEGER PRIMARY KEY, name TEXT, email TEXT)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS services
            (id INTEGER PRIMARY KEY, type TEXT, speed TEXT, price REAL)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS subscriptions
            (id INTEGER PRIMARY KEY, customer_id INTEGER, service_id INTEGER,
            FOREIGN KEY (customer_id) REFERENCES customers (id),
            FOREIGN KEY (service_id) REFERENCES services (id))
        ''')

        self.conn.commit()

    def add_customer(self, name: str, email: str) -> int:
        """
        Add a new customer to the database

        Args:
        name (str): Customer name
        email (str): Customer email

        Returns:
        int: Customer ID
        """
        self.cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", (name, email))
        self.conn.commit()
        return self.cursor.lastrowid

    def add_service(self, service_type: ServiceType, speed: str, price: float) -> int:
        """
        Add a new service to the database

        Args:
        service_type (ServiceType): Type of service
        speed (str): Service speed
        price (float): Service price

        Returns:
        int: Service ID
        """
        self.cursor.execute("INSERT INTO services (type, speed, price) VALUES (?, ?, ?)", 
                            (service_type.value, speed, price))
        self.conn.commit()
        return self.cursor.lastrowid

    def subscribe_customer(self, customer_id: int, service_id: int):
        """
        Subscribe a customer to a service

        Args:
        customer_id (int): Customer ID
        service_id (int): Service ID
        """
        self.cursor.execute("INSERT INTO subscriptions (customer_id, service_id) VALUES (?, ?)", 
                            (customer_id, service_id))
        self.conn.commit()

    def get_customer_subscriptions(self, customer_id: int) -> List[Dict]:
        """
        Get a customer's subscriptions

        Args:
        customer_id (int): Customer ID

        Returns:
        List[Dict]: List of subscriptions
        """
        self.cursor.execute('''
            SELECT s.type, s.speed, s.price 
            FROM subscriptions sub 
            JOIN services s ON sub.service_id = s.id 
            WHERE sub.customer_id = ?
        ''', (customer_id,))

        return [{'type': row[0], 'speed': row[1], 'price': row[2]} for row in self.cursor.fetchall()]

    def close_connection(self):
        """ Close the database connection """
        self.conn.close()


def main():
    # Example usage
    db = FantomInternetDienst('fantom_internet_dienst.db')

    customer_id = db.add_customer('John Doe', 'john@example.com')
    service_id = db.add_service(ServiceType.INTERNET, '100 Mbps', 50.0)
    db.subscribe_customer(customer_id, service_id)

    subscriptions = db.get_customer_subscriptions(customer_id)
    for subscription in subscriptions:
        print(subscription)

    db.close_connection()


if __name__ == "__main__":
    main()
```
