"""
Generated Code Metadata:
========================
Original URL: https://www.sadadeng.com
Prompt: Develop a database schema for managing construction projects and their statuses, inspired by the project categories mentioned on the Sadad Engineering site.
Generated: DETERMINISTIC_84c6000cc50a5178
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- construction_projects_schema.sql

-- Create a database for construction projects
CREATE DATABASE construction_projects;

-- Use the construction_projects database
USE construction_projects;

-- Create a table for project categories
CREATE TABLE project_categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for project statuses
CREATE TABLE project_statuses (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for construction projects
CREATE TABLE construction_projects (
  id INT AUTO_INCREMENT,
  project_category_id INT,
  project_status_id INT,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  start_date DATE,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (project_category_id) REFERENCES project_categories(id) ON DELETE RESTRICT,
  FOREIGN KEY (project_status_id) REFERENCES project_statuses(id) ON DELETE RESTRICT
);

-- Create a table for project updates
CREATE TABLE project_updates (
  id INT AUTO_INCREMENT,
  construction_project_id INT,
  update_description TEXT,
  update_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (construction_project_id) REFERENCES construction_projects(id) ON DELETE CASCADE
);

-- Create a table for project teams
CREATE TABLE project_teams (
  id INT AUTO_INCREMENT,
  construction_project_id INT,
  team_member_name VARCHAR(255) NOT NULL,
  team_member_role VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (construction_project_id) REFERENCES construction_projects(id) ON DELETE CASCADE
);

-- Insert sample data into project categories
INSERT INTO project_categories (name, description)
VALUES
  ('Residential', 'Residential construction projects'),
  ('Commercial', 'Commercial construction projects'),
  ('Industrial', 'Industrial construction projects');

-- Insert sample data into project statuses
INSERT INTO project_statuses (name, description)
VALUES
  ('Planned', 'Project is in the planning phase'),
  ('In Progress', 'Project is currently in progress'),
  ('Completed', 'Project is completed'),
  ('Delayed', 'Project is delayed'),
  ('Cancelled', 'Project is cancelled');

-- Insert sample data into construction projects
INSERT INTO construction_projects (project_category_id, project_status_id, project_name, project_description, start_date, end_date)
VALUES
  (1, 2, 'Sample Residential Project', 'This is a sample residential project', '2022-01-01', '2023-01-01'),
  (2, 1, 'Sample Commercial Project', 'This is a sample commercial project', NULL, NULL),
  (3, 3, 'Sample Industrial Project', 'This is a sample industrial project', '2020-01-01', '2022-01-01');

-- Insert sample data into project updates
INSERT INTO project_updates (construction_project_id, update_description, update_date)
VALUES
  (1, 'Project started', '2022-01-01'),
  (1, 'Project is 50% complete', '2022-06-01'),
  (2, 'Project planning started', '2022-01-01');

-- Insert sample data into project teams
INSERT INTO project_teams (construction_project_id, team_member_name, team_member_role)
VALUES
  (1, 'John Doe', 'Project Manager'),
  (1, 'Jane Doe', 'Engineer'),
  (2, 'Bob Smith', 'Project Manager');
```
