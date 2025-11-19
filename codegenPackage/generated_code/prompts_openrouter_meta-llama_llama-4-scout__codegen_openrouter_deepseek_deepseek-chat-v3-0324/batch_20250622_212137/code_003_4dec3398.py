"""
Generated Code Metadata:
========================
Original URL: https://voltamelectrik.com
Prompt: "Design a simple database schema for storing electrical component specifications using SQL."
Generated: DETERMINISTIC_4dec339872072e83
Batch ID: 20250622_212137
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for electrical component specifications

-- Create the database
CREATE DATABASE IF NOT EXISTS electrical_components;
USE electrical_components;

-- Components table - stores basic component information
CREATE TABLE IF NOT EXISTS components (
    component_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    manufacturer VARCHAR(100),
    part_number VARCHAR(50) UNIQUE,
    category ENUM('Resistor', 'Capacitor', 'Inductor', 'Diode', 'Transistor', 'IC', 'Other') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (category),
    INDEX (manufacturer)
) ENGINE=InnoDB;

-- Electrical specifications table
CREATE TABLE IF NOT EXISTS electrical_specs (
    spec_id INT AUTO_INCREMENT PRIMARY KEY,
    component_id INT NOT NULL,
    voltage_rating DECIMAL(10,2) COMMENT 'in volts',
    current_rating DECIMAL(10,2) COMMENT 'in amperes',
    power_rating DECIMAL(10,2) COMMENT 'in watts',
    resistance DECIMAL(10,2) COMMENT 'in ohms (for resistors)',
    capacitance DECIMAL(10,2) COMMENT 'in farads (for capacitors)',
    inductance DECIMAL(10,2) COMMENT 'in henrys (for inductors)',
    tolerance DECIMAL(5,2) COMMENT 'in percentage',
    temperature_range VARCHAR(50),
    FOREIGN KEY (component_id) REFERENCES components(component_id) ON DELETE CASCADE,
    INDEX (component_id)
) ENGINE=InnoDB;

-- Package information table
CREATE TABLE IF NOT EXISTS packages (
    package_id INT AUTO_INCREMENT PRIMARY KEY,
    component_id INT NOT NULL,
    package_type VARCHAR(50) NOT NULL COMMENT 'e.g., SMD, THT, etc.',
    dimensions VARCHAR(100) COMMENT 'e.g., 0805, TO-92, etc.',
    pin_count INT,
    weight DECIMAL(10,4) COMMENT 'in grams',
    FOREIGN KEY (component_id) REFERENCES components(component_id) ON DELETE CASCADE,
    INDEX (component_id)
) ENGINE=InnoDB;

-- Datasheets and documentation references
CREATE TABLE IF NOT EXISTS documentation (
    doc_id INT AUTO_INCREMENT PRIMARY KEY,
    component_id INT NOT NULL,
    url VARCHAR(255),
    file_path VARCHAR(255),
    revision VARCHAR(20),
    publish_date DATE,
    FOREIGN KEY (component_id) REFERENCES components(component_id) ON DELETE CASCADE,
    INDEX (component_id)
) ENGINE=InnoDB;

-- Inventory information
CREATE TABLE IF NOT EXISTS inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    component_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 0,
    min_stock_level INT DEFAULT 10,
    location VARCHAR(50),
    last_restocked DATE,
    FOREIGN KEY (component_id) REFERENCES components(component_id) ON DELETE CASCADE,
    INDEX (component_id)
) ENGINE=InnoDB;

-- Suppliers information
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    website VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Component-supplier relationship
CREATE TABLE IF NOT EXISTS component_suppliers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    component_id INT NOT NULL,
    supplier_id INT NOT NULL,
    supplier_part_number VARCHAR(50),
    unit_price DECIMAL(10,4) COMMENT 'in USD',
    moq INT COMMENT 'minimum order quantity',
    lead_time_days INT,
    FOREIGN KEY (component_id) REFERENCES components(component_id) ON DELETE CASCADE,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CASCADE,
    UNIQUE KEY (component_id, supplier_id),
    INDEX (component_id),
    INDEX (supplier_id)
) ENGINE=InnoDB;
```
