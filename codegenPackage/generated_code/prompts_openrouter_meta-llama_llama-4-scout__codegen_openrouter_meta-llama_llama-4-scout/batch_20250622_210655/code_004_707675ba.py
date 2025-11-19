"""
Generated Code Metadata:
========================
Original URL: https://www.caag.com.br
Prompt: Create a SQL database schema to store information about law firm clients, cases, and attorneys, with tables inspired by the practice areas of CAAG (e.g., Direito Empresarial, Direito Civil, etc.).
Generated: DETERMINISTIC_707675baa525b8c3
Batch ID: 20250622_210655
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
CREATE DATABASE law_firm;

-- Use database
USE law_firm;

-- Create table for attorneys
CREATE TABLE attorneys (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  practice_area ENUM(
    'Direito Empresarial',
    'Direito Civil',
    'Direito Penal',
    'Direito Trabalhista',
    'Direito Tributário',
    'Direito Ambiental',
    'Direito do Consumidor'
  ) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for clients
CREATE TABLE clients (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for cases
CREATE TABLE cases (
  id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  attorney_id INT NOT NULL,
  case_description TEXT,
  practice_area ENUM(
    'Direito Empresarial',
    'Direito Civil',
    'Direito Penal',
    'Direito Trabalhista',
    'Direito Tributário',
    'Direito Ambiental',
    'Direito do Consumidor'
  ) NOT NULL,
  case_status ENUM('Open', 'In Progress', 'Closed') NOT NULL DEFAULT 'Open',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE,
  FOREIGN KEY (attorney_id) REFERENCES attorneys(id) ON DELETE CASCADE
);

-- Create table for case updates
CREATE TABLE case_updates (
  id INT AUTO_INCREMENT,
  case_id INT NOT NULL,
  update_description TEXT NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (case_id) REFERENCES cases(id) ON DELETE CASCADE
);

-- Create table for attorney clients
CREATE TABLE attorney_clients (
  attorney_id INT NOT NULL,
  client_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (attorney_id, client_id),
  FOREIGN KEY (attorney_id) REFERENCES attorneys(id) ON DELETE CASCADE,
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- Indexes for faster queries
CREATE INDEX idx_cases_client_id ON cases (client_id);
CREATE INDEX idx_cases_attorney_id ON cases (attorney_id);
CREATE INDEX idx_case_updates_case_id ON case_updates (case_id);
```

```sql
-- example usage
INSERT INTO attorneys (name, email, phone_number, practice_area)
VALUES 
('John Doe', 'john.doe@example.com', '123-456-7890', 'Direito Empresarial'),
('Jane Smith', 'jane.smith@example.com', '987-654-3210', 'Direito Civil');

INSERT INTO clients (name, email, phone_number, address)
VALUES 
('Client1', 'client1@example.com', '555-123-4567', '123 Main St'),
('Client2', 'client2@example.com', '555-987-6543', '456 Elm St');

INSERT INTO cases (client_id, attorney_id, case_description, practice_area)
VALUES 
(1, 1, 'Case description 1', 'Direito Empresarial'),
(2, 2, 'Case description 2', 'Direito Civil');

INSERT INTO case_updates (case_id, update_description)
VALUES 
(1, 'Case update 1'),
(2, 'Case update 2');
```
