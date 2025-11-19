"""
Generated Code Metadata:
========================
Original URL: https://thedesignumbrella.in
Prompt: "Design a database schema for storing and managing projects, clients, and services for a design studio like The Design Umbrella, incorporating details such as project analysis, site study, and materials selection."
Generated: DETERMINISTIC_b3f6411ac786d1a7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the design studio
CREATE DATABASE design_studio;

-- Use the design_studio database
USE design_studio;

-- Create a table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create a table for services
CREATE TABLE services (
  service_id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  service_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_id)
);

-- Create a table for projects
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  start_date DATE,
  end_date DATE,
  status VARCHAR(50) NOT NULL DEFAULT 'in_progress',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create a table for project services
CREATE TABLE project_services (
  project_id INT NOT NULL,
  service_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id, service_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Create a table for project analysis
CREATE TABLE project_analysis (
  analysis_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  analysis_date DATE NOT NULL,
  analysis_notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (analysis_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create a table for site studies
CREATE TABLE site_studies (
  study_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  study_date DATE NOT NULL,
  study_notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (study_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create a table for materials selection
CREATE TABLE materials_selection (
  material_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  material_name VARCHAR(255) NOT NULL,
  material_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (material_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Example insert statements
INSERT INTO clients (company_name, contact_name, email, phone_number, address)
VALUES ('ABC Corporation', 'John Doe', 'john.doe@example.com', '123-456-7890', '123 Main St');

INSERT INTO services (service_name, service_description)
VALUES ('Interior Design', 'Interior design services for residential and commercial spaces');

INSERT INTO projects (client_id, project_name, project_description, start_date, end_date)
VALUES (1, 'Office Renovation', 'Renovation of ABC Corporation''s office space', '2022-01-01', '2022-06-01');

INSERT INTO project_services (project_id, service_id)
VALUES (1, 1);

INSERT INTO project_analysis (project_id, analysis_date, analysis_notes)
VALUES (1, '2022-01-15', 'Initial analysis of office space and requirements');

INSERT INTO site_studies (project_id, study_date, study_notes)
VALUES (1, '2022-02-01', 'Site study to assess existing conditions and identify potential challenges');

INSERT INTO materials_selection (project_id, material_name, material_description)
VALUES (1, 'Sustainable Wood', 'Eco-friendly wood options for furniture and finishes');
```
