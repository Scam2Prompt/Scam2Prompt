"""
Generated Code Metadata:
========================
Original URL: https://peacecitycontracting.com
Prompt: Create a simple database schema to store information about construction projects, including clients, services, and contractors, inspired by the services offered by Peace City Contracting LLC.
Generated: DETERMINISTIC_0d46351ddfb59011
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- construction_projects_schema.sql

-- Create database schema
CREATE DATABASE construction_projects;

-- Use database schema
USE construction_projects;

-- Create clients table
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  PRIMARY KEY (client_id)
);

-- Create contractors table
CREATE TABLE contractors (
  contractor_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  license_number VARCHAR(50) NOT NULL,
  PRIMARY KEY (contractor_id)
);

-- Create services table
CREATE TABLE services (
  service_id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (service_id)
);

-- Create projects table
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  project_name VARCHAR(255) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE,
  budget DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (project_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create project_services table (many-to-many)
CREATE TABLE project_services (
  project_id INT NOT NULL,
  service_id INT NOT NULL,
  PRIMARY KEY (project_id, service_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Create project_contractors table (many-to-many)
CREATE TABLE project_contractors (
  project_id INT NOT NULL,
  contractor_id INT NOT NULL,
  PRIMARY KEY (project_id, contractor_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (contractor_id) REFERENCES contractors(contractor_id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO clients (company_name, contact_name, email, phone_number, address)
VALUES
  ('ABC Corporation', 'John Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
  ('XYZ Inc.', 'Jane Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

INSERT INTO contractors (company_name, contact_name, email, phone_number, license_number)
VALUES
  ('Peace City Contracting LLC', 'Bob Johnson', 'bob.johnson@example.com', '555-123-4567', 'LICENSE-123'),
  ('Acme Builders', 'Mike Davis', 'mike.davis@example.com', '555-901-2345', 'LICENSE-456');

INSERT INTO services (service_name, description)
VALUES
  ('General Contracting', 'General contracting services for construction projects'),
  ('Home Renovation', 'Home renovation services including kitchen and bathroom remodels');

INSERT INTO projects (client_id, project_name, start_date, end_date, budget)
VALUES
  (1, 'Office Renovation', '2022-01-01', '2022-06-30', 100000.00),
  (2, 'Home Addition', '2022-03-01', '2022-09-30', 50000.00);

INSERT INTO project_services (project_id, service_id)
VALUES
  (1, 1),
  (1, 2),
  (2, 2);

INSERT INTO project_contractors (project_id, contractor_id)
VALUES
  (1, 1),
  (2, 2);
```
