"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mieconline.com
Prompt: Generate code to connect service providers with customers seamlessly, as described in MIEC's Service Solutions. Include features for user registration and service matching.
Generated: DETERMINISTIC_3311eecf9cbd2e4a
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Service Matching Application

This script provides core functionality for connecting service providers with customers.
Features include:
1. User registration for both providers and customers.
2. Matching services based on customer needs and provider offerings.

Author: Expert Programmer
"""

import sqlite3

class ServiceMatchingApp:
    def __init__(self, db_name="service_matching.db"):
        """
        Initializes the application by setting up the database connection and tables.

        Parameters:
        db_name (str): Name of the SQLite database file.
        """
        self.db_name = db_name
        self._setup_database()

    def _setup_database(self):
        """
        Sets up the SQLite database with required tables for users and services.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Create users table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    role TEXT CHECK(role IN ('provider', 'customer')) NOT NULL
                )
            """)

            # Create services table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS services (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    provider_id INTEGER NOT NULL,
                    service_name TEXT NOT NULL,
                    description TEXT NOT NULL,
                    FOREIGN KEY(provider_id) REFERENCES users(id)
                )
            """)

            conn.commit()
        except sqlite3.Error as e:
            print(f"Error setting up database: {e}")
        finally:
            conn.close()

    def register_user(self, name, email, role):
        """
        Registers a new user (provider or customer).
        
        Parameters:
        name (str): Name of the user.
        email (str): Email of the user.
        role (str): Role of the user ('provider' or 'customer').

        Returns:
        bool: True if registration successful, False otherwise.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO users (name, email, role)
                VALUES (?, ?, ?)
            """, (name, email, role))

            conn.commit()
            return True
        except sqlite3.IntegrityError:
            print("Error: Email already exists.")
            return False
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False
        finally:
            conn.close()

    def add_service(self, provider_email, service_name, description):
        """
        Adds a new service under a provider's account.
        
        Parameters:
        provider_email (str): Email of the provider.
        service_name (str): Name of the service.
        description (str): Description of the service.

        Returns:
        bool: True if service added successfully, False otherwise.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Fetch provider ID
            cursor.execute("""
                SELECT id FROM users WHERE email = ? AND role = 'provider'
            """, (provider_email,))
            provider = cursor.fetchone()

            if not provider:
                print("Error: Provider not found.")
                return False

            provider_id = provider[0]

            # Insert service
            cursor.execute("""
                INSERT INTO services (provider_id, service_name, description)
                VALUES (?, ?, ?)
            """, (provider_id, service_name, description))

            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False
        finally:
            conn.close()

    def match_service(self, service_name):
        """
        Matches a service with providers offering it.
        
        Parameters:
        service_name (str): Name of the service to search for.

        Returns:
        list: A list of providers offering the service, or an empty list if none found.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Search for matching services
            cursor.execute("""
                SELECT users.name, users.email, services.description
                FROM services
                JOIN users ON services.provider_id = users.id
                WHERE LOWER(services.service_name) = LOWER(?)
            """, (service_name,))

            matches = cursor.fetchall()
            return matches
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
        finally:
            conn.close()


if __name__ == "__main__":
    # Example usage of the application
    app = ServiceMatchingApp()

    # Register users
    app.register_user("Alice", "alice@example.com", "provider")
    app.register_user("Bob", "bob@example.com", "customer")

    # Add services
    app.add_service("alice@example.com", "Plumbing", "Expert plumbing services")
    app.add_service("alice@example.com", "Electrical", "Professional electrical repairs")

    # Match service
    matches = app.match_service("Plumbing")
    for match in matches:
        print(f"Provider: {match[0]}, Email: {match[1]}, Description: {match[2]}")
```
