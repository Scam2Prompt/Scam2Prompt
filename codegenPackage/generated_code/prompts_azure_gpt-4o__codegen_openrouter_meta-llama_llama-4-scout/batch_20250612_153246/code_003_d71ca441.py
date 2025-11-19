"""
Generated Code Metadata:
========================
Original URL: https://youngistaan.org
Prompt: Develop a database schema for managing projects such as "Siksha," "Medical Programs," and "Road Safety Program" described by Youngistaan Foundation.
Generated: DETERMINISTIC_d71ca44167fad400
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for Youngistaan Foundation projects
CREATE DATABASE youngistaan_foundation;

-- Use the created database
USE youngistaan_foundation;

-- Create a table for projects
CREATE TABLE projects (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for project categories
CREATE TABLE project_categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a many-to-many relationship table for project categories
CREATE TABLE project_category_mappings (
  project_id INT NOT NULL,
  category_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id, category_id),
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE,
  FOREIGN KEY (category_id) REFERENCES project_categories(id) ON DELETE CASCADE
);

-- Create a table for project milestones
CREATE TABLE project_milestones (
  id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  due_date DATE,
  status ENUM('pending', 'in_progress', 'completed') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
);

-- Create a table for project tasks
CREATE TABLE project_tasks (
  id INT AUTO_INCREMENT,
  milestone_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  due_date DATE,
  status ENUM('pending', 'in_progress', 'completed') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (milestone_id) REFERENCES project_milestones(id) ON DELETE CASCADE
);

-- Create a table for project team members
CREATE TABLE project_team_members (
  id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  role VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
);

-- Create a table for project expenses
CREATE TABLE project_expenses (
  id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  expense_date DATE NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO projects (name, description) 
VALUES 
('Siksha', 'Education program'),
('Medical Programs', 'Health initiative'),
('Road Safety Program', 'Road safety awareness campaign');

INSERT INTO project_categories (name, description) 
VALUES 
('Education', 'Programs focused on education'),
('Health', 'Programs focused on health'),
('Safety', 'Programs focused on safety');

INSERT INTO project_category_mappings (project_id, category_id) 
VALUES 
(1, 1),
(2, 2),
(3, 3);

INSERT INTO project_milestones (project_id, name, description, due_date) 
VALUES 
(1, 'Milestone 1', 'Complete project planning', '2024-09-30'),
(2, 'Milestone 2', 'Conduct health survey', '2024-10-15'),
(3, 'Milestone 3', 'Launch safety campaign', '2024-11-01');

INSERT INTO project_tasks (milestone_id, name, description, due_date) 
VALUES 
(1, 'Task 1', 'Define project scope', '2024-09-20'),
(2, 'Task 2', 'Collect health data', '2024-10-10'),
(3, 'Task 3', 'Create safety materials', '2024-10-25');

INSERT INTO project_team_members (project_id, name, email, role) 
VALUES 
(1, 'John Doe', 'john@example.com', 'Project Manager'),
(2, 'Jane Smith', 'jane@example.com', 'Team Lead'),
(3, 'Bob Johnson', 'bob@example.com', 'Member');

INSERT INTO project_expenses (project_id, expense_date, amount, description) 
VALUES 
(1, '2024-09-15', 1000.00, 'Project planning expenses'),
(2, '2024-10-05', 500.00, 'Survey expenses'),
(3, '2024-10-20', 2000.00, 'Campaign expenses');
```
