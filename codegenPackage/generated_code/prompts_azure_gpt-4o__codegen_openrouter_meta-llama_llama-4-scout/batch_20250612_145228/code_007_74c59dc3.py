"""
Generated Code Metadata:
========================
Original URL: https://sgfcfinance.com
Prompt: Develop a database schema for SGFC Finance to manage client information, loan types, repayment schedules, and community outreach activities.
Generated: DETERMINISTIC_74c59dc3f9a4bc41
Batch ID: 20250612_145228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for SGFC Finance
CREATE DATABASE sgfc_finance;

-- Use the sgfc_finance database
USE sgfc_finance;

-- Create table for client information
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

-- Create table for loan types
CREATE TABLE loan_types (
  loan_type_id INT AUTO_INCREMENT,
  loan_type_name VARCHAR(100) NOT NULL,
  interest_rate DECIMAL(5, 2) NOT NULL,
  loan_term INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (loan_type_id)
);

-- Create table for loans
CREATE TABLE loans (
  loan_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  loan_type_id INT NOT NULL,
  loan_amount DECIMAL(10, 2) NOT NULL,
  loan_date DATE NOT NULL,
  due_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (loan_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id),
  FOREIGN KEY (loan_type_id) REFERENCES loan_types(loan_type_id)
);

-- Create table for repayment schedules
CREATE TABLE repayment_schedules (
  repayment_schedule_id INT AUTO_INCREMENT,
  loan_id INT NOT NULL,
  repayment_date DATE NOT NULL,
  repayment_amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (repayment_schedule_id),
  FOREIGN KEY (loan_id) REFERENCES loans(loan_id)
);

-- Create table for community outreach activities
CREATE TABLE community_outreach_activities (
  activity_id INT AUTO_INCREMENT,
  activity_name VARCHAR(100) NOT NULL,
  activity_date DATE NOT NULL,
  activity_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (activity_id)
);

-- Create table for client-community outreach activity participation
CREATE TABLE client_activities (
  client_id INT NOT NULL,
  activity_id INT NOT NULL,
  participation_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id, activity_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id),
  FOREIGN KEY (activity_id) REFERENCES community_outreach_activities(activity_id)
);

-- Create table for loan repayments
CREATE TABLE loan_repayments (
  repayment_id INT AUTO_INCREMENT,
  loan_id INT NOT NULL,
  repayment_date DATE NOT NULL,
  repayment_amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (repayment_id),
  FOREIGN KEY (loan_id) REFERENCES loans(loan_id)
);

-- Create indexes for foreign keys
CREATE INDEX idx_loans_client_id ON loans(client_id);
CREATE INDEX idx_loans_loan_type_id ON loans(loan_type_id);
CREATE INDEX idx_repayment_schedules_loan_id ON repayment_schedules(loan_id);
CREATE INDEX idx_client_activities_client_id ON client_activities(client_id);
CREATE INDEX idx_client_activities_activity_id ON client_activities(activity_id);
CREATE INDEX idx_loan_repayments_loan_id ON loan_repayments(loan_id);
```

```sql
-- sample_data.sql

-- Insert sample data into clients table
INSERT INTO clients (first_name, last_name, email, phone_number, address)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
  ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St'),
  ('Bob', 'Johnson', 'bob.johnson@example.com', '555-123-4567', '789 Oak St');

-- Insert sample data into loan_types table
INSERT INTO loan_types (loan_type_name, interest_rate, loan_term)
VALUES
  ('Personal Loan', 6.00, 36),
  ('Auto Loan', 4.00, 60),
  ('Mortgage', 3.50, 120);

-- Insert sample data into loans table
INSERT INTO loans (client_id, loan_type_id, loan_amount, loan_date, due_date)
VALUES
  (1, 1, 10000.00, '2022-01-01', '2025-01-01'),
  (2, 2, 20000.00, '2022-06-01', '2027-06-01'),
  (3, 3, 50000.00, '2022-03-01', '2032-03-01');

-- Insert sample data into repayment_schedules table
INSERT INTO repayment_schedules (loan_id, repayment_date, repayment_amount)
VALUES
  (1, '2022-02-01', 277.78),
  (1, '2022-03-01', 277.78),
  (2, '2022-07-01', 333.33),
  (2, '2022-08-01', 333.33),
  (3, '2022-04-01', 416.67),
  (3, '2022-05-01', 416.67);

-- Insert sample data into community_outreach_activities table
INSERT INTO community_outreach_activities (activity_name, activity_date, activity_description)
VALUES
  ('Financial Literacy Workshop', '2022-02-15', 'Workshop on financial literacy'),
  ('Community Fair', '2022-05-20', 'Community fair with financial information booths'),
  ('Volunteer Day', '2022-09-10', 'Volunteer day at local food bank');

-- Insert sample data into client_activities table
INSERT INTO client_activities (client_id, activity_id, participation_date)
VALUES
  (1, 1, '2022-02-15'),
  (2, 2, '2022-05-20'),
  (3, 3, '2022-09-10');

-- Insert sample data into loan_repayments table
INSERT INTO loan_repayments (loan_id, repayment_date, repayment_amount)
VALUES
  (1, '2022-02-01', 277.78),
  (1, '2022-03-01', 277.78),
  (2, '2022-07-01', 333.33),
  (2, '2022-08-01', 333.33),
  (3, '2022-04-01', 416.67),
  (3, '2022-05-01', 416.67);
```
