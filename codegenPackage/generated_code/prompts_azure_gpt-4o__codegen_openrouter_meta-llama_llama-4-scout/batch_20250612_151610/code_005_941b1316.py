"""
Generated Code Metadata:
========================
Original URL: https://multiservicios3l.com
Prompt: Create a database schema for tracking the fabrication of custom industrial structures, based on the services offered by Multiservicios Industriales 3L.
Generated: DETERMINISTIC_941b1316b23927da
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- fabrication_tracking_schema.sql

-- Create database schema for tracking fabrication of custom industrial structures
CREATE DATABASE fabrication_tracking;

-- Use the database schema
USE fabrication_tracking;

-- Create table for clients
CREATE TABLE clients (
  id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_person VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for projects
CREATE TABLE projects (
  id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  start_date DATE NOT NULL,
  end_date DATE,
  status ENUM('in_progress', 'on_hold', 'completed', 'cancelled') DEFAULT 'in_progress',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- Create table for services offered
CREATE TABLE services (
  id INT AUTO_INCREMENT,
  service_name VARCHAR(100) NOT NULL,
  service_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for project services
CREATE TABLE project_services (
  id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  service_id INT NOT NULL,
  quantity INT NOT NULL,
  unit_cost DECIMAL(10, 2) NOT NULL,
  total_cost DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
);

-- Create table for materials
CREATE TABLE materials (
  id INT AUTO_INCREMENT,
  material_name VARCHAR(100) NOT NULL,
  material_description TEXT,
  unit_cost DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for project materials
CREATE TABLE project_materials (
  id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  material_id INT NOT NULL,
  quantity INT NOT NULL,
  unit_cost DECIMAL(10, 2) NOT NULL,
  total_cost DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE,
  FOREIGN KEY (material_id) REFERENCES materials(id) ON DELETE CASCADE
);

-- Create table for fabrication progress
CREATE TABLE fabrication_progress (
  id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  progress_date DATE NOT NULL,
  progress_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
);

-- Create table for quality control checks
CREATE TABLE quality_control_checks (
  id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  check_date DATE NOT NULL,
  check_description TEXT,
  result ENUM('pass', 'fail') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
);

-- Create table for deliveries
CREATE TABLE deliveries (
  id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  delivery_date DATE NOT NULL,
  delivery_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
);

-- Create indexes for foreign keys
CREATE INDEX idx_project_client_id ON projects (client_id);
CREATE INDEX idx_project_service_id ON project_services (project_id, service_id);
CREATE INDEX idx_project_material_id ON project_materials (project_id, material_id);
CREATE INDEX idx_fabrication_progress_project_id ON fabrication_progress (project_id);
CREATE INDEX idx_quality_control_checks_project_id ON quality_control_checks (project_id);
CREATE INDEX idx_deliveries_project_id ON deliveries (project_id);
```
