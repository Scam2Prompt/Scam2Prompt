"""
Generated Code Metadata:
========================
Original URL: https://obsidiajeans.com.br
Prompt: Create a SQL database schema for managing clothing products, including shorts and jeans, with attributes like product ID, name, price, and material, inspired by the product catalog of Obsidia Jeans.
Generated: DETERMINISTIC_458b95ede761d953
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Clothing Product Management
-- Inspired by Obsidia Jeans product catalog

-- Create the database
CREATE DATABASE IF NOT EXISTS ClothingInventory;
USE ClothingInventory;

-- Product types enumeration
CREATE TABLE IF NOT EXISTS ProductTypes (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL UNIQUE,
    description VARCHAR(255)
);

-- Materials enumeration
CREATE TABLE IF NOT EXISTS Materials (
    material_id INT AUTO_INCREMENT PRIMARY KEY,
    material_name VARCHAR(50) NOT NULL UNIQUE,
    description VARCHAR(255)
);

-- Sizes enumeration
CREATE TABLE IF NOT EXISTS Sizes (
    size_id INT AUTO_INCREMENT PRIMARY KEY,
    size_name VARCHAR(20) NOT NULL UNIQUE,
    description VARCHAR(100)
);

-- Colors enumeration
CREATE TABLE IF NOT EXISTS Colors (
    color_id INT AUTO_INCREMENT PRIMARY KEY,
    color_name VARCHAR(50) NOT NULL UNIQUE,
    hex_code VARCHAR(7)
);

-- Main products table
CREATE TABLE IF NOT EXISTS Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    sku VARCHAR(20) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    type_id INT NOT NULL,
    material_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (type_id) REFERENCES ProductTypes(type_id),
    FOREIGN KEY (material_id) REFERENCES Materials(material_id),
    CHECK (price > 0)
);

-- Product variants (combinations of size and color)
CREATE TABLE IF NOT EXISTS ProductVariants (
    variant_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    size_id INT NOT NULL,
    color_id INT NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    barcode VARCHAR(50) UNIQUE,
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (size_id) REFERENCES Sizes(size_id),
    FOREIGN KEY (color_id) REFERENCES Colors(color_id),
    CHECK (stock_quantity >= 0),
    UNIQUE KEY unique_variant (product_id, size_id, color_id)
);

-- Product images
CREATE TABLE IF NOT EXISTS ProductImages (
    image_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    display_order INT DEFAULT 0,
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE
);

-- Product categories
CREATE TABLE IF NOT EXISTS Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    parent_id INT,
    description VARCHAR(255),
    FOREIGN KEY (parent_id) REFERENCES Categories(category_id) ON DELETE SET NULL
);

-- Product-category mapping
CREATE TABLE IF NOT EXISTS ProductCategories (
    product_id INT NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY (product_id, category_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE CASCADE
);

-- Insert default product types
INSERT IGNORE INTO ProductTypes (type_name, description) VALUES 
('Jeans', 'Denim pants'),
('Shorts', 'Short-length pants');

-- Insert common materials
INSERT IGNORE INTO Materials (material_name, description) VALUES 
('Cotton', '100% cotton fabric'),
('Denim', 'Traditional denim material'),
('Stretch Denim', 'Denim with elastane for stretch'),
('Linen', 'Lightweight linen material');

-- Insert standard sizes
INSERT IGNORE INTO Sizes (size_name, description) VALUES 
('XS', 'Extra Small'),
('S', 'Small'),
('M', 'Medium'),
('L', 'Large'),
('XL', 'Extra Large'),
('XXL', 'Double Extra Large');

-- Insert common colors
INSERT IGNORE INTO Colors (color_name, hex_code) VALUES 
('Black', '#000000'),
('White', '#FFFFFF'),
('Blue', '#0000FF'),
('Dark Blue', '#00008B'),
('Light Blue', '#ADD8E6'),
('Grey', '#808080'),
('Indigo', '#4B0082'),
('Khaki', '#F0E68C');
```
