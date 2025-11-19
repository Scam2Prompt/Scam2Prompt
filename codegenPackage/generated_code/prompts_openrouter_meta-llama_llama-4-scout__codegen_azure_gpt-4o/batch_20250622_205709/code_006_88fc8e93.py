"""
Generated Code Metadata:
========================
Original URL: https://tanhungco.vn
Prompt: "Design a database schema for storing information about agricultural products, including pesticides, herbicides, and fertilizers, similar to those offered by Tấn Hưng Việt Nam."
Generated: DETERMINISTIC_88fc8e936985d372
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about agricultural products
-- including pesticides, herbicides, and fertilizers.

-- Create a table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the category
    Name VARCHAR(100) NOT NULL,                -- Name of the category (e.g., Pesticides, Herbicides, Fertilizers)
    Description TEXT                           -- Optional description of the category
);

-- Create a table for agricultural products
CREATE TABLE AgriculturalProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the product
    Name VARCHAR(255) NOT NULL,                -- Name of the product
    CategoryID INT NOT NULL,                   -- Foreign key referencing ProductCategories
    Manufacturer VARCHAR(255),                 -- Name of the manufacturer
    ActiveIngredients TEXT,                    -- List of active ingredients in the product
    UsageInstructions TEXT,                    -- Instructions for using the product
    SafetyInformation TEXT,                    -- Safety precautions and information
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,      -- Quantity of the product in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE
);

-- Create a table for suppliers
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the supplier
    Name VARCHAR(255) NOT NULL,                -- Name of the supplier
    ContactInfo TEXT,                          -- Contact information for the supplier
    Address TEXT                               -- Address of the supplier
);

-- Create a table for product-supplier relationships
CREATE TABLE ProductSuppliers (
    ProductID INT NOT NULL,                    -- Foreign key referencing AgriculturalProducts
    SupplierID INT NOT NULL,                   -- Foreign key referencing Suppliers
    SupplyPrice DECIMAL(10, 2) NOT NULL,       -- Price at which the supplier provides the product
    FOREIGN KEY (ProductID) REFERENCES AgriculturalProducts(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE,
    PRIMARY KEY (ProductID, SupplierID)        -- Composite primary key to ensure unique relationships
);

-- Create a table for customer orders
CREATE TABLE CustomerOrders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for the order
    CustomerName VARCHAR(255) NOT NULL,        -- Name of the customer
    ContactInfo TEXT,                          -- Contact information for the customer
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL        -- Total amount for the order
);

-- Create a table for order details
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the order detail
    OrderID INT NOT NULL,                         -- Foreign key referencing CustomerOrders
    ProductID INT NOT NULL,                       -- Foreign key referencing AgriculturalProducts
    Quantity INT NOT NULL,                        -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES CustomerOrders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES AgriculturalProducts(ProductID) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_product_name ON AgriculturalProducts(Name);
CREATE INDEX idx_supplier_name ON Suppliers(Name);
CREATE INDEX idx_order_date ON CustomerOrders(OrderDate);
```
