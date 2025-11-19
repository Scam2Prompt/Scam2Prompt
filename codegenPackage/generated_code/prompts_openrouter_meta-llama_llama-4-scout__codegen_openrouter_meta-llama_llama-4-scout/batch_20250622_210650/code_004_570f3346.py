"""
Generated Code Metadata:
========================
Original URL: https://lojaoficial.cloud
Prompt: "Design a database schema for storing architectural project information, including client data and project details, similar to Études' services."
Generated: DETERMINISTIC_570f33466c7039b4
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for storing architectural project information
CREATE DATABASE architectural_projects;

-- Use the database
USE architectural_projects;

-- Create a table for storing client information
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create a table for storing project status
CREATE TABLE project_status (
  status_id INT AUTO_INCREMENT,
  status_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (status_id)
);

-- Insert default project statuses
INSERT INTO project_status (status_name, description)
VALUES 
('New', 'New project proposal'),
('In Progress', 'Project is in progress'),
('On Hold', 'Project is on hold'),
('Completed', 'Project is completed'),
('Cancelled', 'Project is cancelled');

-- Create a table for storing project types
CREATE TABLE project_types (
  type_id INT AUTO_INCREMENT,
  type_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (type_id)
);

-- Insert default project types
INSERT INTO project_types (type_name, description)
VALUES 
('Residential', 'Residential building project'),
('Commercial', 'Commercial building project'),
('Industrial', 'Industrial building project'),
('Renovation', 'Renovation project');

-- Create a table for storing project information
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  project_name VARCHAR(255) NOT NULL,
  project_type_id INT NOT NULL,
  project_status_id INT NOT NULL DEFAULT 1,
  start_date DATE,
  end_date DATE,
  budget DECIMAL(10, 2),
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id),
  FOREIGN KEY (project_type_id) REFERENCES project_types(type_id),
  FOREIGN KEY (project_status_id) REFERENCES project_status(status_id)
);

-- Create a table for storing project phases
CREATE TABLE project_phases (
  phase_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  phase_name VARCHAR(255) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE,
  budget DECIMAL(10, 2),
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (phase_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- Create a table for storing project documents
CREATE TABLE project_documents (
  document_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  document_name VARCHAR(255) NOT NULL,
  document_type VARCHAR(255) NOT NULL,
  document_url VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (document_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- Create a table for storing project tasks
CREATE TABLE project_tasks (
  task_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  task_name VARCHAR(255) NOT NULL,
  task_description TEXT,
  start_date DATE,
  end_date DATE,
  status VARCHAR(255) NOT NULL DEFAULT 'New',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (task_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- Create a table for storing task assignments
CREATE TABLE task_assignments (
  assignment_id INT AUTO_INCREMENT,
  task_id INT NOT NULL,
  assignee_id INT NOT NULL,
  assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (assignment_id),
  FOREIGN KEY (task_id) REFERENCES project_tasks(task_id)
);

-- Create a table for storing users
CREATE TABLE users (
  user_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  role VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id)
);
```
