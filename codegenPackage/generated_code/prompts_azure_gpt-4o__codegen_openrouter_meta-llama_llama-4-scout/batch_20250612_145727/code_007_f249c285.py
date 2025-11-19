"""
Generated Code Metadata:
========================
Original URL: https://nocreditcheck.online
Prompt: Create a database schema for storing microloan offers, including fields like "loan amount," "repayment period," and "unique selling points" (e.g., "instant approval"), based on the structure of nocreditcheck.online.
Generated: DETERMINISTIC_f249c28591244c88
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- microloans_schema.sql

-- Create database schema for microloan offers
CREATE DATABASE microloans;

-- Use the microloans database
USE microloans;

-- Create table for microloan offers
CREATE TABLE loan_offers (
  `id` INT AUTO_INCREMENT,
  `loan_amount` DECIMAL(10, 2) NOT NULL,
  `repayment_period` INT NOT NULL, -- in months
  `interest_rate` DECIMAL(5, 2) NOT NULL,
  `unique_selling_points` JSON,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  CHECK (`loan_amount` > 0),
  CHECK (`repayment_period` > 0),
  CHECK (`interest_rate` >= 0)
);

-- Create table for loan offer features (unique selling points)
CREATE TABLE loan_offer_features (
  `id` INT AUTO_INCREMENT,
  `loan_offer_id` INT NOT NULL,
  `feature_name` VARCHAR(255) NOT NULL,
  `feature_description` TEXT,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`loan_offer_id`) REFERENCES loan_offers(`id`) ON DELETE CASCADE
);

-- Create table for loan applications
CREATE TABLE loan_applications (
  `id` INT AUTO_INCREMENT,
  `loan_offer_id` INT NOT NULL,
  `applicant_name` VARCHAR(255) NOT NULL,
  `applicant_email` VARCHAR(255) UNIQUE NOT NULL,
  `application_date` DATE NOT NULL,
  `status` ENUM('pending', 'approved', 'rejected') DEFAULT 'pending',
  PRIMARY KEY (`id`),
  FOREIGN KEY (`loan_offer_id`) REFERENCES loan_offers(`id`) ON DELETE CASCADE
);

-- Create table for loan repayments
CREATE TABLE loan_repayments (
  `id` INT AUTO_INCREMENT,
  `loan_application_id` INT NOT NULL,
  `repayment_date` DATE NOT NULL,
  `repayment_amount` DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`loan_application_id`) REFERENCES loan_applications(`id`) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO loan_offers (loan_amount, repayment_period, interest_rate, unique_selling_points)
VALUES
  (1000.00, 3, 10.00, '["instant approval", "no collateral required"]'),
  (500.00, 6, 12.00, '["flexible repayment terms", "no credit check"]');

INSERT INTO loan_offer_features (loan_offer_id, feature_name, feature_description)
VALUES
  (1, 'instant approval', 'Get approved for your loan instantly'),
  (1, 'no collateral required', 'No collateral is required to secure your loan'),
  (2, 'flexible repayment terms', 'Choose a repayment term that suits your needs'),
  (2, 'no credit check', 'We do not perform credit checks on our applicants');

INSERT INTO loan_applications (loan_offer_id, applicant_name, applicant_email, application_date)
VALUES
  (1, 'John Doe', 'john.doe@example.com', '2022-01-01'),
  (2, 'Jane Smith', 'jane.smith@example.com', '2022-01-15');
```
