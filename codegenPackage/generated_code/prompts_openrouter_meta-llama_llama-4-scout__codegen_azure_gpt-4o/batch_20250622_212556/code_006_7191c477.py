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

-- Table to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the product
    Description TEXT,                         -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product (up to 10 digits, 2 decimal places)
    InventoryLevel INT NOT NULL,              -- Current inventory level (quantity in stock)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store categories for products
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(255) NOT NULL,                -- Name of the category
    Description TEXT,                          -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the category was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to associate products with categories (many-to-many relationship)
CREATE TABLE ProductCategories (
    ProductID INT NOT NULL,                    -- Foreign key referencing Products table
    CategoryID INT NOT NULL,                   -- Foreign key referencing Categories table
    PRIMARY KEY (ProductID, CategoryID),       -- Composite primary key
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store suppliers for products
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each supplier
    Name VARCHAR(255) NOT NULL,                -- Name of the supplier
    ContactInfo TEXT,                          -- Contact information for the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the supplier was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to associate products with suppliers (many-to-many relationship)
CREATE TABLE ProductSuppliers (
    ProductID INT NOT NULL,                    -- Foreign key referencing Products table
    SupplierID INT NOT NULL,                   -- Foreign key referencing Suppliers table
    PRIMARY KEY (ProductID, SupplierID),       -- Composite primary key
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store price history for products
CREATE TABLE PriceHistory (
    PriceHistoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each price history record
    ProductID INT NOT NULL,                        -- Foreign key referencing Products table
    OldPrice DECIMAL(10, 2) NOT NULL,              -- Previous price of the product
    NewPrice DECIMAL(10, 2) NOT NULL,              -- Updated price of the product
    ChangeDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the price was changed
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store inventory transactions
CREATE TABLE InventoryTransactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    ProductID INT NOT NULL,                       -- Foreign key referencing Products table
    QuantityChange INT NOT NULL,                  -- Change in inventory level (positive or negative)
    TransactionType ENUM('Addition', 'Removal') NOT NULL, -- Type of transaction
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the transaction
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete
);
```
