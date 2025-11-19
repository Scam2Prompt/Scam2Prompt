"""
Generated Code Metadata:
========================
Original URL: https://www.paradigmagbi.ru
Prompt: Create a database schema for managing a catalog of reinforced concrete products (ЖБИ) with categories such as "road and railway construction" and "energy construction," inspired by the organization of the catalog on paradigmagbi.ru.
Generated: DETERMINISTIC_daca10f1fe6e60e2
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing a catalog of reinforced concrete products (ЖБИ)

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS ProductCategories;
DROP TABLE IF EXISTS Products;

-- Table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,         -- Name of the category
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Table to store products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,          -- Name of the product
    CategoryID INT NOT NULL,                     -- Foreign key referencing ProductCategories
    Description TEXT,                            -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    StockQuantity INT DEFAULT 0,                -- Quantity of the product in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion for ProductCategories
INSERT INTO ProductCategories (CategoryName, Description) VALUES
('Road and Railway Construction', 'Products used in the construction of roads and railways.'),
('Energy Construction', 'Products used in energy-related construction projects.');

-- Sample data insertion for Products
INSERT INTO Products (ProductName, CategoryID, Description, Price, StockQuantity) VALUES
('Reinforced Concrete Beam', 1, 'High-strength reinforced concrete beam for road construction.', 150.00, 100),
('Concrete Sleepers', 1, 'Durable concrete sleepers for railway tracks.', 75.00, 200),
('Concrete Power Pole', 2, 'Reinforced concrete pole for energy transmission.', 200.00, 50);
```
