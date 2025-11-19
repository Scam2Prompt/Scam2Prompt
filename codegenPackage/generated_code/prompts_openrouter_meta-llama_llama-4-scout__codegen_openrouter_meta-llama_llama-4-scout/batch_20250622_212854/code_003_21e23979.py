"""
Generated Code Metadata:
========================
Original URL: https://www.premierpointing.com.au
Prompt: "Design a simple database schema to store information about brick and stone restoration projects, including client details, project scope, and service types like tuckpointing and remedial wall tie replacement."
Generated: DETERMINISTIC_21e239799bb80a78
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for brick and stone restoration projects
CREATE DATABASE restoration_projects;

-- Use the restoration_projects database
USE restoration_projects;

-- Create a table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  zip_code VARCHAR(20) NOT NULL,
  PRIMARY KEY (client_id)
);

-- Create a table for service types
CREATE TABLE service_types (
  service_type_id INT AUTO_INCREMENT,
  service_type_name VARCHAR(100) NOT NULL,
  description TEXT,
  PRIMARY KEY (service_type_id)
);

-- Insert initial service types
INSERT INTO service_types (service_type_name, description)
VALUES
  ('Tuckpointing', 'Tuckpointing service to repair mortar joints'),
  ('Remedial Wall Tie Replacement', 'Replacement of wall ties to stabilize walls');

-- Create a table for projects
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  project_name VARCHAR(255) NOT NULL,
  project_scope TEXT NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE,
  status VARCHAR(50) NOT NULL DEFAULT 'In Progress',
  PRIMARY KEY (project_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id)
);

-- Create a table for project services
CREATE TABLE project_services (
  project_service_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  service_type_id INT NOT NULL,
  PRIMARY KEY (project_service_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id),
  FOREIGN KEY (service_type_id) REFERENCES service_types(service_type_id)
);

-- Create a table for project updates
CREATE TABLE project_updates (
  update_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  update_date DATE NOT NULL,
  update_description TEXT NOT NULL,
  PRIMARY KEY (update_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- Create a table for invoices
CREATE TABLE invoices (
  invoice_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  invoice_date DATE NOT NULL,
  invoice_amount DECIMAL(10, 2) NOT NULL,
  payment_status VARCHAR(50) NOT NULL DEFAULT 'Pending',
  PRIMARY KEY (invoice_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id)
);
```

```sql
-- example_data.sql

-- Insert example clients
INSERT INTO clients (company_name, contact_name, email, phone, address, city, state, zip_code)
VALUES
  ('ABC Corporation', 'John Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345'),
  ('XYZ Inc.', 'Jane Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St', 'Othertown', 'NY', '67890');

-- Insert example projects
INSERT INTO projects (client_id, project_name, project_scope, start_date)
VALUES
  (1, 'Project 1', 'Restore brick facade', '2022-01-01'),
  (2, 'Project 2', 'Replace wall ties and tuckpoint', '2022-06-01');

-- Insert example project services
INSERT INTO project_services (project_id, service_type_id)
VALUES
  (1, 1),
  (2, 1),
  (2, 2);

-- Insert example project updates
INSERT INTO project_updates (project_id, update_date, update_description)
VALUES
  (1, '2022-01-15', 'Started demolition'),
  (2, '2022-06-15', 'Completed wall tie replacement');

-- Insert example invoices
INSERT INTO invoices (project_id, invoice_date, invoice_amount)
VALUES
  (1, '2022-02-01', 10000.00),
  (2, '2022-07-01', 20000.00);
```
