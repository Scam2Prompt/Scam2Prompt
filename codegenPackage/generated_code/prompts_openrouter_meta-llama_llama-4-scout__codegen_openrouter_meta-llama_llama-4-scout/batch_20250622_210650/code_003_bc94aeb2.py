"""
Generated Code Metadata:
========================
Original URL: https://corporacionelcristal.com.co
Prompt: Design a database schema for storing information about puppetry groups, similar to Corporación El Cristal, including details about their history and projects.
Generated: DETERMINISTIC_bc94aeb256c3e8cf
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- puppetry_groups database schema

-- Create database
CREATE DATABASE IF NOT EXISTS puppetry_groups;

-- Use database
USE puppetry_groups;

-- Create table for puppetry groups
CREATE TABLE IF NOT EXISTS groups (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  founded_date DATE,
  location VARCHAR(255),
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create table for group history
CREATE TABLE IF NOT EXISTS group_history (
  id INT AUTO_INCREMENT,
  group_id INT NOT NULL,
  event_date DATE NOT NULL,
  event_description TEXT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (group_id) REFERENCES groups(id) ON DELETE CASCADE
);

-- Create table for projects
CREATE TABLE IF NOT EXISTS projects (
  id INT AUTO_INCREMENT,
  group_id INT NOT NULL,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  start_date DATE,
  end_date DATE,
  PRIMARY KEY (id),
  FOREIGN KEY (group_id) REFERENCES groups(id) ON DELETE CASCADE
);

-- Create table for project collaborators
CREATE TABLE IF NOT EXISTS project_collaborators (
  id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  collaborator_name VARCHAR(255) NOT NULL,
  collaborator_role VARCHAR(255),
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
);

-- Create table for project performances
CREATE TABLE IF NOT EXISTS project_performances (
  id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  performance_date DATE NOT NULL,
  performance_location VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
);

-- Example insert statements
INSERT INTO groups (name, description, founded_date, location)
VALUES 
('Corporación El Cristal', 'A puppetry group from Latin America', '2000-01-01', 'Lima, Peru');

INSERT INTO group_history (group_id, event_date, event_description)
VALUES 
(1, '2005-01-01', 'First international tour');

INSERT INTO projects (group_id, project_name, project_description, start_date, end_date)
VALUES 
(1, 'The Glass Puppet', 'A puppetry show for children', '2010-01-01', '2012-12-31');

INSERT INTO project_collaborators (project_id, collaborator_name, collaborator_role)
VALUES 
(1, 'John Doe', 'Puppeteer');

INSERT INTO project_performances (project_id, performance_date, performance_location)
VALUES 
(1, '2011-06-01', 'New York City, USA');
```
