"""
Generated Code Metadata:
========================
Original URL: https://stockyardrefacing.com
Prompt: "Create a simple database schema to store information about cabinet refacing projects, including client details, project timelines, and material used, inspired by the services at stockyardrefacing.com."
Generated: DETERMINISTIC_395f7035388ccc16
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for cabinet refacing projects
CREATE DATABASE cabinet_refacing;

-- Use the database
USE cabinet_refacing;

-- Create a table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  PRIMARY KEY (client_id)
);

-- Create a table for projects
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  project_name VARCHAR(255) NOT NULL,
  start_date DATE,
  end_date DATE,
  status ENUM('pending', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
  PRIMARY KEY (project_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create a table for project timelines
CREATE TABLE project_timelines (
  timeline_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  event_date DATE NOT NULL,
  event_description VARCHAR(255) NOT NULL,
  PRIMARY KEY (timeline_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create a table for materials
CREATE TABLE materials (
  material_id INT AUTO_INCREMENT,
  material_name VARCHAR(255) NOT NULL,
  material_type ENUM('wood', 'laminate', 'paint', 'other') NOT NULL,
  PRIMARY KEY (material_id)
);

-- Create a table for project materials
CREATE TABLE project_materials (
  project_id INT NOT NULL,
  material_id INT NOT NULL,
  quantity DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (project_id, material_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE
);

-- Create a table for contractors
CREATE TABLE contractors (
  contractor_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  PRIMARY KEY (contractor_id)
);

-- Create a table for project contractors
CREATE TABLE project_contractors (
  project_id INT NOT NULL,
  contractor_id INT NOT NULL,
  PRIMARY KEY (project_id, contractor_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (contractor_id) REFERENCES contractors(contractor_id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO clients (first_name, last_name, email, phone_number, address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

INSERT INTO projects (client_id, project_name, start_date, end_date)
VALUES 
(1, 'Kitchen Refacing', '2022-01-01', '2022-01-31'),
(2, 'Bathroom Refacing', '2022-02-01', '2022-02-28');

INSERT INTO project_timelines (project_id, event_date, event_description)
VALUES 
(1, '2022-01-05', 'Demo completed'),
(1, '2022-01-15', 'Cabinet installation completed'),
(2, '2022-02-05', 'Demo started');

INSERT INTO materials (material_name, material_type)
VALUES 
('Oak Wood', 'wood'),
('Laminate', 'laminate'),
('Paint', 'paint');

INSERT INTO project_materials (project_id, material_id, quantity)
VALUES 
(1, 1, 10.00),
(1, 3, 5.00),
(2, 2, 20.00);

INSERT INTO contractors (first_name, last_name, email, phone_number)
VALUES 
('Bob', 'Johnson', 'bob.johnson@example.com', '555-123-4567'),
('Alice', 'Williams', 'alice.williams@example.com', '555-987-6543');

INSERT INTO project_contractors (project_id, contractor_id)
VALUES 
(1, 1),
(2, 2);
```
