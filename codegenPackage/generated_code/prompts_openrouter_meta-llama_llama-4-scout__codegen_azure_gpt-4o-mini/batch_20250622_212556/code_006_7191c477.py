"""
Generated Code Metadata:
========================
Original URL: https://plusmedica-shop.ch
Prompt: "Design a database schema to store information about medical accessories and supplements, including product descriptions, pricing, and inventory levels."
Generated: DETERMINISTIC_7191c4770a0a1280
Batch ID: 20250622_212556
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about medical accessories and supplements

CREATE TABLE Categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    category_name VARCHAR(100) NOT NULL,         -- Name of the category (e.g., "Supplements", "Medical Devices")
    description TEXT,                             -- Description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL,          -- Name of the product
    description TEXT,                             -- Detailed description of the product
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the product, must be non-negative
    inventory_level INT NOT NULL CHECK (inventory_level >= 0), -- Current inventory level, must be non-negative
    category_id INT,                              -- Foreign key referencing the Categories table
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE SET NULL -- Ensures referential integrity
);

CREATE TABLE Suppliers (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each supplier
    supplier_name VARCHAR(255) NOT NULL,         -- Name of the supplier
    contact_info VARCHAR(255),                    -- Contact information for the supplier
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the supplier was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the supplier was last updated
);

CREATE TABLE Product_Suppliers (
    product_id INT,                               -- Foreign key referencing the Products table
    supplier_id INT,                              -- Foreign key referencing the Suppliers table
    supply_price DECIMAL(10, 2) NOT NULL CHECK (supply_price >= 0), -- Price at which the supplier provides the product
    PRIMARY KEY (product_id, supplier_id),       -- Composite primary key
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON Products(product_name);
CREATE INDEX idx_category_name ON Categories(category_name);
CREATE INDEX idx_supplier_name ON Suppliers(supplier_name);
```
