"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meyerseim.com
Prompt: Write Python code to extract genealogical data from a database and organize it into family trees, referencing the Meyer/Seim families as an example.
Generated: DETERMINISTIC_6a58a83b66ea7eda
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from collections import defaultdict

class FamilyTreeExtractor:
    """
    A class to extract genealogical data from a database and organize it into family trees.
    """

    def __init__(self, db_path):
        """
        Initializes the FamilyTreeExtractor.

        Args:
            db_path (str): Path to the SQLite database file.
        """
        self.db_path = db_path

    def connect_to_database(self):
        """
        Establishes a connection to the SQLite database.

        Returns:
            sqlite3.Connection: Connection object to the database.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            return conn
        except sqlite3.Error as e:
            raise Exception(f"Database connection error: {e}")

    def fetch_genealogical_data(self, conn):
        """
        Fetches genealogical data from the database.

        Args:
            conn (sqlite3.Connection): Connection object to the database.

        Returns:
            list[dict]: List of dictionaries containing genealogical data.
        """
        try:
            cursor = conn.cursor()

            # Example query to fetch genealogical data
            # Assumes the database has a table `people` with fields `id`, `name`, `parent_id`
            query = """
                SELECT id, name, parent_id, family_name
                FROM people
                WHERE family_name IN ('Meyer', 'Seim');
            """
            cursor.execute(query)

            # Fetch all rows and convert them into a list of dictionaries
            rows = cursor.fetchall()
            return [
                {"id": row[0], "name": row[1], "parent_id": row[2], "family_name": row[3]}
                for row in rows
            ]
        except sqlite3.Error as e:
            raise Exception(f"Data fetching error: {e}")

    def organize_into_family_trees(self, data):
        """
        Organizes genealogical data into family trees.

        Args:
            data (list[dict]): List of dictionaries containing genealogical data.

        Returns:
            dict: Dictionary where keys are family names and values are family trees.
        """
        # Organize by family name
        families = defaultdict(dict)

        # Build a dictionary for each family name
        for entry in data:
            family_name = entry["family_name"]
            person_id = entry["id"]
            parent_id = entry["parent_id"]

            # Add person to their family structure
            families[family_name][person_id] = {
                "name": entry["name"],
                "parent_id": parent_id,
                "children": [],
            }

        # Link children to their parents within the family
        for family_name, members in families.items():
            for person_id, details in members.items():
                parent_id = details["parent_id"]
                if parent_id and parent_id in members:
                    members[parent_id]["children"].append(details)

        return {family: members for family, members in families.items()}

    def extract_and_build_family_trees(self):
        """
        End-to-end process to extract genealogical data and organize it into family trees.

        Returns:
            dict: Dictionary where keys are family names and values are family trees.
        """
        conn = None
        try:
            # Step 1: Connect to database
            conn = self.connect_to_database()

            # Step 2: Fetch genealogical data
            data = self.fetch_genealogical_data(conn)

            # Step 3: Organize data into family trees
            family_trees = self.organize_into_family_trees(data)

            return family_trees
        finally:
            # Ensure connection is closed
            if conn:
                conn.close()


# Example usage
if __name__ == "__main__":
    # Path to the SQLite database
    database_path = "genealogy.db"

    # Create an instance of the FamilyTreeExtractor
    extractor = FamilyTreeExtractor(database_path)

    try:
        # Extract and build family trees
        family_trees = extractor.extract_and_build_family_trees()

        # Print the family trees (for demonstration purposes)
        for family_name, members in family_trees.items():
            print(f"Family: {family_name}")
            for member_id, details in members.items():
                print(f"  ID: {member_id}, Name: {details['name']}, Parent ID: {details['parent_id']}")
                for child in details["children"]:
                    print(f"    Child: {child['name']}")
    except Exception as e:
        print(f"Error: {e}")
```
