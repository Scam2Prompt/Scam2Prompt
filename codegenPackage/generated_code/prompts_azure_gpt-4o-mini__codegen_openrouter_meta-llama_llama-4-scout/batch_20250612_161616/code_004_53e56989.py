"""
Generated Code Metadata:
========================
Original URL: https://ntalo.co.za
Prompt: Illustrate how to implement a database schema for storing information about construction projects and equipment hire, taking cues from the comprehensive services offered by Ntalo Investments.
Generated: DETERMINISTIC_53e5698916cb472f
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for construction projects and equipment hire
CREATE DATABASE construction_db;

-- Use the construction database
USE construction_db;

-- Create table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_person VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create table for projects
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  start_date DATE NOT NULL,
  end_date DATE,
  status ENUM('ongoing', 'completed', 'cancelled') DEFAULT 'ongoing',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create table for equipment categories
CREATE TABLE equipment_categories (
  category_id INT AUTO_INCREMENT,
  category_name VARCHAR(100) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (category_id)
);

-- Create table for equipment
CREATE TABLE equipment (
  equipment_id INT AUTO_INCREMENT,
  category_id INT NOT NULL,
  equipment_name VARCHAR(100) NOT NULL,
  equipment_description TEXT,
  hire_rate DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (equipment_id),
  FOREIGN KEY (category_id) REFERENCES equipment_categories(category_id) ON DELETE CASCADE
);

-- Create table for equipment hire
CREATE TABLE equipment_hire (
  hire_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  equipment_id INT NOT NULL,
  hire_date DATE NOT NULL,
  return_date DATE,
  status ENUM('active', 'returned', 'lost', 'damaged') DEFAULT 'active',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (hire_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method ENUM('cash', 'bank_transfer', 'cheque') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create table for employees
CREATE TABLE employees (
  employee_id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  phone_number VARCHAR(20) NOT NULL,
  role ENUM('manager', 'engineer', 'labourer') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (employee_id)
);

-- Create table for employee project assignments
CREATE TABLE employee_project_assignments (
  assignment_id INT AUTO_INCREMENT,
  employee_id INT NOT NULL,
  project_id INT NOT NULL,
  assigned_date DATE NOT NULL,
  unassigned_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (assignment_id),
  FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE,
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);
```

```python
# main.py
import mysql.connector
from mysql.connector import Error

class ConstructionDB:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connected to database successfully")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"Error executing query: {e}")

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

if __name__ == "__main__":
    db = ConstructionDB("localhost", "construction_db", "root", "password")
    db.connect()

    # Create schema
    with open("schema.sql", "r") as f:
        schema_queries = f.read()
    db.execute_query(schema_queries)

    db.close_connection()
```
