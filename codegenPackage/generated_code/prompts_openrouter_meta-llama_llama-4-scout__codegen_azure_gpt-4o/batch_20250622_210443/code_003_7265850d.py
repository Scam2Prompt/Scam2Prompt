"""
Generated Code Metadata:
========================
Original URL: https://pavingblockcirebon.com
Prompt: "Design a database schema to store information about different types of concrete products, such as paving blocks, kanstin, and buis beton, similar to those offered by Komando Block Cirebon."
Generated: DETERMINISTIC_7265850d21ddb48f
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about concrete products

-- Create a table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,        -- Name of the category (e.g., Paving Blocks, Kanstin, Buis Beton)
    Description TEXT                           -- Optional description of the category
);

-- Create a table to store concrete products
CREATE TABLE ConcreteProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,         -- Name of the product
    CategoryID INT NOT NULL,                   -- Foreign key linking to ProductCategories
    Dimensions VARCHAR(100),                   -- Dimensions of the product (e.g., 20x10x5 cm)
    Weight DECIMAL(10, 2),                     -- Weight of the product in kilograms
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,      -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) -- Enforce category relationship
);

-- Create a table to store suppliers
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each supplier
    SupplierName VARCHAR(100) NOT NULL,        -- Name of the supplier
    ContactInfo TEXT,                          -- Contact information (e.g., phone, email, address)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the supplier was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store supplier-product relationships
CREATE TABLE SupplierProducts (
    SupplierProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    SupplierID INT NOT NULL,                          -- Foreign key linking to Suppliers
    ProductID INT NOT NULL,                           -- Foreign key linking to ConcreteProducts
    SupplyPrice DECIMAL(10, 2) NOT NULL,              -- Price at which the supplier provides the product
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID), -- Enforce supplier relationship
    FOREIGN KEY (ProductID) REFERENCES ConcreteProducts(ProductID) -- Enforce product relationship
);

-- Create a table to store customer orders
CREATE TABLE CustomerOrders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each order
    CustomerName VARCHAR(100) NOT NULL,              -- Name of the customer
    ContactInfo TEXT,                                -- Contact information (e.g., phone, email, address)
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,             -- Total amount for the order
    Status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store order details
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each record
    OrderID INT NOT NULL,                            -- Foreign key linking to CustomerOrders
    ProductID INT NOT NULL,                          -- Foreign key linking to ConcreteProducts
    Quantity INT NOT NULL,                           -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                   -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES CustomerOrders(OrderID), -- Enforce order relationship
    FOREIGN KEY (ProductID) REFERENCES ConcreteProducts(ProductID) -- Enforce product relationship
);

-- Create indexes for faster queries
CREATE INDEX idx_category_name ON ProductCategories(CategoryName);
CREATE INDEX idx_product_name ON ConcreteProducts(ProductName);
CREATE INDEX idx_supplier_name ON Suppliers(SupplierName);
CREATE INDEX idx_order_date ON CustomerOrders(OrderDate);
```
