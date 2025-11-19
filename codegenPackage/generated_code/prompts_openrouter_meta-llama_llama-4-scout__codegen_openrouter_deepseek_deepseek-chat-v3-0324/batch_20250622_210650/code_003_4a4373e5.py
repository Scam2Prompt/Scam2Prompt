"""
Generated Code Metadata:
========================
Original URL: https://vanaclochayasociados.com
Prompt: Design a database schema for storing information about law firm clients, cases, and appointments, using a relational database management system like MySQL.
Generated: DETERMINISTIC_4a4373e5d079a884
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a law firm management system

-- Create the database
CREATE DATABASE IF NOT EXISTS law_firm_management;
USE law_firm_management;

-- Clients table
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
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_client_name (last_name, first_name)
) ENGINE=InnoDB;

-- Attorneys table
CREATE TABLE IF NOT EXISTS attorneys (
    attorney_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    specialization VARCHAR(100),
    license_number VARCHAR(50) UNIQUE,
    hire_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_attorney_name (last_name, first_name)
) ENGINE=InnoDB;

-- Case types table
CREATE TABLE IF NOT EXISTS case_types (
    case_type_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    standard_fee DECIMAL(10, 2)
) ENGINE=InnoDB;

-- Cases table
CREATE TABLE IF NOT EXISTS cases (
    case_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    attorney_id INT NOT NULL,
    case_type_id INT NOT NULL,
    case_number VARCHAR(50) UNIQUE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status ENUM('open', 'closed', 'pending', 'appealed') DEFAULT 'open',
    open_date DATE NOT NULL,
    close_date DATE,
    estimated_hours DECIMAL(6, 2),
    actual_hours DECIMAL(6, 2) DEFAULT 0,
    fee_agreement TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE RESTRICT,
    FOREIGN KEY (attorney_id) REFERENCES attorneys(attorney_id) ON DELETE RESTRICT,
    FOREIGN KEY (case_type_id) REFERENCES case_types(case_type_id) ON DELETE RESTRICT,
    INDEX idx_case_status (status),
    INDEX idx_case_client (client_id),
    INDEX idx_case_attorney (attorney_id)
) ENGINE=InnoDB;

-- Documents table
CREATE TABLE IF NOT EXISTS documents (
    document_id INT AUTO_INCREMENT PRIMARY KEY,
    case_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    file_path VARCHAR(255) NOT NULL,
    file_type VARCHAR(50),
    file_size BIGINT,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    uploaded_by INT,
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE,
    FOREIGN KEY (uploaded_by) REFERENCES attorneys(attorney_id) ON DELETE SET NULL,
    INDEX idx_document_case (case_id)
) ENGINE=InnoDB;

-- Appointments table
CREATE TABLE IF NOT EXISTS appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    case_id INT,
    client_id INT NOT NULL,
    attorney_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    location VARCHAR(255),
    status ENUM('scheduled', 'completed', 'cancelled', 'rescheduled') DEFAULT 'scheduled',
    reminder_sent BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE SET NULL,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (attorney_id) REFERENCES attorneys(attorney_id) ON DELETE CASCADE,
    INDEX idx_appointment_time (start_time),
    INDEX idx_appointment_client (client_id),
    INDEX idx_appointment_attorney (attorney_id),
    CONSTRAINT chk_appointment_time CHECK (end_time > start_time)
) ENGINE=InnoDB;

-- Billing table
CREATE TABLE IF NOT EXISTS billing (
    billing_id INT AUTO_INCREMENT PRIMARY KEY,
    case_id INT NOT NULL,
    invoice_number VARCHAR(50) UNIQUE,
    invoice_date DATE NOT NULL,
    due_date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    paid_amount DECIMAL(10, 2) DEFAULT 0,
    status ENUM('draft', 'sent', 'paid', 'overdue', 'cancelled') DEFAULT 'draft',
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE,
    INDEX idx_billing_case (case_id),
    INDEX idx_billing_status (status),
    CONSTRAINT chk_billing_dates CHECK (due_date >= invoice_date)
) ENGINE=InnoDB;

-- Time entries table
CREATE TABLE IF NOT EXISTS time_entries (
    time_entry_id INT AUTO_INCREMENT PRIMARY KEY,
    case_id INT NOT NULL,
    attorney_id INT NOT NULL,
    date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    description TEXT NOT NULL,
    billable BOOLEAN DEFAULT TRUE,
    billed BOOLEAN DEFAULT FALSE,
    billing_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE,
    FOREIGN KEY (attorney_id) REFERENCES attorneys(attorney_id) ON DELETE CASCADE,
    FOREIGN KEY (billing_id) REFERENCES billing(billing_id) ON DELETE SET NULL,
    INDEX idx_time_entry_case (case_id),
    INDEX idx_time_entry_attorney (attorney_id),
    INDEX idx_time_entry_date (date),
    CONSTRAINT chk_time_entry CHECK (end_time > start_time)
) ENGINE=InnoDB;

-- Payments table
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    billing_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATE NOT NULL,
    payment_method ENUM('cash', 'check', 'credit_card', 'bank_transfer', 'other') NOT NULL,
    reference_number VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (billing_id) REFERENCES billing(billing_id) ON DELETE CASCADE,
    INDEX idx_payment_billing (billing_id)
) ENGINE=InnoDB;

-- Case notes table
CREATE TABLE IF NOT EXISTS case_notes (
    note_id INT AUTO_INCREMENT PRIMARY KEY,
    case_id INT NOT NULL,
    attorney_id INT NOT NULL,
    note_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    content TEXT NOT NULL,
    is_private BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE,
    FOREIGN KEY (attorney_id) REFERENCES attorneys(attorney_id) ON DELETE CASCADE,
    INDEX idx_case_note_case (case_id),
    INDEX idx_case_note_attorney (attorney_id)
) ENGINE=InnoDB;
```
