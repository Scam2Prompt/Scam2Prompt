"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isoplas.com
Prompt: Create a database schema for managing inventory of food packaging products like microwavable containers, drinking cups, and plastic cutlery, referencing Isoplas Corporation's offerings.
Generated: DETERMINISTIC_099913865e141dde
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for managing inventory of food packaging products

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Suppliers CASCADE;
DROP TABLE IF EXISTS Products CASCADE;
DROP TABLE IF EXISTS Categories CASCADE;
DROP TABLE IF EXISTS Inventory CASCADE;

-- Create a table to store product categories
CREATE TABLE Categories (
    CategoryID SERIAL PRIMARY KEY,  -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,  -- Name of the category
    Description TEXT,  -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table to store suppliers information
CREATE TABLE Suppliers (
    SupplierID SERIAL PRIMARY KEY,  -- Unique identifier for each supplier
    SupplierName VARCHAR(255) NOT NULL,  -- Name of the supplier
    ContactEmail VARCHAR(255),  -- Supplier's contact email
    PhoneNumber VARCHAR(15),  -- Supplier's contact phone number
    Address TEXT,  -- Supplier's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table to store products
CREATE TABLE Products (
    ProductID SERIAL PRIMARY KEY,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,  -- Name of the product
    CategoryID INT REFERENCES Categories(CategoryID) ON DELETE SET NULL,  -- Reference to the product category
    SupplierID INT REFERENCES Suppliers(SupplierID) ON DELETE SET NULL,  -- Reference to the supplier
    Description TEXT,  -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,  -- Price of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table to manage inventory levels
CREATE TABLE Inventory (
    InventoryID SERIAL PRIMARY KEY,  -- Unique identifier for each inventory entry
    ProductID INT REFERENCES Products(ProductID) ON DELETE CASCADE,  -- Reference to the product
    Quantity INT NOT NULL CHECK (Quantity >= 0),  -- Quantity of the product in stock
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Last updated timestamp
    -- Optional: Add a low stock threshold for alerts
    LowStockThreshold INT DEFAULT 10  -- Threshold for low stock alerts
);

-- Indexes for optimization
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_category_name ON Categories(CategoryName);
CREATE INDEX idx_supplier_name ON Suppliers(SupplierName);
CREATE INDEX idx_product_inventory ON Inventory(ProductID);

-- Sample data insertion (optional, for initial setup)
-- This should be commented out in production unless necessary
-- INSERT INTO Categories (CategoryName, Description) VALUES 
-- ('Microwavable Containers', 'Containers suitable for microwaving.'),
-- ('Drinking Cups', 'Disposable cups for beverages.'),
-- ('Plastic Cutlery', 'Forks, spoons, and knives made of plastic.');

-- INSERT INTO Suppliers (SupplierName, ContactEmail, PhoneNumber, Address) VALUES 
-- ('Isoplas Corporation', 'info@isoplas.com', '1234567890', '123 Isoplas Rd, Example City, EX 12345');

-- INSERT INTO Products (ProductName, CategoryID, SupplierID, Description, Price) VALUES 
-- ('Microwavable Bowl', 1, 1, 'Durable microwavable bowl', 2.50),
-- ('Plastic Cup', 2, 1, 'Eco-friendly disposable cup', 0.10),
-- ('Plastic Fork', 3, 1, 'Sturdy plastic fork', 0.05);

-- Commit the transaction
COMMIT;
```
