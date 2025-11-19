"""
Generated Code Metadata:
========================
Original URL: https://odasloucabrazzz.blogspot.com
Prompt: Generate a SQL database schema for a wholesale kitchen supply store like Varejão das Louças that sells to restaurants and hotels.
Generated: DETERMINISTIC_458e1528e876aed6
Batch ID: 20250622_212122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for a Wholesale Kitchen Supply Store

-- Create a table for storing customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    Name VARCHAR(255) NOT NULL,                -- Customer's name
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Customer's email address
    Phone VARCHAR(20),                         -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the customer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for storing product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Product name
    Description TEXT,                         -- Product description
    Price DECIMAL(10, 2) NOT NULL,            -- Product price
    Stock INT NOT NULL,                       -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for storing orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each order
    CustomerID INT NOT NULL,                  -- Reference to the customer who placed the order
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,      -- Total amount for the order
    Status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Foreign key constraint
);

-- Create a table for storing order details
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Reference to the order
    ProductID INT NOT NULL,                       -- Reference to the product
    Quantity INT NOT NULL,                        -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Foreign key constraint
);

-- Create a table for storing suppliers
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each supplier
    Name VARCHAR(255) NOT NULL,                -- Supplier's name
    ContactName VARCHAR(255),                  -- Contact person's name
    Email VARCHAR(255) UNIQUE,                 -- Supplier's email address
    Phone VARCHAR(20),                         -- Supplier's phone number
    Address TEXT,                              -- Supplier's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the supplier was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for storing product-supplier relationships
CREATE TABLE ProductSuppliers (
    ProductSupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each relationship
    ProductID INT NOT NULL,                           -- Reference to the product
    SupplierID INT NOT NULL,                          -- Reference to the supplier
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE -- Foreign key constraint
);

-- Create a table for tracking inventory restocking
CREATE TABLE Restocking (
    RestockingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each restocking event
    ProductID INT NOT NULL,                      -- Reference to the product
    SupplierID INT NOT NULL,                     -- Reference to the supplier
    Quantity INT NOT NULL,                       -- Quantity restocked
    RestockingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of restocking
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE -- Foreign key constraint
);

-- Create indexes for faster queries
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_product_name ON Products(Name);
CREATE INDEX idx_order_customer ON Orders(CustomerID);
CREATE INDEX idx_order_status ON Orders(Status);
CREATE INDEX idx_supplier_email ON Suppliers(Email);
```
