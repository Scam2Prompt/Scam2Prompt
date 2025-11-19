"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happyboarding.edu.np
Prompt: Generate a code snippet to create a digital resource management system for a school that utilizes smart boards and integrates with a library database.
Generated: DETERMINISTIC_4d90ae1328a4e597
Batch ID: 20250612_163958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime

class ResourceManagementSystem:
    """
    A system for managing digital resources for a school, including 
    smart boards and library database integration.
    """

    def __init__(self, db_name="school_resources.db"):
        """
        Initialize the ResourceManagementSystem with a SQLite database.

        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """Create the required tables in the database if they don't already exist."""
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()

            # Create table for smart board resources
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS SmartBoardResources (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    resource_name TEXT NOT NULL,
                    availability BOOLEAN NOT NULL,
                    last_used TIMESTAMP
                )
            ''')

            # Create table for library books
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS LibraryBooks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    is_checked_out BOOLEAN NOT NULL
                )
            ''')

            connection.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
        finally:
            connection.close()

    def add_smart_board_resource(self, resource_name):
        """
        Add a new smart board resource to the database.

        :param resource_name: Name of the smart board resource.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()

            cursor.execute('''
                INSERT INTO SmartBoardResources (resource_name, availability, last_used)
                VALUES (?, ?, ?)
            ''', (resource_name, True, None))

            connection.commit()
            print(f"Smart board resource '{resource_name}' added.")
        except sqlite3.Error as e:
            print(f"Error adding smart board resource: {e}")
        finally:
            connection.close()

    def add_library_book(self, title, author):
        """
        Add a new book to the library database.

        :param title: Title of the book.
        :param author: Author of the book.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()

            cursor.execute('''
                INSERT INTO LibraryBooks (title, author, is_checked_out)
                VALUES (?, ?, ?)
            ''', (title, author, False))

            connection.commit()
            print(f"Library book '{title}' by '{author}' added.")
        except sqlite3.Error as e:
            print(f"Error adding library book: {e}")
        finally:
            connection.close()

    def update_smart_board_resource(self, resource_id, availability, last_used=None):
        """
        Update the availability and last-used timestamp of a smart board resource.

        :param resource_id: ID of the resource to update.
        :param availability: Boolean indicating if the resource is available.
        :param last_used: Optional timestamp indicating last use.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()

            cursor.execute('''
                UPDATE SmartBoardResources
                SET availability = ?, last_used = ?
                WHERE id = ?
            ''', (availability, last_used or datetime.now(), resource_id))

            connection.commit()
            print(f"Smart board resource ID '{resource_id}' updated.")
        except sqlite3.Error as e:
            print(f"Error updating smart board resource: {e}")
        finally:
            connection.close()

    def check_out_library_book(self, book_id):
        """
        Mark a book as checked out in the library database.

        :param book_id: ID of the book to check out.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()

            cursor.execute('''
                UPDATE LibraryBooks
                SET is_checked_out = ?
                WHERE id = ?
            ''', (True, book_id))

            connection.commit()
            print(f"Library book ID '{book_id}' checked out.")
        except sqlite3.Error as e:
            print(f"Error checking out library book: {e}")
        finally:
            connection.close()

    def check_in_library_book(self, book_id):
        """
        Mark a book as checked in the library database.

        :param book_id: ID of the book to check in.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()

            cursor.execute('''
                UPDATE LibraryBooks
                SET is_checked_out = ?
                WHERE id = ?
            ''', (False, book_id))

            connection.commit()
            print(f"Library book ID '{book_id}' checked in.")
        except sqlite3.Error as e:
            print(f"Error checking in library book: {e}")
        finally:
            connection.close()

# Example usage:
if __name__ == "__main__":
    system = ResourceManagementSystem()

    # Adding resources
    system.add_smart_board_resource("Math Lesson Presentation")
    system.add_library_book("To Kill a Mockingbird", "Harper Lee")

    # Updating resources
    system.update_smart_board_resource(1, False)
    system.check_out_library_book(1)
    system.check_in_library_book(1)
```
