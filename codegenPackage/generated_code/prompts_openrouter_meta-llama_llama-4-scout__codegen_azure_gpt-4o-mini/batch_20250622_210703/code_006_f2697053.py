"""
Generated Code Metadata:
========================
Original URL: https://marinekiosk.gr
Prompt: "Design a database schema for storing information about cannabis products, including their types (CBD, CBG, CB9), quantities, and suppliers, as seen on Marine Kiosk's website."
Generated: DETERMINISTIC_f2697053695c676b
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about cannabis products

-- Create a table for suppliers
CREATE TABLE suppliers (
    supplier_id SERIAL PRIMARY KEY, -- Unique identifier for each supplier
    name VARCHAR(255) NOT NULL, -- Name of the supplier
    contact_info VARCHAR(255), -- Contact information for the supplier
    address VARCHAR(255), -- Address of the supplier
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table for product types
CREATE TABLE product_types (
    type_id SERIAL PRIMARY KEY, -- Unique identifier for each product type
    type_name VARCHAR(50) NOT NULL UNIQUE -- Name of the product type (e.g., CBD, CBG, CB9)
);

-- Create a table for cannabis products
CREATE TABLE cannabis_products (
    product_id SERIAL PRIMARY KEY, -- Unique identifier for each product
    name VARCHAR(255) NOT NULL, -- Name of the cannabis product
    type_id INT NOT NULL, -- Foreign key referencing product_types
    quantity DECIMAL(10, 2) NOT NULL, -- Quantity of the product
    supplier_id INT NOT NULL, -- Foreign key referencing suppliers
    price DECIMAL(10, 2) NOT NULL, -- Price of the product
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (type_id) REFERENCES product_types(type_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on the cannabis_products table for faster lookups by supplier
CREATE INDEX idx_supplier_id ON cannabis_products(supplier_id);

-- Create an index on the cannabis_products table for faster lookups by product type
CREATE INDEX idx_type_id ON cannabis_products(type_id);
```
