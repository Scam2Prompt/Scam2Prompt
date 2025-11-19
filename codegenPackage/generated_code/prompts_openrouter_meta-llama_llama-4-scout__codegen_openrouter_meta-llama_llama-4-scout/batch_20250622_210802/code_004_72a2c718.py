"""
Generated Code Metadata:
========================
Original URL: https://cooperativacooprometa.com
Prompt: Design a basic database schema for storing client information, credits, and educational programs for a cooperative like Cooprometa.
Generated: DETERMINISTIC_72a2c718827b14fb
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Cooprometa cooperative
CREATE DATABASE cooprometa;

-- Use the cooprometa database
USE cooprometa;

-- Create table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create table for credits
CREATE TABLE credits (
  credit_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  credit_amount DECIMAL(10, 2) NOT NULL,
  credit_date DATE NOT NULL,
  description VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (credit_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create table for educational programs
CREATE TABLE educational_programs (
  program_id INT AUTO_INCREMENT,
  program_name VARCHAR(255) NOT NULL,
  program_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (program_id)
);

-- Create table for client educational program enrollments
CREATE TABLE client_programs (
  client_id INT NOT NULL,
  program_id INT NOT NULL,
  enrollment_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id, program_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (program_id) REFERENCES educational_programs(program_id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_clients_email ON clients(email);
CREATE INDEX idx_credits_client_id ON credits(client_id);
CREATE INDEX idx_client_programs_client_id ON client_programs(client_id);
CREATE INDEX idx_client_programs_program_id ON client_programs(program_id);
```

```sql
-- example_data.sql

-- Insert example data into the cooprometa database
INSERT INTO clients (first_name, last_name, email, phone_number, address)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
  ('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St');

INSERT INTO credits (client_id, credit_amount, credit_date, description)
VALUES
  (1, 100.00, '2022-01-01', 'Initial credit'),
  (1, 50.00, '2022-02-01', 'Additional credit'),
  (2, 200.00, '2022-03-01', 'Initial credit');

INSERT INTO educational_programs (program_name, program_description)
VALUES
  ('Program 1', 'This is the first educational program'),
  ('Program 2', 'This is the second educational program');

INSERT INTO client_programs (client_id, program_id, enrollment_date)
VALUES
  (1, 1, '2022-01-15'),
  (1, 2, '2022-02-15'),
  (2, 1, '2022-03-15');
```
