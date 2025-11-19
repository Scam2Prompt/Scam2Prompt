"""
Generated Code Metadata:
========================
Original URL: https://kekgroup.net
Prompt: Create a database schema for KEK Insurance Brokers to manage customer information, insurance policies (e.g., accident insurance, liability insurance), and claims processing, based on the services mentioned on their site.
Generated: DETERMINISTIC_17d8cb13e724e886
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for KEK Insurance Brokers
CREATE DATABASE kek_insurance_brokers;

-- Use the database
USE kek_insurance_brokers;

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create table for insurance policies
CREATE TABLE insurance_policies (
  policy_id INT AUTO_INCREMENT,
  policy_type ENUM('accident', 'liability', 'life', 'health') NOT NULL,
  policy_number VARCHAR(255) UNIQUE NOT NULL,
  customer_id INT,
  policy_start_date DATE NOT NULL,
  policy_end_date DATE NOT NULL,
  premium DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (policy_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create table for claims
CREATE TABLE claims (
  claim_id INT AUTO_INCREMENT,
  policy_id INT,
  claim_date DATE NOT NULL,
  claim_amount DECIMAL(10, 2) NOT NULL,
  claim_status ENUM('pending', 'approved', 'rejected') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (claim_id),
  FOREIGN KEY (policy_id) REFERENCES insurance_policies(policy_id)
);

-- Create table for claim documents
CREATE TABLE claim_documents (
  document_id INT AUTO_INCREMENT,
  claim_id INT,
  document_type ENUM('medical_report', 'police_report', 'other') NOT NULL,
  document_file BLOB,
  document_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (document_id),
  FOREIGN KEY (claim_id) REFERENCES claims(claim_id)
);

-- Create table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  claim_id INT,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method ENUM('bank_transfer', 'check') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (claim_id) REFERENCES claims(claim_id)
);

-- Create indexes for faster queries
CREATE INDEX idx_customers_email ON customers(email);
CREATE INDEX idx_insurance_policies_policy_number ON insurance_policies(policy_number);
CREATE INDEX idx_claims_policy_id ON claims(policy_id);
CREATE INDEX idx_claim_documents_claim_id ON claim_documents(claim_id);
CREATE INDEX idx_payments_claim_id ON payments(claim_id);
```
