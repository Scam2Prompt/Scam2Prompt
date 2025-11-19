"""
Generated Code Metadata:
========================
Original URL: https://praiasdeminas.eng.br
Prompt: Develop a database schema for managing pool construction projects, including details like pool type, additional features (e.g., saunas, spas), and customer preferences, inspired by Praias de Minas services.
Generated: DETERMINISTIC_e88d5ab55c970ae0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for pool construction projects
CREATE DATABASE pool_construction;

-- Use the database
USE pool_construction;

-- Create table for pool types
CREATE TABLE pool_types (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for additional features
CREATE TABLE additional_features (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for customers
CREATE TABLE customers (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for pool construction projects
CREATE TABLE projects (
  id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  pool_type_id INT NOT NULL,
  project_date DATE,
  project_status ENUM('pending', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (customer_id) REFERENCES customers(id),
  FOREIGN KEY (pool_type_id) REFERENCES pool_types(id)
);

-- Create table for project features
CREATE TABLE project_features (
  id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  feature_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES projects(id),
  FOREIGN KEY (feature_id) REFERENCES additional_features(id)
);

-- Create table for customer preferences
CREATE TABLE customer_preferences (
  id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  preference_name VARCHAR(255) NOT NULL,
  preference_value VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (customer_id) REFERENCES customers(id)
);

-- Example data for testing
INSERT INTO pool_types (name, description) 
VALUES 
('Concrete Pool', 'A traditional pool made of concrete'),
('Fiberglass Pool', 'A pool made of fiberglass'),
('Vinyl Pool', 'A pool made of vinyl');

INSERT INTO additional_features (name, description) 
VALUES 
('Sauna', 'A small room for relaxation'),
('Spa', 'A small pool for relaxation'),
('Waterfall', 'A feature that creates a waterfall effect');

INSERT INTO customers (first_name, last_name, email, phone_number, address) 
VALUES 
('John', 'Doe', 'john@example.com', '123-456-7890', '123 Main St');

INSERT INTO projects (customer_id, pool_type_id, project_date, project_status) 
VALUES 
(1, 1, '2024-01-01', 'in_progress');

INSERT INTO project_features (project_id, feature_id) 
VALUES 
(1, 1),
(1, 2);

INSERT INTO customer_preferences (customer_id, preference_name, preference_value) 
VALUES 
(1, 'pool_size', '10x20'),
(1, 'pool_color', 'blue');
```
