"""
Generated Code Metadata:
========================
Original URL: https://debnicakaszubska.eu
Prompt: Design a database schema for managing local government projects, including fields for project name, description, location, and status, inspired by the projects listed on the Gmina Dębnica Kaszubska website.
Generated: DETERMINISTIC_8fc4455081118481
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for managing local government projects

-- Create a database
CREATE DATABASE local_government_projects;

-- Use the database
USE local_government_projects;

-- Create a table for project locations
CREATE TABLE locations (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  postal_code VARCHAR(20) NOT NULL,
  PRIMARY KEY (id)
);

-- Create a table for project statuses
CREATE TABLE project_statuses (
  id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create a table for projects
CREATE TABLE projects (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT NOT NULL,
  location_id INT,
  status_id INT NOT NULL DEFAULT 1,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (location_id) REFERENCES locations(id) ON DELETE SET NULL,
  FOREIGN KEY (status_id) REFERENCES project_statuses(id) ON DELETE RESTRICT
);

-- Create a table for project updates
CREATE TABLE project_updates (
  id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  status_id INT NOT NULL,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  description TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE,
  FOREIGN KEY (status_id) REFERENCES project_statuses(id) ON DELETE RESTRICT
);

-- Insert sample data for project statuses
INSERT INTO project_statuses (name, description) VALUES
  ('Planned', 'Project is in the planning phase'),
  ('In Progress', 'Project is currently being implemented'),
  ('Completed', 'Project has been completed'),
  ('Cancelled', 'Project has been cancelled');

-- Insert sample data for project locations
INSERT INTO locations (name, address, city, postal_code) VALUES
  ('Town Hall', 'ul. Główna 1', 'Dębnica Kaszubska', '76-200'),
  ('School', 'ul. Szkolna 2', 'Dębnica Kaszubska', '76-200'),
  ('Park', 'ul. Parkowa 3', 'Dębnica Kaszubska', '76-200');

-- Insert sample data for projects
INSERT INTO projects (name, description, location_id, status_id) VALUES
  ('Town Hall Renovation', 'Renovation of the town hall building', 1, 2),
  ('New School Construction', 'Construction of a new school building', 2, 1),
  ('Park Development', 'Development of the town park', 3, 3);
```
