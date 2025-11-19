"""
Generated Code Metadata:
========================
Original URL: https://www.specialmetal.ir
Prompt: Develop a simple database schema to store information about superalloys, including their types, applications, and standards (e.g., ASTM, BS, JIS).
Generated: DETERMINISTIC_21b173d07877cd53
Batch ID: 20250622_212806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for superalloys information system

-- Create database
CREATE DATABASE IF NOT EXISTS superalloys_db;
USE superalloys_db;

-- Table for alloy types
CREATE TABLE IF NOT EXISTS alloy_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (type_name)
) ENGINE=InnoDB;

-- Table for standards organizations
CREATE TABLE IF NOT EXISTS standards_organizations (
    org_id INT AUTO_INCREMENT PRIMARY KEY,
    org_name VARCHAR(100) NOT NULL,
    org_code VARCHAR(10) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (org_code)
) ENGINE=InnoDB;

-- Table for superalloys
CREATE TABLE IF NOT EXISTS superalloys (
    alloy_id INT AUTO_INCREMENT PRIMARY KEY,
    common_name VARCHAR(100) NOT NULL,
    chemical_name VARCHAR(100),
    type_id INT NOT NULL,
    description TEXT,
    melting_point DECIMAL(10,2),
    density DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES alloy_types(type_id) ON DELETE RESTRICT,
    UNIQUE KEY (common_name)
) ENGINE=InnoDB;

-- Table for applications
CREATE TABLE IF NOT EXISTS applications (
    application_id INT AUTO_INCREMENT PRIMARY KEY,
    application_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (application_name)
) ENGINE=InnoDB;

-- Table for alloy standards
CREATE TABLE IF NOT EXISTS alloy_standards (
    standard_id INT AUTO_INCREMENT PRIMARY KEY,
    alloy_id INT NOT NULL,
    org_id INT NOT NULL,
    standard_code VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (alloy_id) REFERENCES superalloys(alloy_id) ON DELETE CASCADE,
    FOREIGN KEY (org_id) REFERENCES standards_organizations(org_id) ON DELETE RESTRICT,
    UNIQUE KEY (alloy_id, org_id, standard_code)
) ENGINE=InnoDB;

-- Junction table for alloy applications
CREATE TABLE IF NOT EXISTS alloy_applications (
    alloy_id INT NOT NULL,
    application_id INT NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (alloy_id, application_id),
    FOREIGN KEY (alloy_id) REFERENCES superalloys(alloy_id) ON DELETE CASCADE,
    FOREIGN KEY (application_id) REFERENCES applications(application_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for alloy compositions
CREATE TABLE IF NOT EXISTS alloy_compositions (
    composition_id INT AUTO_INCREMENT PRIMARY KEY,
    alloy_id INT NOT NULL,
    element VARCHAR(50) NOT NULL,
    min_percentage DECIMAL(5,2),
    max_percentage DECIMAL(5,2),
    typical_percentage DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (alloy_id) REFERENCES superalloys(alloy_id) ON DELETE CASCADE,
    UNIQUE KEY (alloy_id, element)
) ENGINE=InnoDB;

-- Table for mechanical properties
CREATE TABLE IF NOT EXISTS mechanical_properties (
    property_id INT AUTO_INCREMENT PRIMARY KEY,
    alloy_id INT NOT NULL,
    temperature DECIMAL(10,2) NOT NULL,
    tensile_strength DECIMAL(10,2),
    yield_strength DECIMAL(10,2),
    elongation DECIMAL(10,2),
    hardness VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (alloy_id) REFERENCES superalloys(alloy_id) ON DELETE CASCADE,
    UNIQUE KEY (alloy_id, temperature)
) ENGINE=InnoDB;

-- Indexes for performance
CREATE INDEX idx_superalloys_type ON superalloys(type_id);
CREATE INDEX idx_alloy_standards_alloy ON alloy_standards(alloy_id);
CREATE INDEX idx_alloy_standards_org ON alloy_standards(org_id);
CREATE INDEX idx_alloy_applications_alloy ON alloy_applications(alloy_id);
CREATE INDEX idx_alloy_applications_app ON alloy_applications(application_id);
CREATE INDEX idx_alloy_compositions_alloy ON alloy_compositions(alloy_id);
CREATE INDEX idx_mechanical_properties_alloy ON mechanical_properties(alloy_id);
```
