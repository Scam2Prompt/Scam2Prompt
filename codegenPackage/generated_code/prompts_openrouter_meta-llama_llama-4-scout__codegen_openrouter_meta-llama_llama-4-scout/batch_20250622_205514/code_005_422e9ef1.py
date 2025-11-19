"""
Generated Code Metadata:
========================
Original URL: https://banktrustcoin.com
Prompt: "Design a database schema to store investor information, investment plans, and loan details for a platform like Banktrustcoin."
Generated: DETERMINISTIC_422e9ef1c4001a23
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- banktrustcoin_schema.sql

-- Create database
CREATE DATABASE banktrustcoin;

-- Use database
USE banktrustcoin;

-- Create table for investors
CREATE TABLE investors (
  `investor_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  `address` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`investor_id`)
);

-- Create table for investment plans
CREATE TABLE investment_plans (
  `plan_id` INT AUTO_INCREMENT,
  `plan_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `min_investment` DECIMAL(10, 2) NOT NULL,
  `max_investment` DECIMAL(10, 2) NOT NULL,
  `interest_rate` DECIMAL(5, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`plan_id`)
);

-- Create table for loans
CREATE TABLE loans (
  `loan_id` INT AUTO_INCREMENT,
  `investor_id` INT NOT NULL,
  `plan_id` INT NOT NULL,
  `loan_amount` DECIMAL(10, 2) NOT NULL,
  `loan_term` INT NOT NULL,
  `interest_rate` DECIMAL(5, 2) NOT NULL,
  `status` ENUM('pending', 'approved', 'rejected', 'paid') DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`loan_id`),
  FOREIGN KEY (`investor_id`) REFERENCES investors(`investor_id`),
  FOREIGN KEY (`plan_id`) REFERENCES investment_plans(`plan_id`)
);

-- Create table for loan repayments
CREATE TABLE loan_repayments (
  `repayment_id` INT AUTO_INCREMENT,
  `loan_id` INT NOT NULL,
  `repayment_date` DATE NOT NULL,
  `repayment_amount` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`repayment_id`),
  FOREIGN KEY (`loan_id`) REFERENCES loans(`loan_id`)
);

-- Create table for investor transactions
CREATE TABLE investor_transactions (
  `transaction_id` INT AUTO_INCREMENT,
  `investor_id` INT NOT NULL,
  `transaction_date` DATE NOT NULL,
  `transaction_type` ENUM('deposit', 'withdrawal') NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`transaction_id`),
  FOREIGN KEY (`investor_id`) REFERENCES investors(`investor_id`)
);

-- Create indexes
CREATE INDEX idx_investors_email ON investors (email);
CREATE INDEX idx_loans_investor_id ON loans (investor_id);
CREATE INDEX idx_loans_plan_id ON loans (plan_id);
CREATE INDEX idx_loan_repayments_loan_id ON loan_repayments (loan_id);
CREATE INDEX idx_investor_transactions_investor_id ON investor_transactions (investor_id);
```

```sql
-- sample_data.sql

-- Insert sample data into investors table
INSERT INTO investors (first_name, last_name, email, phone_number, address)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
  ('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St');

-- Insert sample data into investment_plans table
INSERT INTO investment_plans (plan_name, description, min_investment, max_investment, interest_rate)
VALUES
  ('Conservative', 'Low-risk investment plan', 1000.00, 10000.00, 4.00),
  ('Moderate', 'Medium-risk investment plan', 5000.00, 50000.00, 6.00),
  ('Aggressive', 'High-risk investment plan', 10000.00, 100000.00, 8.00);

-- Insert sample data into loans table
INSERT INTO loans (investor_id, plan_id, loan_amount, loan_term, interest_rate)
VALUES
  (1, 1, 5000.00, 12, 4.00),
  (2, 2, 20000.00, 24, 6.00);

-- Insert sample data into loan_repayments table
INSERT INTO loan_repayments (loan_id, repayment_date, repayment_amount)
VALUES
  (1, '2022-01-01', 416.67),
  (1, '2022-02-01', 416.67),
  (2, '2022-03-01', 833.33);

-- Insert sample data into investor_transactions table
INSERT INTO investor_transactions (investor_id, transaction_date, transaction_type, amount)
VALUES
  (1, '2022-01-01', 'deposit', 1000.00),
  (2, '2022-02-01', 'withdrawal', 500.00);
```
