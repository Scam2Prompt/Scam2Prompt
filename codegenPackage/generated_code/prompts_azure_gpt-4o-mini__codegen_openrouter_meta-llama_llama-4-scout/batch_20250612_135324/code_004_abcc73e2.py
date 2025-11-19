"""
Generated Code Metadata:
========================
Original URL: https://strk.site
Prompt: Design a database schema for storing information about completed renovation projects, including client details, project scope, and costs, inspired by the project management approach mentioned on the STRK site.
Generated: DETERMINISTIC_abcc73e29fa08c44
Batch ID: 20250612_135324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for renovation projects
CREATE DATABASE renovation_projects;

-- Use the renovation_projects database
USE renovation_projects;

-- Create a table for clients
CREATE TABLE clients (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for project statuses
CREATE TABLE project_statuses (
  id INT AUTO_INCREMENT,
  status_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Insert default project statuses
INSERT INTO project_statuses (status_name, description)
VALUES
  ('Completed', 'Project completed successfully'),
  ('Cancelled', 'Project cancelled'),
  ('On Hold', 'Project put on hold');

-- Create a table for project scopes
CREATE TABLE project_scopes (
  id INT AUTO_INCREMENT,
  scope_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Insert default project scopes
INSERT INTO project_scopes (scope_name, description)
VALUES
  ('Bathroom Renovation', 'Bathroom renovation project'),
  ('Kitchen Renovation', 'Kitchen renovation project'),
  ('Full House Renovation', 'Full house renovation project');

-- Create a table for projects
CREATE TABLE projects (
  id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  project_scope_id INT NOT NULL,
  project_status_id INT NOT NULL DEFAULT 1,
  project_name VARCHAR(255) NOT NULL,
  start_date DATE,
  completion_date DATE,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id),
  FOREIGN KEY (project_scope_id) REFERENCES project_scopes(id),
  FOREIGN KEY (project_status_id) REFERENCES project_statuses(id)
);

-- Create a table for project costs
CREATE TABLE project_costs (
  id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  cost_name VARCHAR(255) NOT NULL,
  cost_amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES projects(id)
);

-- Create a table for project images
CREATE TABLE project_images (
  id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  image_url VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES projects(id)
);

-- Example usage:
DELIMITER //
CREATE PROCEDURE add_project(
  IN p_client_id INT,
  IN p_project_scope_id INT,
  IN p_project_name VARCHAR(255),
  IN p_start_date DATE,
  IN p_completion_date DATE,
  IN p_description TEXT
)
BEGIN
  INSERT INTO projects (client_id, project_scope_id, project_name, start_date, completion_date, description)
  VALUES (p_client_id, p_project_scope_id, p_project_name, p_start_date, p_completion_date, p_description);
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE add_project_cost(
  IN p_project_id INT,
  IN p_cost_name VARCHAR(255),
  IN p_cost_amount DECIMAL(10, 2)
)
BEGIN
  INSERT INTO project_costs (project_id, cost_name, cost_amount)
  VALUES (p_project_id, p_cost_name, p_cost_amount);
END//
DELIMITER ;
```

```python
# main.py
import mysql.connector
from mysql.connector import Error

class RenovationProjectDB:
  def __init__(self, host_name, db_name, user_name, user_password):
    self.host_name = host_name
    self.db_name = db_name
    self.user_name = user_name
    self.user_password = user_password
    self.connection = None

  def create_connection(self):
    try:
      self.connection = mysql.connector.connect(
        host=self.host_name,
        database=self.db_name,
        user=self.user_name,
        password=self.user_password
      )
      print("Connection to database established")
    except Error as e:
      print(f"Error: '{e}'")

  def execute_query(self, query):
    try:
      cursor = self.connection.cursor()
      cursor.execute(query)
      self.connection.commit()
      print("Query executed successfully")
    except Error as e:
      print(f"Error: '{e}'")

  def read_query(self, query):
    try:
      cursor = self.connection.cursor()
      cursor.execute(query)
      result = cursor.fetchall()
      return result
    except Error as e:
      print(f"Error: '{e}'")

# Example usage:
if __name__ == "__main__":
  db = RenovationProjectDB("localhost", "renovation_projects", "username", "password")
  db.create_connection()

  query = "SELECT * FROM projects"
  result = db.read_query(query)
  for row in result:
    print(row)

  db.connection.close()
```
