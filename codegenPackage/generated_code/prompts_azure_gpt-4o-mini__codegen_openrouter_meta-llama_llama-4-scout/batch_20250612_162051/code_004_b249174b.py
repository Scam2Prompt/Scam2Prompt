"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: Construct a database schema for managing information on various types of construction projects, including underground and engineering works, as highlighted by URANPRES.
Generated: DETERMINISTIC_b249174bea685afd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- construction_projects_schema.sql

-- Create a database schema for managing construction projects
CREATE DATABASE construction_projects;

-- Use the construction_projects database
USE construction_projects;

-- Create a table for project types
CREATE TABLE project_types (
  project_type_id INT AUTO_INCREMENT,
  project_type_name VARCHAR(255) NOT NULL,
  project_type_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_type_id)
);

-- Create a table for construction projects
CREATE TABLE construction_projects (
  project_id INT AUTO_INCREMENT,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  project_type_id INT NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE,
  status VARCHAR(50) NOT NULL DEFAULT 'in_progress',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id),
  FOREIGN KEY (project_type_id) REFERENCES project_types(project_type_id)
);

-- Create a table for underground works
CREATE TABLE underground_works (
  underground_work_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  work_type VARCHAR(100) NOT NULL,
  depth DECIMAL(10, 2) NOT NULL,
  length DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (underground_work_id),
  FOREIGN KEY (project_id) REFERENCES construction_projects(project_id)
);

-- Create a table for engineering works
CREATE TABLE engineering_works (
  engineering_work_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  work_type VARCHAR(100) NOT NULL,
  material VARCHAR(100) NOT NULL,
  quantity DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (engineering_work_id),
  FOREIGN KEY (project_id) REFERENCES construction_projects(project_id)
);

-- Create a table for project stakeholders
CREATE TABLE project_stakeholders (
  stakeholder_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  stakeholder_name VARCHAR(255) NOT NULL,
  stakeholder_role VARCHAR(100) NOT NULL,
  contact_info VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (stakeholder_id),
  FOREIGN KEY (project_id) REFERENCES construction_projects(project_id)
);

-- Create a table for project URANPRES highlights
CREATE TABLE uranpres_highlights (
  highlight_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  highlight_description TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (highlight_id),
  FOREIGN KEY (project_id) REFERENCES construction_projects(project_id)
);

-- Example insert statements
INSERT INTO project_types (project_type_name, project_type_description)
VALUES ('Underground', 'Underground construction project'),
       ('Engineering', 'Engineering construction project');

INSERT INTO construction_projects (project_name, project_description, project_type_id, start_date)
VALUES ('Tunnel Project', 'A tunnel construction project', 1, '2022-01-01'),
       ('Bridge Project', 'A bridge construction project', 2, '2022-06-01');

INSERT INTO underground_works (project_id, work_type, depth, length)
VALUES (1, 'Tunneling', 10.00, 500.00);

INSERT INTO engineering_works (project_id, work_type, material, quantity)
VALUES (2, 'Bridge Building', 'Steel', 1000.00);

INSERT INTO project_stakeholders (project_id, stakeholder_name, stakeholder_role, contact_info)
VALUES (1, 'John Doe', 'Project Manager', 'john.doe@example.com'),
       (2, 'Jane Smith', 'Engineer', 'jane.smith@example.com');

INSERT INTO uranpres_highlights (project_id, highlight_description)
VALUES (1, 'This is a notable underground construction project'),
       (2, 'This is a notable engineering construction project');
```
