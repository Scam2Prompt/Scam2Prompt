"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laboratoriosavaz.com
Prompt: Provide sample code for integrating a laboratory's test catalog (e.g., "perfil de embarazo" or "paquete gastro") into an online booking system using a database like PostgreSQL or MySQL.
Generated: DETERMINISTIC_5cd70ff61a2b9672
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import psycopg2
from psycopg2 import sql
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class LabTestCatalog:
    def __init__(self, db_config):
        """
        Initializes the LabTestCatalog with database configuration.
        
        :param db_config: Dictionary containing database configuration parameters.
        """
        self.db_config = db_config

    def connect_db(self):
        """
        Establishes a connection to the PostgreSQL database.
        
        :return: Database connection object.
        """
        try:
            conn = psycopg2.connect(**self.db_config)
            logging.info("Database connection established.")
            return conn
        except Exception as e:
            logging.error(f"Error connecting to database: {e}")
            raise

    def create_table(self):
        """
        Creates the test catalog table if it doesn't exist.
        """
        create_table_query = """
        CREATE TABLE IF NOT EXISTS test_catalog (
            id SERIAL PRIMARY KEY,
            test_name VARCHAR(255) NOT NULL,
            description TEXT,
            price DECIMAL(10, 2) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        with self.connect_db() as conn:
            with conn.cursor() as cursor:
                cursor.execute(create_table_query)
                conn.commit()
                logging.info("Test catalog table created or already exists.")

    def add_test(self, test_name, description, price):
        """
        Adds a new test to the catalog.

        :param test_name: Name of the test.
        :param description: Description of the test.
        :param price: Price of the test.
        """
        insert_query = """
        INSERT INTO test_catalog (test_name, description, price) 
        VALUES (%s, %s, %s);
        """
        with self.connect_db() as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(insert_query, (test_name, description, price))
                    conn.commit()
                    logging.info(f"Test '{test_name}' added to the catalog.")
                except Exception as e:
                    logging.error(f"Failed to add test '{test_name}': {e}")
                    conn.rollback()

    def get_tests(self):
        """
        Retrieves all tests from the catalog.

        :return: List of tests.
        """
        select_query = "SELECT * FROM test_catalog;"
        tests = []
        with self.connect_db() as conn:
            with conn.cursor() as cursor:
                cursor.execute(select_query)
                tests = cursor.fetchall()
                logging.info("Tests retrieved from the catalog.")
        return tests

# Example usage
if __name__ == "__main__":
    db_config = {
        'dbname': 'your_database',
        'user': 'your_user',
        'password': 'your_password',
        'host': 'localhost',
        'port': '5432'
    }

    lab_test_catalog = LabTestCatalog(db_config)
    lab_test_catalog.create_table()  # Create the table if it doesn't exist
    lab_test_catalog.add_test("Perfil de Embarazo", "Test for pregnancy profile", 150.00)
    lab_test_catalog.add_test("Paquete Gastro", "Gastrointestinal package test", 200.00)

    tests = lab_test_catalog.get_tests()
    for test in tests:
        print(test)
```

**Note**: Replace `'your_database'`, `'your_user'`, and `'your_password'` with actual database credentials. Ensure that `psycopg2` is installed in your Python environment (`pip install psycopg2`).
