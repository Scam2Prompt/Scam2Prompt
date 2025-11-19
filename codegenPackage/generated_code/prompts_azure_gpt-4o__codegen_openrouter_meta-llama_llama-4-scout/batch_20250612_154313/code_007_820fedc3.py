"""
Generated Code Metadata:
========================
Original URL: https://ircmhealth.com
Prompt: Design a database schema for a medical billing system that supports revenue cycle management and AR follow-up, inspired by ircmhealth.com's offerings.
Generated: DETERMINISTIC_820fedc3f8d784b4
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- medical_billing_schema.sql

-- Create database schema for medical billing system
CREATE DATABASE medical_billing;

-- Use medical_billing database
USE medical_billing;

-- Create patients table
CREATE TABLE patients (
  patient_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  date_of_birth DATE NOT NULL,
  email VARCHAR(100) UNIQUE,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  city VARCHAR(100),
  state VARCHAR(100),
  zip_code VARCHAR(10),
  PRIMARY KEY (patient_id)
);

-- Create providers table
CREATE TABLE providers (
  provider_id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  npi VARCHAR(20) UNIQUE,
  address VARCHAR(255),
  city VARCHAR(100),
  state VARCHAR(100),
  zip_code VARCHAR(10),
  PRIMARY KEY (provider_id)
);

-- Create insurance_companies table
CREATE TABLE insurance_companies (
  insurance_company_id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  address VARCHAR(255),
  city VARCHAR(100),
  state VARCHAR(100),
  zip_code VARCHAR(10),
  PRIMARY KEY (insurance_company_id)
);

-- Create patient_insurance table
CREATE TABLE patient_insurance (
  patient_id INT NOT NULL,
  insurance_company_id INT NOT NULL,
  policy_number VARCHAR(50) NOT NULL,
  coverage_start_date DATE,
  coverage_end_date DATE,
  PRIMARY KEY (patient_id, insurance_company_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
  FOREIGN KEY (insurance_company_id) REFERENCES insurance_companies(insurance_company_id)
);

-- Create claims table
CREATE TABLE claims (
  claim_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  provider_id INT NOT NULL,
  insurance_company_id INT NOT NULL,
  claim_date DATE NOT NULL,
  claim_amount DECIMAL(10, 2) NOT NULL,
  status VARCHAR(50) NOT NULL,
  PRIMARY KEY (claim_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
  FOREIGN KEY (provider_id) REFERENCES providers(provider_id),
  FOREIGN KEY (insurance_company_id) REFERENCES insurance_companies(insurance_company_id)
);

-- Create payments table
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  claim_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(50) NOT NULL,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (claim_id) REFERENCES claims(claim_id)
);

-- Create accounts_receivable table
CREATE TABLE accounts_receivable (
  ar_id INT AUTO_INCREMENT,
  claim_id INT NOT NULL,
  balance DECIMAL(10, 2) NOT NULL,
  last_follow_up_date DATE,
  next_follow_up_date DATE,
  PRIMARY KEY (ar_id),
  FOREIGN KEY (claim_id) REFERENCES claims(claim_id)
);

-- Create follow_up_log table
CREATE TABLE follow_up_log (
  log_id INT AUTO_INCREMENT,
  ar_id INT NOT NULL,
  follow_up_date DATE NOT NULL,
  notes VARCHAR(255),
  PRIMARY KEY (log_id),
  FOREIGN KEY (ar_id) REFERENCES accounts_receivable(ar_id)
);

-- Create users table
CREATE TABLE users (
  user_id INT AUTO_INCREMENT,
  username VARCHAR(50) NOT NULL,
  password VARCHAR(255) NOT NULL,
  role VARCHAR(50) NOT NULL,
  PRIMARY KEY (user_id)
);

-- Create permissions table
CREATE TABLE permissions (
  permission_id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  claim_id INT,
  ar_id INT,
  permission VARCHAR(50) NOT NULL,
  PRIMARY KEY (permission_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  FOREIGN KEY (claim_id) REFERENCES claims(claim_id),
  FOREIGN KEY (ar_id) REFERENCES accounts_receivable(ar_id)
);
```

```sql
-- Example data insertion
INSERT INTO patients (first_name, last_name, date_of_birth, email, phone_number, address, city, state, zip_code)
VALUES ('John', 'Doe', '1990-01-01', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345');

INSERT INTO providers (name, npi, address, city, state, zip_code)
VALUES ('Anytown Medical Group', '1234567890', '456 Elm St', 'Anytown', 'CA', '12345');

INSERT INTO insurance_companies (name, address, city, state, zip_code)
VALUES ('Blue Cross Blue Shield', '789 Oak St', 'Anytown', 'CA', '12345');

INSERT INTO patient_insurance (patient_id, insurance_company_id, policy_number, coverage_start_date, coverage_end_date)
VALUES (1, 1, '1234567890', '2020-01-01', '2021-12-31');

INSERT INTO claims (patient_id, provider_id, insurance_company_id, claim_date, claim_amount, status)
VALUES (1, 1, 1, '2020-02-01', 100.00, 'Pending');

INSERT INTO payments (claim_id, payment_date, payment_amount, payment_method)
VALUES (1, '2020-03-01', 50.00, 'Check');

INSERT INTO accounts_receivable (claim_id, balance, last_follow_up_date, next_follow_up_date)
VALUES (1, 50.00, '2020-03-01', '2020-04-01');

INSERT INTO follow_up_log (ar_id, follow_up_date, notes)
VALUES (1, '2020-04-01', 'Follow-up with patient');

INSERT INTO users (username, password, role)
VALUES ('admin', 'password', 'Admin');

INSERT INTO permissions (user_id, claim_id, ar_id, permission)
VALUES (1, 1, 1, 'View');
```
