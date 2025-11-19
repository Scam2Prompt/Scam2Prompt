"""
Generated Code Metadata:
========================
Original URL: https://bitcoin-miner.shop
Prompt: Design a database schema for storing business listings similar to those found on bitcoin-miner.shop.
Generated: DETERMINISTIC_f6678843c41c1ada
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for business listings
CREATE DATABASE business_listings;

-- Use the database
USE business_listings;

-- Create table for business categories
CREATE TABLE categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for business listings
CREATE TABLE listings (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  category_id INT,
  address VARCHAR(255),
  city VARCHAR(100),
  state VARCHAR(100),
  country VARCHAR(100),
  postal_code VARCHAR(20),
  phone_number VARCHAR(20),
  email VARCHAR(100),
  website VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL
);

-- Create table for business listing images
CREATE TABLE listing_images (
  id INT AUTO_INCREMENT,
  listing_id INT,
  image_url VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (listing_id) REFERENCES listings(id) ON DELETE CASCADE
);

-- Create table for business listing reviews
CREATE TABLE reviews (
  id INT AUTO_INCREMENT,
  listing_id INT,
  rating TINYINT NOT NULL,
  comment TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (listing_id) REFERENCES listings(id) ON DELETE CASCADE
);

-- Create index on category_id in listings table
CREATE INDEX idx_category_id ON listings (category_id);

-- Create index on listing_id in listing_images table
CREATE INDEX idx_listing_id_images ON listing_images (listing_id);

-- Create index on listing_id in reviews table
CREATE INDEX idx_listing_id_reviews ON reviews (listing_id);
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
    db = Database("localhost", "business_listings", "root", "password")
    db.connect()

    # Create tables
    with open("schema.sql", "r") as f:
        queries = f.read().split(";")
        for query in queries:
            if query.strip():
                db.execute_query(query)

    # Insert sample data
    insert_category_query = "INSERT INTO categories (name, description) VALUES ('Mining', 'Bitcoin mining company')"
    db.execute_query(insert_category_query)

    insert_listing_query = "INSERT INTO listings (title, description, category_id) VALUES ('Bitcoin Miner', 'Bitcoin mining company', 1)"
    db.execute_query(insert_listing_query)

    # Fetch data
    fetch_categories_query = "SELECT * FROM categories"
    categories = db.fetch_data(fetch_categories_query)
    print(categories)
```
