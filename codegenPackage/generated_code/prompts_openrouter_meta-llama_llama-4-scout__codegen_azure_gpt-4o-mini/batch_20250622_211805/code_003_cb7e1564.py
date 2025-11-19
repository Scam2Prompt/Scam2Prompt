"""
Generated Code Metadata:
========================
Original URL: https://isoplas.com
Prompt: "Design a database schema to store product information for a packaging company that manufactures and supplies various types of food packaging products, including microwavable containers and drinking cups."
Generated: DETERMINISTIC_cb7e15641ef6261b
Batch ID: 20250622_211805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a packaging company that manufactures food packaging products

-- Create a table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,         -- Name of the product category
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Create a table to store products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,           -- Name of the product
    CategoryID INT NOT NULL,                      -- Foreign key referencing ProductCategories
    Description TEXT,                             -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,        -- Quantity of the product in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store suppliers
CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each supplier
    SupplierName VARCHAR(100) NOT NULL,          -- Name of the supplier
    ContactName VARCHAR(100),                     -- Contact person at the supplier
    Phone VARCHAR(15),                           -- Phone number of the supplier
    Email VARCHAR(100),                          -- Email address of the supplier
    Address VARCHAR(255),                        -- Address of the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the supplier was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the supplier was last updated
);

-- Create a table to store product-supplier relationships
CREATE TABLE ProductSuppliers (
    ProductSupplierID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the relationship
    ProductID INT NOT NULL,                            -- Foreign key referencing Products
    SupplierID INT NOT NULL,                           -- Foreign key referencing Suppliers
    SupplyPrice DECIMAL(10, 2) NOT NULL,              -- Price at which the supplier supplies the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp for when the relationship was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the relationship was last updated
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store product reviews
CREATE TABLE ProductReviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each review
    ProductID INT NOT NULL,                          -- Foreign key referencing Products
    ReviewText TEXT,                                 -- Text of the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5),      -- Rating given by the reviewer (1 to 5)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the review was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the review was last updated
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);
```
