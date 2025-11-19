"""
Generated Code Metadata:
========================
Original URL: https://arbitum.cz
Prompt: Create a database schema for managing client accounts, including tracking insolvency cases, tax filings, and debt restructuring plans, inspired by Arbitum Consulting's services.
Generated: DETERMINISTIC_d0efb8dd6fb3c7aa
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for client accounts
CREATE DATABASE client_accounts;

-- Use the client_accounts database
USE client_accounts;

-- Create a table for clients
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

-- Create a table for insolvency cases
CREATE TABLE insolvency_cases (
  id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  case_number VARCHAR(50) NOT NULL,
  case_type VARCHAR(100) NOT NULL,
  filing_date DATE,
  status VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- Create a table for tax filings
CREATE TABLE tax_filings (
  id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  filing_year INT NOT NULL,
  filing_date DATE,
  tax_status VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- Create a table for debt restructuring plans
CREATE TABLE debt_restructuring_plans (
  id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  plan_name VARCHAR(255) NOT NULL,
  plan_type VARCHAR(100) NOT NULL,
  start_date DATE,
  end_date DATE,
  status VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- Create a table for payments
CREATE TABLE payments (
  id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- Create a table for case notes
CREATE TABLE case_notes (
  id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  case_id INT,
  note_text TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE,
  FOREIGN KEY (case_id) REFERENCES insolvency_cases(id) ON DELETE SET NULL
);

-- Create indexes for faster queries
CREATE INDEX idx_client_id ON insolvency_cases(client_id);
CREATE INDEX idx_client_id ON tax_filings(client_id);
CREATE INDEX idx_client_id ON debt_restructuring_plans(client_id);
CREATE INDEX idx_client_id ON payments(client_id);
CREATE INDEX idx_case_id ON case_notes(case_id);

-- Insert sample data for testing
INSERT INTO clients (name, email, phone_number, address)
VALUES 
('John Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

INSERT INTO insolvency_cases (client_id, case_number, case_type, filing_date, status)
VALUES 
(1, 'CASE-001', 'Chapter 7', '2020-01-01', 'Open'),
(2, 'CASE-002', 'Chapter 13', '2020-06-01', 'In Progress');

INSERT INTO tax_filings (client_id, filing_year, filing_date, tax_status)
VALUES 
(1, 2020, '2020-04-15', 'Filed'),
(2, 2020, '2020-10-15', 'Pending');

INSERT INTO debt_restructuring_plans (client_id, plan_name, plan_type, start_date, end_date, status)
VALUES 
(1, 'Plan A', 'Debt Consolidation', '2020-03-01', '2020-09-01', 'Completed'),
(2, 'Plan B', 'Debt Settlement', '2020-09-01', '2021-03-01', 'In Progress');

INSERT INTO payments (client_id, payment_date, payment_amount, payment_method)
VALUES 
(1, '2020-05-01', 1000.00, 'Credit Card'),
(2, '2020-11-01', 500.00, 'Check');

INSERT INTO case_notes (client_id, case_id, note_text)
VALUES 
(1, 1, 'Client filed for Chapter 7 bankruptcy'),
(2, 2, 'Client is making monthly payments');
```
