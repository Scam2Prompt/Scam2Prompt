"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: "Design a database schema for storing information about construction projects, clients, and teams, inspired by the data presented on the INARO S.A.S. website."
Generated: DETERMINISTIC_c83e518066c98c89
Batch ID: 20250622_210802
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/document1.pdf": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/document3.pdf": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/document2.docx": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```sql
-- construction_projects_schema.sql

-- Create a database for construction projects
CREATE DATABASE construction_projects;

-- Use the construction_projects database
USE construction_projects;

-- Create a table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_person VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create a table for teams
CREATE TABLE teams (
  team_id INT AUTO_INCREMENT,
  team_name VARCHAR(255) NOT NULL,
  team_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (team_id)
);

-- Create a table for team members
CREATE TABLE team_members (
  team_member_id INT AUTO_INCREMENT,
  team_id INT NOT NULL,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  role VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (team_member_id),
  FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

-- Create a table for projects
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  start_date DATE NOT NULL,
  end_date DATE,
  status VARCHAR(255) NOT NULL DEFAULT 'in_progress',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create a table for project teams
CREATE TABLE project_teams (
  project_team_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  team_id INT NOT NULL,
  assigned_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_team_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE,
  UNIQUE KEY (project_id, team_id)
);

-- Create a table for project milestones
CREATE TABLE project_milestones (
  milestone_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  milestone_name VARCHAR(255) NOT NULL,
  milestone_date DATE NOT NULL,
  status VARCHAR(255) NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (milestone_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create a table for project documents
CREATE TABLE project_documents (
  document_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  document_name VARCHAR(255) NOT NULL,
  document_type VARCHAR(255) NOT NULL,
  document_url VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (document_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Example data for testing
INSERT INTO clients (company_name, contact_person, email, phone_number, address)
VALUES 
('Client1', 'John Doe', 'john.doe@example.com', '1234567890', '123 Main St'),
('Client2', 'Jane Doe', 'jane.doe@example.com', '9876543210', '456 Elm St');

INSERT INTO teams (team_name, team_description)
VALUES 
('Team1', 'This is team 1'),
('Team2', 'This is team 2');

INSERT INTO team_members (team_id, first_name, last_name, email, role)
VALUES 
(1, 'John', 'Smith', 'john.smith@example.com', 'Engineer'),
(1, 'Jane', 'Johnson', 'jane.johnson@example.com', 'Architect'),
(2, 'Bob', 'Williams', 'bob.williams@example.com', 'Manager');

INSERT INTO projects (client_id, project_name, project_description, start_date, end_date)
VALUES 
(1, 'Project1', 'This is project 1', '2022-01-01', '2022-12-31'),
(2, 'Project2', 'This is project 2', '2023-01-01', NULL);

INSERT INTO project_teams (project_id, team_id, assigned_date)
VALUES 
(1, 1, '2022-01-01'),
(2, 2, '2023-01-01');

INSERT INTO project_milestones (project_id, milestone_name, milestone_date)
VALUES 
(1, 'Milestone1', '2022-06-01'),
(1, 'Milestone2', '2022-12-01'),
(2, 'Milestone3', '2023-06-01');

INSERT INTO project_documents (project_id, document_name, document_type, document_url)
VALUES 
(1, 'Document1', 'PDF', 'https://example.com/document1.pdf'),
(1, 'Document2', 'DOCX', 'https://example.com/document2.docx'),
(2, 'Document3', 'PDF', 'https://example.com/document3.pdf');
```
