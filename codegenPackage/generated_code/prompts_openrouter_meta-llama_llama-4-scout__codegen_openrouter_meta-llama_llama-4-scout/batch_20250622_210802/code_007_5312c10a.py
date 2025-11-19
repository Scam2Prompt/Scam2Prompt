"""
Generated Code Metadata:
========================
Original URL: https://lkinc.co.za
Prompt: Design a database schema to store financial data for a company, inspired by Lund & Kieck's accounting and bookkeeping services.
Generated: DETERMINISTIC_5312c10afb404ee3
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- financial_database_schema.sql

-- Create database
CREATE DATABASE financial_database;

-- Use database
USE financial_database;

-- Create table for accounts
CREATE TABLE accounts (
  account_id INT AUTO_INCREMENT,
  account_name VARCHAR(255) NOT NULL,
  account_type ENUM('asset', 'liability', 'equity', 'revenue', 'expense') NOT NULL,
  balance DECIMAL(10, 2) DEFAULT 0.00,
  PRIMARY KEY (account_id)
);

-- Create table for transactions
CREATE TABLE transactions (
  transaction_id INT AUTO_INCREMENT,
  account_id INT NOT NULL,
  transaction_date DATE NOT NULL,
  transaction_type ENUM('debit', 'credit') NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  description VARCHAR(255),
  PRIMARY KEY (transaction_id),
  FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  customer_name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  zip_code VARCHAR(20) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  PRIMARY KEY (customer_id)
);

-- Create table for invoices
CREATE TABLE invoices (
  invoice_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  invoice_date DATE NOT NULL,
  due_date DATE NOT NULL,
  total DECIMAL(10, 2) NOT NULL,
  paid DECIMAL(10, 2) DEFAULT 0.00,
  status ENUM('pending', 'paid', 'overdue') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (invoice_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create table for invoice items
CREATE TABLE invoice_items (
  item_id INT AUTO_INCREMENT,
  invoice_id INT NOT NULL,
  account_id INT NOT NULL,
  item_description VARCHAR(255) NOT NULL,
  quantity INT NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  total DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (item_id),
  FOREIGN KEY (invoice_id) REFERENCES invoices(invoice_id),
  FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

-- Create table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  invoice_id INT NOT NULL,
  payment_date DATE NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  payment_method ENUM('cash', 'bank_transfer', 'credit_card') NOT NULL,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (invoice_id) REFERENCES invoices(invoice_id)
);

-- Create indexes
CREATE INDEX idx_accounts_account_name ON accounts (account_name);
CREATE INDEX idx_transactions_account_id ON transactions (account_id);
CREATE INDEX idx_invoices_customer_id ON invoices (customer_id);
CREATE INDEX idx_invoice_items_invoice_id ON invoice_items (invoice_id);
CREATE INDEX idx_payments_invoice_id ON payments (invoice_id);

-- Insert sample data
INSERT INTO accounts (account_name, account_type, balance)
VALUES
  ('Cash', 'asset', 1000.00),
  ('Accounts Receivable', 'asset', 5000.00),
  ('Accounts Payable', 'liability', 2000.00),
  ('Revenue', 'revenue', 0.00),
  ('Expense', 'expense', 0.00);

INSERT INTO customers (customer_name, address, city, state, zip_code, email, phone_number)
VALUES
  ('John Doe', '123 Main St', 'Anytown', 'CA', '12345', 'john.doe@example.com', '555-555-5555'),
  ('Jane Smith', '456 Elm St', 'Othertown', 'NY', '67890', 'jane.smith@example.com', '555-123-4567');

INSERT INTO invoices (customer_id, invoice_date, due_date, total)
VALUES
  (1, '2022-01-01', '2022-01-31', 1000.00),
  (2, '2022-02-01', '2022-02-28', 2000.00);

INSERT INTO invoice_items (invoice_id, account_id, item_description, quantity, unit_price, total)
VALUES
  (1, 1, 'Consulting services', 10, 100.00, 1000.00),
  (2, 2, 'Accounting services', 20, 100.00, 2000.00);

INSERT INTO transactions (account_id, transaction_date, transaction_type, amount, description)
VALUES
  (1, '2022-01-01', 'debit', 1000.00, 'Initial deposit'),
  (2, '2022-01-15', 'credit', 5000.00, 'Customer payment');

INSERT INTO payments (invoice_id, payment_date, amount, payment_method)
VALUES
  (1, '2022-01-20', 1000.00, 'bank_transfer'),
  (2, '2022-02-20', 2000.00, 'cash');
```
