"""
Generated Code Metadata:
========================
Original URL: https://2ms.pt
Prompt: "Design a simple database schema for storing property information similar to what is presented on 2ms.pt, including fields for address, city, and contact details."
Generated: DETERMINISTIC_ad9e8fad320d7684
Batch ID: 20250622_204855
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://kaunas.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for storing property information
CREATE DATABASE property_database;

-- Use the created database
USE property_database;

-- Create a table for cities
CREATE TABLE cities (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create a table for properties
CREATE TABLE properties (
  id INT AUTO_INCREMENT,
  address VARCHAR(255) NOT NULL,
  city_id INT,
  phone_number VARCHAR(20),
  email VARCHAR(100),
  website VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (city_id) REFERENCES cities(id) ON DELETE SET NULL
);

-- Create a table for property contacts
CREATE TABLE property_contacts (
  id INT AUTO_INCREMENT,
  property_id INT,
  contact_name VARCHAR(100) NOT NULL,
  contact_phone VARCHAR(20),
  contact_email VARCHAR(100),
  PRIMARY KEY (id),
  FOREIGN KEY (property_id) REFERENCES properties(id) ON DELETE CASCADE
);

-- Example data for testing
INSERT INTO cities (name) VALUES
  ('Vilnius'),
  ('Kaunas'),
  ('Klaipėda');

INSERT INTO properties (address, city_id, phone_number, email, website) VALUES
  ('Gedimino g. 1', 1, '+370 12345678', 'info@example.com', 'https://example.com'),
  ('K. Donelaičio g. 10', 2, '+370 87654321', 'kaunas@example.com', 'https://kaunas.example.com');

INSERT INTO property_contacts (property_id, contact_name, contact_phone, contact_email) VALUES
  (1, 'Jonas Biliūnas', '+370 90123456', 'jonas.biliunas@example.com'),
  (2, 'Petras Šakys', '+370 11122233', 'petras.sakys@example.com');
```

```python
# property_service.py

import mysql.connector
from mysql.connector import Error

class PropertyService:
  def __init__(self, db_config):
    self.db_config = db_config

  def get_connection(self):
    try:
      return mysql.connector.connect(
        host=self.db_config['host'],
        database=self.db_config['database'],
        user=self.db_config['user'],
        password=self.db_config['password']
      )
    except Error as e:
      print(f"Error: '{e}'")

  def get_properties(self):
    connection = self.get_connection()
    cursor = connection.cursor()
    query = """
      SELECT p.id, p.address, c.name AS city, p.phone_number, p.email, p.website
      FROM properties p
      JOIN cities c ON p.city_id = c.id
    """
    cursor.execute(query)
    return cursor.fetchall()

  def get_property_contacts(self, property_id):
    connection = self.get_connection()
    cursor = connection.cursor()
    query = """
      SELECT pc.id, pc.contact_name, pc.contact_phone, pc.contact_email
      FROM property_contacts pc
      WHERE pc.property_id = %s
    """
    cursor.execute(query, (property_id,))
    return cursor.fetchall()

# Example usage
if __name__ == "__main__":
  db_config = {
    'host': 'localhost',
    'database': 'property_database',
    'user': 'your_username',
    'password': 'your_password'
  }

  property_service = PropertyService(db_config)
  properties = property_service.get_properties()
  for prop in properties:
    print(prop)

  contacts = property_service.get_property_contacts(1)
  for contact in contacts:
    print(contact)
```
