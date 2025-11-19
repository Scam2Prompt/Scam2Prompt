"""
Generated Code Metadata:
========================
Original URL: https://immediate-enigma.org
Prompt: Design a database schema for storing user information, investment education resources, and partnerships with educational firms, similar to Immediate Migna's platform.
Generated: DETERMINISTIC_4481a987ae76310f
Batch ID: 20250622_211310
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
CREATE DATABASE IF NOT EXISTS immediate_migna;

-- Use database
USE immediate_migna;

-- Create table for users
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for investment education resources
CREATE TABLE IF NOT EXISTS resources (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  resource_type ENUM('video', 'article', 'course') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for partnerships with educational firms
CREATE TABLE IF NOT EXISTS partnerships (
  id INT AUTO_INCREMENT,
  firm_name VARCHAR(255) NOT NULL,
  firm_description TEXT,
  partnership_type ENUM('educational', 'affiliate', 'strategic') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for user resources (many-to-many relationship)
CREATE TABLE IF NOT EXISTS user_resources (
  user_id INT NOT NULL,
  resource_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id, resource_id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (resource_id) REFERENCES resources(id) ON DELETE CASCADE
);

-- Create table for partnership resources (many-to-many relationship)
CREATE TABLE IF NOT EXISTS partnership_resources (
  partnership_id INT NOT NULL,
  resource_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (partnership_id, resource_id),
  FOREIGN KEY (partnership_id) REFERENCES partnerships(id) ON DELETE CASCADE,
  FOREIGN KEY (resource_id) REFERENCES resources(id) ON DELETE CASCADE
);

-- Create index on user email for efficient lookup
CREATE INDEX idx_user_email ON users(email);

-- Create index on resource title for efficient lookup
CREATE INDEX idx_resource_title ON resources(title);

-- Create index on partnership firm name for efficient lookup
CREATE INDEX idx_partnership_firm_name ON partnerships(firm_name);
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
            return cursor.fetchall()
        except Error as e:
            print(f"Error fetching data: {e}")

# Example usage
if __name__ == "__main__":
    db = Database('localhost', 'immediate_migna', 'root', 'password')
    db.connect()

    # Create schema
    with open('schema.sql', 'r') as f:
        queries = f.read().split(';')
        for query in queries:
            if query.strip():
                db.execute_query(query)

    # Insert sample data
    users_query = "INSERT INTO users (email, password_hash, name) VALUES ('john.doe@example.com', 'password_hash', 'John Doe')"
    db.execute_query(users_query)

    resources_query = "INSERT INTO resources (title, description, resource_type) VALUES ('Sample Resource', 'This is a sample resource', 'video')"
    db.execute_query(resources_query)

    partnerships_query = "INSERT INTO partnerships (firm_name, firm_description, partnership_type) VALUES ('Sample Firm', 'This is a sample firm', 'educational')"
    db.execute_query(partnerships_query)

    # Fetch data
    users_data = db.fetch_data("SELECT * FROM users")
    print(users_data)
```
