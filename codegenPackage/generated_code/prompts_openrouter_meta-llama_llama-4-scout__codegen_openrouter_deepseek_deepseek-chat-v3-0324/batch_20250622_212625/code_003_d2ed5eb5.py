"""
Generated Code Metadata:
========================
Original URL: https://newhomepoocoin.blogspot.com
Prompt: "Design a simple database schema for a shoe inventory management system that includes tables for different shoe types (sapatos, sandalias, tenis) and their attributes."
Generated: DETERMINISTIC_d2ed5eb5de6b0893
Batch ID: 20250622_212625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Shoe Inventory Management System

-- Table for storing shoe types
CREATE TABLE shoe_types (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table for storing shoe brands
CREATE TABLE brands (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE,
    country_of_origin VARCHAR(50),
    founded_year INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table for storing shoe materials
CREATE TABLE materials (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    is_synthetic BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table for storing shoe colors
CREATE TABLE colors (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE,
    hex_code VARCHAR(7),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table for storing shoe sizes
CREATE TABLE sizes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    us_size DECIMAL(3,1) NOT NULL UNIQUE,
    eu_size DECIMAL(3,1) NOT NULL,
    uk_size DECIMAL(3,1) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Main table for storing shoes inventory
CREATE TABLE shoes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    shoe_type_id INT NOT NULL,
    brand_id INT NOT NULL,
    model_name VARCHAR(100) NOT NULL,
    gender ENUM('Men', 'Women', 'Unisex') NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    cost DECIMAL(10,2) NOT NULL,
    sku VARCHAR(50) NOT NULL UNIQUE,
    barcode VARCHAR(50) UNIQUE,
    release_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (shoe_type_id) REFERENCES shoe_types(id),
    FOREIGN KEY (brand_id) REFERENCES brands(id)
);

-- Junction table for shoe materials
CREATE TABLE shoe_materials (
    shoe_id INT NOT NULL,
    material_id INT NOT NULL,
    percentage INT,
    PRIMARY KEY (shoe_id, material_id),
    FOREIGN KEY (shoe_id) REFERENCES shoes(id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(id) ON DELETE CASCADE
);

-- Junction table for shoe colors
CREATE TABLE shoe_colors (
    shoe_id INT NOT NULL,
    color_id INT NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (shoe_id, color_id),
    FOREIGN KEY (shoe_id) REFERENCES shoes(id) ON DELETE CASCADE,
    FOREIGN KEY (color_id) REFERENCES colors(id) ON DELETE CASCADE
);

-- Table for storing inventory stock
CREATE TABLE inventory (
    id INT PRIMARY KEY AUTO_INCREMENT,
    shoe_id INT NOT NULL,
    size_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 0,
    reorder_threshold INT DEFAULT 10,
    last_restock_date TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (shoe_id) REFERENCES shoes(id),
    FOREIGN KEY (size_id) REFERENCES sizes(id),
    UNIQUE KEY (shoe_id, size_id)
);

-- Table for storing shoe images
CREATE TABLE shoe_images (
    id INT PRIMARY KEY AUTO_INCREMENT,
    shoe_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    alt_text VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (shoe_id) REFERENCES shoes(id) ON DELETE CASCADE
);

-- Insert default shoe types
INSERT INTO shoe_types (name, description) VALUES 
('Sapatos', 'Formal or dress shoes'),
('Sandalias', 'Open-toe footwear with straps'),
('Tenis', 'Athletic shoes or sneakers');
```
