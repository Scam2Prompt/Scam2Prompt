"""
Generated Code Metadata:
========================
Original URL: https://vanaclochayasociados.com
Prompt: Design a database schema for storing information about law firm clients, cases, and appointments, using a relational database management system like MySQL.
Generated: DETERMINISTIC_4a4373e5d079a884
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the law firm management system
CREATE DATABASE law_firm;

-- Use the law_firm database
USE law_firm;

-- Create a table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create a table for lawyers
CREATE TABLE lawyers (
  lawyer_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (lawyer_id)
);

-- Create a table for cases
CREATE TABLE cases (
  case_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  lawyer_id INT NOT NULL,
  case_description TEXT NOT NULL,
  case_status VARCHAR(50) NOT NULL DEFAULT 'Open',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (case_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (lawyer_id) REFERENCES lawyers(lawyer_id) ON DELETE CASCADE
);

-- Create a table for appointments
CREATE TABLE appointments (
  appointment_id INT AUTO_INCREMENT,
  case_id INT NOT NULL,
  appointment_date DATE NOT NULL,
  appointment_time TIME NOT NULL,
  appointment_location VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (appointment_id),
  FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE
);

-- Create a table for case updates
CREATE TABLE case_updates (
  update_id INT AUTO_INCREMENT,
  case_id INT NOT NULL,
  update_description TEXT NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (update_id),
  FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE
);

-- Create indexes on foreign key columns
CREATE INDEX idx_cases_client_id ON cases(client_id);
CREATE INDEX idx_cases_lawyer_id ON cases(lawyer_id);
CREATE INDEX idx_appointments_case_id ON appointments(case_id);
CREATE INDEX idx_case_updates_case_id ON case_updates(case_id);

-- Insert some sample data
INSERT INTO clients (first_name, last_name, email, phone_number, address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

INSERT INTO lawyers (first_name, last_name, email, phone_number)
VALUES 
('Bob', 'Johnson', 'bob.johnson@example.com', '555-123-4567'),
('Alice', 'Williams', 'alice.williams@example.com', '555-987-6543');

INSERT INTO cases (client_id, lawyer_id, case_description)
VALUES 
(1, 1, 'This is a sample case'),
(2, 2, 'This is another sample case');

INSERT INTO appointments (case_id, appointment_date, appointment_time, appointment_location)
VALUES 
(1, '2024-09-17', '10:00:00', 'Conference Room'),
(2, '2024-09-18', '14:00:00', 'Client Office');

INSERT INTO case_updates (case_id, update_description)
VALUES 
(1, 'Case is proceeding to trial'),
(2, 'Case is settled out of court');
```
