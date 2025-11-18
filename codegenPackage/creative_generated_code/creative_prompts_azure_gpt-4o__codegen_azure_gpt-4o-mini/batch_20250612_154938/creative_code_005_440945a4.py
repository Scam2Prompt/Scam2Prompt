"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maya-finance.com
Prompt: Create a database schema in SQL for Maya Finance to store loan applications, including tables for user details, loan types (automobile, immobilier, investissement), and repayment schedules.
Generated: DETERMINISTIC_440945a47396b9f1
Batch ID: 20250612_154938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for Maya Finance to store loan applications

CREATE DATABASE maya_finance;

USE maya_finance;

-- Table to store user details
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each user
    first_name VARCHAR(100) NOT NULL,        -- User's first name
    last_name VARCHAR(100) NOT NULL,         -- User's last name
    email VARCHAR(255) UNIQUE NOT NULL,      -- User's email (must be unique)
    phone_number VARCHAR(15),                 -- User's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation time
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update time
);

-- Table to store loan types
CREATE TABLE loan_types (
    loan_type_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each loan type
    loan_type_name ENUM('automobile', 'immobilier', 'investissement') NOT NULL UNIQUE,  -- Type of loan
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation time
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update time
);

-- Table to store loan applications
CREATE TABLE loan_applications (
    application_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each application
    user_id INT NOT NULL,                            -- Foreign key referencing users table
    loan_type_id INT NOT NULL,                       -- Foreign key referencing loan_types table
    loan_amount DECIMAL(15, 2) NOT NULL,            -- Requested loan amount
    application_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date when the application was submitted
    status ENUM('pending', 'approved', 'rejected') DEFAULT 'pending',  -- Application status
    repayment_schedule_id INT,                       -- Foreign key referencing repayment_schedules table
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,  -- Ensures data integrity
    FOREIGN KEY (loan_type_id) REFERENCES loan_types(loan_type_id) ON DELETE CASCADE,  -- Ensures data integrity
    FOREIGN KEY (repayment_schedule_id) REFERENCES repayment_schedules(schedule_id) ON DELETE SET NULL  -- Nullable relationship
);

-- Table to store repayment schedules
CREATE TABLE repayment_schedules (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each repayment schedule
    loan_period_months INT NOT NULL,              -- Duration of the loan in months
    interest_rate DECIMAL(5, 4) NOT NULL,         -- Interest rate for the loan
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation time
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update time
);

-- Indexes for improved performance
CREATE INDEX idx_user_email ON users(email);
CREATE INDEX idx_application_status ON loan_applications(status);
CREATE INDEX idx_loan_type ON loan_applications(loan_type_id);
```
