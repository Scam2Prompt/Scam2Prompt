"""
Generated Code Metadata:
========================
Original URL: https://trackdieselperu.com
Prompt: "Create a SQL database schema to store information about heavy machinery, their spare parts, and maintenance services offered by a company like Track Diesel Peru S.R.L."
Generated: DETERMINISTIC_0391f4c7bb75d285
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# SQL Database Schema for Heavy Machinery Management System

```sql
-- Database schema for Track Diesel Peru S.R.L. machinery management system
-- Creates tables for machinery, spare parts, services, and maintenance records

CREATE TABLE manufacturers (
    manufacturer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(50),
    contact_email VARCHAR(100),
    contact_phone VARCHAR(20),
    website VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_manufacturer_email CHECK (contact_email LIKE '%@%.%')
);

CREATE TABLE machinery_types (
    type_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE machinery (
    machine_id INT PRIMARY KEY AUTO_INCREMENT,
    serial_number VARCHAR(50) UNIQUE NOT NULL,
    model VARCHAR(100) NOT NULL,
    manufacturer_id INT NOT NULL,
    type_id INT NOT NULL,
    purchase_date DATE,
    purchase_price DECIMAL(12, 2),
    current_value DECIMAL(12, 2),
    operational_status ENUM('operational', 'maintenance', 'out_of_service', 'retired') DEFAULT 'operational',
    last_maintenance_date DATE,
    next_maintenance_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id),
    FOREIGN KEY (type_id) REFERENCES machinery_types(type_id),
    CONSTRAINT chk_machine_dates CHECK (purchase_date <= last_maintenance_date AND last_maintenance_date <= next_maintenance_date)
);

CREATE TABLE spare_parts (
    part_id INT PRIMARY KEY AUTO_INCREMENT,
    part_number VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    compatible_machine_types JSON,
    manufacturer_id INT,
    unit_price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    min_stock_level INT DEFAULT 5,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id),
    CONSTRAINT chk_part_price CHECK (unit_price > 0),
    CONSTRAINT chk_part_stock CHECK (stock_quantity >= 0)
);

CREATE TABLE service_types (
    service_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    standard_duration_minutes INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE maintenance_services (
    maintenance_id INT PRIMARY KEY AUTO_INCREMENT,
    machine_id INT NOT NULL,
    service_id INT NOT NULL,
    service_date DATE NOT NULL,
    completion_date DATE,
    technician_notes TEXT,
    cost DECIMAL(10, 2),
    status ENUM('scheduled', 'in_progress', 'completed', 'cancelled') DEFAULT 'scheduled',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (machine_id) REFERENCES machinery(machine_id),
    FOREIGN KEY (service_id) REFERENCES service_types(service_id),
    CONSTRAINT chk_service_dates CHECK (service_date <= completion_date)
);

CREATE TABLE maintenance_parts (
    maintenance_part_id INT PRIMARY KEY AUTO_INCREMENT,
    maintenance_id INT NOT NULL,
    part_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    unit_price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (maintenance_id) REFERENCES maintenance_services(maintenance_id),
    FOREIGN KEY (part_id) REFERENCES spare_parts(part_id),
    CONSTRAINT chk_maintenance_part_quantity CHECK (quantity > 0),
    CONSTRAINT chk_maintenance_part_price CHECK (unit_price >= 0)
);

CREATE TABLE clients (
    client_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    tax_id VARCHAR(20),
    address TEXT,
    contact_person VARCHAR(100),
    contact_email VARCHAR(100),
    contact_phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_client_email CHECK (contact_email LIKE '%@%.%')
);

CREATE TABLE service_contracts (
    contract_id INT PRIMARY KEY AUTO_INCREMENT,
    client_id INT NOT NULL,
    machine_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    service_interval_days INT NOT NULL,
    contract_value DECIMAL(12, 2) NOT NULL,
    payment_status ENUM('active', 'cancelled', 'completed') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (machine_id) REFERENCES machinery(machine_id),
    CONSTRAINT chk_contract_dates CHECK (start_date < end_date),
    CONSTRAINT chk_contract_interval CHECK (service_interval_days > 0)
);

CREATE TABLE invoices (
    invoice_id INT PRIMARY KEY AUTO_INCREMENT,
    contract_id INT,
    client_id INT NOT NULL,
    invoice_date DATE NOT NULL,
    due_date DATE NOT NULL,
    total_amount DECIMAL(12, 2) NOT NULL,
    tax_amount DECIMAL(12, 2) NOT NULL,
    status ENUM('draft', 'sent', 'paid', 'overdue', 'cancelled') DEFAULT 'draft',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (contract_id) REFERENCES service_contracts(contract_id),
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    CONSTRAINT chk_invoice_dates CHECK (invoice_date <= due_date),
    CONSTRAINT chk_invoice_amounts CHECK (total_amount > 0 AND tax_amount >= 0)
);

CREATE TABLE invoice_items (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    invoice_id INT NOT NULL,
    description VARCHAR(255) NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    unit_price DECIMAL(10, 2) NOT NULL,
    tax_rate DECIMAL(5, 2) DEFAULT 0.18,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (invoice_id) REFERENCES invoices(invoice_id),
    CONSTRAINT chk_item_quantity CHECK (quantity > 0),
    CONSTRAINT chk_item_price CHECK (unit_price >= 0),
    CONSTRAINT chk_tax_rate CHECK (tax_rate >= 0 AND tax_rate <= 1)
);

-- Indexes for performance optimization
CREATE INDEX idx_machine_serial ON machinery(serial_number);
CREATE INDEX idx_part_number ON spare_parts(part_number);
CREATE INDEX idx_maintenance_machine ON maintenance_services(machine_id);
CREATE INDEX idx_maintenance_date ON maintenance_services(service_date);
CREATE INDEX idx_contract_client ON service_contracts(client_id);
CREATE INDEX idx_invoice_client ON invoices(client_id);
CREATE INDEX idx_invoice_status ON invoices(status);
```
