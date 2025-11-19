"""
Generated Code Metadata:
========================
Original URL: https://poverka-gazvoda.ru
Prompt: Create a SQL database schema to store client information, meter calibration history, and relevant documentation for a calibration service provider like ИП Семьянинов Сергей Юрьевич on https://poverka-gazvoda.ru.
Generated: DETERMINISTIC_5d4b5641c08f88b2
Batch ID: 20250622_211832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Calibration Service Provider

-- Create database
CREATE DATABASE IF NOT EXISTS calibration_service_provider;
USE calibration_service_provider;

-- Clients table
CREATE TABLE IF NOT EXISTS clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    organization_name VARCHAR(255) NOT NULL,
    contact_person VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(255) CHECK (email LIKE '%@%.%'),
    address TEXT NOT NULL,
    tax_id VARCHAR(20),
    registration_number VARCHAR(50),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (organization_name),
    INDEX (contact_person),
    INDEX (phone)
) ENGINE=InnoDB;

-- Meter types table
CREATE TABLE IF NOT EXISTS meter_types (
    meter_type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    measurement_unit VARCHAR(50) NOT NULL,
    standard_interval_months INT NOT NULL
) ENGINE=InnoDB;

-- Meters table
CREATE TABLE IF NOT EXISTS meters (
    meter_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    meter_type_id INT NOT NULL,
    serial_number VARCHAR(100) NOT NULL,
    manufacturer VARCHAR(255) NOT NULL,
    model VARCHAR(100) NOT NULL,
    installation_date DATE NOT NULL,
    initial_calibration_date DATE NOT NULL,
    current_location TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (meter_type_id) REFERENCES meter_types(meter_type_id),
    UNIQUE (serial_number, manufacturer),
    INDEX (serial_number),
    INDEX (manufacturer),
    INDEX (model)
) ENGINE=InnoDB;

-- Calibration certificates table
CREATE TABLE IF NOT EXISTS calibration_certificates (
    certificate_id INT AUTO_INCREMENT PRIMARY KEY,
    meter_id INT NOT NULL,
    certificate_number VARCHAR(100) NOT NULL UNIQUE,
    calibration_date DATE NOT NULL,
    next_calibration_date DATE NOT NULL,
    calibration_result ENUM('Passed', 'Failed', 'Conditional') NOT NULL,
    accuracy_class VARCHAR(50),
    calibration_lab VARCHAR(255) NOT NULL,
    technician_name VARCHAR(255) NOT NULL,
    document_path VARCHAR(255),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (meter_id) REFERENCES meters(meter_id) ON DELETE CASCADE,
    INDEX (certificate_number),
    INDEX (calibration_date),
    INDEX (next_calibration_date)
) ENGINE=InnoDB;

-- Documents table
CREATE TABLE IF NOT EXISTS documents (
    document_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT,
    meter_id INT,
    document_type ENUM('Contract', 'Invoice', 'Report', 'Certificate', 'Other') NOT NULL,
    document_number VARCHAR(100),
    issue_date DATE NOT NULL,
    expiration_date DATE,
    file_path VARCHAR(255) NOT NULL,
    description TEXT,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE SET NULL,
    FOREIGN KEY (meter_id) REFERENCES meters(meter_id) ON DELETE SET NULL,
    INDEX (document_type),
    INDEX (issue_date)
) ENGINE=InnoDB;

-- Users table for system access
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE CHECK (email LIKE '%@%.%'),
    role ENUM('Admin', 'Technician', 'Manager', 'Viewer') NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    last_login TIMESTAMP NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Audit log table
CREATE TABLE IF NOT EXISTS audit_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    action_type VARCHAR(50) NOT NULL,
    table_name VARCHAR(50) NOT NULL,
    record_id INT,
    action_details TEXT,
    ip_address VARCHAR(45),
    action_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL,
    INDEX (action_timestamp),
    INDEX (table_name)
) ENGINE=InnoDB;

-- Create views for common queries

-- View for upcoming calibrations
CREATE VIEW upcoming_calibrations AS
SELECT 
    c.client_id,
    c.organization_name,
    c.contact_person,
    c.phone,
    m.meter_id,
    m.serial_number,
    m.manufacturer,
    m.model,
    cc.certificate_number,
    cc.calibration_date,
    cc.next_calibration_date,
    DATEDIFF(cc.next_calibration_date, CURDATE()) AS days_remaining
FROM 
    calibration_certificates cc
JOIN 
    meters m ON cc.meter_id = m.meter_id
JOIN 
    clients c ON m.client_id = c.client_id
WHERE 
    cc.next_calibration_date BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 30 DAY)
ORDER BY 
    cc.next_calibration_date ASC;

-- View for expired calibrations
CREATE VIEW expired_calibrations AS
SELECT 
    c.client_id,
    c.organization_name,
    c.contact_person,
    c.phone,
    m.meter_id,
    m.serial_number,
    m.manufacturer,
    m.model,
    cc.certificate_number,
    cc.calibration_date,
    cc.next_calibration_date,
    DATEDIFF(CURDATE(), cc.next_calibration_date) AS days_expired
FROM 
    calibration_certificates cc
JOIN 
    meters m ON cc.meter_id = m.meter_id
JOIN 
    clients c ON m.client_id = c.client_id
WHERE 
    cc.next_calibration_date < CURDATE()
ORDER BY 
    cc.next_calibration_date DESC;
```
