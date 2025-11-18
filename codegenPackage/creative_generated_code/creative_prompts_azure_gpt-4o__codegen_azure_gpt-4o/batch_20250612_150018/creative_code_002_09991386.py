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
-- Database schema for managing inventory of food packaging products
-- This schema is designed to handle products offered by Isoplas Corporation

-- Table for storing details about product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category (e.g., Containers, Cups, Cutlery)
    Description TEXT                           -- Optional description of the category
);

-- Table for storing details about individual products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product (e.g., Microwaveable Container 500ml)
    CategoryID INT NOT NULL,                   -- Foreign key referencing the product category
    SKU VARCHAR(255) UNIQUE NOT NULL,          -- Stock Keeping Unit (unique identifier for the product)
    UnitPrice DECIMAL(10, 2) NOT NULL,         -- Price per unit of the product
    QuantityInStock INT NOT NULL DEFAULT 0,    -- Current stock level of the product
    ReorderLevel INT NOT NULL DEFAULT 0,       -- Stock level at which reordering is triggered
    IsActive BOOLEAN NOT NULL DEFAULT TRUE,    -- Indicates if the product is active (available for sale)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    CONSTRAINT FK_ProductCategory FOREIGN KEY (CategoryID) 
        REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE
);

-- Table for tracking supplier information
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the supplier
    SupplierName VARCHAR(255) NOT NULL,        -- Name of the supplier
    ContactPerson VARCHAR(255),               -- Name of the contact person at the supplier
    PhoneNumber VARCHAR(50),                  -- Phone number for the supplier
    EmailAddress VARCHAR(255),                -- Email address for the supplier
    Address TEXT                              -- Physical address of the supplier
);

-- Table for managing purchases from suppliers (inventory replenishment)
CREATE TABLE Purchases (
    PurchaseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the purchase
    SupplierID INT NOT NULL,                   -- Foreign key referencing the supplier
    ProductID INT NOT NULL,                    -- Foreign key referencing the product
    Quantity INT NOT NULL,                     -- Quantity of the product purchased
    TotalCost DECIMAL(10, 2) NOT NULL,         -- Total cost of the purchase
    PurchaseDate DATE NOT NULL,                -- Date the purchase was made
    CONSTRAINT FK_PurchaseSupplier FOREIGN KEY (SupplierID) 
        REFERENCES Suppliers(SupplierID) ON DELETE CASCADE,
    CONSTRAINT FK_PurchaseProduct FOREIGN KEY (ProductID) 
        REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table for tracking sales of products
CREATE TABLE Sales (
    SaleID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the sale
    ProductID INT NOT NULL,                    -- Foreign key referencing the product
    QuantitySold INT NOT NULL,                 -- Quantity of the product sold
    TotalRevenue DECIMAL(10, 2) NOT NULL,      -- Total revenue generated from the sale
    SaleDate DATE NOT NULL,                    -- Date the sale occurred
    CONSTRAINT FK_SaleProduct FOREIGN KEY (ProductID) 
        REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Optional: Table for logging stock changes (e.g., manual adjustments)
CREATE TABLE StockAdjustments (
    AdjustmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the adjustment
    ProductID INT NOT NULL,                      -- Foreign key referencing the product
    AdjustmentType ENUM('Increase', 'Decrease') NOT NULL, -- Type of adjustment
    Quantity INT NOT NULL,                       -- Quantity increased or decreased
    Reason VARCHAR(255),                         -- Reason for the adjustment
    AdjustmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for the adjustment
    CONSTRAINT FK_AdjustmentProduct FOREIGN KEY (ProductID) 
        REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Ensure strict data integrity with transaction-safe storage engines
-- Recommended engine: InnoDB
```
