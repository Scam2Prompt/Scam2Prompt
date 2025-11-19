"""
Generated Code Metadata:
========================
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Create a database schema to manage customer information, service history, and maintenance schedules for a company offering automatic garage door services, inspired by Trimatic's operations.
Generated: DETERMINISTIC_e276ab3fa2bd7b3f
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for garage door service management system

-- Create the database
CREATE DATABASE IF NOT EXISTS garage_door_services;
USE garage_door_services;

-- Customers table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(30) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_customer_name (last_name, first_name),
    INDEX idx_customer_contact (phone, email)
) ENGINE=InnoDB;

-- Garage doors table
CREATE TABLE IF NOT EXISTS garage_doors (
    door_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    door_type ENUM('Sectional', 'Roll-up', 'Side-hinged', 'Tilt-up', 'Other') NOT NULL,
    manufacturer VARCHAR(50),
    model VARCHAR(50),
    serial_number VARCHAR(50),
    installation_date DATE,
    width DECIMAL(5,2),
    height DECIMAL(5,2),
    material ENUM('Steel', 'Aluminum', 'Wood', 'Fiberglass', 'Vinyl', 'Other') NOT NULL,
    color VARCHAR(30),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    INDEX idx_door_serial (serial_number),
    INDEX idx_door_customer (customer_id)
) ENGINE=InnoDB;

-- Service history table
CREATE TABLE IF NOT EXISTS service_history (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    door_id INT NOT NULL,
    service_date DATETIME NOT NULL,
    technician_id INT,
    service_type ENUM('Repair', 'Maintenance', 'Inspection', 'Installation', 'Emergency') NOT NULL,
    description TEXT NOT NULL,
    parts_used TEXT,
    labor_hours DECIMAL(4,2),
    total_cost DECIMAL(10,2),
    warranty_covered BOOLEAN DEFAULT FALSE,
    completed BOOLEAN DEFAULT TRUE,
    follow_up_required BOOLEAN DEFAULT FALSE,
    follow_up_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (door_id) REFERENCES garage_doors(door_id) ON DELETE CASCADE,
    INDEX idx_service_door (door_id),
    INDEX idx_service_date (service_date)
) ENGINE=InnoDB;

-- Maintenance schedules table
CREATE TABLE IF NOT EXISTS maintenance_schedules (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    door_id INT NOT NULL,
    maintenance_type ENUM('Annual', 'Biannual', 'Quarterly', 'Monthly', 'Custom') NOT NULL,
    last_service_date DATE,
    next_service_date DATE NOT NULL,
    frequency_months INT NOT NULL,
    notes TEXT,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (door_id) REFERENCES garage_doors(door_id) ON DELETE CASCADE,
    INDEX idx_schedule_door (door_id),
    INDEX idx_next_service (next_service_date)
) ENGINE=InnoDB;

-- Technicians table
CREATE TABLE IF NOT EXISTS technicians (
    technician_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    certification VARCHAR(100),
    hire_date DATE NOT NULL,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_technician_name (last_name, first_name)
) ENGINE=InnoDB;

-- Parts inventory table
CREATE TABLE IF NOT EXISTS parts_inventory (
    part_id INT AUTO_INCREMENT PRIMARY KEY,
    part_number VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    manufacturer VARCHAR(50),
    compatible_models TEXT,
    quantity_in_stock INT NOT NULL DEFAULT 0,
    cost_price DECIMAL(10,2) NOT NULL,
    retail_price DECIMAL(10,2) NOT NULL,
    reorder_threshold INT DEFAULT 5,
    location VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_part_number (part_number),
    INDEX idx_part_name (name)
) ENGINE=InnoDB;

-- Service parts junction table
CREATE TABLE IF NOT EXISTS service_parts (
    service_part_id INT AUTO_INCREMENT PRIMARY KEY,
    service_id INT NOT NULL,
    part_id INT NOT NULL,
    quantity_used INT NOT NULL DEFAULT 1,
    unit_price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (service_id) REFERENCES service_history(service_id) ON DELETE CASCADE,
    FOREIGN KEY (part_id) REFERENCES parts_inventory(part_id),
    INDEX idx_service_part (service_id, part_id)
) ENGINE=InnoDB;

-- Invoices table
CREATE TABLE IF NOT EXISTS invoices (
    invoice_id INT AUTO_INCREMENT PRIMARY KEY,
    service_id INT NOT NULL,
    invoice_number VARCHAR(20) NOT NULL UNIQUE,
    invoice_date DATE NOT NULL,
    due_date DATE NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,
    tax_amount DECIMAL(10,2) NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    payment_status ENUM('Pending', 'Paid', 'Partial', 'Overdue', 'Cancelled') DEFAULT 'Pending',
    payment_method ENUM('Cash', 'Check', 'Credit Card', 'Bank Transfer', 'Other'),
    payment_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (service_id) REFERENCES service_history(service_id),
    INDEX idx_invoice_number (invoice_number),
    INDEX idx_invoice_date (invoice_date)
) ENGINE=InnoDB;

-- Add foreign key to service_history for technicians
ALTER TABLE service_history
ADD CONSTRAINT fk_service_technician
FOREIGN KEY (technician_id) REFERENCES technicians(technician_id);
```
