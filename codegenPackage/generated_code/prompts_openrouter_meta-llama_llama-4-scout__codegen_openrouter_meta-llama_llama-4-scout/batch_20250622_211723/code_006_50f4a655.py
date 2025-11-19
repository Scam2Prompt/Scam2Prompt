"""
Generated Code Metadata:
========================
Original URL: https://genesisicu.com
Prompt: Design a database schema for storing customer information and financial data for a credit union, considering the various services offered by Genesis Investment Credit Union.
Generated: DETERMINISTIC_50f4a655f10e29a9
Batch ID: 20250622_211723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Genesis Investment Credit Union
CREATE DATABASE genesis_credit_union;

-- Use the database
USE genesis_credit_union;

-- Create table for customers
CREATE TABLE customers (
  `customer_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(50) NOT NULL,
  `last_name` VARCHAR(50) NOT NULL,
  `date_of_birth` DATE NOT NULL,
  `email` VARCHAR(100) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20) NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`customer_id`)
);

-- Create table for accounts
CREATE TABLE accounts (
  `account_id` INT AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `account_type` ENUM('checking', 'savings', 'loan', 'credit_card') NOT NULL,
  `account_number` VARCHAR(20) UNIQUE NOT NULL,
  `balance` DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`account_id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`customer_id`)
);

-- Create table for transactions
CREATE TABLE transactions (
  `transaction_id` INT AUTO_INCREMENT,
  `account_id` INT NOT NULL,
  `transaction_date` DATE NOT NULL,
  `transaction_type` ENUM('deposit', 'withdrawal', 'transfer') NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `description` VARCHAR(255),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`transaction_id`),
  FOREIGN KEY (`account_id`) REFERENCES accounts(`account_id`)
);

-- Create table for loans
CREATE TABLE loans (
  `loan_id` INT AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `loan_type` ENUM('personal', 'mortgage', 'auto') NOT NULL,
  `loan_amount` DECIMAL(10, 2) NOT NULL,
  `interest_rate` DECIMAL(5, 2) NOT NULL,
  `loan_term` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`loan_id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`customer_id`)
);

-- Create table for credit cards
CREATE TABLE credit_cards (
  `credit_card_id` INT AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `card_number` VARCHAR(20) UNIQUE NOT NULL,
  `expiration_date` DATE NOT NULL,
  `credit_limit` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`credit_card_id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`customer_id`)
);

-- Create table for investments
CREATE TABLE investments (
  `investment_id` INT AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `investment_type` ENUM('stock', 'bond', 'mutual_fund') NOT NULL,
  `investment_amount` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`investment_id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`customer_id`)
);

-- Create table for payments
CREATE TABLE payments (
  `payment_id` INT AUTO_INCREMENT,
  `account_id` INT,
  `loan_id` INT,
  `credit_card_id` INT,
  `payment_date` DATE NOT NULL,
  `payment_amount` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`payment_id`),
  FOREIGN KEY (`account_id`) REFERENCES accounts(`account_id`),
  FOREIGN KEY (`loan_id`) REFERENCES loans(`loan_id`),
  FOREIGN KEY (`credit_card_id`) REFERENCES credit_cards(`credit_card_id`)
);

-- Create indexes on foreign key columns
CREATE INDEX idx_accounts_customer_id ON accounts (customer_id);
CREATE INDEX idx_transactions_account_id ON transactions (account_id);
CREATE INDEX idx_loans_customer_id ON loans (customer_id);
CREATE INDEX idx_credit_cards_customer_id ON credit_cards (customer_id);
CREATE INDEX idx_investments_customer_id ON investments (customer_id);
CREATE INDEX idx_payments_account_id ON payments (account_id);
CREATE INDEX idx_payments_loan_id ON payments (loan_id);
CREATE INDEX idx_payments_credit_card_id ON payments (credit_card_id);
```

```sql
-- sample_data.sql

-- Insert sample data into customers table
INSERT INTO customers (first_name, last_name, date_of_birth, email, phone_number, address)
VALUES
  ('John', 'Doe', '1990-01-01', 'john.doe@example.com', '123-456-7890', '123 Main St'),
  ('Jane', 'Doe', '1995-06-01', 'jane.doe@example.com', '987-654-3210', '456 Elm St');

-- Insert sample data into accounts table
INSERT INTO accounts (customer_id, account_type, account_number, balance)
VALUES
  (1, 'checking', '1234567890', 1000.00),
  (1, 'savings', '9876543210', 5000.00),
  (2, 'checking', '1111111111', 2000.00);

-- Insert sample data into transactions table
INSERT INTO transactions (account_id, transaction_date, transaction_type, amount, description)
VALUES
  (1, '2022-01-01', 'deposit', 500.00, 'Payroll deposit'),
  (1, '2022-01-05', 'withdrawal', 200.00, 'ATM withdrawal'),
  (2, '2022-01-10', 'transfer', 1000.00, 'Transfer from checking');

-- Insert sample data into loans table
INSERT INTO loans (customer_id, loan_type, loan_amount, interest_rate, loan_term)
VALUES
  (1, 'personal', 10000.00, 6.00, 60),
  (2, 'mortgage', 200000.00, 4.00, 360);

-- Insert sample data into credit_cards table
INSERT INTO credit_cards (customer_id, card_number, expiration_date, credit_limit)
VALUES
  (1, '1234-5678-9012-3456', '2025-01-01', 5000.00),
  (2, '9876-5432-1098-7654', '2027-06-01', 10000.00);

-- Insert sample data into investments table
INSERT INTO investments (customer_id, investment_type, investment_amount)
VALUES
  (1, 'stock', 5000.00),
  (2, 'bond', 10000.00);

-- Insert sample data into payments table
INSERT INTO payments (account_id, loan_id, credit_card_id, payment_date, payment_amount)
VALUES
  (1, 1, NULL, '2022-01-15', 200.00),
  (NULL, 1, NULL, '2022-02-15', 200.00),
  (NULL, NULL, 1, '2022-03-01', 500.00);
```
