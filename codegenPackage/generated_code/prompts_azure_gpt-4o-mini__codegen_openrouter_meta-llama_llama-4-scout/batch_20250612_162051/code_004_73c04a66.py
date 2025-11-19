"""
Generated Code Metadata:
========================
Original URL: https://ecolux-btp.com
Prompt: Design a database schema for managing construction projects, clients, and materials, reflecting the operational structure of ECOLUX, which includes residential and commercial projects.
Generated: DETERMINISTIC_73c04a6622ce8759
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for ECOLUX construction projects
CREATE DATABASE ecolux;

-- Use the ecolux database
USE ecolux;

-- Create table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_person VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  client_type ENUM('residential', 'commercial') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create table for projects
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  project_name VARCHAR(255) NOT NULL,
  project_type ENUM('residential', 'commercial') NOT NULL,
  project_status ENUM('in_progress', 'completed', 'cancelled') NOT NULL DEFAULT 'in_progress',
  start_date DATE NOT NULL,
  end_date DATE,
  budget DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create table for materials
CREATE TABLE materials (
  material_id INT AUTO_INCREMENT,
  material_name VARCHAR(100) NOT NULL,
  material_type VARCHAR(50) NOT NULL,
  unit_cost DECIMAL(10, 2) NOT NULL,
  unit_of_measurement VARCHAR(20) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (material_id)
);

-- Create table for project materials
CREATE TABLE project_materials (
  project_id INT NOT NULL,
  material_id INT NOT NULL,
  quantity DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id, material_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE
);

-- Create table for employees
CREATE TABLE employees (
  employee_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  role ENUM('manager', 'engineer', 'laborer') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (employee_id)
);

-- Create table for project employees
CREATE TABLE project_employees (
  project_id INT NOT NULL,
  employee_id INT NOT NULL,
  role ENUM('manager', 'engineer', 'laborer') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id, employee_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method ENUM('cash', 'bank_transfer', 'credit_card') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create table for invoices
CREATE TABLE invoices (
  invoice_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  invoice_date DATE NOT NULL,
  invoice_amount DECIMAL(10, 2) NOT NULL,
  invoice_status ENUM('pending', 'paid', 'overdue') NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (invoice_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);
```
