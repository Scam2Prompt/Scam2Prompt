"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramjiacro.com
Prompt: Design a database schema in SQL for managing inventory of acrylic yarn products, based on the offerings of Ramji Acro.
Generated: DETERMINISTIC_94d1acd1397a40c8
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing inventory of acrylic yarn products

-- Create a database for the inventory system
CREATE DATABASE IF NOT EXISTS acrylic_yarn_inventory;

-- Use the created database
USE acrylic_yarn_inventory;

-- Table for storing information about yarn categories
CREATE TABLE IF NOT EXISTS yarn_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    category_name VARCHAR(100) NOT NULL,          -- Name of the yarn category
    description TEXT,                              -- Description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the category was last updated
);

-- Table for storing information about yarn products
CREATE TABLE IF NOT EXISTS yarn_products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL,            -- Name of the yarn product
    category_id INT NOT NULL,                       -- Foreign key referencing the yarn_categories table
    color VARCHAR(50) NOT NULL,                    -- Color of the yarn
    weight DECIMAL(5, 2) NOT NULL,                 -- Weight of the yarn in grams
    price DECIMAL(10, 2) NOT NULL,                 -- Price of the yarn product
    stock_quantity INT NOT NULL DEFAULT 0,         -- Quantity of the product in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (category_id) REFERENCES yarn_categories(category_id) ON DELETE CASCADE  -- Ensuring referential integrity
);

-- Table for storing supplier information
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each supplier
    supplier_name VARCHAR(255) NOT NULL,            -- Name of the supplier
    contact_info VARCHAR(255),                       -- Contact information for the supplier
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the supplier was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the supplier was last updated
);

-- Table for tracking supplier product relationships
CREATE TABLE IF NOT EXISTS supplier_products (
    supplier_product_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each supplier product entry
    product_id INT NOT NULL,                             -- Foreign key referencing the yarn_products table
    supplier_id INT NOT NULL,                            -- Foreign key referencing the suppliers table
    delivery_date DATE NOT NULL,                         -- Date when the product was delivered
    quantity_received INT NOT NULL,                      -- Quantity of the product received
    FOREIGN KEY (product_id) REFERENCES yarn_products(product_id) ON DELETE CASCADE,  -- Ensuring referential integrity
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CASCADE   -- Ensuring referential integrity
);

-- Table for managing product sales
CREATE TABLE IF NOT EXISTS sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,            -- Unique identifier for each sale
    product_id INT NOT NULL,                           -- Foreign key referencing the yarn_products table
    quantity_sold INT NOT NULL,                        -- Quantity of the product sold
    sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp for when the sale occurred
    total_price DECIMAL(10, 2) NOT NULL,             -- Total price for the sale
    FOREIGN KEY (product_id) REFERENCES yarn_products(product_id) ON DELETE CASCADE  -- Ensuring referential integrity
);

-- End of schema creation
```
