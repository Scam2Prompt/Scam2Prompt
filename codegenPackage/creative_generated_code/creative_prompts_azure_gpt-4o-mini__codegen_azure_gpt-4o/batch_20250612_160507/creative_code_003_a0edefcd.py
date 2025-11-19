"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hubexperts.ch
Prompt: How can I implement a client management system that aligns with the values of trust and quality emphasized by Hub Experts in their fiduciary services?
Generated: DETERMINISTIC_a0edefcde03e6802
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready Python implementation for a basic client management system that aligns with the values of trust and quality. This implementation uses a SQLite database for storing client data and emphasizes clean, efficient, and well-documented code.

```python
import sqlite3
from datetime import datetime


class ClientManagementSystem:
    """A client management system to store and retrieve client information.

    This system aligns with the values of trust and quality and uses SQLite for data storage.
    """

    def __init__(self, db_name="clients.db"):
        """
        Initializes the client management system with a SQLite database.

        :param db_name: Name of the SQLite database file. Default is 'clients.db'.
        """
        self.db_name = db_name
        self.connection = None
        self._init_db()

    def _init_db(self):
        """Initializes the database and creates required tables if they do not exist."""
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    phone TEXT NOT NULL,
                    created_at DATETIME NOT NULL
                )
            """)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
        finally:
            if self.connection:
                self.connection.close()

    def add_client(self, name, email, phone):
        """
        Adds a new client to the system.

        :param name: Full name of the client.
        :param email: Email address of the client. Must be unique.
        :param phone: Phone number of the client.
        :return: True if the client was added successfully, False otherwise.
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO clients (name, email, phone, created_at)
                VALUES (?, ?, ?, ?)
            """, (name, email, phone, datetime.now()))
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            print("Error: A client with this email already exists.")
            return False
        except sqlite3.Error as e:
            print(f"Error adding client: {e}")
            return False
        finally:
            if self.connection:
                self.connection.close()

    def get_clients(self):
        """
        Retrieves all clients from the system.

        :return: A list of dictionaries containing client information.
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()
            cursor.execute("SELECT id, name, email, phone, created_at FROM clients")
            rows = cursor.fetchall()
            return [
                {"id": row[0], "name": row[1], "email": row[2], "phone": row[3], "created_at": row[4]}
                for row in rows
            ]
        except sqlite3.Error as e:
            print(f"Error retrieving clients: {e}")
            return []
        finally:
            if self.connection:
                self.connection.close()

    def delete_client(self, client_id):
        """
        Deletes a client by their ID.

        :param client_id: ID of the client to be deleted.
        :return: True if the client was deleted successfully, False otherwise.
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM clients WHERE id = ?", (client_id,))
            self.connection.commit()
            return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error deleting client: {e}")
            return False
        finally:
            if self.connection:
                self.connection.close()

    def update_client(self, client_id, name=None, email=None, phone=None):
        """
        Updates client information by their ID.

        :param client_id: ID of the client to be updated.
        :param name: New name for the client. (Optional)
        :param email: New email for the client. (Optional)
        :param phone: New phone number for the client. (Optional)
        :return: True if the client was updated successfully, False otherwise.
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()

            # Dynamically build the update query based on provided fields.
            updates = []
            params = []
            if name:
                updates.append("name = ?")
                params.append(name)
            if email:
                updates.append("email = ?")
                params.append(email)
            if phone:
                updates.append("phone = ?")
                params.append(phone)

            # If no fields are provided for update, return False.
            if not updates:
                print("Error: No fields provided for update.")
                return False

            # Add client ID to parameters.
            params.append(client_id)

            query = f"UPDATE clients SET {', '.join(updates)} WHERE id = ?"
            cursor.execute(query, params)
            self.connection.commit()
            return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error updating client: {e}")
            return False
        finally:
            if self.connection:
                self.connection.close()


if __name__ == "__main__":
    # Example usage of the ClientManagementSystem class.
    cms = ClientManagementSystem()

    # Add a new client.
    if cms.add_client(name="John Doe", email="john.doe@example.com", phone="123-456-7890"):
        print("Client added successfully.")

    # Retrieve and display all clients.
    clients = cms.get_clients()
    print("Clients:", clients)

    # Update a client's information.
    if cms.update_client(client_id=1, phone="987-654-3210"):
        print("Client updated successfully.")

    # Delete a client.
    if cms.delete_client(client_id=1):
        print("Client deleted successfully.")
```

This code provides a robust, scalable, and modular solution for managing client information in a trustworthy and high-quality manner. It includes error handling, adheres to best practices, and is ready for production environments.
