"""
Generated Code Metadata:
========================
Original URL: https://espinelycia.com
Prompt: "Design a simple database schema to store information about hydraulic, sanitary, gas, and firefighting networks, including their designs, constructions, and maintenance records, inspired by the services offered by Espinel y Cia."
Generated: DETERMINISTIC_e6432d87387fc3ee
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- networks.sql

-- Create a database for storing network information
CREATE DATABASE network_database;

-- Use the created database
USE network_database;

-- Create a table for network types
CREATE TABLE network_types (
  id INT AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  description TEXT,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create a table for networks
CREATE TABLE networks (
  id INT AUTO_INCREMENT,
  type_id INT NOT NULL,
  name VARCHAR(100) NOT NULL,
  design_date DATE,
  construction_date DATE,
  PRIMARY KEY (id),
  FOREIGN KEY (type_id) REFERENCES network_types(id)
);

-- Create a table for network designs
CREATE TABLE network_designs (
  id INT AUTO_INCREMENT,
  network_id INT NOT NULL,
  design_document BLOB,
  design_date DATE NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (network_id) REFERENCES networks(id)
);

-- Create a table for network constructions
CREATE TABLE network_constructions (
  id INT AUTO_INCREMENT,
  network_id INT NOT NULL,
  construction_status VARCHAR(50) NOT NULL,
  construction_date DATE,
  PRIMARY KEY (id),
  FOREIGN KEY (network_id) REFERENCES networks(id)
);

-- Create a table for maintenance records
CREATE TABLE maintenance_records (
  id INT AUTO_INCREMENT,
  network_id INT NOT NULL,
  maintenance_date DATE NOT NULL,
  description TEXT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (network_id) REFERENCES networks(id)
);

-- Create a table for maintenance activities
CREATE TABLE maintenance_activities (
  id INT AUTO_INCREMENT,
  maintenance_record_id INT NOT NULL,
  activity_date DATE NOT NULL,
  activity_description TEXT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (maintenance_record_id) REFERENCES maintenance_records(id)
);

-- Insert network types
INSERT INTO network_types (name, description)
VALUES
  ('Hydraulic', 'Hydraulic network'),
  ('Sanitary', 'Sanitary network'),
  ('Gas', 'Gas network'),
  ('Firefighting', 'Firefighting network');

-- Example usage:
DELIMITER //
CREATE PROCEDURE add_network(
  IN p_type_id INT,
  IN p_name VARCHAR(100),
  IN p_design_date DATE,
  IN p_construction_date DATE
)
BEGIN
  DECLARE EXIT HANDLER FOR SQLEXCEPTION
  BEGIN
    ROLLBACK;
    RESIGNAL SET MESSAGE_TEXT = 'Error adding network';
  END;

  START TRANSACTION;

  INSERT INTO networks (type_id, name, design_date, construction_date)
  VALUES (p_type_id, p_name, p_design_date, p_construction_date);

  COMMIT;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE add_maintenance_record(
  IN p_network_id INT,
  IN p_maintenance_date DATE,
  IN p_description TEXT
)
BEGIN
  DECLARE EXIT HANDLER FOR SQLEXCEPTION
  BEGIN
    ROLLBACK;
    RESIGNAL SET MESSAGE_TEXT = 'Error adding maintenance record';
  END;

  START TRANSACTION;

  INSERT INTO maintenance_records (network_id, maintenance_date, description)
  VALUES (p_network_id, p_maintenance_date, p_description);

  COMMIT;
END//
DELIMITER ;
```

```python
# networks.py

import mysql.connector
from mysql.connector import Error

class NetworkDatabase:
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

  def add_network(self, type_id, name, design_date, construction_date):
    try:
      cursor = self.connection.cursor()
      query = "CALL add_network(%s, %s, %s, %s)"
      cursor.execute(query, (type_id, name, design_date, construction_date))
      self.connection.commit()
      print("Network added")
    except Error as e:
      print(f"Error adding network: {e}")

  def add_maintenance_record(self, network_id, maintenance_date, description):
    try:
      cursor = self.connection.cursor()
      query = "CALL add_maintenance_record(%s, %s, %s)"
      cursor.execute(query, (network_id, maintenance_date, description))
      self.connection.commit()
      print("Maintenance record added")
    except Error as e:
      print(f"Error adding maintenance record: {e}")

  def close_connection(self):
    if self.connection.is_connected():
      self.connection.close()
      print("Database connection closed")

# Example usage:
if __name__ == "__main__":
  db = NetworkDatabase("localhost", "network_database", "user", "password")
  db.connect()
  db.add_network(1, "Hydraulic Network", "2022-01-01", "2022-01-15")
  db.add_maintenance_record(1, "2022-02-01", "Maintenance activity")
  db.close_connection()
```
