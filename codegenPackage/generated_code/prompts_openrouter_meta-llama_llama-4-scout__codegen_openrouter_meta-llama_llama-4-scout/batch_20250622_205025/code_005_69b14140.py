"""
Generated Code Metadata:
========================
Original URL: https://unitedcabinetry.com.au
Prompt: "Design a simple database schema to store information about cabinetry projects, including client details, project specifications, and installation schedules."
Generated: DETERMINISTIC_69b1414071cd4392
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for cabinetry projects
CREATE DATABASE cabinetry_projects;

-- Use the cabinetry_projects database
USE cabinetry_projects;

-- Create a table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  PRIMARY KEY (client_id)
);

-- Create a table for project specifications
CREATE TABLE project_specs (
  project_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  material VARCHAR(255) NOT NULL,
  finish VARCHAR(255) NOT NULL,
  dimensions VARCHAR(255) NOT NULL,
  PRIMARY KEY (project_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create a table for installation schedules
CREATE TABLE installation_schedules (
  schedule_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  installation_date DATE NOT NULL,
  installation_time TIME NOT NULL,
  PRIMARY KEY (schedule_id),
  FOREIGN KEY (project_id) REFERENCES project_specs(project_id) ON DELETE CASCADE
);

-- Create a table for project status updates
CREATE TABLE project_status_updates (
  update_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  update_date DATE NOT NULL,
  update_description TEXT NOT NULL,
  PRIMARY KEY (update_id),
  FOREIGN KEY (project_id) REFERENCES project_specs(project_id) ON DELETE CASCADE
);

-- Create a stored procedure to insert a new client
DELIMITER //
CREATE PROCEDURE insert_client(
  IN p_first_name VARCHAR(255),
  IN p_last_name VARCHAR(255),
  IN p_email VARCHAR(255),
  IN p_phone_number VARCHAR(20),
  IN p_address VARCHAR(255)
)
BEGIN
  INSERT INTO clients (first_name, last_name, email, phone_number, address)
  VALUES (p_first_name, p_last_name, p_email, p_phone_number, p_address);
END//
DELIMITER ;

-- Create a stored procedure to insert a new project
DELIMITER //
CREATE PROCEDURE insert_project(
  IN p_client_id INT,
  IN p_project_name VARCHAR(255),
  IN p_project_description TEXT,
  IN p_material VARCHAR(255),
  IN p_finish VARCHAR(255),
  IN p_dimensions VARCHAR(255)
)
BEGIN
  INSERT INTO project_specs (client_id, project_name, project_description, material, finish, dimensions)
  VALUES (p_client_id, p_project_name, p_project_description, p_material, p_finish, p_dimensions);
END//
DELIMITER ;

-- Create a stored procedure to insert a new installation schedule
DELIMITER //
CREATE PROCEDURE insert_installation_schedule(
  IN p_project_id INT,
  IN p_installation_date DATE,
  IN p_installation_time TIME
)
BEGIN
  INSERT INTO installation_schedules (project_id, installation_date, installation_time)
  VALUES (p_project_id, p_installation_date, p_installation_time);
END//
DELIMITER ;

-- Example usage:
CALL insert_client('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St');
SET @client_id = LAST_INSERT_ID();

CALL insert_project(@client_id, 'Kitchen Cabinets', 'New kitchen cabinets', 'Oak', 'White', '10x10');
SET @project_id = LAST_INSERT_ID();

CALL insert_installation_schedule(@project_id, '2024-09-17', '09:00:00');
```

```python
import mysql.connector
from mysql.connector import Error

class CabinetryProjectDB:
  def __init__(self, host_name, db_name, user_name, user_password):
    self.host_name = host_name
    self.db_name = db_name
    self.user_name = user_name
    self.user_password = user_password
    self.connection = None

  def connect(self):
    try:
      self.connection = mysql.connector.connect(
        host=self.host_name,
        database=self.db_name,
        user=self.user_name,
        password=self.user_password
      )
      print("Connected to database")
    except Error as e:
      print(f"Error connecting to database: {e}")

  def insert_client(self, first_name, last_name, email, phone_number, address):
    try:
      cursor = self.connection.cursor()
      query = "CALL insert_client(%s, %s, %s, %s, %s)"
      cursor.execute(query, (first_name, last_name, email, phone_number, address))
      self.connection.commit()
      return cursor.lastrowid
    except Error as e:
      print(f"Error inserting client: {e}")

  def insert_project(self, client_id, project_name, project_description, material, finish, dimensions):
    try:
      cursor = self.connection.cursor()
      query = "CALL insert_project(%s, %s, %s, %s, %s, %s)"
      cursor.execute(query, (client_id, project_name, project_description, material, finish, dimensions))
      self.connection.commit()
      return cursor.lastrowid
    except Error as e:
      print(f"Error inserting project: {e}")

  def insert_installation_schedule(self, project_id, installation_date, installation_time):
    try:
      cursor = self.connection.cursor()
      query = "CALL insert_installation_schedule(%s, %s, %s)"
      cursor.execute(query, (project_id, installation_date, installation_time))
      self.connection.commit()
      return cursor.lastrowid
    except Error as e:
      print(f"Error inserting installation schedule: {e}")

# Example usage:
db = CabinetryProjectDB('localhost', 'cabinetry_projects', 'username', 'password')
db.connect()

client_id = db.insert_client('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St')
project_id = db.insert_project(client_id, 'Kitchen Cabinets', 'New kitchen cabinets', 'Oak', 'White', '10x10')
installation_schedule_id = db.insert_installation_schedule(project_id, '2024-09-17', '09:00:00')
```
