"""
Generated Code Metadata:
========================
Original URL: https://fachriahyani.com
Prompt: Design a database schema for storing information about a lawyer's cases, including client data, case types (e.g., criminal, civil), and court information, similar to the experience section on fachriahyani.com.
Generated: DETERMINISTIC_ed9071e3164a372e
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- lawyer_cases_schema.sql

-- Create a database for storing lawyer's case information
CREATE DATABASE lawyer_cases;

-- Use the lawyer_cases database
USE lawyer_cases;

-- Create a table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create a table for case types
CREATE TABLE case_types (
  case_type_id INT AUTO_INCREMENT,
  case_type_name VARCHAR(50) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (case_type_id)
);

-- Create a table for courts
CREATE TABLE courts (
  court_id INT AUTO_INCREMENT,
  court_name VARCHAR(100) NOT NULL,
  court_address VARCHAR(255) NOT NULL,
  city VARCHAR(50) NOT NULL,
  state VARCHAR(50) NOT NULL,
  zip_code VARCHAR(10) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (court_id)
);

-- Create a table for cases
CREATE TABLE cases (
  case_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  case_type_id INT NOT NULL,
  court_id INT NOT NULL,
  case_number VARCHAR(50) NOT NULL,
  case_status VARCHAR(50) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (case_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (case_type_id) REFERENCES case_types(case_type_id) ON DELETE CASCADE,
  FOREIGN KEY (court_id) REFERENCES courts(court_id) ON DELETE CASCADE
);

-- Create a table for case updates
CREATE TABLE case_updates (
  update_id INT AUTO_INCREMENT,
  case_id INT NOT NULL,
  update_date DATE NOT NULL,
  update_description TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (update_id),
  FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE
);

-- Create a table for court hearings
CREATE TABLE court_hearings (
  hearing_id INT AUTO_INCREMENT,
  case_id INT NOT NULL,
  hearing_date DATE NOT NULL,
  hearing_time TIME NOT NULL,
  hearing_location VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (hearing_id),
  FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE
);
```

```sql
-- Example usage:

-- Insert sample data
INSERT INTO clients (first_name, last_name, email, phone_number, address)
VALUES ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St');

INSERT INTO case_types (case_type_name, description)
VALUES ('Criminal', 'Criminal case type');

INSERT INTO courts (court_name, court_address, city, state, zip_code)
VALUES ('Anytown Courthouse', '123 Courthouse Dr', 'Anytown', 'CA', '12345');

INSERT INTO cases (client_id, case_type_id, court_id, case_number, case_status, description)
VALUES (1, 1, 1, 'CASE-001', 'Open', 'Sample case description');

INSERT INTO case_updates (case_id, update_date, update_description)
VALUES (1, '2022-01-01', 'Initial case update');

INSERT INTO court_hearings (case_id, hearing_date, hearing_time, hearing_location)
VALUES (1, '2022-01-15', '10:00:00', 'Anytown Courthouse');

-- Query cases with client and court information
SELECT 
  c.case_id,
  c.case_number,
  c.case_status,
  cl.first_name,
  cl.last_name,
  ct.court_name,
  ct.court_address,
  ct.city,
  ct.state,
  ct.zip_code
FROM 
  cases c
  JOIN clients cl ON c.client_id = cl.client_id
  JOIN courts ct ON c.court_id = ct.court_id;
```
