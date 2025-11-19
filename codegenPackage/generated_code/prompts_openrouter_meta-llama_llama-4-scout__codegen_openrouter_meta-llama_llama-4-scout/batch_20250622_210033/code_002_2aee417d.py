"""
Generated Code Metadata:
========================
Original URL: https://zirciulit.com
Prompt: "Design a database schema to store information about interior design projects, including client details, project phases, and product information, inspired by Zirciulit Design Firm's workflow."
Generated: DETERMINISTIC_2aee417d3e443547
Batch ID: 20250622_210033
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- interior_design_projects.sql

-- Create database schema
CREATE DATABASE interior_design_projects;

-- Use database schema
USE interior_design_projects;

-- Create clients table
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

-- Create projects table
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  start_date DATE,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create project_phases table
CREATE TABLE project_phases (
  phase_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  phase_name VARCHAR(255) NOT NULL,
  phase_description TEXT,
  start_date DATE,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (phase_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create products table
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  product_category VARCHAR(255) NOT NULL,
  product_subcategory VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id)
);

-- Create project_phase_products table (many-to-many relationship)
CREATE TABLE project_phase_products (
  project_id INT NOT NULL,
  phase_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id, phase_id, product_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (phase_id) REFERENCES project_phases(phase_id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create users table for authentication (optional)
CREATE TABLE users (
  user_id INT AUTO_INCREMENT,
  username VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  role ENUM('admin', 'designer', 'manager') NOT NULL DEFAULT 'designer',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id)
);

-- Example inserts
INSERT INTO clients (first_name, last_name, email, phone_number, address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

INSERT INTO projects (client_id, project_name, project_description, start_date, end_date)
VALUES 
(1, 'Living Room Renovation', 'Modern living room renovation', '2022-01-01', '2022-06-01'),
(2, 'Kitchen Remodel', 'Contemporary kitchen remodel', '2022-03-01', '2022-08-01');

INSERT INTO project_phases (project_id, phase_name, phase_description, start_date, end_date)
VALUES 
(1, 'Design', 'Design phase', '2022-01-01', '2022-02-01'),
(1, 'Implementation', 'Implementation phase', '2022-02-01', '2022-06-01'),
(2, 'Design', 'Design phase', '2022-03-01', '2022-04-01'),
(2, 'Implementation', 'Implementation phase', '2022-04-01', '2022-08-01');

INSERT INTO products (product_name, product_description, product_category, product_subcategory)
VALUES 
('Sofa', 'Modern sofa', 'Furniture', 'Seating'),
('Table', 'Dining table', 'Furniture', 'Tables'),
('Lamp', 'Table lamp', 'Lighting', 'Table Lamps');

INSERT INTO project_phase_products (project_id, phase_id, product_id, quantity)
VALUES 
(1, 1, 1, 2),
(1, 2, 1, 1),
(2, 1, 2, 1),
(2, 2, 3, 3);
```
