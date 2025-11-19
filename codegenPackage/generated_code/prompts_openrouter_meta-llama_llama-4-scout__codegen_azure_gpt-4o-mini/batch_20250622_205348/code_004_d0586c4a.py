"""
Generated Code Metadata:
========================
Original URL: https://holambraalimentos.com.br
Prompt: "Design a database schema to store information about meat products, suppliers, and customers for a company like Holambra Alimentos."
Generated: DETERMINISTIC_d0586c4a07259832
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Holambra Alimentos

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Suppliers;
DROP TABLE IF EXISTS MeatProducts;

-- Table to store information about meat products
CREATE TABLE MeatProducts (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each meat product
    ProductName VARCHAR(100) NOT NULL,         -- Name of the meat product
    ProductType VARCHAR(50) NOT NULL,          -- Type of meat (e.g., beef, chicken, pork)
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the meat product
    QuantityInStock INT NOT NULL,               -- Quantity available in stock
    SupplierID INT,                             -- Foreign key referencing Suppliers
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE SET NULL
);

-- Table to store information about suppliers
CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each supplier
    SupplierName VARCHAR(100) NOT NULL,         -- Name of the supplier
    ContactName VARCHAR(100),                    -- Contact person's name
    Phone VARCHAR(15),                          -- Contact phone number
    Email VARCHAR(100),                         -- Contact email address
    Address VARCHAR(255)                        -- Supplier's address
);

-- Table to store information about customers
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each customer
    CustomerName VARCHAR(100) NOT NULL,          -- Name of the customer
    Phone VARCHAR(15),                           -- Customer's phone number
    Email VARCHAR(100),                          -- Customer's email address
    Address VARCHAR(255)                         -- Customer's address
);

-- Table to store orders made by customers
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each order
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    OrderDate DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,        -- Total amount for the order
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Table to store details of each order item
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each order item
    OrderID INT NOT NULL,                        -- Foreign key referencing Orders
    ProductID INT NOT NULL,                      -- Foreign key referencing MeatProducts
    Quantity INT NOT NULL,                       -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES MeatProducts(ProductID) ON DELETE CASCADE
);

-- Indexes can be added for performance optimization as needed
-- Example: CREATE INDEX idx_product_name ON MeatProducts(ProductName);
```
