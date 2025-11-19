"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: "Design a simple database schema for storing fire safety equipment inspection and maintenance records."
Generated: DETERMINISTIC_4ed5ab0f73ae2376
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- fire_safety_equipment_schema.sql

-- Create a database for fire safety equipment records
CREATE DATABASE fire_safety_equipment;

-- Use the database
USE fire_safety_equipment;

-- Create a table for equipment types
CREATE TABLE equipment_types (
  id INT AUTO_INCREMENT,
  equipment_type VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for inspection and maintenance records
CREATE TABLE inspection_maintenance_records (
  id INT AUTO_INCREMENT,
  equipment_type_id INT NOT NULL,
  equipment_id VARCHAR(255) NOT NULL,
  inspection_date DATE NOT NULL,
  maintenance_date DATE,
  inspected_by VARCHAR(255) NOT NULL,
  maintained_by VARCHAR(255),
  inspection_result VARCHAR(255) NOT NULL,
  maintenance_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (equipment_type_id) REFERENCES equipment_types(id)
);

-- Create a table for equipment details
CREATE TABLE equipment_details (
  id INT AUTO_INCREMENT,
  equipment_type_id INT NOT NULL,
  equipment_id VARCHAR(255) NOT NULL,
  installation_date DATE NOT NULL,
  last_inspection_date DATE,
  last_maintenance_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (equipment_type_id) REFERENCES equipment_types(id),
  UNIQUE KEY (equipment_id)
);

-- Create a table for users
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  role ENUM('admin', 'inspector', 'maintainer') NOT NULL DEFAULT 'inspector',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (username),
  UNIQUE KEY (email)
);

-- Insert sample data
INSERT INTO equipment_types (equipment_type, description)
VALUES
  ('Fire Extinguisher', 'A device used to put out fires'),
  ('Fire Alarm', 'A system that detects and alerts people of fires'),
  ('Sprinkler System', 'A system that disperses water to put out fires');

INSERT INTO users (username, email, password, role)
VALUES
  ('admin', 'admin@example.com', 'password', 'admin'),
  ('inspector', 'inspector@example.com', 'password', 'inspector'),
  ('maintainer', 'maintainer@example.com', 'password', 'maintainer');
```

```python
# fire_safety_equipment.py
import mysql.connector
from mysql.connector import Error

class FireSafetyEquipmentDB:
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
    cursor = self.connection.cursor()
    with open('fire_safety_equipment_schema.sql', 'r') as f:
      schema = f.read()
    cursor.execute(schema, multi=True)
    self.connection.commit()
    print("Tables created")

  def insert_equipment_type(self, equipment_type, description):
    cursor = self.connection.cursor()
    query = "INSERT INTO equipment_types (equipment_type, description) VALUES (%s, %s)"
    cursor.execute(query, (equipment_type, description))
    self.connection.commit()
    print("Equipment type inserted")

  def insert_inspection_maintenance_record(self, equipment_type_id, equipment_id, inspection_date, inspected_by, inspection_result):
    cursor = self.connection.cursor()
    query = """
      INSERT INTO inspection_maintenance_records (equipment_type_id, equipment_id, inspection_date, inspected_by, inspection_result)
      VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (equipment_type_id, equipment_id, inspection_date, inspected_by, inspection_result))
    self.connection.commit()
    print("Inspection/maintenance record inserted")

  def close_connection(self):
    if self.connection.is_connected():
      self.connection.close()
      print("Database connection closed")

if __name__ == "__main__":
  db = FireSafetyEquipmentDB('localhost', 'fire_safety_equipment', 'root', 'password')
  db.connect()
  db.create_tables()
  db.insert_equipment_type('Fire Extinguisher', 'A device used to put out fires')
  db.insert_inspection_maintenance_record(1, 'ABC123', '2022-01-01', 'John Doe', 'Pass')
  db.close_connection()
```
