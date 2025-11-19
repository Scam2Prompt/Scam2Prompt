"""
Generated Code Metadata:
========================
Original URL: https://onchain-adventures.com
Prompt: Design a database schema for managing consultancy projects and client interactions, based on the services provided by Dusanto Consultancy Trading OU.
Generated: DETERMINISTIC_5d21d88515226317
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- dusanto_consultancy_schema.sql

-- Create database schema for managing consultancy projects and client interactions
CREATE DATABASE dusanto_consultancy;

-- Use the created database
USE dusanto_consultancy;

-- Create table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create table for services offered by Dusanto Consultancy
CREATE TABLE services (
  service_id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  service_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_id)
);

-- Create table for projects
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  start_date DATE,
  end_date DATE,
  status ENUM('ongoing', 'completed', 'cancelled') DEFAULT 'ongoing',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create table for project services
CREATE TABLE project_services (
  project_id INT NOT NULL,
  service_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id, service_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Create table for interactions (meetings, calls, emails)
CREATE TABLE interactions (
  interaction_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  interaction_type ENUM('meeting', 'call', 'email') NOT NULL,
  interaction_date DATE NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (interaction_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create table for users (consultants)
CREATE TABLE users (
  user_id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  role ENUM('admin', 'consultant') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id)
);

-- Create table for project assignments
CREATE TABLE project_assignments (
  project_id INT NOT NULL,
  user_id INT NOT NULL,
  assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id, user_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
```

```sql
-- Example data for testing
INSERT INTO clients (company_name, contact_name, email, phone_number, address)
VALUES
  ('Acme Inc.', 'John Doe', 'john.doe@example.com', '+1 123 456 7890', '123 Main St'),
  ('Example Corp.', 'Jane Smith', 'jane.smith@example.com', '+1 987 654 3210', '456 Elm St');

INSERT INTO services (service_name, service_description)
VALUES
  ('Strategy Development', 'Development of a comprehensive business strategy'),
  ('Operational Improvement', 'Improvement of operational efficiency');

INSERT INTO projects (client_id, project_name, project_description, start_date, end_date)
VALUES
  (1, 'Acme Inc. Strategy Project', 'Develop a comprehensive business strategy', '2022-01-01', '2022-12-31'),
  (2, 'Example Corp. Operational Improvement', 'Improve operational efficiency', '2023-01-01', NULL);

INSERT INTO project_services (project_id, service_id)
VALUES
  (1, 1),
  (2, 2);

INSERT INTO interactions (project_id, interaction_type, interaction_date, description)
VALUES
  (1, 'meeting', '2022-01-15', 'Initial meeting with client'),
  (2, 'call', '2023-02-01', 'Follow-up call with client');

INSERT INTO users (username, email, password_hash, role)
VALUES
  ('admin', 'admin@example.com', 'password_hash', 'admin'),
  ('consultant', 'consultant@example.com', 'password_hash', 'consultant');

INSERT INTO project_assignments (project_id, user_id)
VALUES
  (1, 2),
  (2, 2);
```
