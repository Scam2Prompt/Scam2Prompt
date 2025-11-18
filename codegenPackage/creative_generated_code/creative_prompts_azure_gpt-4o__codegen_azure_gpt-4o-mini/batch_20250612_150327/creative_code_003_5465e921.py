"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.be
Prompt: Create a database schema for managing private label cleaning tool production, inspired by PDC Brush's operational model.
Generated: DETERMINISTIC_5465e921e19b876b
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing private label cleaning tool production

-- Drop existing tables if they exist
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Suppliers;
DROP TABLE IF EXISTS Categories;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS OrderItems;

-- Table for storing product categories
CREATE TABLE Categories (
    CategoryID SERIAL PRIMARY KEY,      -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL, -- Name of the category
    Description TEXT                     -- Description of the category
);

-- Table for storing supplier information
CREATE TABLE Suppliers (
    SupplierID SERIAL PRIMARY KEY,     -- Unique identifier for each supplier
    SupplierName VARCHAR(100) NOT NULL, -- Name of the supplier
    ContactName VARCHAR(100),          -- Contact person's name
    Phone VARCHAR(15),                 -- Contact phone number
    Email VARCHAR(100),                -- Contact email
    Address TEXT                       -- Supplier address
);

-- Table for storing product information
CREATE TABLE Products (
    ProductID SERIAL PRIMARY KEY,      -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL, -- Name of the product
    Description TEXT,                  -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,     -- Price of the product
    StockQuantity INT DEFAULT 0,       -- Current stock quantity
    CategoryID INT REFERENCES Categories(CategoryID), -- Foreign key to Category
    SupplierID INT REFERENCES Suppliers(SupplierID),   -- Foreign key to Supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Update timestamp
);

-- Table for storing orders
CREATE TABLE Orders (
    OrderID SERIAL PRIMARY KEY,        -- Unique identifier for each order
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Order date
    CustomerName VARCHAR(100) NOT NULL, -- Name of the customer
    TotalAmount DECIMAL(10, 2) NOT NULL, -- Total order amount
    Status VARCHAR(20) DEFAULT 'Pending' -- Order status (e.g., Pending, Shipped, Completed)
);

-- Table for storing items in each order
CREATE TABLE OrderItems (
    OrderItemID SERIAL PRIMARY KEY,    -- Unique identifier for each order item
    OrderID INT REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Foreign key to Order
    ProductID INT REFERENCES Products(ProductID) ON DELETE CASCADE, -- Foreign key to Product
    Quantity INT NOT NULL,              -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL       -- Price at the time of order
);

-- Indexes for performance enhancement
CREATE INDEX idx_products_category ON Products(CategoryID);
CREATE INDEX idx_orders_customer ON Orders(CustomerName);
CREATE INDEX idx_orderitems_order ON OrderItems(OrderID);

-- Trigger for managing stock upon order insertion
CREATE OR REPLACE FUNCTION update_stock() RETURNS TRIGGER AS $$
BEGIN
    -- Decrease stock quantity by the ordered quantity
    UPDATE Products
    SET StockQuantity = StockQuantity - NEW.Quantity
    WHERE ProductID = NEW.ProductID;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_update_stock
AFTER INSERT ON OrderItems
FOR EACH ROW
EXECUTE FUNCTION update_stock();

-- Error handling for foreign key constraints and data integrity
-- Ensure that order items cannot be created for non-existent products or orders
```
