"""
Generated Code Metadata:
========================
Original URL: https://arrendamosjv.com
Prompt: Design a database schema to store information about properties, clients, and rental contracts for a real estate company like Arrendamos J V SAS, using a relational database management system like MySQL.
Generated: DETERMINISTIC_6a4e0a979adc9345
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# MySQL Database Schema for Real Estate Management System

```sql
-- Database creation
CREATE DATABASE IF NOT EXISTS real_estate_management;
USE real_estate_management;

-- Clients table
CREATE TABLE IF NOT EXISTS clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    id_type ENUM('CC', 'CE', 'PASSPORT', 'NIT') NOT NULL,
    id_number VARCHAR(20) UNIQUE NOT NULL,
    address VARCHAR(200) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_id_number (id_number)
) ENGINE=InnoDB;

-- Property types table
CREATE TABLE IF NOT EXISTS property_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT
) ENGINE=InnoDB;

-- Properties table
CREATE TABLE IF NOT EXISTS properties (
    property_id INT AUTO_INCREMENT PRIMARY KEY,
    owner_id INT NOT NULL,
    type_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    address VARCHAR(200) NOT NULL,
    city VARCHAR(50) NOT NULL,
    neighborhood VARCHAR(50) NOT NULL,
    stratum TINYINT NOT NULL,
    area DECIMAL(10, 2) NOT NULL COMMENT 'Area in square meters',
    rooms TINYINT NOT NULL,
    bathrooms TINYINT NOT NULL,
    parking_spaces TINYINT DEFAULT 0,
    price DECIMAL(12, 2) NOT NULL COMMENT 'Monthly rental price',
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (owner_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES property_types(type_id),
    INDEX idx_city (city),
    INDEX idx_price (price),
    INDEX idx_availability (is_available)
) ENGINE=InnoDB;

-- Property features table (many-to-many relationship)
CREATE TABLE IF NOT EXISTS property_features (
    property_id INT NOT NULL,
    feature VARCHAR(50) NOT NULL,
    PRIMARY KEY (property_id, feature),
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Property images table
CREATE TABLE IF NOT EXISTS property_images (
    image_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    INDEX idx_property (property_id)
) ENGINE=InnoDB;

-- Contract statuses table
CREATE TABLE IF NOT EXISTS contract_statuses (
    status_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) UNIQUE NOT NULL,
    description TEXT
) ENGINE=InnoDB;

-- Rental contracts table
CREATE TABLE IF NOT EXISTS rental_contracts (
    contract_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT NOT NULL,
    tenant_id INT NOT NULL,
    status_id INT NOT NULL DEFAULT 1,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    monthly_rent DECIMAL(12, 2) NOT NULL,
    deposit_amount DECIMAL(12, 2) NOT NULL,
    contract_terms TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES properties(property_id),
    FOREIGN KEY (tenant_id) REFERENCES clients(client_id),
    FOREIGN KEY (status_id) REFERENCES contract_statuses(status_id),
    INDEX idx_dates (start_date, end_date),
    INDEX idx_status (status_id),
    CONSTRAINT chk_dates CHECK (end_date > start_date)
) ENGINE=InnoDB;

-- Payments table
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    contract_id INT NOT NULL,
    amount DECIMAL(12, 2) NOT NULL,
    payment_date DATE NOT NULL,
    payment_method ENUM('CASH', 'BANK_TRANSFER', 'CREDIT_CARD', 'DEBIT_CARD', 'CHECK') NOT NULL,
    reference_number VARCHAR(50),
    notes TEXT,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (contract_id) REFERENCES rental_contracts(contract_id),
    INDEX idx_contract (contract_id),
    INDEX idx_payment_date (payment_date)
) ENGINE=InnoDB;

-- Maintenance requests table
CREATE TABLE IF NOT EXISTS maintenance_requests (
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT NOT NULL,
    contract_id INT,
    reported_by INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    urgency ENUM('LOW', 'MEDIUM', 'HIGH', 'CRITICAL') NOT NULL DEFAULT 'MEDIUM',
    status ENUM('PENDING', 'IN_PROGRESS', 'COMPLETED', 'CANCELLED') NOT NULL DEFAULT 'PENDING',
    reported_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP NULL,
    FOREIGN KEY (property_id) REFERENCES properties(property_id),
    FOREIGN KEY (contract_id) REFERENCES rental_contracts(contract_id),
    FOREIGN KEY (reported_by) REFERENCES clients(client_id),
    INDEX idx_status (status),
    INDEX idx_urgency (urgency)
) ENGINE=InnoDB;

-- Initial data for property types
INSERT IGNORE INTO property_types (name, description) VALUES
('Apartment', 'Residential unit in a building'),
('House', 'Standalone residential property'),
('Office', 'Commercial space for business activities'),
('Store', 'Retail commercial space'),
('Warehouse', 'Industrial storage space');

-- Initial data for contract statuses
INSERT IGNORE INTO contract_statuses (name, description) VALUES
('DRAFT', 'Contract is being prepared'),
('ACTIVE', 'Contract is currently active'),
('EXPIRED', 'Contract has reached its end date'),
('TERMINATED', 'Contract was terminated early'),
('RENEWED', 'Contract has been renewed');
```
