"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: "Design a database schema for storing client information, projects, and services offered by an engineering and architecture firm like TWM Associates."
Generated: DETERMINISTIC_8aa82f37c4e3a42c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for TWM Associates
CREATE DATABASE twm_associates;

-- Use the twm_associates database
USE twm_associates;

-- Create a table for clients
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT,
    company_name VARCHAR(255) NOT NULL,
    contact_first_name VARCHAR(100) NOT NULL,
    contact_last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    address_street VARCHAR(255) NOT NULL,
    address_city VARCHAR(100) NOT NULL,
    address_state VARCHAR(100) NOT NULL,
    address_zip VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
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
    status ENUM('in_progress', 'completed', 'cancelled') NOT NULL DEFAULT 'in_progress',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (project_id),
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create a table for services
CREATE TABLE services (
    service_id INT AUTO_INCREMENT,
    service_name VARCHAR(255) NOT NULL,
    service_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (service_id)
);

-- Create a table for project services
CREATE TABLE project_services (
    project_id INT NOT NULL,
    service_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (project_id, service_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Create a table for employees
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    role ENUM('engineer', 'architect', 'manager') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (employee_id)
);

-- Create a table for project employees
CREATE TABLE project_employees (
    project_id INT NOT NULL,
    employee_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (project_id, employee_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE
);

-- Insert sample data into clients table
INSERT INTO clients (company_name, contact_first_name, contact_last_name, email, phone_number, address_street, address_city, address_state, address_zip)
VALUES 
('ABC Corporation', 'John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'New York', 'NY', '10001'),
('XYZ Inc.', 'Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Park Ave', 'New York', 'NY', '10002');

-- Insert sample data into projects table
INSERT INTO projects (client_id, project_name, project_description, start_date, end_date, status)
VALUES 
(1, 'Project Alpha', 'This is project alpha', '2022-01-01', '2022-12-31', 'completed'),
(1, 'Project Beta', 'This is project beta', '2023-01-01', NULL, 'in_progress'),
(2, 'Project Gamma', 'This is project gamma', '2022-06-01', '2023-06-30', 'completed');

-- Insert sample data into services table
INSERT INTO services (service_name, service_description)
VALUES 
('Structural Engineering', 'Structural engineering services'),
('Architectural Design', 'Architectural design services'),
('Project Management', 'Project management services');

-- Insert sample data into project_services table
INSERT INTO project_services (project_id, service_id)
VALUES 
(1, 1),
(1, 2),
(2, 1),
(2, 3),
(3, 2),
(3, 3);

-- Insert sample data into employees table
INSERT INTO employees (first_name, last_name, email, phone_number, role)
VALUES 
('Alice', 'Johnson', 'alice.johnson@example.com', '111-222-3333', 'engineer'),
('Bob', 'Williams', 'bob.williams@example.com', '444-555-6666', 'architect'),
('Charlie', 'Davis', 'charlie.davis@example.com', '777-888-9999', 'manager');

-- Insert sample data into project_employees table
INSERT INTO project_employees (project_id, employee_id)
VALUES 
(1, 1),
(1, 2),
(2, 1),
(2, 3),
(3, 2),
(3, 3);
```
