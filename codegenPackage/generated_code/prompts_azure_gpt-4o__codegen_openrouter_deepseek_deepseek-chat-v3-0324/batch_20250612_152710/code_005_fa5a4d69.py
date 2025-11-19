"""
Generated Code Metadata:
========================
Original URL: https://plm.cr
Prompt: Create a database schema for tracking logistics operations across different regimes, such as industrial zones, free trade zones, and fiscal storage zones, as described by PLM.
Generated: DETERMINISTIC_fa5a4d692b89d327
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking logistics operations across different regimes

-- Create the database
CREATE DATABASE IF NOT EXISTS logistics_tracking;
USE logistics_tracking;

-- Table for different regime types
CREATE TABLE IF NOT EXISTS regimes (
    regime_id INT AUTO_INCREMENT PRIMARY KEY,
    regime_name VARCHAR(100) NOT NULL,
    description TEXT,
    customs_requirements TEXT,
    tax_implications TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (regime_name)
) ENGINE=InnoDB;

-- Table for locations/zones
CREATE TABLE IF NOT EXISTS zones (
    zone_id INT AUTO_INCREMENT PRIMARY KEY,
    zone_name VARCHAR(100) NOT NULL,
    regime_id INT NOT NULL,
    location_code VARCHAR(50) NOT NULL,
    address TEXT,
    country VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    contact_email VARCHAR(100),
    contact_phone VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (regime_id) REFERENCES regimes(regime_id) ON DELETE CASCADE,
    UNIQUE KEY (location_code)
) ENGINE=InnoDB;

-- Table for goods/products
CREATE TABLE IF NOT EXISTS goods (
    goods_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    hs_code VARCHAR(50),
    weight DECIMAL(10,2),
    volume DECIMAL(10,2),
    unit_of_measure VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for logistics operations
CREATE TABLE IF NOT EXISTS operations (
    operation_id INT AUTO_INCREMENT PRIMARY KEY,
    operation_type ENUM('import', 'export', 'transfer', 'storage') NOT NULL,
    reference_number VARCHAR(100) NOT NULL,
    origin_zone_id INT,
    destination_zone_id INT,
    planned_date DATETIME,
    actual_date DATETIME,
    status ENUM('planned', 'in_transit', 'completed', 'cancelled') NOT NULL DEFAULT 'planned',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (origin_zone_id) REFERENCES zones(zone_id) ON DELETE SET NULL,
    FOREIGN KEY (destination_zone_id) REFERENCES zones(zone_id) ON DELETE SET NULL,
    UNIQUE KEY (reference_number)
) ENGINE=InnoDB;

-- Junction table for goods in operations
CREATE TABLE IF NOT EXISTS operation_goods (
    operation_goods_id INT AUTO_INCREMENT PRIMARY KEY,
    operation_id INT NOT NULL,
    goods_id INT NOT NULL,
    quantity INT NOT NULL,
    declared_value DECIMAL(12,2),
    customs_status VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (operation_id) REFERENCES operations(operation_id) ON DELETE CASCADE,
    FOREIGN KEY (goods_id) REFERENCES goods(goods_id) ON DELETE CASCADE,
    UNIQUE KEY (operation_id, goods_id)
) ENGINE=InnoDB;

-- Table for documents related to operations
CREATE TABLE IF NOT EXISTS documents (
    document_id INT AUTO_INCREMENT PRIMARY KEY,
    operation_id INT NOT NULL,
    document_type VARCHAR(100) NOT NULL,
    document_number VARCHAR(100) NOT NULL,
    issue_date DATE,
    expiry_date DATE,
    file_path VARCHAR(255),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (operation_id) REFERENCES operations(operation_id) ON DELETE CASCADE,
    UNIQUE KEY (document_number)
) ENGINE=InnoDB;

-- Table for compliance checks
CREATE TABLE IF NOT EXISTS compliance_checks (
    check_id INT AUTO_INCREMENT PRIMARY KEY,
    operation_id INT NOT NULL,
    check_type VARCHAR(100) NOT NULL,
    check_status ENUM('pending', 'passed', 'failed', 'exception') NOT NULL DEFAULT 'pending',
    performed_by VARCHAR(100),
    performed_at DATETIME,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (operation_id) REFERENCES operations(operation_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for audit logs
CREATE TABLE IF NOT EXISTS audit_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(100),
    action VARCHAR(100) NOT NULL,
    entity_type VARCHAR(100) NOT NULL,
    entity_id INT,
    old_values JSON,
    new_values JSON,
    ip_address VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Initial data for common regimes
INSERT INTO regimes (regime_name, description, customs_requirements, tax_implications)
VALUES 
    ('Industrial Zone', 'Designated area for manufacturing and industrial activities', 'Customs clearance required for goods entering/exiting', 'Tax benefits for manufacturing activities'),
    ('Free Trade Zone', 'Area where goods may be landed, handled, manufactured or reconfigured without customs intervention', 'No customs duties unless entering domestic market', 'No VAT or import taxes while in zone'),
    ('Fiscal Storage Zone', 'Warehousing area with special tax treatment', 'Customs supervision required', 'Suspended VAT and duties until release for consumption');
```
