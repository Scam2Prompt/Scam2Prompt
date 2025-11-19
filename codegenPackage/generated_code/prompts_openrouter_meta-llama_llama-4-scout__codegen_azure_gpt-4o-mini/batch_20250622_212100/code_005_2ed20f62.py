"""
Generated Code Metadata:
========================
Original URL: https://www.cymrepuestos.com.ar
Prompt: "Create a database schema for storing information about automotive spare parts, including product categories, brands, and supplier details, inspired by CYM Repuestos' product offerings."
Generated: DETERMINISTIC_2ed20f62577f434c
Batch ID: 20250622_212100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about automotive spare parts

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS suppliers;
DROP TABLE IF EXISTS brands;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS spare_parts;

-- Table to store supplier details
CREATE TABLE suppliers (
    supplier_id SERIAL PRIMARY KEY, -- Unique identifier for each supplier
    name VARCHAR(255) NOT NULL, -- Name of the supplier
    contact_email VARCHAR(255) UNIQUE NOT NULL, -- Unique email for supplier contact
    phone_number VARCHAR(20), -- Phone number of the supplier
    address TEXT, -- Address of the supplier
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store product categories
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY, -- Unique identifier for each category
    category_name VARCHAR(255) NOT NULL UNIQUE, -- Name of the category
    description TEXT, -- Description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store brands
CREATE TABLE brands (
    brand_id SERIAL PRIMARY KEY, -- Unique identifier for each brand
    brand_name VARCHAR(255) NOT NULL UNIQUE, -- Name of the brand
    description TEXT, -- Description of the brand
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store spare parts information
CREATE TABLE spare_parts (
    part_id SERIAL PRIMARY KEY, -- Unique identifier for each spare part
    part_name VARCHAR(255) NOT NULL, -- Name of the spare part
    category_id INT NOT NULL, -- Foreign key referencing categories
    brand_id INT NOT NULL, -- Foreign key referencing brands
    supplier_id INT NOT NULL, -- Foreign key referencing suppliers
    price DECIMAL(10, 2) NOT NULL, -- Price of the spare part
    stock_quantity INT DEFAULT 0, -- Quantity in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (brand_id) REFERENCES brands(brand_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_part_name ON spare_parts(part_name);
CREATE INDEX idx_category_name ON categories(category_name);
CREATE INDEX idx_brand_name ON brands(brand_name);
CREATE INDEX idx_supplier_name ON suppliers(name);
```
