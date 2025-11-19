"""
Generated Code Metadata:
========================
Original URL: https://mail.gtempus.com
Prompt: Write a SQL database schema for Grupo de Seguros Tempus to manage customer data, insurance policies, claims, and advisor commissions.
Generated: DETERMINISTIC_d25e528a954a4a1b
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Grupo de Seguros Tempus
CREATE DATABASE grupo_seguros_tempus;

-- Use the database
USE grupo_seguros_tempus;

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
  customer_id INT NOT NULL,
  policy_type VARCHAR(100) NOT NULL,
  policy_number VARCHAR(255) UNIQUE NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  premium DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (policy_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create table for claims
CREATE TABLE claims (
  claim_id INT AUTO_INCREMENT,
  policy_id INT NOT NULL,
  claim_date DATE NOT NULL,
  claim_amount DECIMAL(10, 2) NOT NULL,
  claim_status VARCHAR(50) NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (claim_id),
  FOREIGN KEY (policy_id) REFERENCES insurance_policies(policy_id)
);

-- Create table for advisors
CREATE TABLE advisors (
  advisor_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (advisor_id)
);

-- Create table for advisor commissions
CREATE TABLE advisor_commissions (
  commission_id INT AUTO_INCREMENT,
  advisor_id INT NOT NULL,
  policy_id INT NOT NULL,
  commission_amount DECIMAL(10, 2) NOT NULL,
  commission_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (commission_id),
  FOREIGN KEY (advisor_id) REFERENCES advisors(advisor_id),
  FOREIGN KEY (policy_id) REFERENCES insurance_policies(policy_id)
);

-- Create table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  policy_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (policy_id) REFERENCES insurance_policies(policy_id)
);

-- Create indexes for faster queries
CREATE INDEX idx_customers_email ON customers(email);
CREATE INDEX idx_insurance_policies_policy_number ON insurance_policies(policy_number);
CREATE INDEX idx_claims_policy_id ON claims(policy_id);
CREATE INDEX idx_advisor_commissions_advisor_id ON advisor_commissions(advisor_id);
CREATE INDEX idx_advisor_commissions_policy_id ON advisor_commissions(policy_id);
```
