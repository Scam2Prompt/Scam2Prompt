"""
Generated Code Metadata:
========================
Original URL: https://europarquets.be
Prompt: Develop a simple database schema for tracking projects and clients for a small business focused on aerogommage services, including tables for client information, project details, and service types.
Generated: DETERMINISTIC_3ea1093a5c87f446
Batch ID: 20250622_212043
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for aerogommage services
CREATE DATABASE aerogommage;

-- Use the aerogommage database
USE aerogommage;

-- Create table for service types
CREATE TABLE service_types (
  service_type_id INT AUTO_INCREMENT,
  service_type_name VARCHAR(255) NOT NULL,
  service_type_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_type_id)
);

-- Create table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create table for projects
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  service_type_id INT NOT NULL,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  start_date DATE,
  end_date DATE,
  status ENUM('pending', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (service_type_id) REFERENCES service_types(service_type_id) ON DELETE CASCADE
);

-- Create table for project services (many-to-many relationship)
CREATE TABLE project_services (
  project_id INT NOT NULL,
  service_type_id INT NOT NULL,
  PRIMARY KEY (project_id, service_type_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (service_type_id) REFERENCES service_types(service_type_id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_client_id ON projects(client_id);
CREATE INDEX idx_service_type_id ON projects(service_type_id);
CREATE INDEX idx_project_id ON project_services(project_id);
CREATE INDEX idx_service_type_id ON project_services(service_type_id);

-- Insert sample data
INSERT INTO service_types (service_type_name, service_type_description)
VALUES 
('Aerogommage', 'Abrasive blasting using compressed air'),
('Painting', 'Application of paint to surfaces');

INSERT INTO clients (first_name, last_name, email, phone_number, address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

INSERT INTO projects (client_id, service_type_id, project_name, project_description, start_date, end_date)
VALUES 
(1, 1, 'Car Restoration', 'Restoration of a classic car', '2022-01-01', '2022-12-31'),
(2, 2, 'Furniture Painting', 'Painting of furniture', '2023-01-01', '2023-06-30');

INSERT INTO project_services (project_id, service_type_id)
VALUES 
(1, 1),
(2, 2);
```
