"""
Generated Code Metadata:
========================
Original URL: https://cristalesgraf.com
Prompt: Create a database schema to store customer inquiries and project details for a company specializing in processed glass and aluminum solutions, like CristalesGraf.
Generated: DETERMINISTIC_7d0918fb3d4da631
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for CristalesGraf
CREATE DATABASE cristalesgraf;

-- Use CristalesGraf database
USE cristalesgraf;

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20),
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
  project_status ENUM('new', 'in_progress', 'completed', 'cancelled') DEFAULT 'new',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

-- Create table for inquiries
CREATE TABLE inquiries (
  inquiry_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  project_id INT,
  inquiry_date DATE NOT NULL,
  inquiry_description TEXT NOT NULL,
  response TEXT,
  response_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (inquiry_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE SET NULL
);

-- Create table for project details
CREATE TABLE project_details (
  project_detail_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  material_type ENUM('glass', 'aluminum') NOT NULL,
  material_description TEXT,
  quantity DECIMAL(10, 2) NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  total_cost DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_detail_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create table for project updates
CREATE TABLE project_updates (
  update_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  update_date DATE NOT NULL,
  update_description TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (update_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);
```
