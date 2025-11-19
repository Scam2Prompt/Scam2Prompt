"""
Generated Code Metadata:
========================
Original URL: https://swepsepoocoin.blogspot.com
Prompt: Write a SQL query to design a database schema for storing shoe information, including shoe type (e.g., sandalia, sapato social, tenis de corrida), size, and color.
Generated: DETERMINISTIC_3d0d886a2ca420a6
Batch ID: 20250622_212524
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for shoe inventory management system
CREATE TABLE shoe_types (
    type_id INT PRIMARY KEY AUTO_INCREMENT,
    type_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT uc_type_name UNIQUE (type_name)
);

CREATE TABLE colors (
    color_id INT PRIMARY KEY AUTO_INCREMENT,
    color_name VARCHAR(50) NOT NULL,
    hex_code VARCHAR(7),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT uc_color_name UNIQUE (color_name)
);

CREATE TABLE sizes (
    size_id INT PRIMARY KEY AUTO_INCREMENT,
    size_value DECIMAL(4,1) NOT NULL,
    size_system ENUM('US', 'UK', 'EU', 'JP', 'CM') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT uc_size_value_system UNIQUE (size_value, size_system)
);

CREATE TABLE shoes (
    shoe_id INT PRIMARY KEY AUTO_INCREMENT,
    type_id INT NOT NULL,
    model_name VARCHAR(100) NOT NULL,
    gender ENUM('Men', 'Women', 'Unisex', 'Kids') NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES shoe_types(type_id) ON DELETE RESTRICT
);

CREATE TABLE shoe_inventory (
    inventory_id INT PRIMARY KEY AUTO_INCREMENT,
    shoe_id INT NOT NULL,
    color_id INT NOT NULL,
    size_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 0,
    sku VARCHAR(50) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (shoe_id) REFERENCES shoes(shoe_id) ON DELETE CASCADE,
    FOREIGN KEY (color_id) REFERENCES colors(color_id) ON DELETE RESTRICT,
    FOREIGN KEY (size_id) REFERENCES sizes(size_id) ON DELETE RESTRICT,
    CONSTRAINT uc_shoe_color_size UNIQUE (shoe_id, color_id, size_id)
);

-- Indexes for performance optimization
CREATE INDEX idx_shoe_type ON shoes(type_id);
CREATE INDEX idx_inventory_shoe ON shoe_inventory(shoe_id);
CREATE INDEX idx_inventory_color ON shoe_inventory(color_id);
CREATE INDEX idx_inventory_size ON shoe_inventory(size_id);
```
