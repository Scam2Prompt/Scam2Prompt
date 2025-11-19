"""
Generated Code Metadata:
========================
Original URL: https://thegladiatorshoes.com
Prompt: Create a database schema for storing product details from Gladiator Shoes, including attributes like toe type ("steel toe," "composite toe"), industry use case, and certification status (e.g., "CE Certified").
Generated: DETERMINISTIC_570cc4c362256048
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Gladiator Shoes product catalog
CREATE DATABASE IF NOT EXISTS gladiator_shoes;
USE gladiator_shoes;

-- Product table
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    sku VARCHAR(50) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Toe type table
CREATE TABLE IF NOT EXISTS toe_types (
    toe_type_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
) ENGINE=InnoDB;

-- Industry use cases table
CREATE TABLE IF NOT EXISTS industries (
    industry_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
) ENGINE=InnoDB;

-- Certifications table
CREATE TABLE IF NOT EXISTS certifications (
    certification_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    issuing_body VARCHAR(100)
) ENGINE=InnoDB;

-- Junction table for product-to-toe type relationship
CREATE TABLE IF NOT EXISTS product_toe_types (
    product_id INT NOT NULL,
    toe_type_id INT NOT NULL,
    PRIMARY KEY (product_id, toe_type_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (toe_type_id) REFERENCES toe_types(toe_type_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Junction table for product-to-industry relationship
CREATE TABLE IF NOT EXISTS product_industries (
    product_id INT NOT NULL,
    industry_id INT NOT NULL,
    PRIMARY KEY (product_id, industry_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (industry_id) REFERENCES industries(industry_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Junction table for product-to-certification relationship
CREATE TABLE IF NOT EXISTS product_certifications (
    product_id INT NOT NULL,
    certification_id INT NOT NULL,
    certification_status ENUM('pending', 'certified', 'expired') NOT NULL DEFAULT 'pending',
    certification_date DATE,
    expiry_date DATE,
    PRIMARY KEY (product_id, certification_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (certification_id) REFERENCES certifications(certification_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Indexes for better performance
CREATE INDEX idx_product_name ON products(name);
CREATE INDEX idx_product_sku ON products(sku);
CREATE INDEX idx_certification_status ON product_certifications(certification_status);
```
