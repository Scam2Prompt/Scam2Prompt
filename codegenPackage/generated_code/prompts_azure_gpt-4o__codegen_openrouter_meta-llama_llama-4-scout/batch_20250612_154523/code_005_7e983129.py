"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: Create a SQL database schema for managing accounting data for NGOs, based on the "Contabilidad de ONG" course offered by AulaContable.
Generated: DETERMINISTIC_7e983129f742e30b
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for NGO accounting
CREATE DATABASE ngo_accounting;

-- Use the database
USE ngo_accounting;

-- Create table for accounts
CREATE TABLE accounts (
  id INT AUTO_INCREMENT,
  account_number VARCHAR(255) NOT NULL,
  account_name VARCHAR(255) NOT NULL,
  account_type ENUM('asset', 'liability', 'equity', 'revenue', 'expense') NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (account_number)
);

-- Create table for transactions
CREATE TABLE transactions (
  id INT AUTO_INCREMENT,
  account_id INT NOT NULL,
  transaction_date DATE NOT NULL,
  transaction_type ENUM('debit', 'credit') NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (account_id) REFERENCES accounts(id) ON DELETE CASCADE
);

-- Create table for donors
CREATE TABLE donors (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20),
  address TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for donations
CREATE TABLE donations (
  id INT AUTO_INCREMENT,
  donor_id INT NOT NULL,
  transaction_id INT,
  donation_date DATE NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (donor_id) REFERENCES donors(id) ON DELETE CASCADE,
  FOREIGN KEY (transaction_id) REFERENCES transactions(id) ON DELETE SET NULL
);

-- Create table for expenses
CREATE TABLE expenses (
  id INT AUTO_INCREMENT,
  account_id INT NOT NULL,
  expense_date DATE NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (account_id) REFERENCES accounts(id) ON DELETE CASCADE
);

-- Create table for projects
CREATE TABLE projects (
  id INT AUTO_INCREMENT,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  start_date DATE NOT NULL,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for project expenses
CREATE TABLE project_expenses (
  id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  expense_id INT NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE,
  FOREIGN KEY (expense_id) REFERENCES expenses(id) ON DELETE CASCADE
);

-- Create table for financial reports
CREATE TABLE financial_reports (
  id INT AUTO_INCREMENT,
  report_date DATE NOT NULL,
  report_type ENUM('balance_sheet', 'income_statement', 'cash_flow') NOT NULL,
  report_data TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);
```
