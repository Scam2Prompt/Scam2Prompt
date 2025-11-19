"""
Generated Code Metadata:
========================
Original URL: https://uaeinterior.com
Prompt: Design a database schema for storing information about interior design projects, including project details, client information, and space planning, based on the services provided by Amazing Interior.
Generated: DETERMINISTIC_04782efdd28b7ed1
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Amazing Interior Database Schema

-- Create database
CREATE DATABASE amazing_interior;

-- Use database
USE amazing_interior;

-- Create tables

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

CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  start_date DATE,
  end_date DATE,
  status ENUM('in_progress', 'completed', 'cancelled') DEFAULT 'in_progress',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

CREATE TABLE spaces (
  space_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  space_name VARCHAR(255) NOT NULL,
  space_type ENUM('living_room', 'bedroom', 'kitchen', 'bathroom', 'other'),
  length DECIMAL(10, 2),
  width DECIMAL(10, 2),
  area DECIMAL(10, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (space_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

CREATE TABLE services (
  service_id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  service_description TEXT,
  service_cost DECIMAL(10, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_id)
);

CREATE TABLE project_services (
  project_id INT NOT NULL,
  service_id INT NOT NULL,
  quantity INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id, service_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

CREATE TABLE materials (
  material_id INT AUTO_INCREMENT,
  material_name VARCHAR(255) NOT NULL,
  material_description TEXT,
  material_cost DECIMAL(10, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (material_id)
);

CREATE TABLE space_materials (
  space_id INT NOT NULL,
  material_id INT NOT NULL,
  quantity INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (space_id, material_id),
  FOREIGN KEY (space_id) REFERENCES spaces(space_id) ON DELETE CASCADE,
  FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE
);

-- Indexes
CREATE INDEX idx_client_email ON clients(email);
CREATE INDEX idx_project_client_id ON projects(client_id);
CREATE INDEX idx_space_project_id ON spaces(project_id);
CREATE INDEX idx_project_service_id ON project_services(project_id, service_id);
CREATE INDEX idx_space_material_id ON space_materials(space_id, material_id);

-- Views

CREATE VIEW project_details AS
SELECT 
  p.project_id,
  c.client_id,
  c.first_name,
  c.last_name,
  p.project_name,
  p.project_description,
  p.start_date,
  p.end_date,
  p.status
FROM projects p
JOIN clients c ON p.client_id = c.client_id;

CREATE VIEW space_planning AS
SELECT 
  s.space_id,
  p.project_id,
  s.space_name,
  s.space_type,
  s.length,
  s.width,
  s.area
FROM spaces s
JOIN projects p ON s.project_id = p.project_id;

-- Stored Procedures

DELIMITER //
CREATE PROCEDURE get_project_details(IN project_id INT)
BEGIN
  SELECT * FROM project_details WHERE project_id = project_id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE get_space_planning(IN project_id INT)
BEGIN
  SELECT * FROM space_planning WHERE project_id = project_id;
END//
DELIMITER ;

-- Triggers

DELIMITER //
CREATE TRIGGER update_project_status
BEFORE UPDATE ON projects
FOR EACH ROW
BEGIN
  IF NEW.status <> OLD.status THEN
    INSERT INTO project_status_history (project_id, status, updated_at)
    VALUES (NEW.project_id, NEW.status, NOW());
  END IF;
END//
DELIMITER ;

-- Example usage:

-- Insert client
INSERT INTO clients (first_name, last_name, email, phone_number, address)
VALUES ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St');

-- Insert project
INSERT INTO projects (client_id, project_name, project_description, start_date, end_date)
VALUES (1, 'Living Room Renovation', 'Renovate living room with new furniture and flooring', '2022-01-01', '2022-06-01');

-- Insert space
INSERT INTO spaces (project_id, space_name, space_type, length, width, area)
VALUES (1, 'Living Room', 'living_room', 10.0, 12.0, 120.0);

-- Insert service
INSERT INTO services (service_name, service_description, service_cost)
VALUES ('Furniture Installation', 'Install new furniture', 1000.00);

-- Insert project service
INSERT INTO project_services (project_id, service_id, quantity)
VALUES (1, 1, 1);

-- Get project details
CALL get_project_details(1);

-- Get space planning
CALL get_space_planning(1);
```
