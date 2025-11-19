"""
Generated Code Metadata:
========================
Original URL: https://clarkconstructionllc.net
Prompt: Design a simple database schema to manage client projects and services for a construction company like Clark Construction LLC.
Generated: DETERMINISTIC_b707e2b714067697
Batch ID: 20250622_211514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for the construction company
CREATE DATABASE construction_company;

-- Use the construction company database
USE construction_company;

-- Create a table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  zip_code VARCHAR(20) NOT NULL,
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
  status VARCHAR(50) NOT NULL DEFAULT 'in_progress',
  PRIMARY KEY (project_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create a table for services
CREATE TABLE services (
  service_id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  service_description TEXT,
  service_cost DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (service_id)
);

-- Create a many-to-many relationship table for project services
CREATE TABLE project_services (
  project_id INT NOT NULL,
  service_id INT NOT NULL,
  PRIMARY KEY (project_id, service_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Create a table for project managers
CREATE TABLE project_managers (
  manager_id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  PRIMARY KEY (manager_id)
);

-- Create a many-to-many relationship table for project managers
CREATE TABLE project_manager_assignments (
  project_id INT NOT NULL,
  manager_id INT NOT NULL,
  PRIMARY KEY (project_id, manager_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (manager_id) REFERENCES project_managers(manager_id) ON DELETE CASCADE
);

-- Create a table for project updates
CREATE TABLE project_updates (
  update_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  update_date DATE NOT NULL,
  update_description TEXT NOT NULL,
  PRIMARY KEY (update_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create a table for invoices
CREATE TABLE invoices (
  invoice_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  invoice_date DATE NOT NULL,
  invoice_amount DECIMAL(10, 2) NOT NULL,
  payment_status VARCHAR(50) NOT NULL DEFAULT 'pending',
  PRIMARY KEY (invoice_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);
```

```sql
-- sample_data.sql

-- Insert sample data into the database
INSERT INTO clients (company_name, contact_name, email, phone_number, address, city, state, zip_code)
VALUES
  ('Clark Construction LLC', 'John Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345'),
  ('ABC Corporation', 'Jane Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St', 'Othertown', 'NY', '67890');

INSERT INTO projects (client_id, project_name, project_description, start_date, end_date)
VALUES
  (1, 'Project 1', 'This is project 1', '2022-01-01', '2022-12-31'),
  (1, 'Project 2', 'This is project 2', '2023-01-01', NULL),
  (2, 'Project 3', 'This is project 3', '2022-06-01', '2022-12-31');

INSERT INTO services (service_name, service_description, service_cost)
VALUES
  ('Construction Management', 'Construction management services', 10000.00),
  ('Design Services', 'Design services for construction projects', 5000.00),
  ('Project Management', 'Project management services for construction projects', 20000.00);

INSERT INTO project_services (project_id, service_id)
VALUES
  (1, 1),
  (1, 2),
  (2, 3),
  (3, 1);

INSERT INTO project_managers (first_name, last_name, email, phone_number)
VALUES
  ('Bob', 'Johnson', 'bob.johnson@example.com', '555-123-4567'),
  ('Alice', 'Williams', 'alice.williams@example.com', '555-987-6543');

INSERT INTO project_manager_assignments (project_id, manager_id)
VALUES
  (1, 1),
  (2, 2),
  (3, 1);

INSERT INTO project_updates (project_id, update_date, update_description)
VALUES
  (1, '2022-06-01', 'Project 1 update 1'),
  (1, '2022-12-01', 'Project 1 update 2'),
  (2, '2023-06-01', 'Project 2 update 1');

INSERT INTO invoices (project_id, invoice_date, invoice_amount)
VALUES
  (1, '2022-07-01', 50000.00),
  (1, '2022-12-01', 100000.00),
  (2, '2023-07-01', 20000.00);
```
