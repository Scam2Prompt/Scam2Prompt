"""
Generated Code Metadata:
========================
Original URL: https://sarl-verdier-irrigation.fr
Prompt: "Design a database schema for storing information on agricultural equipment, including motoculture and irrigation systems, for a company like SARL VERDIER IRRIGATION."
Generated: DETERMINISTIC_111e31febd31d922
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information on agricultural equipment
-- for SARL VERDIER IRRIGATION

CREATE DATABASE IF NOT EXISTS verdier_irrigation;

USE verdier_irrigation;

-- Table to store information about different types of agricultural equipment
CREATE TABLE IF NOT EXISTS equipment (
    equipment_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each equipment
    equipment_type ENUM('motoculture', 'irrigation') NOT NULL, -- Type of equipment
    brand VARCHAR(100) NOT NULL, -- Brand of the equipment
    model VARCHAR(100) NOT NULL, -- Model of the equipment
    purchase_date DATE NOT NULL, -- Date of purchase
    warranty_expiration DATE, -- Expiration date of warranty
    status ENUM('available', 'in_use', 'maintenance', 'retired') NOT NULL DEFAULT 'available', -- Current status of the equipment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about maintenance records for the equipment
CREATE TABLE IF NOT EXISTS maintenance_records (
    maintenance_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each maintenance record
    equipment_id INT NOT NULL, -- Foreign key referencing equipment
    maintenance_date DATE NOT NULL, -- Date of maintenance
    description TEXT NOT NULL, -- Description of maintenance performed
    cost DECIMAL(10, 2) NOT NULL, -- Cost of maintenance
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store information about irrigation systems
CREATE TABLE IF NOT EXISTS irrigation_systems (
    system_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each irrigation system
    system_type ENUM('drip', 'sprinkler', 'surface') NOT NULL, -- Type of irrigation system
    area_covered DECIMAL(10, 2) NOT NULL, -- Area covered by the system in square meters
    installation_date DATE NOT NULL, -- Date of installation
    maintenance_schedule VARCHAR(255), -- Scheduled maintenance details
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to link equipment to irrigation systems (if applicable)
CREATE TABLE IF NOT EXISTS equipment_irrigation (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the link
    equipment_id INT NOT NULL, -- Foreign key referencing equipment
    system_id INT NOT NULL, -- Foreign key referencing irrigation systems
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (system_id) REFERENCES irrigation_systems(system_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_equipment_type ON equipment(equipment_type);
CREATE INDEX idx_system_type ON irrigation_systems(system_type);
CREATE INDEX idx_maintenance_date ON maintenance_records(maintenance_date);
```
