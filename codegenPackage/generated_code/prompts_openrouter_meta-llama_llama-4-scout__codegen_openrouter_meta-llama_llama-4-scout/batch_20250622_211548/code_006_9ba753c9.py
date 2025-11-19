"""
Generated Code Metadata:
========================
Original URL: https://pipelinefinanceconseil.com
Prompt: "Design a database schema to store client information and savings plans for a financial advisory firm like Pipeline Finance Conseil."
Generated: DETERMINISTIC_9ba753c905af4d40
Batch ID: 20250622_211548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Pipeline Finance Conseil
CREATE DATABASE pipeline_finance_conseil;

-- Use the database
USE pipeline_finance_conseil;

-- Create a table to store client information
CREATE TABLE clients (
  `client_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  `address` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`client_id`)
);

-- Create a table to store savings plans
CREATE TABLE savings_plans (
  `plan_id` INT AUTO_INCREMENT,
  `client_id` INT NOT NULL,
  `plan_name` VARCHAR(255) NOT NULL,
  `plan_type` ENUM('short_term', 'long_term') NOT NULL,
  `goal_amount` DECIMAL(10, 2) NOT NULL,
  `monthly_contribution` DECIMAL(10, 2) NOT NULL,
  `start_date` DATE NOT NULL,
  `end_date` DATE,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`plan_id`),
  FOREIGN KEY (`client_id`) REFERENCES clients(`client_id`) ON DELETE CASCADE
);

-- Create a table to store plan transactions
CREATE TABLE plan_transactions (
  `transaction_id` INT AUTO_INCREMENT,
  `plan_id` INT NOT NULL,
  `transaction_date` DATE NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `type` ENUM('deposit', 'withdrawal') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`transaction_id`),
  FOREIGN KEY (`plan_id`) REFERENCES savings_plans(`plan_id`) ON DELETE CASCADE
);

-- Create a table to store advisor information
CREATE TABLE advisors (
  `advisor_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`advisor_id`)
);

-- Create a table to store client-advisor relationships
CREATE TABLE client_advisors (
  `client_id` INT NOT NULL,
  `advisor_id` INT NOT NULL,
  `assigned_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`client_id`, `advisor_id`),
  FOREIGN KEY (`client_id`) REFERENCES clients(`client_id`) ON DELETE CASCADE,
  FOREIGN KEY (`advisor_id`) REFERENCES advisors(`advisor_id`) ON DELETE CASCADE
);

-- Example data for testing
INSERT INTO clients (first_name, last_name, email, phone_number, address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St');

INSERT INTO advisors (first_name, last_name, email, phone_number)
VALUES 
('Alice', 'Smith', 'alice.smith@example.com', '555-123-4567'),
('Bob', 'Johnson', 'bob.johnson@example.com', '555-987-6543');

INSERT INTO savings_plans (client_id, plan_name, plan_type, goal_amount, monthly_contribution, start_date)
VALUES 
(1, 'Short-term savings', 'short_term', 1000.00, 50.00, '2022-01-01'),
(2, 'Long-term savings', 'long_term', 10000.00, 200.00, '2022-01-01');

INSERT INTO plan_transactions (plan_id, transaction_date, amount, type)
VALUES 
(1, '2022-01-15', 50.00, 'deposit'),
(1, '2022-02-15', 50.00, 'deposit'),
(2, '2022-01-15', 200.00, 'deposit');

INSERT INTO client_advisors (client_id, advisor_id)
VALUES 
(1, 1),
(2, 2);
```
