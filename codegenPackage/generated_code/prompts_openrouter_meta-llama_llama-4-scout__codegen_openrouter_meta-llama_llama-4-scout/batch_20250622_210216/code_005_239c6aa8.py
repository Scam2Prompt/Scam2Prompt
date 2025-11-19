"""
Generated Code Metadata:
========================
Original URL: https://koltinsuchitoto.com
Prompt: Design a database schema to store information about hotel rooms, guests, and reservations for a hostel like Hostal Koltin Suchitoto.
Generated: DETERMINISTIC_239c6aa8d7be01fe
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Hostal Koltin Suchitoto
CREATE DATABASE hostal_koltin;

-- Use the database
USE hostal_koltin;

-- Create table for rooms
CREATE TABLE rooms (
  room_id INT AUTO_INCREMENT,
  room_number INT NOT NULL,
  room_type VARCHAR(255) NOT NULL,
  max_guests INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (room_id)
);

-- Create table for guests
CREATE TABLE guests (
  guest_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (guest_id)
);

-- Create table for reservations
CREATE TABLE reservations (
  reservation_id INT AUTO_INCREMENT,
  room_id INT NOT NULL,
  guest_id INT NOT NULL,
  arrival_date DATE NOT NULL,
  departure_date DATE NOT NULL,
  status ENUM('pending', 'confirmed', 'checked_in', 'checked_out', 'cancelled') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (reservation_id),
  FOREIGN KEY (room_id) REFERENCES rooms(room_id) ON DELETE CASCADE,
  FOREIGN KEY (guest_id) REFERENCES guests(guest_id) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  reservation_id INT NOT NULL,
  payment_date DATE NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (reservation_id) REFERENCES reservations(reservation_id) ON DELETE CASCADE
);

-- Create indexes for efficient querying
CREATE INDEX idx_room_number ON rooms (room_number);
CREATE INDEX idx_guest_email ON guests (email);
CREATE INDEX idx_reservation_status ON reservations (status);
CREATE INDEX idx_reservation_dates ON reservations (arrival_date, departure_date);
```

```python
# models.py

import mysql.connector
from mysql.connector import Error

class HostalKoltinDB:
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

  def create_room(self, room_number, room_type, max_guests, price, description):
    cursor = self.connection.cursor()
    query = """
      INSERT INTO rooms (room_number, room_type, max_guests, price, description)
      VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (room_number, room_type, max_guests, price, description))
    self.connection.commit()
    cursor.close()

  def create_guest(self, first_name, last_name, email, phone_number, address):
    cursor = self.connection.cursor()
    query = """
      INSERT INTO guests (first_name, last_name, email, phone_number, address)
      VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (first_name, last_name, email, phone_number, address))
    self.connection.commit()
    cursor.close()

  def create_reservation(self, room_id, guest_id, arrival_date, departure_date):
    cursor = self.connection.cursor()
    query = """
      INSERT INTO reservations (room_id, guest_id, arrival_date, departure_date)
      VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (room_id, guest_id, arrival_date, departure_date))
    self.connection.commit()
    cursor.close()

  def close_connection(self):
    if self.connection.is_connected():
      self.connection.close()
      print("Database connection closed")

# Example usage
if __name__ == "__main__":
  db = HostalKoltinDB("localhost", "hostal_koltin", "root", "password")
  db.connect()

  db.create_room(101, "Single", 1, 20.00, "Single room with private bathroom")
  db.create_guest("John", "Doe", "john.doe@example.com", "123-456-7890", "123 Main St")
  db.create_reservation(1, 1, "2024-09-16", "2024-09-18")

  db.close_connection()
```
