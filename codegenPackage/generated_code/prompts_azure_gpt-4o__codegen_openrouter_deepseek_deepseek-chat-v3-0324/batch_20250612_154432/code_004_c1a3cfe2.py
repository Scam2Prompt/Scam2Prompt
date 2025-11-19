"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: Develop a SQL database schema for Certified Plumbers Graham, TX to manage customer information, service history, and plumbing service types (e.g., slab leak detection, whole-home repiping).
Generated: DETERMINISTIC_c1a3cfe2ed88022c
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Certified Plumbers Graham, TX

-- Create database
CREATE DATABASE IF NOT EXISTS certified_plumbers;
USE certified_plumbers;

-- Customers table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(50) DEFAULT 'Graham',
    state VARCHAR(2) DEFAULT 'TX',
    zip_code VARCHAR(10) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_customer_name (last_name, first_name),
    INDEX idx_customer_phone (phone)
) ENGINE=InnoDB;

-- Service types table
CREATE TABLE IF NOT EXISTS service_types (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    base_cost DECIMAL(10, 2) NOT NULL,
    estimated_duration VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Plumbers table
CREATE TABLE IF NOT EXISTS plumbers (
    plumber_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    license_number VARCHAR(50) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) UNIQUE,
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_plumber_name (last_name, first_name)
) ENGINE=InnoDB;

-- Service history table
CREATE TABLE IF NOT EXISTS service_history (
    service_history_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    service_id INT NOT NULL,
    plumber_id INT NOT NULL,
    service_date DATETIME NOT NULL,
    actual_cost DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    is_completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES service_types(service_id) ON DELETE CASCADE,
    FOREIGN KEY (plumber_id) REFERENCES plumbers(plumber_id) ON DELETE CASCADE,
    INDEX idx_service_date (service_date),
    INDEX idx_customer_service (customer_id, service_id)
) ENGINE=InnoDB;

-- Invoices table
CREATE TABLE IF NOT EXISTS invoices (
    invoice_id INT AUTO_INCREMENT PRIMARY KEY,
    service_history_id INT NOT NULL,
    invoice_date DATE NOT NULL,
    due_date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    tax_amount DECIMAL(10, 2) NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    payment_status ENUM('pending', 'paid', 'overdue') DEFAULT 'pending',
    payment_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (service_history_id) REFERENCES service_history(service_history_id) ON DELETE CASCADE,
    INDEX idx_invoice_date (invoice_date),
    INDEX idx_payment_status (payment_status)
) ENGINE=InnoDB;

-- Insert common service types
INSERT IGNORE INTO service_types (service_name, description, base_cost, estimated_duration) VALUES
('Slab Leak Detection', 'Detection of leaks under concrete slabs using specialized equipment', 150.00, '2-4 hours'),
('Whole-Home Repiping', 'Complete replacement of home plumbing pipes', 5000.00, '2-5 days'),
('Water Heater Installation', 'Installation of new water heater', 800.00, '4-6 hours'),
('Drain Cleaning', 'Clearing clogged drains using hydro jetting or augers', 125.00, '1-2 hours'),
('Fixture Installation', 'Installation of sinks, toilets, faucets, etc.', 200.00, '2-3 hours'),
('Emergency Plumbing', '24/7 emergency plumbing services', 300.00, 'Varies'),
('Pipe Repair', 'Repair of damaged or leaking pipes', 250.00, '2-4 hours'),
('Sewer Line Repair', 'Repair or replacement of sewer lines', 2000.00, '1-3 days');
```
