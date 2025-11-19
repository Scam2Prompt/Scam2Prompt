"""
Generated Code Metadata:
========================
Original URL: https://panchsheelbank.com
Prompt: Create a database schema for managing safe deposit locker allocations, inspired by the services offered by Panchsheel Mercantile Co-op. Bank Ltd.
Generated: DETERMINISTIC_c426045e9e12ce4c
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Safe Deposit Locker Management System

-- Create the database
CREATE DATABASE IF NOT EXISTS locker_management_system;
USE locker_management_system;

-- Table for storing branch information
CREATE TABLE IF NOT EXISTS branches (
    branch_id INT AUTO_INCREMENT PRIMARY KEY,
    branch_name VARCHAR(100) NOT NULL,
    address TEXT NOT NULL,
    contact_number VARCHAR(15) NOT NULL,
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (branch_name)
) ENGINE=InnoDB;

-- Table for storing locker types and sizes
CREATE TABLE IF NOT EXISTS locker_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL,
    dimensions VARCHAR(50) NOT NULL,
    annual_rent DECIMAL(10, 2) NOT NULL,
    security_deposit DECIMAL(10, 2) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (type_name)
) ENGINE=InnoDB;

-- Table for storing physical locker boxes
CREATE TABLE IF NOT EXISTS lockers (
    locker_id INT AUTO_INCREMENT PRIMARY KEY,
    branch_id INT NOT NULL,
    type_id INT NOT NULL,
    locker_number VARCHAR(20) NOT NULL,
    status ENUM('available', 'occupied', 'under_maintenance') DEFAULT 'available',
    location_description VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (branch_id) REFERENCES branches(branch_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES locker_types(type_id) ON DELETE CASCADE,
    UNIQUE KEY (branch_id, locker_number)
) ENGINE=InnoDB;

-- Table for storing customer information
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('male', 'female', 'other'),
    address TEXT NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(50) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    email VARCHAR(100),
    id_proof_type VARCHAR(50) NOT NULL,
    id_proof_number VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (id_proof_type, id_proof_number)
) ENGINE=InnoDB;

-- Table for storing locker rental agreements
CREATE TABLE IF NOT EXISTS locker_allocations (
    allocation_id INT AUTO_INCREMENT PRIMARY KEY,
    locker_id INT NOT NULL,
    customer_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    annual_rent DECIMAL(10, 2) NOT NULL,
    security_deposit DECIMAL(10, 2) NOT NULL,
    payment_status ENUM('paid', 'unpaid', 'partial') DEFAULT 'unpaid',
    status ENUM('active', 'terminated', 'expired') DEFAULT 'active',
    nominee_name VARCHAR(100),
    nominee_relation VARCHAR(50),
    nominee_contact VARCHAR(15),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (locker_id) REFERENCES lockers(locker_id) ON DELETE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    CHECK (end_date > start_date)
) ENGINE=InnoDB;

-- Table for storing payment transactions
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    allocation_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATE NOT NULL,
    payment_method ENUM('cash', 'cheque', 'online_transfer', 'card') NOT NULL,
    transaction_reference VARCHAR(100),
    received_by VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (allocation_id) REFERENCES locker_allocations(allocation_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for storing locker access logs
CREATE TABLE IF NOT EXISTS access_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    allocation_id INT NOT NULL,
    access_time DATETIME NOT NULL,
    accessed_by VARCHAR(100) NOT NULL,
    purpose VARCHAR(255),
    staff_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (allocation_id) REFERENCES locker_allocations(allocation_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for storing system users (bank staff)
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    branch_id INT,
    username VARCHAR(50) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    role ENUM('admin', 'manager', 'staff') NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    last_login DATETIME,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (branch_id) REFERENCES branches(branch_id) ON DELETE SET NULL,
    UNIQUE KEY (username),
    UNIQUE KEY (email)
) ENGINE=InnoDB;

-- Table for storing system audit logs
CREATE TABLE IF NOT EXISTS audit_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    action VARCHAR(50) NOT NULL,
    table_name VARCHAR(50) NOT NULL,
    record_id INT,
    old_values TEXT,
    new_values TEXT,
    ip_address VARCHAR(45),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- Indexes for better performance
CREATE INDEX idx_lockers_branch ON lockers(branch_id);
CREATE INDEX idx_lockers_type ON lockers(type_id);
CREATE INDEX idx_allocations_customer ON locker_allocations(customer_id);
CREATE INDEX idx_allocations_locker ON locker_allocations(locker_id);
CREATE INDEX idx_payments_allocation ON payments(allocation_id);
CREATE INDEX idx_access_logs_allocation ON access_logs(allocation_id);
```
