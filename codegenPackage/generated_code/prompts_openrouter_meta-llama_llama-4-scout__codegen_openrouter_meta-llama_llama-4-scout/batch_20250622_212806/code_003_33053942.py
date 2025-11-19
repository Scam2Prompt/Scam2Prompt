"""
Generated Code Metadata:
========================
Original URL: https://www.construyerk.com
Prompt: "Design a database schema for storing information about construction projects, including client details, project timelines, and budget, for a company like Construye RK."
Generated: DETERMINISTIC_33053942c4a0f909
Batch ID: 20250622_212806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- construction_projects_schema.sql

-- Create a database for construction projects
CREATE DATABASE construction_projects;

-- Use the construction_projects database
USE construction_projects;

-- Create a table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_person VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  PRIMARY KEY (client_id)
);

-- Create a table for projects
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  start_date DATE NOT NULL,
  end_date DATE,
  budget DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (project_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create a table for project timelines
CREATE TABLE project_timelines (
  timeline_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  milestone VARCHAR(255) NOT NULL,
  milestone_date DATE NOT NULL,
  status VARCHAR(50) NOT NULL CHECK (status IN ('pending', 'in_progress', 'completed')),
  PRIMARY KEY (timeline_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create a table for project expenses
CREATE TABLE project_expenses (
  expense_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  expense_date DATE NOT NULL,
  expense_amount DECIMAL(10, 2) NOT NULL,
  expense_description TEXT,
  PRIMARY KEY (expense_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create a table for project payments
CREATE TABLE project_payments (
  payment_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(50) NOT NULL,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create a stored procedure to insert a new client
DELIMITER //
CREATE PROCEDURE insert_client(
  IN p_company_name VARCHAR(255),
  IN p_contact_person VARCHAR(255),
  IN p_email VARCHAR(255),
  IN p_phone_number VARCHAR(20),
  IN p_address VARCHAR(255)
)
BEGIN
  INSERT INTO clients (company_name, contact_person, email, phone_number, address)
  VALUES (p_company_name, p_contact_person, p_email, p_phone_number, p_address);
END//
DELIMITER ;

-- Create a stored procedure to insert a new project
DELIMITER //
CREATE PROCEDURE insert_project(
  IN p_client_id INT,
  IN p_project_name VARCHAR(255),
  IN p_project_description TEXT,
  IN p_start_date DATE,
  IN p_end_date DATE,
  IN p_budget DECIMAL(10, 2)
)
BEGIN
  INSERT INTO projects (client_id, project_name, project_description, start_date, end_date, budget)
  VALUES (p_client_id, p_project_name, p_project_description, p_start_date, p_end_date, p_budget);
END//
DELIMITER ;

-- Example usage:
CALL insert_client('Construye RK Client', 'John Doe', 'john.doe@example.com', '1234567890', '123 Main St');
CALL insert_project(1, 'Construction Project 1', 'This is a construction project', '2022-01-01', '2022-12-31', 1000000.00);
```
