"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: "Create a database schema for managing electrical contractor services, including traffic signals, street lighting, and underground utilities."
Generated: DETERMINISTIC_e4942e3df39d6717
Batch ID: 20250622_204749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- electrical_contractor_services.sql

-- Create database schema
CREATE DATABASE electrical_contractor_services;

-- Use database schema
USE electrical_contractor_services;

-- Create table for contractors
CREATE TABLE contractors (
  contractor_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  PRIMARY KEY (contractor_id)
);

-- Create table for services
CREATE TABLE services (
  service_id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (service_id)
);

-- Create table for traffic signals
CREATE TABLE traffic_signals (
  signal_id INT AUTO_INCREMENT,
  location VARCHAR(255) NOT NULL,
  installation_date DATE,
  maintenance_due_date DATE,
  contractor_id INT,
  PRIMARY KEY (signal_id),
  FOREIGN KEY (contractor_id) REFERENCES contractors(contractor_id)
);

-- Create table for street lighting
CREATE TABLE street_lighting (
  light_id INT AUTO_INCREMENT,
  location VARCHAR(255) NOT NULL,
  installation_date DATE,
  maintenance_due_date DATE,
  contractor_id INT,
  PRIMARY KEY (light_id),
  FOREIGN KEY (contractor_id) REFERENCES contractors(contractor_id)
);

-- Create table for underground utilities
CREATE TABLE underground_utilities (
  utility_id INT AUTO_INCREMENT,
  location VARCHAR(255) NOT NULL,
  utility_type VARCHAR(255) NOT NULL,
  installation_date DATE,
  maintenance_due_date DATE,
  contractor_id INT,
  PRIMARY KEY (utility_id),
  FOREIGN KEY (contractor_id) REFERENCES contractors(contractor_id)
);

-- Create table for work orders
CREATE TABLE work_orders (
  work_order_id INT AUTO_INCREMENT,
  contractor_id INT NOT NULL,
  service_id INT NOT NULL,
  description TEXT,
  start_date DATE NOT NULL,
  end_date DATE,
  status VARCHAR(50) NOT NULL DEFAULT 'pending',
  PRIMARY KEY (work_order_id),
  FOREIGN KEY (contractor_id) REFERENCES contractors(contractor_id),
  FOREIGN KEY (service_id) REFERENCES services(service_id)
);

-- Create table for work order assignments
CREATE TABLE work_order_assignments (
  assignment_id INT AUTO_INCREMENT,
  work_order_id INT NOT NULL,
  contractor_id INT NOT NULL,
  assigned_date DATE NOT NULL,
  PRIMARY KEY (assignment_id),
  FOREIGN KEY (work_order_id) REFERENCES work_orders(work_order_id),
  FOREIGN KEY (contractor_id) REFERENCES contractors(contractor_id)
);

-- Create table for maintenance records
CREATE TABLE maintenance_records (
  record_id INT AUTO_INCREMENT,
  equipment_id INT,
  equipment_type VARCHAR(255) NOT NULL,
  maintenance_date DATE NOT NULL,
  description TEXT,
  contractor_id INT NOT NULL,
  PRIMARY KEY (record_id),
  FOREIGN KEY (contractor_id) REFERENCES contractors(contractor_id)
);

-- Create indexes
CREATE INDEX idx_contractor_id ON traffic_signals (contractor_id);
CREATE INDEX idx_contractor_id ON street_lighting (contractor_id);
CREATE INDEX idx_contractor_id ON underground_utilities (contractor_id);
CREATE INDEX idx_contractor_id ON work_orders (contractor_id);
CREATE INDEX idx_service_id ON work_orders (service_id);

-- Insert sample data
INSERT INTO contractors (company_name, contact_name, email, phone_number, address)
VALUES 
('ABC Electrical', 'John Doe', 'john.doe@abc.com', '123-456-7890', '123 Main St'),
('DEF Electric', 'Jane Smith', 'jane.smith@def.com', '987-654-3210', '456 Elm St');

INSERT INTO services (service_name, description)
VALUES 
('Traffic Signal Installation', 'Installation of traffic signals'),
('Street Lighting Maintenance', 'Maintenance of street lighting'),
('Underground Utility Installation', 'Installation of underground utilities');

INSERT INTO traffic_signals (location, installation_date, maintenance_due_date, contractor_id)
VALUES 
('Main St and Elm St', '2020-01-01', '2025-01-01', 1),
('Oak St and Maple St', '2019-06-01', '2024-06-01', 2);

INSERT INTO street_lighting (location, installation_date, maintenance_due_date, contractor_id)
VALUES 
('Main St', '2018-01-01', '2023-01-01', 1),
('Elm St', '2017-06-01', '2022-06-01', 2);

INSERT INTO underground_utilities (location, utility_type, installation_date, maintenance_due_date, contractor_id)
VALUES 
('Main St', 'electric', '2015-01-01', '2020-01-01', 1),
('Elm St', 'gas', '2016-06-01', '2021-06-01', 2);

INSERT INTO work_orders (contractor_id, service_id, description, start_date, end_date)
VALUES 
(1, 1, 'Install traffic signal', '2022-01-01', '2022-01-31'),
(2, 2, 'Maintain street lighting', '2022-02-01', '2022-02-28');

INSERT INTO work_order_assignments (work_order_id, contractor_id, assigned_date)
VALUES 
(1, 1, '2022-01-01'),
(2, 2, '2022-02-01');

INSERT INTO maintenance_records (equipment_id, equipment_type, maintenance_date, description, contractor_id)
VALUES 
(1, 'traffic signal', '2022-01-15', 'Routine maintenance', 1),
(2, 'street light', '2022-02-15', 'Routine maintenance', 2);
```
