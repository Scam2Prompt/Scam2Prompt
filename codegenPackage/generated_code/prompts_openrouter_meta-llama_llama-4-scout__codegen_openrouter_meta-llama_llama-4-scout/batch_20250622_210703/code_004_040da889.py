"""
Generated Code Metadata:
========================
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: "Design a database schema to store information about construction projects, clients, and team members for a design-build and turnkey construction services company, and provide an example of how to query the database."
Generated: DETERMINISTIC_040da88968a618df
Batch ID: 20250622_210703
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
CREATE DATABASE construction_services;

-- Use database
USE construction_services;

-- Create table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  PRIMARY KEY (client_id)
);

-- Create table for team members
CREATE TABLE team_members (
  team_member_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  role VARCHAR(255) NOT NULL,
  phone_number VARCHAR(20),
  PRIMARY KEY (team_member_id)
);

-- Create table for projects
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  start_date DATE,
  end_date DATE,
  status VARCHAR(255) NOT NULL DEFAULT 'in_progress',
  PRIMARY KEY (project_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create table for project team members
CREATE TABLE project_team_members (
  project_id INT NOT NULL,
  team_member_id INT NOT NULL,
  role VARCHAR(255) NOT NULL,
  PRIMARY KEY (project_id, team_member_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (team_member_id) REFERENCES team_members(team_member_id) ON DELETE CASCADE
);

-- Create table for project milestones
CREATE TABLE project_milestones (
  milestone_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  milestone_name VARCHAR(255) NOT NULL,
  milestone_date DATE NOT NULL,
  status VARCHAR(255) NOT NULL DEFAULT 'pending',
  PRIMARY KEY (milestone_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Insert example data
INSERT INTO clients (company_name, contact_name, email, phone_number, address)
VALUES
  ('ABC Corporation', 'John Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
  ('XYZ Inc.', 'Jane Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

INSERT INTO team_members (first_name, last_name, email, role, phone_number)
VALUES
  ('Bob', 'Johnson', 'bob.johnson@example.com', 'Project Manager', '555-123-4567'),
  ('Alice', 'Williams', 'alice.williams@example.com', 'Engineer', '555-901-2345');

INSERT INTO projects (client_id, project_name, project_description, start_date, end_date)
VALUES
  (1, 'Office Renovation', 'Renovation of office space', '2022-01-01', '2022-06-01'),
  (2, 'Warehouse Expansion', 'Expansion of warehouse facility', '2022-03-01', '2022-09-01');

INSERT INTO project_team_members (project_id, team_member_id, role)
VALUES
  (1, 1, 'Project Manager'),
  (1, 2, 'Engineer'),
  (2, 1, 'Project Manager');

INSERT INTO project_milestones (project_id, milestone_name, milestone_date)
VALUES
  (1, 'Design Completion', '2022-02-01'),
  (1, 'Construction Start', '2022-03-01'),
  (2, 'Site Preparation', '2022-04-01');

-- Example query: Get all projects with client information and team members
SELECT 
  p.project_id,
  p.project_name,
  c.company_name AS client_company,
  c.contact_name AS client_contact,
  tm.first_name AS team_member_first_name,
  tm.last_name AS team_member_last_name,
  tm.role AS team_member_role
FROM 
  projects p
  JOIN clients c ON p.client_id = c.client_id
  JOIN project_team_members ptm ON p.project_id = ptm.project_id
  JOIN team_members tm ON ptm.team_member_id = tm.team_member_id
ORDER BY 
  p.project_id, tm.last_name;
```

```python
# query.py
import mysql.connector
from mysql.connector import Error

def connect_to_database(host_name, database_name, user_name, user_password):
    try:
        connection = mysql.connector.connect(
            host=host_name,
            database=database_name,
            user=user_name,
            password=user_password
        )
        return connection
    except Error as error:
        print(f"Error: '{error}'")

def query_database(connection):
    query = """
        SELECT 
          p.project_id,
          p.project_name,
          c.company_name AS client_company,
          c.contact_name AS client_contact,
          tm.first_name AS team_member_first_name,
          tm.last_name AS team_member_last_name,
          tm.role AS team_member_role
        FROM 
          projects p
          JOIN clients c ON p.client_id = c.client_id
          JOIN project_team_members ptm ON p.project_id = ptm.project_id
          JOIN team_members tm ON ptm.team_member_id = tm.team_member_id
        ORDER BY 
          p.project_id, tm.last_name;
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Error as error:
        print(f"Error: '{error}'")

def main():
    host_name = 'localhost'
    database_name = 'construction_services'
    user_name = 'your_username'
    user_password = 'your_password'

    connection = connect_to_database(host_name, database_name, user_name, user_password)
    if connection:
        query_database(connection)
        connection.close()

if __name__ == "__main__":
    main()
```
