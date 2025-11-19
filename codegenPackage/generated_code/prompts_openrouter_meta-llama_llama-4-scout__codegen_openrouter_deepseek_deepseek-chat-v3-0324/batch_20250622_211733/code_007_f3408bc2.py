"""
Generated Code Metadata:
========================
Original URL: https://sardagnapoeta.com.br
Prompt: Design a simple database schema to store information about law firm clients, cases, and attorneys, using a relational database management system like MySQL.
Generated: DETERMINISTIC_f3408bc21acf4cb0
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a law firm database schema
-- Includes tables for clients, cases, attorneys, and their relationships

-- Create the database
CREATE DATABASE IF NOT EXISTS law_firm;
USE law_firm;

-- Table to store attorney information
CREATE TABLE IF NOT EXISTS attorneys (
    attorney_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    specialization VARCHAR(100),
    bar_number VARCHAR(50) UNIQUE NOT NULL,
    hire_date DATE NOT NULL,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Table to store client information
CREATE TABLE IF NOT EXISTS clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(255),
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(20),
    date_of_birth DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_client_email CHECK (email IS NULL OR email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Table to store case information
CREATE TABLE IF NOT EXISTS cases (
    case_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    case_type VARCHAR(50) NOT NULL,
    status ENUM('open', 'closed', 'pending', 'settled') DEFAULT 'open',
    filing_date DATE NOT NULL,
    closing_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Junction table for attorney-case assignments
CREATE TABLE IF NOT EXISTS attorney_case_assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    attorney_id INT NOT NULL,
    case_id INT NOT NULL,
    role VARCHAR(50) NOT NULL,
    date_assigned DATE NOT NULL,
    date_ended DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (attorney_id) REFERENCES attorneys(attorney_id) ON DELETE CASCADE,
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE,
    UNIQUE KEY unique_assignment (attorney_id, case_id, role)
) ENGINE=InnoDB;

-- Table to store case documents
CREATE TABLE IF NOT EXISTS case_documents (
    document_id INT AUTO_INCREMENT PRIMARY KEY,
    case_id INT NOT NULL,
    attorney_id INT NOT NULL,
    document_name VARCHAR(100) NOT NULL,
    document_type VARCHAR(50) NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE,
    FOREIGN KEY (attorney_id) REFERENCES attorneys(attorney_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table to store billing information
CREATE TABLE IF NOT EXISTS billing_records (
    billing_id INT AUTO_INCREMENT PRIMARY KEY,
    case_id INT NOT NULL,
    attorney_id INT NOT NULL,
    hours DECIMAL(10,2) NOT NULL,
    rate DECIMAL(10,2) NOT NULL,
    description TEXT NOT NULL,
    billing_date DATE NOT NULL,
    status ENUM('unpaid', 'paid', 'disputed') DEFAULT 'unpaid',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE,
    FOREIGN KEY (attorney_id) REFERENCES attorneys(attorney_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table to store case notes
CREATE TABLE IF NOT EXISTS case_notes (
    note_id INT AUTO_INCREMENT PRIMARY KEY,
    case_id INT NOT NULL,
    attorney_id INT NOT NULL,
    note TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE,
    FOREIGN KEY (attorney_id) REFERENCES attorneys(attorney_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Create indexes for performance optimization
CREATE INDEX idx_client_name ON clients(last_name, first_name);
CREATE INDEX idx_case_client ON cases(client_id);
CREATE INDEX idx_case_status ON cases(status);
CREATE INDEX idx_attorney_case ON attorney_case_assignments(attorney_id, case_id);
CREATE INDEX idx_billing_case ON billing_records(case_id);
```
