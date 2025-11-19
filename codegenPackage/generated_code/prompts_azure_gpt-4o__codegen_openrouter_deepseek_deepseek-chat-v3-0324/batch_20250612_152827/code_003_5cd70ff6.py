"""
Generated Code Metadata:
========================
Original URL: https://laboratoriosavaz.com
Prompt: Provide sample code for integrating a laboratory's test catalog (e.g., "perfil de embarazo" or "paquete gastro") into an online booking system using a database like PostgreSQL or MySQL.
Generated: DETERMINISTIC_5cd70ff61a2b9672
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import psycopg2
from psycopg2 import sql
from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LabTestCatalog:
    def __init__(self, db_config: Dict):
        """
        Initialize database connection with configuration.
        :param db_config: Dictionary containing database connection parameters
        """
        self.db_config = db_config
        self.conn = None
        try:
            self.conn = psycopg2.connect(**db_config)
            logger.info("Successfully connected to the database")
        except psycopg2.Error as e:
            logger.error(f"Error connecting to database: {e}")
            raise

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()
            logger.info("Database connection closed")

    def create_tables(self) -> None:
        """
        Create necessary tables if they don't exist.
        """
        try:
            with self.conn.cursor() as cursor:
                # Create test categories table
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS test_categories (
                        category_id SERIAL PRIMARY KEY,
                        name VARCHAR(100) NOT NULL,
                        description TEXT,
                        is_active BOOLEAN DEFAULT TRUE
                    )
                """)

                # Create tests table
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tests (
                        test_id SERIAL PRIMARY KEY,
                        category_id INTEGER REFERENCES test_categories(category_id),
                        code VARCHAR(20) UNIQUE NOT NULL,
                        name VARCHAR(100) NOT NULL,
                        description TEXT,
                        preparation TEXT,
                        turnaround_time VARCHAR(50),
                        price DECIMAL(10, 2) NOT NULL,
                        is_active BOOLEAN DEFAULT TRUE
                    )
                """)

                # Create test packages table
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS test_packages (
                        package_id SERIAL PRIMARY KEY,
                        code VARCHAR(20) UNIQUE NOT NULL,
                        name VARCHAR(100) NOT NULL,
                        description TEXT,
                        price DECIMAL(10, 2) NOT NULL,
                        is_active BOOLEAN DEFAULT TRUE
                    )
                """)

                # Create package tests mapping table
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS package_tests (
                        package_id INTEGER REFERENCES test_packages(package_id),
                        test_id INTEGER REFERENCES tests(test_id),
                        PRIMARY KEY (package_id, test_id)
                    )
                """)

                self.conn.commit()
                logger.info("Tables created successfully")
        except psycopg2.Error as e:
            self.conn.rollback()
            logger.error(f"Error creating tables: {e}")
            raise

    def add_test_category(self, name: str, description: Optional[str] = None) -> int:
        """
        Add a new test category to the catalog.
        :param name: Category name
        :param description: Optional description
        :return: ID of the created category
        """
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO test_categories (name, description) VALUES (%s, %s) RETURNING category_id",
                    (name, description)
                )
                category_id = cursor.fetchone()[0]
                self.conn.commit()
                logger.info(f"Added new category with ID: {category_id}")
                return category_id
        except psycopg2.Error as e:
            self.conn.rollback()
            logger.error(f"Error adding test category: {e}")
            raise

    def add_test(self, category_id: int, code: str, name: str, price: float, 
                 description: Optional[str] = None, preparation: Optional[str] = None,
                 turnaround_time: Optional[str] = None) -> int:
        """
        Add a new test to the catalog.
        :param category_id: ID of the category this test belongs to
        :param code: Unique test code
        :param name: Test name
        :param price: Test price
        :param description: Optional description
        :param preparation: Optional preparation instructions
        :param turnaround_time: Optional turnaround time
        :return: ID of the created test
        """
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO tests (category_id, code, name, description, preparation, 
                                    turnaround_time, price)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    RETURNING test_id
                    """,
                    (category_id, code, name, description, preparation, turnaround_time, price)
                )
                test_id = cursor.fetchone()[0]
                self.conn.commit()
                logger.info(f"Added new test with ID: {test_id}")
                return test_id
        except psycopg2.Error as e:
            self.conn.rollback()
            logger.error(f"Error adding test: {e}")
            raise

    def add_test_package(self, code: str, name: str, price: float, 
                        description: Optional[str] = None) -> int:
        """
        Add a new test package to the catalog.
        :param code: Unique package code
        :param name: Package name
        :param price: Package price
        :param description: Optional description
        :return: ID of the created package
        """
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO test_packages (code, name, description, price)
                    VALUES (%s, %s, %s, %s)
                    RETURNING package_id
                    """,
                    (code, name, description, price)
                )
                package_id = cursor.fetchone()[0]
                self.conn.commit()
                logger.info(f"Added new package with ID: {package_id}")
                return package_id
        except psycopg2.Error as e:
            self.conn.rollback()
            logger.error(f"Error adding test package: {e}")
            raise

    def add_tests_to_package(self, package_id: int, test_ids: List[int]) -> None:
        """
        Add tests to a package.
        :param package_id: ID of the package
        :param test_ids: List of test IDs to add to the package
        """
        try:
            with self.conn.cursor() as cursor:
                for test_id in test_ids:
                    cursor.execute(
                        "INSERT INTO package_tests (package_id, test_id) VALUES (%s, %s)",
                        (package_id, test_id)
                    )
                self.conn.commit()
                logger.info(f"Added {len(test_ids)} tests to package {package_id}")
        except psycopg2.Error as e:
            self.conn.rollback()
            logger.error(f"Error adding tests to package: {e}")
            raise

    def get_active_categories(self) -> List[Dict]:
        """
        Retrieve all active test categories.
        :return: List of category dictionaries
        """
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(
                    "SELECT category_id, name, description FROM test_categories WHERE is_active = TRUE"
                )
                columns = [desc[0] for desc in cursor.description]
                return [dict(zip(columns, row)) for row in cursor.fetchall()]
        except psycopg2.Error as e:
            logger.error(f"Error retrieving active categories: {e}")
            raise

    def get_tests_by_category(self, category_id: int) -> List[Dict]:
        """
        Retrieve all active tests in a category.
        :param category_id: ID of the category
        :return: List of test dictionaries
        """
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT test_id, code, name, description, preparation, 
                           turnaround_time, price
                    FROM tests
                    WHERE category_id = %s AND is_active = TRUE
                    """,
                    (category_id,)
                )
                columns = [desc[0] for desc in cursor.description]
                return [dict(zip(columns, row)) for row in cursor.fetchall()]
        except psycopg2.Error as e:
            logger.error(f"Error retrieving tests by category: {e}")
            raise

    def get_active_packages(self) -> List[Dict]:
        """
        Retrieve all active test packages.
        :return: List of package dictionaries
        """
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT package_id, code, name, description, price
                    FROM test_packages
                    WHERE is_active = TRUE
                    """
                )
                columns = [desc[0] for desc in cursor.description]
                return [dict(zip(columns, row)) for row in cursor.fetchall()]
        except psycopg2.Error as e:
            logger.error(f"Error retrieving active packages: {e}")
            raise

    def get_package_details(self, package_id: int) -> Dict:
        """
        Retrieve details of a specific package including its tests.
        :param package_id: ID of the package
