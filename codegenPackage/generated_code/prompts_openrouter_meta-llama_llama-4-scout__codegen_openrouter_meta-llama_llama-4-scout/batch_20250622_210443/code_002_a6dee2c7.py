"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: "Design a database schema to store property inspection data, including photos, user information, and inspection reports, for an application like App Vistoria."
Generated: DETERMINISTIC_a6dee2c7e9d8ed2f
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE IF NOT EXISTS app_vistoria;

-- Use database
USE app_vistoria;

-- Create table for users
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  role ENUM('admin', 'inspector', 'client') NOT NULL DEFAULT 'client',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for properties
CREATE TABLE IF NOT EXISTS properties (
  id INT AUTO_INCREMENT,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  zip_code VARCHAR(20) NOT NULL,
  country VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for inspections
CREATE TABLE IF NOT EXISTS inspections (
  id INT AUTO_INCREMENT,
  property_id INT NOT NULL,
  user_id INT NOT NULL,
  inspection_date DATE NOT NULL,
  report TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (property_id) REFERENCES properties(id) ON DELETE CASCADE,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for photos
CREATE TABLE IF NOT EXISTS photos (
  id INT AUTO_INCREMENT,
  inspection_id INT NOT NULL,
  photo BLOB NOT NULL,
  description VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (inspection_id) REFERENCES inspections(id) ON DELETE CASCADE
);

-- Create table for inspection reports
CREATE TABLE IF NOT EXISTS inspection_reports (
  id INT AUTO_INCREMENT,
  inspection_id INT NOT NULL,
  report BLOB NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (inspection_id) REFERENCES inspections(id) ON DELETE CASCADE
);

-- Create indexes
CREATE INDEX idx_inspections_property_id ON inspections (property_id);
CREATE INDEX idx_inspections_user_id ON inspections (user_id);
CREATE INDEX idx_photos_inspection_id ON photos (inspection_id);
CREATE INDEX idx_inspection_reports_inspection_id ON inspection_reports (inspection_id);
```

```python
# models.py
import mysql.connector
from mysql.connector import Error

class Database:
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
            print("Connected to database")
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

    def fetch_data(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error fetching data: {e}")

# Usage
if __name__ == "__main__":
    db = Database("localhost", "app_vistoria", "root", "password")
    db.connect()

    # Create schema
    with open("schema.sql", "r") as f:
        queries = f.read().split(";")
        for query in queries:
            if query.strip():
                db.execute_query(query)

    # Insert sample data
    users_query = "INSERT INTO users (name, email, password) VALUES ('John Doe', 'john@example.com', 'password')"
    db.execute_query(users_query)

    properties_query = "INSERT INTO properties (address, city, state, zip_code, country) VALUES ('123 Main St', 'Anytown', 'CA', '12345', 'USA')"
    db.execute_query(properties_query)

    inspections_query = "INSERT INTO inspections (property_id, user_id, inspection_date) VALUES (1, 1, '2022-01-01')"
    db.execute_query(inspections_query)

    # Fetch data
    inspections_data = db.fetch_data("SELECT * FROM inspections")
    for row in inspections_data:
        print(row)
```
