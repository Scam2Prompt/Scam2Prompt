"""
Generated Code Metadata:
========================
Original URL: https://albatrosspa.cl
Prompt: "Design a database schema for a construction project management system, incorporating features like project tracking, team collaboration, and client communication, similar to Albatros SPA's approach to project management."
Generated: DETERMINISTIC_3aa5a495f2b19d9e
Batch ID: 20250622_211510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- construction_project_management_schema.sql

-- Create database schema
CREATE DATABASE construction_project_management;

-- Use database schema
USE construction_project_management;

-- Create tables

CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  start_date DATE NOT NULL,
  end_date DATE,
  status ENUM('planned', 'in_progress', 'completed', 'cancelled') DEFAULT 'planned',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id)
);

CREATE TABLE teams (
  team_id INT AUTO_INCREMENT,
  team_name VARCHAR(255) NOT NULL,
  team_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (team_id)
);

CREATE TABLE team_members (
  team_member_id INT AUTO_INCREMENT,
  team_id INT NOT NULL,
  user_id INT NOT NULL,
  role ENUM('admin', 'member') DEFAULT 'member',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (team_member_id),
  FOREIGN KEY (team_id) REFERENCES teams(team_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE users (
  user_id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id)
);

CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  client_name VARCHAR(255) NOT NULL,
  client_email VARCHAR(255) NOT NULL,
  client_phone VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

CREATE TABLE project_tasks (
  task_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  task_name VARCHAR(255) NOT NULL,
  task_description TEXT,
  start_date DATE NOT NULL,
  end_date DATE,
  status ENUM('to_do', 'in_progress', 'completed') DEFAULT 'to_do',
  assigned_to INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (task_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id),
  FOREIGN KEY (assigned_to) REFERENCES users(user_id)
);

CREATE TABLE communications (
  communication_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  sender_id INT NOT NULL,
  recipient_id INT,
  message TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (communication_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id),
  FOREIGN KEY (sender_id) REFERENCES users(user_id),
  FOREIGN KEY (recipient_id) REFERENCES users(user_id)
);

CREATE TABLE project_updates (
  update_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  update_description TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (update_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

CREATE TABLE client_communications (
  client_communication_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  project_id INT NOT NULL,
  message TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_communication_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- Create indexes

CREATE INDEX idx_projects_status ON projects (status);
CREATE INDEX idx_project_tasks_status ON project_tasks (status);
CREATE INDEX idx_communications_project_id ON communications (project_id);
CREATE INDEX idx_client_communications_project_id ON client_communications (project_id);

-- Create views

CREATE VIEW project_task_overview AS
SELECT 
  p.project_name,
  pt.task_name,
  pt.status,
  u.username AS assigned_to
FROM 
  projects p
  JOIN project_tasks pt ON p.project_id = pt.project_id
  LEFT JOIN users u ON pt.assigned_to = u.user_id;

CREATE VIEW client_communication_overview AS
SELECT 
  c.client_name,
  cc.message,
  p.project_name
FROM 
  clients c
  JOIN client_communications cc ON c.client_id = cc.client_id
  JOIN projects p ON cc.project_id = p.project_id;
```

```sql
-- Insert sample data

INSERT INTO users (username, email, password_hash, first_name, last_name)
VALUES 
  ('john_doe', 'john@example.com', 'password_hash', 'John', 'Doe'),
  ('jane_doe', 'jane@example.com', 'password_hash', 'Jane', 'Doe');

INSERT INTO teams (team_name, team_description)
VALUES 
  ('Construction Team', 'Main construction team');

INSERT INTO team_members (team_id, user_id, role)
VALUES 
  (1, 1, 'admin'),
  (1, 2, 'member');

INSERT INTO projects (project_name, project_description, start_date, end_date, status)
VALUES 
  ('Sample Project', 'This is a sample project', '2022-01-01', '2022-12-31', 'in_progress');

INSERT INTO project_tasks (project_id, task_name, task_description, start_date, end_date, status, assigned_to)
VALUES 
  (1, 'Task 1', 'This is task 1', '2022-01-01', '2022-01-31', 'in_progress', 1);

INSERT INTO communications (project_id, sender_id, recipient_id, message)
VALUES 
  (1, 1, 2, 'Hello, this is a test message');

INSERT INTO clients (client_name, client_email, client_phone)
VALUES 
  ('Sample Client', 'client@example.com', '1234567890');

INSERT INTO client_communications (client_id, project_id, message)
VALUES 
  (1, 1, 'Hello, this is a test message from client');
```
