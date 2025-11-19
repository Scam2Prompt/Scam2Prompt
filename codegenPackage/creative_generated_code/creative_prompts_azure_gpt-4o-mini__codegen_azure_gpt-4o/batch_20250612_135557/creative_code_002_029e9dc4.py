"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apperley.ca
Prompt: How can I implement a search function in a genealogy application to find ancestors by first name and surname, inspired by the search features on Apperley.ca?
Generated: DETERMINISTIC_029e9dc4c9180f98
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

class GenealogyDatabase:
    """
    A class to represent a genealogy database.
    """

    def __init__(self, db_path):
        """
        Initializes the connection to the database.
        
        Args:
            db_path (str): Path to the SQLite database file.
        """
        self.db_path = db_path
        self.connection = None

    def connect(self):
        """
        Establishes a connection to the SQLite database.
        """
        try:
            self.connection = sqlite3.connect(self.db_path)
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def disconnect(self):
        """
        Closes the connection to the SQLite database.
        """
        if self.connection:
            self.connection.close()

    def search_ancestors(self, first_name, surname):
        """
        Searches for ancestors in the database by first name and surname.
        
        Args:
            first_name (str): First name of the ancestor.
            surname (str): Surname of the ancestor.
        
        Returns:
            list: A list of dictionaries containing ancestor details.
        """
        if not self.connection:
            raise ValueError("Database connection is not established.")

        query = """
        SELECT id, first_name, surname, birth_date, death_date
        FROM ancestors
        WHERE first_name LIKE ? AND surname LIKE ?
        """
        try:
            cursor = self.connection.cursor()
            # Use parameterized query to prevent SQL injection
            wildcard_first_name = f"%{first_name}%"
            wildcard_surname = f"%{surname}%"
            cursor.execute(query, (wildcard_first_name, wildcard_surname))
            
            # Fetch all results
            rows = cursor.fetchall()
            
            # Transform rows into a list of dictionaries for better usability
            results = [
                {
                    "id": row[0],
                    "first_name": row[1],
                    "surname": row[2],
                    "birth_date": row[3],
                    "death_date": row[4],
                }
                for row in rows
            ]
            
            return results
        except sqlite3.Error as e:
            print(f"Error during search query: {e}")
            raise

if __name__ == "__main__":
    # Example Usage
    db = GenealogyDatabase("genealogy.db")
    
    try:
        db.connect()

        # Perform a search
        first_name = input("Enter first name to search: ").strip()
        surname = input("Enter surname to search: ").strip()
        results = db.search_ancestors(first_name, surname)
        
        if results:
            print("Search Results:")
            for ancestor in results:
                print(
                    f"ID: {ancestor['id']}, "
                    f"Name: {ancestor['first_name']} {ancestor['surname']}, "
                    f"Birth Date: {ancestor['birth_date']}, "
                    f"Death Date: {ancestor['death_date']}"
                )
        else:
            print("No ancestors found matching the search criteria.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    finally:
        db.disconnect()
```

### Notes:
- This code assumes there is a SQLite database file named `genealogy.db`, with a table named `ancestors` containing columns: `id`, `first_name`, `surname`, `birth_date`, and `death_date`.
- Proper error handling is included for both database operations and general exceptions.
- The code is designed to prevent SQL injection by using parameterized queries.
- The search supports partial matches (`LIKE`) using wildcards.
