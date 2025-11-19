"""
Generated Code Metadata:
========================
Original URL: https://www.pavainc.com
Prompt: Design a database schema to store information about various stone products, including Premium Pennsylvania Bluestone, Treads, Steps, and Boulders, and their respective suppliers.
Generated: DETERMINISTIC_3f518451611763e2
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about stone products and their suppliers

-- Create a table to store supplier information
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each supplier
    Name VARCHAR(255) NOT NULL,                -- Name of the supplier
    ContactEmail VARCHAR(255),                 -- Contact email of the supplier
    ContactPhone VARCHAR(20),                  -- Contact phone number of the supplier
    Address TEXT,                              -- Address of the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(255) NOT NULL,                -- Name of the category (e.g., Premium Pennsylvania Bluestone, Treads, Steps, Boulders)
    Description TEXT,                          -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table to store stone product information
CREATE TABLE StoneProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,                -- Name of the stone product
    CategoryID INT NOT NULL,                   -- Foreign key referencing ProductCategories
    SupplierID INT NOT NULL,                   -- Foreign key referencing Suppliers
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    StockQuantity INT NOT NULL,                -- Quantity of the product in stock
    Description TEXT,                          -- Description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE, -- Cascade delete for category
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE -- Cascade delete for supplier
);

-- Create a table to store product images
CREATE TABLE ProductImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each image
    ProductID INT NOT NULL,                    -- Foreign key referencing StoneProducts
    ImageURL VARCHAR(2083) NOT NULL,           -- URL of the product image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (ProductID) REFERENCES StoneProducts(ProductID) ON DELETE CASCADE -- Cascade delete for product
);

-- Create a table to store supplier ratings
CREATE TABLE SupplierRatings (
    RatingID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each rating
    SupplierID INT NOT NULL,                   -- Foreign key referencing Suppliers
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating value (1 to 5)
    Review TEXT,                               -- Review text
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE -- Cascade delete for supplier
);

-- Indexes for faster queries
CREATE INDEX idx_supplier_name ON Suppliers(Name);
CREATE INDEX idx_product_name ON StoneProducts(Name);
CREATE INDEX idx_category_name ON ProductCategories(Name);
```
