"""
Generated Code Metadata:
========================
Original URL: https://aluminiosmendoza.cl
Prompt: "Create a SQL database schema to store information about aluminum window products, thermopanel PVC, and security blinds, including fields for product description, price, and installation details, similar to those provided by Aluminios Mendoza."
Generated: DETERMINISTIC_508facf791a9904c
Batch ID: 20250622_212434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Aluminum Window Products, Thermopanel PVC, and Security Blinds

-- Products table to store common product information
CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_type ENUM('aluminum_window', 'thermopanel_pvc', 'security_blind') NOT NULL,
    product_code VARCHAR(20) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    material VARCHAR(50),
    color VARCHAR(30),
    standard_size BOOLEAN DEFAULT TRUE,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Product prices table (allowing different prices for different configurations)
CREATE TABLE product_prices (
    price_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    width_cm DECIMAL(8,2),
    height_cm DECIMAL(8,2),
    unit_price DECIMAL(10,2) NOT NULL,
    installation_price DECIMAL(10,2),
    discount_percentage DECIMAL(5,2) DEFAULT 0.00,
    valid_from DATE NOT NULL,
    valid_to DATE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    INDEX (product_id, width_cm, height_cm)
);

-- Aluminum window specific attributes
CREATE TABLE aluminum_windows (
    product_id INT PRIMARY KEY,
    glass_type VARCHAR(50),
    frame_thickness_mm DECIMAL(5,2),
    thermal_break BOOLEAN DEFAULT FALSE,
    sound_proofing_level VARCHAR(20),
    security_features VARCHAR(100),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Thermopanel PVC specific attributes
CREATE TABLE thermopanel_pvc (
    product_id INT PRIMARY KEY,
    chamber_count INT,
    u_value DECIMAL(5,2),
    glass_layers INT,
    gas_filled BOOLEAN DEFAULT FALSE,
    energy_efficiency_class CHAR(1),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Security blinds specific attributes
CREATE TABLE security_blinds (
    product_id INT PRIMARY KEY,
    slat_width_mm DECIMAL(5,2),
    slat_material VARCHAR(30),
    operation_type ENUM('manual', 'motorized'),
    security_rating VARCHAR(20),
    weather_resistance VARCHAR(20),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Installation services table
CREATE TABLE installation_services (
    service_id INT PRIMARY KEY AUTO_INCREMENT,
    product_type ENUM('aluminum_window', 'thermopanel_pvc', 'security_blind') NOT NULL,
    service_name VARCHAR(100) NOT NULL,
    description TEXT,
    base_price DECIMAL(10,2) NOT NULL,
    price_per_unit DECIMAL(10,2),
    unit_type VARCHAR(20),
    active BOOLEAN DEFAULT TRUE
);

-- Product images table
CREATE TABLE product_images (
    image_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    caption VARCHAR(100),
    display_order INT DEFAULT 0,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    INDEX (product_id, display_order)
);

-- Product categories for classification
CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    parent_category_id INT,
    FOREIGN KEY (parent_category_id) REFERENCES categories(category_id) ON DELETE SET NULL
);

-- Product to category mapping
CREATE TABLE product_categories (
    product_id INT NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY (product_id, category_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
);

-- Warranty information
CREATE TABLE warranties (
    warranty_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    duration_months INT NOT NULL,
    coverage_description TEXT,
    terms_and_conditions TEXT,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Product specifications (key-value pairs for additional attributes)
CREATE TABLE product_specifications (
    spec_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    spec_name VARCHAR(100) NOT NULL,
    spec_value VARCHAR(255) NOT NULL,
    spec_unit VARCHAR(20),
    display_order INT DEFAULT 0,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    INDEX (product_id, display_order)
);

-- Create a view for active products with prices
CREATE VIEW active_products_with_prices AS
SELECT 
    p.product_id,
    p.product_type,
    p.product_code,
    p.name,
    p.description,
    pp.width_cm,
    pp.height_cm,
    pp.unit_price,
    pp.installation_price,
    pp.discount_percentage,
    (pp.unit_price * (1 - pp.discount_percentage/100)) AS discounted_price
FROM 
    products p
JOIN 
    product_prices pp ON p.product_id = pp.product_id
WHERE 
    p.active = TRUE
    AND (pp.valid_to IS NULL OR pp.valid_to >= CURDATE())
    AND pp.valid_from <= CURDATE();
```
