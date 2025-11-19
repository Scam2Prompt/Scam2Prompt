"""
Generated Code Metadata:
========================
Original URL: https://taiko-t.com
Prompt: Generate a SQL database schema to store information about construction projects, including project type (e.g., pole construction, electrical and civil engineering), location, and project status, for a company like 株式会社タイコーテクノ.
Generated: DETERMINISTIC_82e85303a5f33780
Batch ID: 20250622_205156
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

-- Create a table for project types
CREATE TABLE project_types (
  `project_type_id` INT AUTO_INCREMENT,
  `project_type_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  PRIMARY KEY (`project_type_id`),
  UNIQUE KEY (`project_type_name`)
);

-- Create a table for locations
CREATE TABLE locations (
  `location_id` INT AUTO_INCREMENT,
  `address` VARCHAR(255) NOT NULL,
  `city` VARCHAR(100) NOT NULL,
  `prefecture` VARCHAR(100) NOT NULL,
  `country` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`location_id`),
  UNIQUE KEY (`address`, `city`, `prefecture`, `country`)
);

-- Create a table for project statuses
CREATE TABLE project_statuses (
  `status_id` INT AUTO_INCREMENT,
  `status_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  PRIMARY KEY (`status_id`),
  UNIQUE KEY (`status_name`)
);

-- Create a table for construction projects
CREATE TABLE construction_projects (
  `project_id` INT AUTO_INCREMENT,
  `project_type_id` INT NOT NULL,
  `location_id` INT NOT NULL,
  `status_id` INT NOT NULL DEFAULT 1, -- Assuming 1 is 'Not Started'
  `project_name` VARCHAR(255) NOT NULL,
  `start_date` DATE,
  `end_date` DATE,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`project_id`),
  FOREIGN KEY (`project_type_id`) REFERENCES project_types(`project_type_id`),
  FOREIGN KEY (`location_id`) REFERENCES locations(`location_id`),
  FOREIGN KEY (`status_id`) REFERENCES project_statuses(`status_id`)
);

-- Insert sample data for project types
INSERT INTO project_types (`project_type_name`, `description`)
VALUES
  ('Pole Construction', 'Construction of poles for electrical or communication purposes'),
  ('Electrical Engineering', 'Electrical engineering projects'),
  ('Civil Engineering', 'Civil engineering projects');

-- Insert sample data for project statuses
INSERT INTO project_statuses (`status_name`, `description`)
VALUES
  ('Not Started', 'Project has not started yet'),
  ('In Progress', 'Project is currently in progress'),
  ('Completed', 'Project has been completed'),
  ('Cancelled', 'Project has been cancelled');

-- Insert sample data for locations
INSERT INTO locations (`address`, `city`, `prefecture`, `country`)
VALUES
  ('1-1-1, Shibuya', 'Shibuya', 'Tokyo', 'Japan'),
  ('2-2-2, Shinjuku', 'Shinjuku', 'Tokyo', 'Japan');

-- Insert sample data for construction projects
INSERT INTO construction_projects (`project_type_id`, `location_id`, `project_name`, `start_date`, `end_date`)
VALUES
  (1, 1, 'Pole Construction Project 1', '2022-01-01', '2022-06-30'),
  (2, 2, 'Electrical Engineering Project 1', '2022-07-01', '2022-12-31');
```
