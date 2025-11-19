"""
Generated Code Metadata:
========================
Original URL: https://sstco.ma
Prompt: Design a database schema to store information about construction projects, including project details, timelines, and personnel assignments, similar to what SSTCO might use to manage its projects.
Generated: DETERMINISTIC_13138450eeb756bd
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- construction_projects.sql

-- Create database schema for construction projects
CREATE DATABASE construction_projects;

-- Use the construction_projects database
USE construction_projects;

-- Create table for project details
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  client_name VARCHAR(255) NOT NULL,
  project_manager_id INT,
  start_date DATE NOT NULL,
  end_date DATE,
  status ENUM('planned', 'in_progress', 'completed', 'cancelled') DEFAULT 'planned',
  PRIMARY KEY (project_id)
);

-- Create table for project timelines
CREATE TABLE project_timelines (
  timeline_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  task_name VARCHAR(255) NOT NULL,
  task_description TEXT,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  status ENUM('planned', 'in_progress', 'completed') DEFAULT 'planned',
  PRIMARY KEY (timeline_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create table for personnel
CREATE TABLE personnel (
  personnel_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  role ENUM('engineer', 'architect', 'project_manager', 'laborer') NOT NULL,
  PRIMARY KEY (personnel_id)
);

-- Create table for project personnel assignments
CREATE TABLE project_assignments (
  assignment_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  personnel_id INT NOT NULL,
  role VARCHAR(255) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE,
  PRIMARY KEY (assignment_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (personnel_id) REFERENCES personnel(personnel_id) ON DELETE CASCADE
);

-- Create table for project managers
CREATE TABLE project_managers (
  project_manager_id INT AUTO_INCREMENT,
  personnel_id INT NOT NULL,
  PRIMARY KEY (project_manager_id),
  FOREIGN KEY (personnel_id) REFERENCES personnel(personnel_id) ON DELETE CASCADE
);

-- Create indexes for efficient querying
CREATE INDEX idx_project_name ON projects (project_name);
CREATE INDEX idx_project_id ON project_timelines (project_id);
CREATE INDEX idx_personnel_id ON project_assignments (personnel_id);

-- Example data insertion
INSERT INTO personnel (first_name, last_name, email, role)
VALUES 
('John', 'Doe', 'john.doe@example.com', 'project_manager'),
('Jane', 'Doe', 'jane.doe@example.com', 'engineer'),
('Bob', 'Smith', 'bob.smith@example.com', 'architect');

INSERT INTO projects (project_name, project_description, client_name, project_manager_id, start_date, end_date)
VALUES 
('Project Alpha', 'Construction of a new office building', 'ABC Corporation', 1, '2022-01-01', '2023-01-01');

INSERT INTO project_timelines (project_id, task_name, task_description, start_date, end_date)
VALUES 
(1, 'Site preparation', 'Prepare the construction site', '2022-01-01', '2022-02-01'),
(1, 'Foundation work', 'Lay the foundation for the building', '2022-02-01', '2022-04-01');

INSERT INTO project_assignments (project_id, personnel_id, role, start_date, end_date)
VALUES 
(1, 1, 'Project Manager', '2022-01-01', NULL),
(1, 2, 'Engineer', '2022-01-01', NULL),
(1, 3, 'Architect', '2022-01-01', NULL);

INSERT INTO project_managers (project_manager_id, personnel_id)
VALUES 
(1, 1);
```
