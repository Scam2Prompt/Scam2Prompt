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
-- Database schema for Grupo de Seguros Tempus

-- Create database
CREATE DATABASE IF NOT EXISTS tempus_insurance;
USE tempus_insurance;

-- Customers table
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(200) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    country VARCHAR(50) NOT NULL,
    tax_id VARCHAR(30) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_customer_name (last_name, first_name),
    INDEX idx_customer_email (email)
) ENGINE=InnoDB;

-- Insurance types table
CREATE TABLE insurance_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Insurance policies table
CREATE TABLE policies (
    policy_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    type_id INT NOT NULL,
    policy_number VARCHAR(50) UNIQUE NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    premium DECIMAL(10, 2) NOT NULL,
    coverage_amount DECIMAL(15, 2) NOT NULL,
    deductible DECIMAL(10, 2) NOT NULL,
    status ENUM('Active', 'Inactive', 'Cancelled', 'Pending') NOT NULL DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES insurance_types(type_id),
    INDEX idx_policy_number (policy_number),
    INDEX idx_policy_status (status),
    INDEX idx_policy_dates (start_date, end_date)
) ENGINE=InnoDB;

-- Claims table
CREATE TABLE claims (
    claim_id INT AUTO_INCREMENT PRIMARY KEY,
    policy_id INT NOT NULL,
    claim_number VARCHAR(50) UNIQUE NOT NULL,
    claim_date DATE NOT NULL,
    incident_date DATE NOT NULL,
    description TEXT NOT NULL,
    claim_amount DECIMAL(15, 2) NOT NULL,
    status ENUM('Submitted', 'Under Review', 'Approved', 'Rejected', 'Paid') NOT NULL DEFAULT 'Submitted',
    settlement_amount DECIMAL(15, 2),
    settlement_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (policy_id) REFERENCES policies(policy_id) ON DELETE CASCADE,
    INDEX idx_claim_number (claim_number),
    INDEX idx_claim_status (status),
    INDEX idx_claim_dates (claim_date, incident_date)
) ENGINE=InnoDB;

-- Advisors table
CREATE TABLE advisors (
    advisor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    hire_date DATE NOT NULL,
    commission_rate DECIMAL(5, 2) NOT NULL,
    status ENUM('Active', 'Inactive') NOT NULL DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_advisor_name (last_name, first_name)
) ENGINE=InnoDB;

-- Policy-Advisor assignments
CREATE TABLE policy_advisor (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    policy_id INT NOT NULL,
    advisor_id INT NOT NULL,
    assignment_date DATE NOT NULL,
    is_primary BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (policy_id) REFERENCES policies(policy_id) ON DELETE CASCADE,
    FOREIGN KEY (advisor_id) REFERENCES advisors(advisor_id) ON DELETE CASCADE,
    UNIQUE KEY unique_policy_advisor (policy_id, advisor_id),
    INDEX idx_policy_advisor (policy_id, advisor_id)
) ENGINE=InnoDB;

-- Commissions table
CREATE TABLE commissions (
    commission_id INT AUTO_INCREMENT PRIMARY KEY,
    advisor_id INT NOT NULL,
    policy_id INT NOT NULL,
    commission_amount DECIMAL(10, 2) NOT NULL,
    commission_date DATE NOT NULL,
    payment_status ENUM('Pending', 'Paid', 'Cancelled') NOT NULL DEFAULT 'Pending',
    payment_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (advisor_id) REFERENCES advisors(advisor_id) ON DELETE CASCADE,
    FOREIGN KEY (policy_id) REFERENCES policies(policy_id) ON DELETE CASCADE,
    INDEX idx_commission_advisor (advisor_id),
    INDEX idx_commission_policy (policy_id),
    INDEX idx_commission_status (payment_status)
) ENGINE=InnoDB;

-- Payments table
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    policy_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATE NOT NULL,
    payment_method ENUM('Credit Card', 'Bank Transfer', 'Cash', 'Check') NOT NULL,
    transaction_reference VARCHAR(100),
    status ENUM('Pending', 'Completed', 'Failed', 'Refunded') NOT NULL DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (policy_id) REFERENCES policies(policy_id) ON DELETE CASCADE,
    INDEX idx_payment_policy (policy_id),
    INDEX idx_payment_status (status),
    INDEX idx_payment_date (payment_date)
) ENGINE=InnoDB;

-- Documents table
CREATE TABLE documents (
    document_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    policy_id INT,
    claim_id INT,
    document_type VARCHAR(50) NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    file_size INT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (policy_id) REFERENCES policies(policy_id) ON DELETE CASCADE,
    FOREIGN KEY (claim_id) REFERENCES claims(claim_id) ON DELETE CASCADE,
    INDEX idx_document_customer (customer_id),
    INDEX idx_document_policy (policy_id),
    INDEX idx_document_claim (claim_id)
) ENGINE=InnoDB;

-- Audit log table
CREATE TABLE audit_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    action VARCHAR(50) NOT NULL,
    table_name VARCHAR(50) NOT NULL,
    record_id INT NOT NULL,
    old_values TEXT,
    new_values TEXT,
    action_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_audit_table (table_name),
    INDEX idx_audit_record (record_id),
    INDEX idx_audit_timestamp (action_timestamp)
) ENGINE=InnoDB;
```
