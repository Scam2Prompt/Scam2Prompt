"""
Generated Code Metadata:
========================
Original URL: https://vinescoin.com
Prompt: Design a database schema to store information about small-batch producers, cooking oils, and their regions, inspired by Authentic Oil's curated selection and regional diversity.
Generated: DETERMINISTIC_90b8d3a39bd56cb6
Batch ID: 20250622_211427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Authentic Oil's curated selection
CREATE DATABASE authentic_oil;

-- Use the database
USE authentic_oil;

-- Create table for regions
CREATE TABLE regions (
  region_id INT AUTO_INCREMENT,
  region_name VARCHAR(255) NOT NULL,
  region_description TEXT,
  PRIMARY KEY (region_id)
);

-- Create table for producers
CREATE TABLE producers (
  producer_id INT AUTO_INCREMENT,
  producer_name VARCHAR(255) NOT NULL,
  producer_description TEXT,
  region_id INT,
  PRIMARY KEY (producer_id),
  FOREIGN KEY (region_id) REFERENCES regions(region_id) ON DELETE SET NULL
);

-- Create table for cooking oils
CREATE TABLE cooking_oils (
  oil_id INT AUTO_INCREMENT,
  oil_name VARCHAR(255) NOT NULL,
  oil_description TEXT,
  producer_id INT,
  PRIMARY KEY (oil_id),
  FOREIGN KEY (producer_id) REFERENCES producers(producer_id) ON DELETE SET NULL
);

-- Create table for oil regions (many-to-many relationship)
CREATE TABLE oil_regions (
  oil_id INT,
  region_id INT,
  PRIMARY KEY (oil_id, region_id),
  FOREIGN KEY (oil_id) REFERENCES cooking_oils(oil_id) ON DELETE CASCADE,
  FOREIGN KEY (region_id) REFERENCES regions(region_id) ON DELETE CASCADE
);

-- Create indexes for efficient querying
CREATE INDEX idx_producer_region ON producers (region_id);
CREATE INDEX idx_oil_producer ON cooking_oils (producer_id);
CREATE INDEX idx_oil_region ON oil_regions (oil_id, region_id);

-- Example data insertion
INSERT INTO regions (region_name, region_description)
VALUES 
  ('Tuscany', 'A region in central Italy'),
  ('Andalusia', 'A region in southern Spain'),
  ('California', 'A state in the western United States');

INSERT INTO producers (producer_name, producer_description, region_id)
VALUES 
  ('Tuscan Olive Co.', 'A producer of high-quality olive oils', 1),
  ('Andalusian Oil Makers', 'A producer of artisanal oils', 2),
  ('California Olive Ranch', 'A producer of sustainable olive oils', 3);

INSERT INTO cooking_oils (oil_name, oil_description, producer_id)
VALUES 
  ('Tuscan Extra Virgin', 'A rich and full-bodied olive oil', 1),
  ('Andalusian Arbequina', 'A smooth and fruity oil', 2),
  ('California Avocado Oil', 'A mild and versatile oil', 3);

INSERT INTO oil_regions (oil_id, region_id)
VALUES 
  (1, 1),
  (2, 2),
  (3, 3),
  (1, 3);  -- Tuscan Extra Virgin also available in California
```

```python
# producer_service.py

import mysql.connector
from mysql.connector import Error

class ProducerService:
  def __init__(self, db_config):
    self.db_config = db_config

  def get_producers(self):
    try:
      with mysql.connector.connect(**self.db_config) as connection:
        cursor = connection.cursor()
        query = "SELECT * FROM producers"
        cursor.execute(query)
        return cursor.fetchall()
    except Error as e:
      print(f"Error: {e}")

  def get_producer(self, producer_id):
    try:
      with mysql.connector.connect(**self.db_config) as connection:
        cursor = connection.cursor()
        query = "SELECT * FROM producers WHERE producer_id = %s"
        cursor.execute(query, (producer_id,))
        return cursor.fetchone()
    except Error as e:
      print(f"Error: {e}")

  def create_producer(self, producer_name, producer_description, region_id):
    try:
      with mysql.connector.connect(**self.db_config) as connection:
        cursor = connection.cursor()
        query = "INSERT INTO producers (producer_name, producer_description, region_id) VALUES (%s, %s, %s)"
        cursor.execute(query, (producer_name, producer_description, region_id))
        connection.commit()
        return cursor.lastrowid
    except Error as e:
      print(f"Error: {e}")

# Usage
db_config = {
  'host': 'localhost',
  'database': 'authentic_oil',
  'user': 'your_username',
  'password': 'your_password'
}

producer_service = ProducerService(db_config)
producers = producer_service.get_producers()
for producer in producers:
  print(producer)
```
