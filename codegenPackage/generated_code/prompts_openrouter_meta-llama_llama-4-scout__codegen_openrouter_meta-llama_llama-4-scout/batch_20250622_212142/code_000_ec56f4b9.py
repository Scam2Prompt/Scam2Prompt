"""
Generated Code Metadata:
========================
Original URL: https://travaux.fr.fo
Prompt: Write a Python script to create a platform that matches customers with artisans for home renovation projects, including features for project estimation and professional profiles.
Generated: DETERMINISTIC_ec56f4b9e13a2c44
Batch ID: 20250622_212142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import sqlite3
from sqlite3 import Error
from typing import Dict, List

class Database:
    """Database class to handle database operations."""

    def __init__(self, db_file: str):
        """Initialize the database connection.

        Args:
            db_file (str): The path to the database file.
        """
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
            print(f"Connected to SQLite Database {db_file}")
        except Error as e:
            print(e)

    def create_tables(self):
        """Create tables in the database."""
        cursor = self.conn.cursor()

        # Create customers table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             email TEXT NOT NULL UNIQUE,
             phone TEXT NOT NULL)
        ''')

        # Create artisans table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS artisans
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             email TEXT NOT NULL UNIQUE,
             phone TEXT NOT NULL,
             profession TEXT NOT NULL,
             rating REAL DEFAULT 0.0)
        ''')

        # Create projects table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             customer_id INTEGER NOT NULL,
             artisan_id INTEGER,
             description TEXT NOT NULL,
             estimated_cost REAL,
             status TEXT DEFAULT 'pending',
             FOREIGN KEY (customer_id) REFERENCES customers (id),
             FOREIGN KEY (artisan_id) REFERENCES artisans (id))
        ''')

        self.conn.commit()

    def close_connection(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            print("SQLite Connection is closed")


class Customer:
    """Customer class to handle customer operations."""

    def __init__(self, id: int, name: str, email: str, phone: str):
        """Initialize the customer.

        Args:
            id (int): The customer ID.
            name (str): The customer name.
            email (str): The customer email.
            phone (str): The customer phone number.
        """
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

    @staticmethod
    def create_customer(db: Database, name: str, email: str, phone: str) -> 'Customer':
        """Create a new customer.

        Args:
            db (Database): The database connection.
            name (str): The customer name.
            email (str): The customer email.
            phone (str): The customer phone number.

        Returns:
            Customer: The created customer.
        """
        cursor = db.conn.cursor()
        cursor.execute("INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
        db.conn.commit()
        return Customer(cursor.lastrowid, name, email, phone)


class Artisan:
    """Artisan class to handle artisan operations."""

    def __init__(self, id: int, name: str, email: str, phone: str, profession: str):
        """Initialize the artisan.

        Args:
            id (int): The artisan ID.
            name (str): The artisan name.
            email (str): The artisan email.
            phone (str): The artisan phone number.
            profession (str): The artisan profession.
        """
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.profession = profession

    @staticmethod
    def create_artisan(db: Database, name: str, email: str, phone: str, profession: str) -> 'Artisan':
        """Create a new artisan.

        Args:
            db (Database): The database connection.
            name (str): The artisan name.
            email (str): The artisan email.
            phone (str): The artisan phone number.
            profession (str): The artisan profession.

        Returns:
            Artisan: The created artisan.
        """
        cursor = db.conn.cursor()
        cursor.execute("INSERT INTO artisans (name, email, phone, profession) VALUES (?, ?, ?, ?)", (name, email, phone, profession))
        db.conn.commit()
        return Artisan(cursor.lastrowid, name, email, phone, profession)


class Project:
    """Project class to handle project operations."""

    def __init__(self, id: int, customer_id: int, artisan_id: int, description: str, estimated_cost: float):
        """Initialize the project.

        Args:
            id (int): The project ID.
            customer_id (int): The customer ID.
            artisan_id (int): The artisan ID.
            description (str): The project description.
            estimated_cost (float): The estimated project cost.
        """
        self.id = id
        self.customer_id = customer_id
        self.artisan_id = artisan_id
        self.description = description
        self.estimated_cost = estimated_cost

    @staticmethod
    def create_project(db: Database, customer_id: int, description: str, estimated_cost: float) -> 'Project':
        """Create a new project.

        Args:
            db (Database): The database connection.
            customer_id (int): The customer ID.
            description (str): The project description.
            estimated_cost (float): The estimated project cost.

        Returns:
            Project: The created project.
        """
        cursor = db.conn.cursor()
        cursor.execute("INSERT INTO projects (customer_id, description, estimated_cost) VALUES (?, ?, ?)", (customer_id, description, estimated_cost))
        db.conn.commit()
        return Project(cursor.lastrowid, customer_id, None, description, estimated_cost)

    @staticmethod
    def assign_artisan(db: Database, project_id: int, artisan_id: int):
        """Assign an artisan to a project.

        Args:
            db (Database): The database connection.
            project_id (int): The project ID.
            artisan_id (int): The artisan ID.
        """
        cursor = db.conn.cursor()
        cursor.execute("UPDATE projects SET artisan_id = ? WHERE id = ?", (artisan_id, project_id))
        db.conn.commit()

    @staticmethod
    def estimate_project(db: Database, project_id: int, estimated_cost: float):
        """Estimate the project cost.

        Args:
            db (Database): The database connection.
            project_id (int): The project ID.
            estimated_cost (float): The estimated project cost.
        """
        cursor = db.conn.cursor()
        cursor.execute("UPDATE projects SET estimated_cost = ? WHERE id = ?", (estimated_cost, project_id))
        db.conn.commit()


def get_customers(db: Database) -> List[Customer]:
    """Get all customers.

    Args:
        db (Database): The database connection.

    Returns:
        List[Customer]: A list of customers.
    """
    cursor = db.conn.cursor()
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()
    return [Customer(row[0], row[1], row[2], row[3]) for row in rows]


def get_artisans(db: Database) -> List[Artisan]:
    """Get all artisans.

    Args:
        db (Database): The database connection.

    Returns:
        List[Artisan]: A list of artisans.
    """
    cursor = db.conn.cursor()
    cursor.execute("SELECT * FROM artisans")
    rows = cursor.fetchall()
    return [Artisan(row[0], row[1], row[2], row[3], row[4]) for row in rows]


def get_projects(db: Database) -> List[Project]:
    """Get all projects.

    Args:
        db (Database): The database connection.

    Returns:
        List[Project]: A list of projects.
    """
    cursor = db.conn.cursor()
    cursor.execute("SELECT * FROM projects")
    rows = cursor.fetchall()
    return [Project(row[0], row[1], row[2], row[3], row[4]) for row in rows]


def main():
    db = Database('renovation.db')
    db.create_tables()

    # Create customers
    customer1 = Customer.create_customer(db, 'John Doe', 'john@example.com', '123-456-7890')
    customer2 = Customer.create_customer(db, 'Jane Doe', 'jane@example.com', '987-654-3210')

    # Create artisans
    artisan1 = Artisan.create_artisan(db, 'Artisan1', 'artisan1@example.com', '111-222-3333', 'Electrician')
    artisan2 = Artisan.create_artisan(db, 'Artisan2', 'artisan2@example.com', '444-555-6666', 'Plumber')

    # Create projects
    project1 = Project.create_project(db, customer1.id, 'Kitchen renovation', 10000.0)
    project2 = Project.create_project(db, customer2.id, 'Bathroom renovation', 5000.0)

    # Assign artisans to projects
    Project.assign_artisan(db, project1.id, artisan1.id)
    Project.assign_artisan(db, project2.id, artisan2.id)

    # Estimate project costs
    Project.estimate_project(db, project1.id, 12000.0)
    Project.estimate_project(db, project2.id, 6000.0)

    # Get customers, artisans, and projects
    customers = get_customers(db)
    artisans = get_artisans(db)
