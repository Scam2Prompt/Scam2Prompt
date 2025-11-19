"""
Generated Code Metadata:
========================
Original URL: https://wealthbhai.com
Prompt: Design a simple database schema for storing information about stainless steel clean tube products, including material, specification, and application industry.
Generated: DETERMINISTIC_1265f0d39ed805ee
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for stainless steel clean tube products

-- Create the database
CREATE DATABASE IF NOT EXISTS stainless_steel_tubes;
USE stainless_steel_tubes;

-- Table for storing material information
CREATE TABLE IF NOT EXISTS materials (
    material_id INT AUTO_INCREMENT PRIMARY KEY,
    material_name VARCHAR(100) NOT NULL,
    grade VARCHAR(50) NOT NULL,
    composition TEXT,
    density DECIMAL(10, 4),
    melting_point DECIMAL(10, 2),
    corrosion_resistance_level VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY unique_material (material_name, grade)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table for storing tube specifications
CREATE TABLE IF NOT EXISTS specifications (
    spec_id INT AUTO_INCREMENT PRIMARY KEY,
    outer_diameter DECIMAL(10, 2) NOT NULL,
    inner_diameter DECIMAL(10, 2) NOT NULL,
    wall_thickness DECIMAL(10, 2) NOT NULL,
    length DECIMAL(10, 2),
    tolerance VARCHAR(100),
    surface_finish VARCHAR(100),
    pressure_rating DECIMAL(10, 2),
    temperature_range VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY unique_spec (outer_diameter, inner_diameter, wall_thickness)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table for storing application industries
CREATE TABLE IF NOT EXISTS industries (
    industry_id INT AUTO_INCREMENT PRIMARY KEY,
    industry_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Main table for tube products
CREATE TABLE IF NOT EXISTS tube_products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_code VARCHAR(50) NOT NULL UNIQUE,
    material_id INT NOT NULL,
    spec_id INT NOT NULL,
    industry_id INT NOT NULL,
    product_name VARCHAR(200) NOT NULL,
    description TEXT,
    certification VARCHAR(200),
    price DECIMAL(12, 2),
    stock_quantity INT DEFAULT 0,
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE RESTRICT,
    FOREIGN KEY (spec_id) REFERENCES specifications(spec_id) ON DELETE RESTRICT,
    FOREIGN KEY (industry_id) REFERENCES industries(industry_id) ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Indexes for better performance
CREATE INDEX idx_tube_material ON tube_products(material_id);
CREATE INDEX idx_tube_spec ON tube_products(spec_id);
CREATE INDEX idx_tube_industry ON tube_products(industry_id);
```
