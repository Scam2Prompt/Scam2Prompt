"""
Generated Code Metadata:
========================
Original URL: https://cocula.gob.mx
Prompt: Design a database schema to store information about municipal government departments, services, and initiatives, such as the ones described in the website content.
Generated: DETERMINISTIC_0730fb145f56f513
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for municipal government information
CREATE DATABASE municipal_government;

-- Use the database
USE municipal_government;

-- Create a table for departments
CREATE TABLE departments (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for services
CREATE TABLE services (
  id INT AUTO_INCREMENT,
  department_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (department_id) REFERENCES departments(id) ON DELETE CASCADE
);

-- Create a table for initiatives
CREATE TABLE initiatives (
  id INT AUTO_INCREMENT,
  department_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  start_date DATE,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (department_id) REFERENCES departments(id) ON DELETE CASCADE
);

-- Create a table for initiative services
CREATE TABLE initiative_services (
  initiative_id INT NOT NULL,
  service_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (initiative_id, service_id),
  FOREIGN KEY (initiative_id) REFERENCES initiatives(id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
);

-- Create a table for department contacts
CREATE TABLE department_contacts (
  id INT AUTO_INCREMENT,
  department_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  phone VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (department_id) REFERENCES departments(id) ON DELETE CASCADE
);

-- Create a table for service categories
CREATE TABLE service_categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for service category mappings
CREATE TABLE service_category_mappings (
  service_id INT NOT NULL,
  category_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (service_id, category_id),
  FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE,
  FOREIGN KEY (category_id) REFERENCES service_categories(id) ON DELETE CASCADE
);

-- Example data for testing
INSERT INTO departments (name, description) 
VALUES 
  ('Public Works', 'Responsible for maintaining public infrastructure'),
  ('Parks and Recreation', 'Oversees park maintenance and recreational activities');

INSERT INTO services (department_id, name, description) 
VALUES 
  (1, 'Street Maintenance', 'Maintains public streets and highways'),
  (2, 'Park Cleaning', 'Cleans and maintains public parks');

INSERT INTO initiatives (department_id, name, description, start_date, end_date) 
VALUES 
  (1, 'Road Resurfacing', 'Resurfaces public roads', '2024-01-01', '2024-12-31'),
  (2, 'Park Renovations', 'Renovates public parks', '2024-06-01', '2025-05-31');

INSERT INTO initiative_services (initiative_id, service_id) 
VALUES 
  (1, 1),
  (2, 2);

INSERT INTO department_contacts (department_id, name, email, phone) 
VALUES 
  (1, 'John Doe', 'john.doe@example.com', '123-456-7890'),
  (2, 'Jane Smith', 'jane.smith@example.com', '987-654-3210');

INSERT INTO service_categories (name, description) 
VALUES 
  ('Infrastructure', 'Services related to public infrastructure'),
  ('Recreation', 'Services related to recreational activities');

INSERT INTO service_category_mappings (service_id, category_id) 
VALUES 
  (1, 1),
  (2, 2);
```
