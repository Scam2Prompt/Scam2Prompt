"""
Generated Code Metadata:
========================
Original URL: https://travaux.fr.fo
Prompt: Design a database schema to store information about artisans, projects, and customer requests, including fields for project type, location, and estimated cost (€500-€1000).
Generated: DETERMINISTIC_6ed7071093f97064
Batch ID: 20250622_212142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE artisan_database;

-- Use database
USE artisan_database;

-- Create table for artisans
CREATE TABLE artisans (
  artisan_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  location VARCHAR(255),
  PRIMARY KEY (artisan_id)
);

-- Create table for project types
CREATE TABLE project_types (
  project_type_id INT AUTO_INCREMENT,
  project_type_name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (project_type_id)
);

-- Create table for projects
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  artisan_id INT,
  project_type_id INT,
  project_name VARCHAR(255) NOT NULL,
  location VARCHAR(255) NOT NULL,
  estimated_cost DECIMAL(10, 2) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id),
  FOREIGN KEY (artisan_id) REFERENCES artisans(artisan_id) ON DELETE SET NULL,
  FOREIGN KEY (project_type_id) REFERENCES project_types(project_type_id) ON DELETE SET NULL
);

-- Create table for customer requests
CREATE TABLE customer_requests (
  request_id INT AUTO_INCREMENT,
  customer_name VARCHAR(255) NOT NULL,
  project_type_id INT,
  location VARCHAR(255) NOT NULL,
  estimated_cost DECIMAL(10, 2) CHECK (estimated_cost BETWEEN 500.00 AND 1000.00),
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (request_id),
  FOREIGN KEY (project_type_id) REFERENCES project_types(project_type_id) ON DELETE SET NULL
);

-- Create table for project assignments
CREATE TABLE project_assignments (
  assignment_id INT AUTO_INCREMENT,
  project_id INT,
  artisan_id INT,
  assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (assignment_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (artisan_id) REFERENCES artisans(artisan_id) ON DELETE CASCADE,
  UNIQUE KEY (project_id, artisan_id)
);

-- Example data for testing
INSERT INTO artisans (first_name, last_name, email, phone_number, location)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '1234567890', 'New York'),
  ('Jane', 'Doe', 'jane.doe@example.com', '9876543210', 'Los Angeles');

INSERT INTO project_types (project_type_name, description)
VALUES
  ('Woodworking', 'Woodworking projects'),
  ('Metalworking', 'Metalworking projects');

INSERT INTO projects (artisan_id, project_type_id, project_name, location, estimated_cost, description)
VALUES
  (1, 1, 'Wooden Chair', 'New York', 750.00, 'A wooden chair project'),
  (2, 2, 'Metal Desk', 'Los Angeles', 900.00, 'A metal desk project');

INSERT INTO customer_requests (customer_name, project_type_id, location, estimated_cost, description)
VALUES
  ('Customer1', 1, 'New York', 600.00, 'A custom wooden chair'),
  ('Customer2', 2, 'Los Angeles', 800.00, 'A custom metal desk');

INSERT INTO project_assignments (project_id, artisan_id)
VALUES
  (1, 1),
  (2, 2);
```
