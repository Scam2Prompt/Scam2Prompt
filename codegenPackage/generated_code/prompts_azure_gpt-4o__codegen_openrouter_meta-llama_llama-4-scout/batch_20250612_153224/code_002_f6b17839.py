"""
Generated Code Metadata:
========================
Original URL: https://vivekenterprises.co.in
Prompt: Generate code to create a database schema for tracking interior design projects, including fields for civil works, furniture, HVAC, electrical systems, and fire protection installations.
Generated: DETERMINISTIC_f6b178390fba24d1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- interior_design_projects.sql

-- Create database schema for interior design projects
CREATE DATABASE interior_design;

-- Use the database schema
USE interior_design;

-- Create table for projects
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  project_name VARCHAR(255) NOT NULL,
  client_name VARCHAR(255) NOT NULL,
  start_date DATE,
  end_date DATE,
  status VARCHAR(50) NOT NULL DEFAULT 'in_progress',
  PRIMARY KEY (project_id)
);

-- Create table for civil works
CREATE TABLE civil_works (
  civil_work_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  work_type VARCHAR(100) NOT NULL,
  description TEXT,
  start_date DATE,
  end_date DATE,
  status VARCHAR(50) NOT NULL DEFAULT 'in_progress',
  PRIMARY KEY (civil_work_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create table for furniture installations
CREATE TABLE furniture_installations (
  furniture_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  furniture_type VARCHAR(100) NOT NULL,
  quantity INT NOT NULL,
  description TEXT,
  installation_date DATE,
  PRIMARY KEY (furniture_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create table for HVAC installations
CREATE TABLE hvac_installations (
  hvac_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  hvac_type VARCHAR(100) NOT NULL,
  description TEXT,
  installation_date DATE,
  PRIMARY KEY (hvac_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create table for electrical systems
CREATE TABLE electrical_systems (
  electrical_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  system_type VARCHAR(100) NOT NULL,
  description TEXT,
  installation_date DATE,
  PRIMARY KEY (electrical_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create table for fire protection installations
CREATE TABLE fire_protection_installations (
  fire_protection_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  installation_type VARCHAR(100) NOT NULL,
  description TEXT,
  installation_date DATE,
  PRIMARY KEY (fire_protection_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create table for project updates
CREATE TABLE project_updates (
  update_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  update_date DATE NOT NULL,
  update_description TEXT NOT NULL,
  PRIMARY KEY (update_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create table for users
CREATE TABLE users (
  user_id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  role VARCHAR(50) NOT NULL DEFAULT 'user',
  PRIMARY KEY (user_id)
);

-- Create table for project assignments
CREATE TABLE project_assignments (
  assignment_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  user_id INT NOT NULL,
  PRIMARY KEY (assignment_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Indexes for faster queries
CREATE INDEX idx_project_id ON civil_works (project_id);
CREATE INDEX idx_project_id ON furniture_installations (project_id);
CREATE INDEX idx_project_id ON hvac_installations (project_id);
CREATE INDEX idx_project_id ON electrical_systems (project_id);
CREATE INDEX idx_project_id ON fire_protection_installations (project_id);
CREATE INDEX idx_project_id ON project_updates (project_id);
CREATE INDEX idx_project_id ON project_assignments (project_id);
CREATE INDEX idx_user_id ON project_assignments (user_id);

-- Views for easier data retrieval
CREATE VIEW project_details AS
SELECT 
  p.project_id,
  p.project_name,
  p.client_name,
  p.start_date,
  p.end_date,
  p.status
FROM projects p;

CREATE VIEW civil_work_details AS
SELECT 
  cw.civil_work_id,
  cw.project_id,
  cw.work_type,
  cw.description,
  cw.start_date,
  cw.end_date,
  cw.status
FROM civil_works cw;

CREATE VIEW furniture_installation_details AS
SELECT 
  fi.furniture_id,
  fi.project_id,
  fi.furniture_type,
  fi.quantity,
  fi.description,
  fi.installation_date
FROM furniture_installations fi;

CREATE VIEW hvac_installation_details AS
SELECT 
  hi.hvac_id,
  hi.project_id,
  hi.hvac_type,
  hi.description,
  hi.installation_date
FROM hvac_installations hi;

CREATE VIEW electrical_system_details AS
SELECT 
  es.electrical_id,
  es.project_id,
  es.system_type,
  es.description,
  es.installation_date
FROM electrical_systems es;

CREATE VIEW fire_protection_installation_details AS
SELECT 
  fpi.fire_protection_id,
  fpi.project_id,
  fpi.installation_type,
  fpi.description,
  fpi.installation_date
FROM fire_protection_installations fpi;
```
