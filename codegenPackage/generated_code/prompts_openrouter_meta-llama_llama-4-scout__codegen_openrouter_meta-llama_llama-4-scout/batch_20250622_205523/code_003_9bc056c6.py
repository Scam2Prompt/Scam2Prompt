"""
Generated Code Metadata:
========================
Original URL: https://skytrustasset.com
Prompt: "Design a database schema to store information about Sky Trust Ltd investors, their deposit amounts, and chosen tariff plans."
Generated: DETERMINISTIC_9bc056c6573332d6
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Sky Trust Ltd investors
CREATE DATABASE sky_trust;

-- Use the created database
USE sky_trust;

-- Create table for investors
CREATE TABLE investors (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  `address` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for tariff plans
CREATE TABLE tariff_plans (
  `id` INT AUTO_INCREMENT,
  `plan_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `min_deposit` DECIMAL(10, 2) NOT NULL,
  `max_deposit` DECIMAL(10, 2) NOT NULL,
  `interest_rate` DECIMAL(5, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for investor deposits
CREATE TABLE investor_deposits (
  `id` INT AUTO_INCREMENT,
  `investor_id` INT NOT NULL,
  `tariff_plan_id` INT NOT NULL,
  `deposit_amount` DECIMAL(10, 2) NOT NULL,
  `deposit_date` DATE NOT NULL,
  `maturity_date` DATE,
  `interest_earned` DECIMAL(10, 2) DEFAULT 0.00,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`investor_id`) REFERENCES investors(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`tariff_plan_id`) REFERENCES tariff_plans(`id`) ON DELETE CASCADE
);

-- Create table for investor transactions
CREATE TABLE investor_transactions (
  `id` INT AUTO_INCREMENT,
  `investor_deposit_id` INT NOT NULL,
  `transaction_date` DATE NOT NULL,
  `transaction_type` ENUM('deposit', 'withdrawal', 'interest') NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`investor_deposit_id`) REFERENCES investor_deposits(`id`) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_investor_deposits_investor_id ON investor_deposits (investor_id);
CREATE INDEX idx_investor_deposits_tariff_plan_id ON investor_deposits (tariff_plan_id);
CREATE INDEX idx_investor_transactions_investor_deposit_id ON investor_transactions (investor_deposit_id);
```

```sql
-- sample_data.sql

-- Insert sample data into investors table
INSERT INTO investors (name, email, phone_number, address)
VALUES
  ('John Doe', 'john.doe@example.com', '1234567890', '123 Main St'),
  ('Jane Doe', 'jane.doe@example.com', '9876543210', '456 Elm St');

-- Insert sample data into tariff_plans table
INSERT INTO tariff_plans (plan_name, description, min_deposit, max_deposit, interest_rate)
VALUES
  ('Basic Plan', 'Basic plan with 5% interest rate', 100.00, 1000.00, 5.00),
  ('Premium Plan', 'Premium plan with 10% interest rate', 1000.00, 10000.00, 10.00);

-- Insert sample data into investor_deposits table
INSERT INTO investor_deposits (investor_id, tariff_plan_id, deposit_amount, deposit_date, maturity_date)
VALUES
  (1, 1, 500.00, '2022-01-01', '2023-01-01'),
  (2, 2, 5000.00, '2022-06-01', '2023-06-01');

-- Insert sample data into investor_transactions table
INSERT INTO investor_transactions (investor_deposit_id, transaction_date, transaction_type, amount)
VALUES
  (1, '2022-01-01', 'deposit', 500.00),
  (1, '2022-07-01', 'interest', 25.00),
  (2, '2022-06-01', 'deposit', 5000.00);
```
