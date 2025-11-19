"""
Generated Code Metadata:
========================
Original URL: https://alsafwaq8.com
Prompt: "Design a simple database schema for an inventory management system for a clothing store like الصفوة للملابس الجاهزة, considering their product categories and size charts."
Generated: DETERMINISTIC_0f2fd4d7a6fdd5f4
Batch ID: 20250622_205627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an inventory management system for a clothing store

-- Create a table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,         -- Name of the product category
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for size charts
CREATE TABLE SizeCharts (
    SizeID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each size
    SizeLabel VARCHAR(50) NOT NULL,             -- Label for the size (e.g., S, M, L, XL)
    Description TEXT,                            -- Description of the size (e.g., measurements)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the size was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,          -- Name of the product
    CategoryID INT NOT NULL,                     -- Foreign key referencing ProductCategories
    SizeID INT NOT NULL,                         -- Foreign key referencing SizeCharts
    Quantity INT NOT NULL DEFAULT 0,             -- Quantity of the product in stock
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (SizeID) REFERENCES SizeCharts(SizeID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for suppliers
CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each supplier
    SupplierName VARCHAR(100) NOT NULL,         -- Name of the supplier
    ContactInfo VARCHAR(255),                    -- Contact information for the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the supplier was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for product supplier relationships
CREATE TABLE ProductSuppliers (
    ProductSupplierID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the relationship
    ProductID INT NOT NULL,                          -- Foreign key referencing Products
    SupplierID INT NOT NULL,                         -- Foreign key referencing Suppliers
    SupplyPrice DECIMAL(10, 2) NOT NULL,            -- Price at which the supplier supplies the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the relationship was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE -- Ensures referential integrity
);
```
