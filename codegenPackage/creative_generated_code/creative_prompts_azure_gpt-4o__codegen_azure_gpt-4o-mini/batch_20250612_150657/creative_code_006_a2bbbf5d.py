"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perucotiza.com
Prompt: Design a database schema in SQL to store information retrieved from PeruCotiza, including categories like "repuestos" (e.g., motor, frenos) and "accesorios" (e.g., alarmas, seguridad).
Generated: DETERMINISTIC_a2bbbf5daeef16de
Batch ID: 20250612_150657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing information from PeruCotiza

-- Create a database for PeruCotiza
CREATE DATABASE PeruCotizaDB;

-- Switch to the newly created database
USE PeruCotizaDB;

-- Table for storing product categories
CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    category_name VARCHAR(100) NOT NULL,          -- Name of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record update
);

-- Table for storing products
CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each product
    category_id INT NOT NULL,                     -- Foreign key referencing Categories
    product_name VARCHAR(255) NOT NULL,          -- Name of the product
    description TEXT,                             -- Description of the product
    price DECIMAL(10,2) NOT NULL,                -- Price of the product
    stock INT NOT NULL,                           -- Stock quantity of the product
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record update
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table for storing suppliers
CREATE TABLE Suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each supplier
    supplier_name VARCHAR(255) NOT NULL,          -- Name of the supplier
    contact_info VARCHAR(255),                     -- Contact information for the supplier
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record update
);

-- Table for storing product-supplier relationships
CREATE TABLE ProductSuppliers (
    product_supplier_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product-supplier relationship
    product_id INT NOT NULL,                            -- Foreign key referencing Products
    supplier_id INT NOT NULL,                           -- Foreign key referencing Suppliers
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record update
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Sample inserts to populate Categories table
INSERT INTO Categories (category_name) VALUES
('repuestos'),
('accesorios');

-- Sample inserts to populate Products table
INSERT INTO Products (category_id, product_name, description, price, stock) VALUES
(1, 'Motor', 'Motor for vehicles', 1200.00, 10),
(1, 'Frenos', 'Brake pads', 150.00, 50),
(2, 'Alarmas', 'Vehicle alarm system', 300.00, 20),
(2, 'Seguridad', 'Security cameras', 250.00, 15);

-- Sample inserts to populate Suppliers table
INSERT INTO Suppliers (supplier_name, contact_info) VALUES
('Supplier A', 'contact@suppa.com'),
('Supplier B', 'contact@suppb.com');

-- Sample inserts to populate ProductSuppliers table
INSERT INTO ProductSuppliers (product_id, supplier_id) VALUES 
(1, 1),  -- Motor supplied by Supplier A
(2, 2),  -- Frenos supplied by Supplier B
(3, 1),  -- Alarmas supplied by Supplier A
(4, 2);  -- Seguridad supplied by Supplier B
```
