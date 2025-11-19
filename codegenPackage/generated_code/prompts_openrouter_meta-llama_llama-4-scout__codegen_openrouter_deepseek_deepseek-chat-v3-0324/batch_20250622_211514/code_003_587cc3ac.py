"""
Generated Code Metadata:
========================
Original URL: https://therammaninc.com
Prompt: "Design a database schema to store information about various locking hub products, including Dodge RAM, Chevy/GMC, and Toyota models."
Generated: DETERMINISTIC_587cc3ac63925182
Batch ID: 20250622_211514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for locking hub products
-- Supports Dodge RAM, Chevy/GMC, and Toyota models with proper relationships

-- First, ensure the database exists
CREATE DATABASE IF NOT EXISTS locking_hub_products;
USE locking_hub_products;

-- Table to store vehicle makes
CREATE TABLE IF NOT EXISTS vehicle_makes (
    make_id INT AUTO_INCREMENT PRIMARY KEY,
    make_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT uc_make_name UNIQUE (make_name)
) ENGINE=InnoDB;

-- Table to store vehicle models
CREATE TABLE IF NOT EXISTS vehicle_models (
    model_id INT AUTO_INCREMENT PRIMARY KEY,
    make_id INT NOT NULL,
    model_name VARCHAR(50) NOT NULL,
    generation VARCHAR(50),
    production_years VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_make FOREIGN KEY (make_id) REFERENCES vehicle_makes(make_id) ON DELETE CASCADE,
    CONSTRAINT uc_model_make UNIQUE (make_id, model_name, generation)
) ENGINE=InnoDB;

-- Table to store hub product types
CREATE TABLE IF NOT EXISTS hub_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT uc_type_name UNIQUE (type_name)
) ENGINE=InnoDB;

-- Table to store locking hub products
CREATE TABLE IF NOT EXISTS locking_hubs (
    hub_id INT AUTO_INCREMENT PRIMARY KEY,
    model_id INT NOT NULL,
    type_id INT NOT NULL,
    part_number VARCHAR(50) NOT NULL,
    description TEXT,
    material VARCHAR(50),
    finish VARCHAR(50),
    thread_size VARCHAR(20),
    price DECIMAL(10, 2),
    in_stock BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_model FOREIGN KEY (model_id) REFERENCES vehicle_models(model_id) ON DELETE CASCADE,
    CONSTRAINT fk_type FOREIGN KEY (type_id) REFERENCES hub_types(type_id) ON DELETE CASCADE,
    CONSTRAINT uc_part_number UNIQUE (part_number)
) ENGINE=InnoDB;

-- Table to store product images
CREATE TABLE IF NOT EXISTS product_images (
    image_id INT AUTO_INCREMENT PRIMARY KEY,
    hub_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_hub FOREIGN KEY (hub_id) REFERENCES locking_hubs(hub_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table to store compatibility notes
CREATE TABLE IF NOT EXISTS compatibility_notes (
    note_id INT AUTO_INCREMENT PRIMARY KEY,
    hub_id INT NOT NULL,
    note TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_hub_note FOREIGN KEY (hub_id) REFERENCES locking_hubs(hub_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Indexes for performance optimization
CREATE INDEX idx_hub_model ON locking_hubs(model_id);
CREATE INDEX idx_hub_type ON locking_hubs(type_id);
CREATE INDEX idx_hub_part_number ON locking_hubs(part_number);
CREATE INDEX idx_image_hub ON product_images(hub_id);
```
