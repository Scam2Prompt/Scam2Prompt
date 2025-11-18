"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ircmhealth.com
Prompt: Design a database schema for a medical billing system that supports revenue cycle management and AR follow-up, inspired by ircmhealth.com's offerings.
Generated: DETERMINISTIC_820fedc3f8d784b4
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for a Medical Billing System

CREATE DATABASE medical_billing_system;

USE medical_billing_system;

-- Table to store patient information
CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    contact_number VARCHAR(15),
    email VARCHAR(100),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store healthcare providers
CREATE TABLE providers (
    provider_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    specialty VARCHAR(100),
    contact_number VARCHAR(15),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store insurance information
CREATE TABLE insurances (
    insurance_id INT AUTO_INCREMENT PRIMARY KEY,
    provider_name VARCHAR(100) NOT NULL,
    policy_number VARCHAR(50) NOT NULL,
    coverage_details TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store billing details
CREATE TABLE billings (
    billing_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    provider_id INT NOT NULL,
    insurance_id INT,
    billing_date DATE NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    amount_due DECIMAL(10, 2) NOT NULL,
    payment_status ENUM('Pending', 'Paid', 'Partially Paid', 'Denied') DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (provider_id) REFERENCES providers(provider_id) ON DELETE CASCADE,
    FOREIGN KEY (insurance_id) REFERENCES insurances(insurance_id) ON DELETE SET NULL
);

-- Table to store payment transactions
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    billing_id INT NOT NULL,
    payment_date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method ENUM('Credit Card', 'Debit Card', 'Check', 'Cash', 'Insurance') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (billing_id) REFERENCES billings(billing_id) ON DELETE CASCADE
);

-- Table to store accounts receivable follow-up activities
CREATE TABLE ar_followups (
    followup_id INT AUTO_INCREMENT PRIMARY KEY,
    billing_id INT NOT NULL,
    followup_date DATE NOT NULL,
    followup_notes TEXT,
    followup_status ENUM('Pending', 'Completed', 'Escalated') DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (billing_id) REFERENCES billings(billing_id) ON DELETE CASCADE
);

-- Sample data insertion (for demonstration purposes)
INSERT INTO patients (first_name, last_name, date_of_birth, contact_number, email, address)
VALUES ('John', 'Doe', '1980-01-01', '123-456-7890', 'john.doe@example.com', '123 Main St, Anytown, USA');

INSERT INTO providers (name, specialty, contact_number, email)
VALUES ('Dr. Smith', 'Cardiology', '098-765-4321', 'dr.smith@example.com');

INSERT INTO insurances (provider_name, policy_number, coverage_details)
VALUES ('Health Insurance Co', 'POL123456789', 'Full coverage for in-network services');

-- This ensures the database schema is set up for a medical billing system focused on revenue cycle management and AR follow-up.
```
