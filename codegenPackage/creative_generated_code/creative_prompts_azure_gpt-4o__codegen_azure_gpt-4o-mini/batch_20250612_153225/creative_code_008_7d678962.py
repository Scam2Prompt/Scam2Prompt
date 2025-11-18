"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vgtindia.in
Prompt: Generate a database schema to store product details for agricultural equipment like "Animal Feed Pallet Machine" and "Vacuum Cleaner," based on the categories listed on the Vinglob Greentech website.
Generated: DETERMINISTIC_7d678962547a96f4
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing product details for agricultural equipment

CREATE DATABASE IF NOT EXISTS AgriculturalEquipmentDB;
USE AgriculturalEquipmentDB;

-- Table to store product categories
CREATE TABLE IF NOT EXISTS ProductCategories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store product details
CREATE TABLE IF NOT EXISTS Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    category_id INT,
    specifications TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES ProductCategories(category_id)
        ON DELETE SET NULL ON UPDATE CASCADE
);

-- Example insertions for product categories
INSERT INTO ProductCategories (category_name, description) VALUES 
('Feed Processing Equipment', 'Machinery used for processing animal feed.'),
('Cleaning Equipment', 'Tools designed for cleaning agricultural environments.');

-- Example insertions for products
INSERT INTO Products (product_name, category_id, specifications, price, stock_quantity) VALUES 
('Animal Feed Pallet Machine', 1, 'Efficient palletizing machine for animal feed.', 15000.00, 10),
('Vacuum Cleaner', 2, 'Industrial vacuum cleaner for large spaces.', 300.00, 20);
```
