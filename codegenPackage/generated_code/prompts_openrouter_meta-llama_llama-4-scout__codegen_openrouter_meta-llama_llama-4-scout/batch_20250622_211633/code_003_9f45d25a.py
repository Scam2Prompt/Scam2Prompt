"""
Generated Code Metadata:
========================
Original URL: https://medioswow.com
Prompt: "Design a database schema to store information about outdoor advertising locations, including cities, prices, and availability, inspired by the services offered by WOW MEDIA."
Generated: DETERMINISTIC_9f45d25a9b6b7974
Batch ID: 20250622_211633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for outdoor advertising locations
CREATE DATABASE outdoor_advertising;

-- Use the database
USE outdoor_advertising;

-- Create table for cities
CREATE TABLE cities (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  state VARCHAR(255) NOT NULL,
  country VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for advertising locations
CREATE TABLE locations (
  id INT AUTO_INCREMENT,
  city_id INT NOT NULL,
  address VARCHAR(255) NOT NULL,
  latitude DECIMAL(10, 8) NOT NULL,
  longitude DECIMAL(11, 8) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (city_id) REFERENCES cities(id) ON DELETE CASCADE
);

-- Create table for advertising boards
CREATE TABLE boards (
  id INT AUTO_INCREMENT,
  location_id INT NOT NULL,
  board_type VARCHAR(255) NOT NULL,
  size VARCHAR(255) NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (location_id) REFERENCES locations(id) ON DELETE CASCADE
);

-- Create table for availability
CREATE TABLE availability (
  id INT AUTO_INCREMENT,
  board_id INT NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  is_available BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (board_id) REFERENCES boards(id) ON DELETE CASCADE
);

-- Create table for bookings
CREATE TABLE bookings (
  id INT AUTO_INCREMENT,
  board_id INT NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  client_name VARCHAR(255) NOT NULL,
  client_email VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (board_id) REFERENCES boards(id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_city_name ON cities (name);
CREATE INDEX idx_location_address ON locations (address);
CREATE INDEX idx_board_type ON boards (board_type);
CREATE INDEX idx_availability_board_id ON availability (board_id);
CREATE INDEX idx_bookings_board_id ON bookings (board_id);
```

```python
# main.py

import mysql.connector
from mysql.connector import Error

class OutdoorAdvertisingDB:
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

  def create_tables(self):
    try:
      cursor = self.connection.cursor()
      with open('schema.sql', 'r') as f:
        schema = f.read()
      cursor.execute(schema, multi=True)
      self.connection.commit()
      print("Tables created")
    except Error as e:
      print(f"Error creating tables: {e}")

  def insert_city(self, name, state, country):
    try:
      cursor = self.connection.cursor()
      query = "INSERT INTO cities (name, state, country) VALUES (%s, %s, %s)"
      cursor.execute(query, (name, state, country))
      self.connection.commit()
      print("City inserted")
    except Error as e:
      print(f"Error inserting city: {e}")

  def insert_location(self, city_id, address, latitude, longitude):
    try:
      cursor = self.connection.cursor()
      query = "INSERT INTO locations (city_id, address, latitude, longitude) VALUES (%s, %s, %s, %s)"
      cursor.execute(query, (city_id, address, latitude, longitude))
      self.connection.commit()
      print("Location inserted")
    except Error as e:
      print(f"Error inserting location: {e}")

  def insert_board(self, location_id, board_type, size, price):
    try:
      cursor = self.connection.cursor()
      query = "INSERT INTO boards (location_id, board_type, size, price) VALUES (%s, %s, %s, %s)"
      cursor.execute(query, (location_id, board_type, size, price))
      self.connection.commit()
      print("Board inserted")
    except Error as e:
      print(f"Error inserting board: {e}")

  def close_connection(self):
    if self.connection.is_connected():
      self.connection.close()
      print("Database connection closed")

if __name__ == "__main__":
  db = OutdoorAdvertisingDB('localhost', 'outdoor_advertising', 'root', 'password')
  db.connect()
  db.create_tables()
  db.insert_city('New York', 'NY', 'USA')
  db.insert_location(1, '123 Main St', 40.7128, -74.0060)
  db.insert_board(1, 'Billboard', '14x48', 5000.00)
  db.close_connection()
```
