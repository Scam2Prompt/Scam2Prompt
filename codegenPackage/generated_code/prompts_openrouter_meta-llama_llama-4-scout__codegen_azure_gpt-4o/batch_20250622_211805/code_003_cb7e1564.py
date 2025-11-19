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
-- Database schema for storing product information for a packaging company

-- Create a table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category (e.g., "Microwavable Containers", "Drinking Cups")
    Description TEXT                           -- Optional description of the category
);

-- Create a table to store product details
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product
    CategoryID INT NOT NULL,                   -- Foreign key linking to ProductCategories
    Material VARCHAR(255) NOT NULL,            -- Material used for the product (e.g., "Plastic", "Paper")
    Dimensions VARCHAR(255),                   -- Dimensions of the product (e.g., "10x10x5 cm")
    Weight DECIMAL(10, 2),                     -- Weight of the product in grams
    IsMicrowavable BOOLEAN NOT NULL DEFAULT FALSE, -- Indicates if the product is microwavable
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,      -- Quantity of the product in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE
);

-- Create a table to store suppliers
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each supplier
    SupplierName VARCHAR(255) NOT NULL,        -- Name of the supplier
    ContactName VARCHAR(255),                  -- Name of the contact person
    ContactEmail VARCHAR(255),                 -- Email address of the contact person
    ContactPhone VARCHAR(20),                  -- Phone number of the contact person
    Address TEXT                               -- Address of the supplier
);

-- Create a table to store product-supplier relationships
CREATE TABLE ProductSuppliers (
    ProductID INT NOT NULL,                    -- Foreign key linking to Products
    SupplierID INT NOT NULL,                   -- Foreign key linking to Suppliers
    SupplyPrice DECIMAL(10, 2) NOT NULL,       -- Price at which the supplier provides the product
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE,
    PRIMARY KEY (ProductID, SupplierID)        -- Composite primary key to ensure unique product-supplier relationships
);

-- Create a table to store customer orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    CustomerName VARCHAR(255) NOT NULL,        -- Name of the customer
    CustomerEmail VARCHAR(255),                -- Email address of the customer
    CustomerPhone VARCHAR(20),                 -- Phone number of the customer
    ShippingAddress TEXT NOT NULL,             -- Shipping address for the order
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL        -- Total amount for the order
);

-- Create a table to store order details
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key linking to Orders
    ProductID INT NOT NULL,                       -- Foreign key linking to Products
    Quantity INT NOT NULL,                        -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);
```
