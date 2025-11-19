"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: "Generate a sample database schema for storing information about construction projects, including underground construction, geological surveys, and client details, similar to what URANPRES, s.r.o. might use."
Generated: DETERMINISTIC_b4c184fb22988bf2
Batch ID: 20250622_210655
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

-- Create a table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_person VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create a table for geological surveys
CREATE TABLE geological_surveys (
  survey_id INT AUTO_INCREMENT,
  project_id INT,
  survey_date DATE NOT NULL,
  survey_type VARCHAR(100) NOT NULL,
  results TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (survey_id),
  FOREIGN KEY (project_id) REFERENCES construction_projects(project_id)
);

-- Create a table for underground construction
CREATE TABLE underground_construction (
  construction_id INT AUTO_INCREMENT,
  project_id INT,
  construction_type VARCHAR(100) NOT NULL,
  depth DECIMAL(10, 2) NOT NULL,
  length DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (construction_id),
  FOREIGN KEY (project_id) REFERENCES construction_projects(project_id)
);

-- Create a table for construction projects
CREATE TABLE construction_projects (
  project_id INT AUTO_INCREMENT,
  client_id INT,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  start_date DATE NOT NULL,
  end_date DATE,
  status VARCHAR(50) NOT NULL DEFAULT 'in_progress',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id)
);

-- Create a table for project personnel
CREATE TABLE project_personnel (
  personnel_id INT AUTO_INCREMENT,
  project_id INT,
  personnel_name VARCHAR(255) NOT NULL,
  role VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (personnel_id),
  FOREIGN KEY (project_id) REFERENCES construction_projects(project_id)
);

-- Create a table for project documents
CREATE TABLE project_documents (
  document_id INT AUTO_INCREMENT,
  project_id INT,
  document_type VARCHAR(100) NOT NULL,
  document_file BLOB NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (document_id),
  FOREIGN KEY (project_id) REFERENCES construction_projects(project_id)
);

-- Create indexes on foreign key columns
CREATE INDEX idx_geological_surveys_project_id ON geological_surveys (project_id);
CREATE INDEX idx_underground_construction_project_id ON underground_construction (project_id);
CREATE INDEX idx_construction_projects_client_id ON construction_projects (client_id);
CREATE INDEX idx_project_personnel_project_id ON project_personnel (project_id);
CREATE INDEX idx_project_documents_project_id ON project_documents (project_id);
```

```sql
-- Example usage:

-- Insert a client
INSERT INTO clients (company_name, contact_person, email, phone_number, address)
VALUES ('Example Client', 'John Doe', 'john.doe@example.com', '123-456-7890', '123 Main St');

-- Insert a construction project
INSERT INTO construction_projects (client_id, project_name, project_description, start_date)
VALUES (1, 'Example Project', 'This is an example project', '2022-01-01');

-- Insert a geological survey
INSERT INTO geological_surveys (project_id, survey_date, survey_type, results)
VALUES (1, '2022-01-15', 'soil_test', 'Soil test results');

-- Insert underground construction details
INSERT INTO underground_construction (project_id, construction_type, depth, length)
VALUES (1, 'tunnel', 10.0, 100.0);

-- Retrieve all construction projects with client information
SELECT cp.project_id, cp.project_name, c.company_name AS client_name
FROM construction_projects cp
JOIN clients c ON cp.client_id = c.client_id;
```
