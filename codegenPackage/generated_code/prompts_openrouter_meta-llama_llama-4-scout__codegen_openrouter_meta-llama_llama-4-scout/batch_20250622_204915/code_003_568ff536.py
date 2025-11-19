"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: "Design a database schema to store information about civil engineering projects, including project details, client information, and service offerings like waterproofing and structural repairs."
Generated: DETERMINISTIC_568ff5363d6bf527
Batch ID: 20250622_204915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for civil engineering projects
CREATE DATABASE civil_engineering_projects;

-- Use the database
USE civil_engineering_projects;

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

-- Create a table for projects
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  start_date DATE NOT NULL,
  end_date DATE,
  status ENUM('ongoing', 'completed', 'cancelled') DEFAULT 'ongoing',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create a table for service offerings
CREATE TABLE service_offerings (
  service_id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  service_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_id)
);

-- Create a table for project services
CREATE TABLE project_services (
  project_id INT NOT NULL,
  service_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id, service_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES service_offerings(service_id) ON DELETE CASCADE
);

-- Create a table for waterproofing services
CREATE TABLE waterproofing_services (
  waterproofing_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  waterproofing_type VARCHAR(255) NOT NULL,
  area VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (waterproofing_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create a table for structural repairs
CREATE TABLE structural_repairs (
  repair_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  repair_type VARCHAR(255) NOT NULL,
  location VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (repair_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Insert sample data into clients table
INSERT INTO clients (company_name, contact_person, email, phone_number, address)
VALUES 
('ABC Corporation', 'John Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('DEF Inc.', 'Jane Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

-- Insert sample data into projects table
INSERT INTO projects (client_id, project_name, project_description, start_date, end_date)
VALUES 
(1, 'Project 1', 'This is project 1', '2022-01-01', '2022-12-31'),
(1, 'Project 2', 'This is project 2', '2023-01-01', NULL),
(2, 'Project 3', 'This is project 3', '2022-06-01', '2023-06-01');

-- Insert sample data into service offerings table
INSERT INTO service_offerings (service_name, service_description)
VALUES 
('Waterproofing', 'Waterproofing services for buildings'),
('Structural Repairs', 'Structural repair services for buildings');

-- Insert sample data into project services table
INSERT INTO project_services (project_id, service_id)
VALUES 
(1, 1),
(1, 2),
(2, 1),
(3, 2);

-- Insert sample data into waterproofing services table
INSERT INTO waterproofing_services (project_id, waterproofing_type, area, description)
VALUES 
(1, 'Basement Waterproofing', 'Basement', 'Waterproofing for basement'),
(2, 'Roof Waterproofing', 'Roof', 'Waterproofing for roof');

-- Insert sample data into structural repairs table
INSERT INTO structural_repairs (project_id, repair_type, location, description)
VALUES 
(1, 'Column Repair', 'Column 1', 'Repair for column 1'),
(3, 'Beam Repair', 'Beam 2', 'Repair for beam 2');
```
