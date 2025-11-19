"""
Generated Code Metadata:
========================
Original URL: https://johnbarrybaker.com
Prompt: Design a database schema for storing client information and accident details for a personal injury law firm, ensuring it includes fields for various accident types and client contact methods.
Generated: DETERMINISTIC_769a9dba55fc72dc
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for the personal injury law firm
CREATE DATABASE personal_injury_law_firm;

-- Use the database
USE personal_injury_law_firm;

-- Create a table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  city VARCHAR(100),
  state VARCHAR(100),
  zip_code VARCHAR(10),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create a table for accident types
CREATE TABLE accident_types (
  accident_type_id INT AUTO_INCREMENT,
  accident_type VARCHAR(100) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (accident_type_id)
);

-- Create a table for accidents
CREATE TABLE accidents (
  accident_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  accident_type_id INT NOT NULL,
  accident_date DATE NOT NULL,
  accident_location VARCHAR(255) NOT NULL,
  description TEXT,
  injuries TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (accident_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (accident_type_id) REFERENCES accident_types(accident_type_id) ON DELETE RESTRICT
);

-- Create a table for client contact methods
CREATE TABLE client_contact_methods (
  contact_method_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  contact_method VARCHAR(100) NOT NULL,
  contact_value VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (contact_method_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create a table for accident evidence
CREATE TABLE accident_evidence (
  evidence_id INT AUTO_INCREMENT,
  accident_id INT NOT NULL,
  evidence_type VARCHAR(100) NOT NULL,
  evidence_description TEXT,
  evidence_file BLOB,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (evidence_id),
  FOREIGN KEY (accident_id) REFERENCES accidents(accident_id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_clients_email ON clients(email);
CREATE INDEX idx_accidents_client_id ON accidents(client_id);
CREATE INDEX idx_accidents_accident_type_id ON accidents(accident_type_id);

-- Insert sample data
INSERT INTO clients (first_name, last_name, email, phone_number, address, city, state, zip_code)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St', 'Othertown', 'NY', '67890');

INSERT INTO accident_types (accident_type, description)
VALUES 
('Car Accident', 'A collision involving one or more vehicles'),
('Slip and Fall', 'A fall due to a slippery or uneven surface'),
('Medical Malpractice', 'A medical error or negligence');

INSERT INTO accidents (client_id, accident_type_id, accident_date, accident_location, description, injuries)
VALUES 
(1, 1, '2022-01-01', 'Main St and Elm St', 'A car ran a red light and hit my car', 'Broken arm and leg'),
(2, 2, '2022-06-01', 'A grocery store', 'I slipped on a wet floor and fell', 'Concussion and bruises');

INSERT INTO client_contact_methods (client_id, contact_method, contact_value)
VALUES 
(1, 'Email', 'john.doe@example.com'),
(1, 'Phone', '123-456-7890'),
(2, 'Email', 'jane.smith@example.com');

INSERT INTO accident_evidence (accident_id, evidence_type, evidence_description, evidence_file)
VALUES 
(1, 'Police Report', 'A report from the police department', NULL),
(1, 'Medical Records', 'Records from the hospital', NULL);
```
