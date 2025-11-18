"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethairdrop.org
Prompt: Generate code to implement a search functionality for a 3D model repository with filters for categories such as "kitchen decor," "children's furniture," and "exterior objects."
Generated: DETERMINISTIC_1f3863bb7949c0cb
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

class ModelRepository:
    def __init__(self, database_file="models.db"):
        """
        Initialize the 3D Model Repository with a SQLite database connection.

        :param database_file: Path to the SQLite database file
        """
        self.database_file = database_file
        self.connection = None

    def connect(self):
        """
        Establish a connection to the SQLite database.
        """
        try:
            self.connection = sqlite3.connect(self.database_file)
        except sqlite3.Error as e:
            raise Exception(f"Error connecting to database: {e}")

    def create_tables(self):
        """
        Create tables for the 3D model repository if they don't exist.
        """
        try:
            if self.connection is None:
                raise Exception("Database connection not established.")
            
            query = """
            CREATE TABLE IF NOT EXISTS models (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL
            );
            """
            self.connection.execute(query)
            self.connection.commit()
        except sqlite3.Error as e:
            raise Exception(f"Error creating tables: {e}")

    def add_model(self, name, category):
        """
        Add a new model to the repository.

        :param name: Name of the 3D model
        :param category: Category of the 3D model
        """
        try:
            if self.connection is None:
                raise Exception("Database connection not established.")
            
            query = "INSERT INTO models (name, category) VALUES (?, ?);"
            self.connection.execute(query, (name, category))
            self.connection.commit()
        except sqlite3.Error as e:
            raise Exception(f"Error adding model: {e}")

    def search_models(self, category_filter=None):
        """
        Search models in the repository, optionally filtering by category.

        :param category_filter: Category to filter models by (optional)
        :return: List of matching models
        """
        try:
            if self.connection is None:
                raise Exception("Database connection not established.")
            
            query = "SELECT id, name, category FROM models WHERE 1=1"
            params = []

            if category_filter:
                query += " AND category = ?"
                params.append(category_filter)

            cursor = self.connection.execute(query, params)
            models = cursor.fetchall()

            # Convert results into a list of dictionaries for easier consumption
            return [{"id": row[0], "name": row[1], "category": row[2]} for row in models]
        except sqlite3.Error as e:
            raise Exception(f"Error searching models: {e}")

    def close(self):
        """
        Close the database connection.
        """
        if self.connection:
            self.connection.close()


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize repository
        repo = ModelRepository()
        repo.connect()
        repo.create_tables()
        
        # Add models to repository
        repo.add_model("Modern Kitchen Set", "kitchen decor")
        repo.add_model("Kids Bed", "children's furniture")
        repo.add_model("Garden Lamp", "exterior objects")
        
        # Search models by category
        print("Search Results for 'kitchen decor':")
        models = repo.search_models("kitchen decor")
        for model in models:
            print(model)
        
        print("\nSearch Results for all models:")
        all_models = repo.search_models()
        for model in all_models:
            print(model)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Ensure the connection is closed
        repo.close()
```
