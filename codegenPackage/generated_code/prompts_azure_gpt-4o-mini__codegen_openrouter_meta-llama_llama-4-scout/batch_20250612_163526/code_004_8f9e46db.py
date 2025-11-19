"""
Generated Code Metadata:
========================
Original URL: https://clarkconstructionllc.net
Prompt: Design a simple database schema for a construction company that includes tables for services like painting, drywall, and home additions, based on the service offerings of Clark Construction LLC.
Generated: DETERMINISTIC_8f9e46dbc12bea17
Batch ID: 20250612_163526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Clark Construction LLC
CREATE DATABASE clark_construction;

-- Use the database
USE clark_construction;

-- Create table for services
CREATE TABLE services (
  service_id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  service_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_id)
);

-- Create table for service categories
CREATE TABLE service_categories (
  category_id INT AUTO_INCREMENT,
  category_name VARCHAR(255) NOT NULL,
  category_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (category_id)
);

-- Create table for services offered by Clark Construction LLC
CREATE TABLE offered_services (
  offered_service_id INT AUTO_INCREMENT,
  service_id INT NOT NULL,
  category_id INT NOT NULL,
  service_cost DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (offered_service_id),
  FOREIGN KEY (service_id) REFERENCES services(service_id),
  FOREIGN KEY (category_id) REFERENCES service_categories(category_id)
);

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create table for projects
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  project_status VARCHAR(50) NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create table for project services
CREATE TABLE project_services (
  project_service_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  offered_service_id INT NOT NULL,
  service_start_date DATE NOT NULL,
  service_end_date DATE,
  service_status VARCHAR(50) NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_service_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id),
  FOREIGN KEY (offered_service_id) REFERENCES offered_services(offered_service_id)
);

-- Insert sample data for services
INSERT INTO services (service_name, service_description)
VALUES
('Painting', 'Interior and exterior painting services'),
('Drywall', 'Installation and repair of drywall'),
('Home Additions', 'Design and construction of home additions');

-- Insert sample data for service categories
INSERT INTO service_categories (category_name, category_description)
VALUES
('Residential', 'Services offered for residential properties'),
('Commercial', 'Services offered for commercial properties');

-- Insert sample data for offered services
INSERT INTO offered_services (service_id, category_id, service_cost)
VALUES
(1, 1, 2000.00),
(2, 1, 1500.00),
(3, 1, 5000.00);

-- Insert sample data for customers
INSERT INTO customers (first_name, last_name, email, phone_number, address)
VALUES
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St');

-- Insert sample data for projects
INSERT INTO projects (customer_id, project_name, project_description)
VALUES
(1, 'John Doe''s Home Renovation', 'Renovation of John Doe''s home');

-- Insert sample data for project services
INSERT INTO project_services (project_id, offered_service_id, service_start_date)
VALUES
(1, 1, '2024-01-01'),
(1, 2, '2024-01-15');
```
