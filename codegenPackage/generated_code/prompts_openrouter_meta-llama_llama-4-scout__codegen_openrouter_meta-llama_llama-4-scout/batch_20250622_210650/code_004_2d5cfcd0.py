"""
Generated Code Metadata:
========================
Original URL: https://simplecede.com
Prompt: Design a simple database schema for a company like Simplécede that wants to store information about its projects, team members, and contacts.
Generated: DETERMINISTIC_2d5cfcd070fbfae4
Batch ID: 20250622_210650
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
CREATE DATABASE simplecede;

-- Use database
USE simplecede;

-- Create table for team members
CREATE TABLE team_members (
  `id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `job_title` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for projects
CREATE TABLE projects (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `start_date` DATE NOT NULL,
  `end_date` DATE,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for project team members
CREATE TABLE project_team_members (
  `project_id` INT NOT NULL,
  `team_member_id` INT NOT NULL,
  `role` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`project_id`, `team_member_id`),
  FOREIGN KEY (`project_id`) REFERENCES projects(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`team_member_id`) REFERENCES team_members(`id`) ON DELETE CASCADE
);

-- Create table for contacts
CREATE TABLE contacts (
  `id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for project contacts
CREATE TABLE project_contacts (
  `project_id` INT NOT NULL,
  `contact_id` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`project_id`, `contact_id`),
  FOREIGN KEY (`project_id`) REFERENCES projects(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`contact_id`) REFERENCES contacts(`id`) ON DELETE CASCADE
);

-- Example insert statements
INSERT INTO team_members (first_name, last_name, email, job_title)
VALUES 
('John', 'Doe', 'john.doe@example.com', 'Software Engineer'),
('Jane', 'Doe', 'jane.doe@example.com', 'Project Manager');

INSERT INTO projects (name, description, start_date, end_date)
VALUES 
('Project 1', 'This is project 1', '2022-01-01', '2022-12-31'),
('Project 2', 'This is project 2', '2023-01-01', NULL);

INSERT INTO project_team_members (project_id, team_member_id, role)
VALUES 
(1, 1, 'Developer'),
(1, 2, 'Project Manager'),
(2, 1, 'Lead Developer');

INSERT INTO contacts (first_name, last_name, email, phone_number)
VALUES 
('Bob', 'Smith', 'bob.smith@example.com', '123-456-7890'),
('Alice', 'Johnson', 'alice.johnson@example.com', NULL);

INSERT INTO project_contacts (project_id, contact_id)
VALUES 
(1, 1),
(2, 2);
```
