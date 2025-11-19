"""
Generated Code Metadata:
========================
Original URL: https://afranaden.org
Prompt: Develop a simple database schema to store information about humanitarian projects, including project names, locations, and types of aid provided, inspired by the projects listed on the organization's website.
Generated: DETERMINISTIC_b249a34637b3590f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- humanitarian_projects_schema.sql

-- Create a database for humanitarian projects
CREATE DATABASE humanitarian_projects;

-- Use the database
USE humanitarian_projects;

-- Create a table for project locations
CREATE TABLE locations (
  id INT AUTO_INCREMENT,
  city VARCHAR(255) NOT NULL,
  country VARCHAR(255) NOT NULL,
  latitude DECIMAL(10, 8),
  longitude DECIMAL(11, 8),
  PRIMARY KEY (id)
);

-- Create a table for types of aid
CREATE TABLE aid_types (
  id INT AUTO_INCREMENT,
  aid_type VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create a table for humanitarian projects
CREATE TABLE projects (
  id INT AUTO_INCREMENT,
  project_name VARCHAR(255) NOT NULL,
  location_id INT,
  start_date DATE,
  end_date DATE,
  description TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (location_id) REFERENCES locations(id) ON DELETE CASCADE
);

-- Create a many-to-many relationship table for projects and aid types
CREATE TABLE project_aid_types (
  project_id INT,
  aid_type_id INT,
  PRIMARY KEY (project_id, aid_type_id),
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE,
  FOREIGN KEY (aid_type_id) REFERENCES aid_types(id) ON DELETE CASCADE
);

-- Create indexes for foreign keys
CREATE INDEX idx_projects_location_id ON projects (location_id);
CREATE INDEX idx_project_aid_types_project_id ON project_aid_types (project_id);
CREATE INDEX idx_project_aid_types_aid_type_id ON project_aid_types (aid_type_id);

-- Example data insertion
INSERT INTO locations (city, country, latitude, longitude)
VALUES 
('Kabul', 'Afghanistan', 34.5167, 69.1833),
('Goma', 'Democratic Republic of Congo', 1.6833, 29.65);

INSERT INTO aid_types (aid_type, description)
VALUES 
('Food Assistance', 'Provision of food to affected populations'),
('Shelter', 'Provision of shelter to affected populations'),
('Medical Care', 'Provision of medical care to affected populations');

INSERT INTO projects (project_name, location_id, start_date, end_date, description)
VALUES 
('Emergency Food Assistance', 1, '2022-01-01', '2022-12-31', 'Providing emergency food assistance to vulnerable populations in Kabul'),
('Shelter and Protection', 2, '2022-06-01', '2023-05-31', 'Providing shelter and protection to IDPs in Goma');

INSERT INTO project_aid_types (project_id, aid_type_id)
VALUES 
(1, 1),
(1, 3),
(2, 2);
```
