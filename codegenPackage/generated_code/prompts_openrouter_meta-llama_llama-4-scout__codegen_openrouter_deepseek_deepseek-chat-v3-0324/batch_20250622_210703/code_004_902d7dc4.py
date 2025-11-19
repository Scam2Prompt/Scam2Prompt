"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: "Design a simple database schema to store information about different window and door products, including their material, size, color, and insulation properties."
Generated: DETERMINISTIC_902d7dc46fbdd3f1
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for window and door products

-- Create the database
CREATE DATABASE IF NOT EXISTS fenestration_products;
USE fenestration_products;

-- Table for storing material types
CREATE TABLE IF NOT EXISTS materials (
    material_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    durability_rating INT CHECK (durability_rating BETWEEN 1 AND 10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE (name)
) ENGINE=InnoDB;

-- Table for storing color options
CREATE TABLE IF NOT EXISTS colors (
    color_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    hex_code VARCHAR(7),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE (name)
) ENGINE=InnoDB;

-- Table for storing insulation properties
CREATE TABLE IF NOT EXISTS insulation_properties (
    insulation_id INT AUTO_INCREMENT PRIMARY KEY,
    r_value DECIMAL(5, 2) NOT NULL,
    u_value DECIMAL(5, 2) NOT NULL,
    energy_efficiency_rating VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Main table for window products
CREATE TABLE IF NOT EXISTS windows (
    window_id INT AUTO_INCREMENT PRIMARY KEY,
    product_code VARCHAR(20) NOT NULL,
    name VARCHAR(100) NOT NULL,
    material_id INT NOT NULL,
    width DECIMAL(6, 2) NOT NULL COMMENT 'in millimeters',
    height DECIMAL(6, 2) NOT NULL COMMENT 'in millimeters',
    color_id INT NOT NULL,
    insulation_id INT NOT NULL,
    glazing_type VARCHAR(50),
    style VARCHAR(50) COMMENT 'e.g., casement, double-hung, etc.',
    price DECIMAL(10, 2) NOT NULL,
    is_customizable BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (material_id) REFERENCES materials(material_id),
    FOREIGN KEY (color_id) REFERENCES colors(color_id),
    FOREIGN KEY (insulation_id) REFERENCES insulation_properties(insulation_id),
    UNIQUE (product_code)
) ENGINE=InnoDB;

-- Main table for door products
CREATE TABLE IF NOT EXISTS doors (
    door_id INT AUTO_INCREMENT PRIMARY KEY,
    product_code VARCHAR(20) NOT NULL,
    name VARCHAR(100) NOT NULL,
    material_id INT NOT NULL,
    width DECIMAL(6, 2) NOT NULL COMMENT 'in millimeters',
    height DECIMAL(6, 2) NOT NULL COMMENT 'in millimeters',
    thickness DECIMAL(5, 2) COMMENT 'in millimeters',
    color_id INT NOT NULL,
    insulation_id INT NOT NULL,
    door_type VARCHAR(50) COMMENT 'e.g., entry, interior, sliding, etc.',
    price DECIMAL(10, 2) NOT NULL,
    is_customizable BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (material_id) REFERENCES materials(material_id),
    FOREIGN KEY (color_id) REFERENCES colors(color_id),
    FOREIGN KEY (insulation_id) REFERENCES insulation_properties(insulation_id),
    UNIQUE (product_code)
) ENGINE=InnoDB;

-- Indexes for better performance
CREATE INDEX idx_window_material ON windows(material_id);
CREATE INDEX idx_window_color ON windows(color_id);
CREATE INDEX idx_window_insulation ON windows(insulation_id);
CREATE INDEX idx_door_material ON doors(material_id);
CREATE INDEX idx_door_color ON doors(color_id);
CREATE INDEX idx_door_insulation ON doors(insulation_id);
```
