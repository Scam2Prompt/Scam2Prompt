"""
Generated Code Metadata:
========================
Original URL: https://perumakers.org
Prompt: Create a database schema for managing projects and collaborators for an organization like Perú Makers, with fields for project name, description, collaborators, and institutional partners.
Generated: DETERMINISTIC_ddc5fce2960ceb7a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for Perú Makers organization
CREATE DATABASE peru_makers;

-- Use the Perú Makers database
USE peru_makers;

-- Create a table for projects
CREATE TABLE projects (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for collaborators
CREATE TABLE collaborators (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  role VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for institutional partners
CREATE TABLE institutional_partners (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a many-to-many relationship table for projects and collaborators
CREATE TABLE project_collaborators (
  project_id INT NOT NULL,
  collaborator_id INT NOT NULL,
  role VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id, collaborator_id),
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE,
  FOREIGN KEY (collaborator_id) REFERENCES collaborators(id) ON DELETE CASCADE
);

-- Create a many-to-many relationship table for projects and institutional partners
CREATE TABLE project_institutional_partners (
  project_id INT NOT NULL,
  institutional_partner_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id, institutional_partner_id),
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE,
  FOREIGN KEY (institutional_partner_id) REFERENCES institutional_partners(id) ON DELETE CASCADE
);

-- Create indexes for efficient querying
CREATE INDEX idx_project_collaborators_project_id ON project_collaborators(project_id);
CREATE INDEX idx_project_collaborators_collaborator_id ON project_collaborators(collaborator_id);
CREATE INDEX idx_project_institutional_partners_project_id ON project_institutional_partners(project_id);
CREATE INDEX idx_project_institutional_partners_institutional_partner_id ON project_institutional_partners(institutional_partner_id);
```

```sql
-- example_data.sql

-- Insert example data into the database
INSERT INTO projects (name, description)
VALUES
  ('Project 1', 'This is the description of project 1'),
  ('Project 2', 'This is the description of project 2');

INSERT INTO collaborators (name, email, role)
VALUES
  ('John Doe', 'john.doe@example.com', 'Developer'),
  ('Jane Doe', 'jane.doe@example.com', 'Designer');

INSERT INTO institutional_partners (name, description)
VALUES
  ('Partner 1', 'This is the description of partner 1'),
  ('Partner 2', 'This is the description of partner 2');

INSERT INTO project_collaborators (project_id, collaborator_id, role)
VALUES
  (1, 1, 'Lead Developer'),
  (1, 2, 'UI/UX Designer'),
  (2, 1, 'Developer');

INSERT INTO project_institutional_partners (project_id, institutional_partner_id)
VALUES
  (1, 1),
  (2, 2);
```
