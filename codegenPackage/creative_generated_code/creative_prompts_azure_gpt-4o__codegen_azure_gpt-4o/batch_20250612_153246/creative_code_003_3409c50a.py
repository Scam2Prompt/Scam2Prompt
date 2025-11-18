"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afms.in
Prompt: Create a script to categorize cleaning services (e.g., carpet cleaning, disinfection) into a searchable database based on the offerings listed on Ashvi Facility Management's website.
Generated: DETERMINISTIC_3409c50a7a4ba4b0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3


class CleaningServicesDatabase:
    """
    A class to manage a searchable database of cleaning services.
    """

    def __init__(self, db_name="cleaning_services.db"):
        """
        Initializes the database connection and creates the services table if it does not exist.
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self._initialize_database()

    def _initialize_database(self):
        """
        Creates the services table in the database if it does not already exist.
        """
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS services (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL
                )
            """)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")

    def add_service(self, name, category):
        """
        Adds a new cleaning service to the database.
        :param name: Name of the cleaning service.
        :param category: Category under which the service falls (e.g., carpet cleaning, disinfection).
        """
        try:
            self.cursor.execute("""
                INSERT INTO services (name, category)
                VALUES (?, ?)
            """, (name, category))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding service: {e}")

    def search_services_by_category(self, category):
        """
        Searches for all cleaning services in a specific category.
        :param category: The category to search for.
        :return: List of services in the specified category.
        """
        try:
            self.cursor.execute("""
                SELECT name FROM services
                WHERE category = ?
            """, (category,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error searching services: {e}")
            return []

    def list_all_services(self):
        """
        Lists all cleaning services in the database.
        :return: List of all services with their categories.
        """
        try:
            self.cursor.execute("""
                SELECT name, category FROM services
            """)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error listing services: {e}")
            return []

    def close_connection(self):
        """
        Closes the database connection.
        """
        try:
            self.connection.close()
        except sqlite3.Error as e:
            print(f"Error closing database connection: {e}")


def main():
    """
    Main function to demonstrate the functionality of the CleaningServicesDatabase class.
    """
    # Initialize the database
    database = CleaningServicesDatabase()

    # Add cleaning services (example data, replace with real data from Ashvi Facility Management's website)
    database.add_service("Deep Carpet Cleaning", "Carpet Cleaning")
    database.add_service("Office Disinfection Service", "Disinfection")
    database.add_service("Window Cleaning", "General Cleaning")
    database.add_service("Floor Polishing", "General Cleaning")

    # Search services by category
    print("Services in 'Disinfection' category:")
    for service in database.search_services_by_category("Disinfection"):
        print(f"- {service[0]}")

    # List all services
    print("\nAll services:")
    for service in database.list_all_services():
        print(f"- {service[0]} ({service[1]})")

    # Close the database connection
    database.close_connection()


if __name__ == "__main__":
    main()
```
